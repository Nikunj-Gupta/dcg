import torch.nn as nn
import torch.nn.functional as F
import torch as th
import numpy as np
import torch.nn.init as init
from utils.th_utils import orthogonal_init_
from torch.nn import LayerNorm
from torch_geometric.nn import GCNConv, GATConv, GATv2Conv 

class GNNAgent(nn.Module):
    def __init__(self, input_shape, args):
        super(GNNAgent, self).__init__()
        self.args = args
        cg_edges = args.cg_edges 
        agent = args.agent 
        self.N = args.n_agents 
        self.edge_index = self.build_edge_index(type=cg_edges) 

        print(f"Using {agent} Agent and cg_edges={cg_edges}") 

        self.fc1 = nn.Linear(input_shape, args.rnn_hidden_dim)

        in_channels = args.rnn_hidden_dim
        out_channels = args.rnn_hidden_dim
        if agent == "gcn": self.conv1 = GCNConv(in_channels, out_channels) 
        if agent == "gat": self.conv1 = GATConv(in_channels, out_channels) 
        if agent == "gatv2": self.conv1 = GATv2Conv(in_channels, out_channels) 

        self.rnn = nn.GRUCell(args.rnn_hidden_dim, args.rnn_hidden_dim)
        self.fc2 = nn.Linear(args.rnn_hidden_dim, args.n_actions)
        self.layer_norm = LayerNorm(args.rnn_hidden_dim)

    def init_hidden(self):
        # make hidden states on same device as model
        return self.fc1.weight.new(1, self.args.rnn_hidden_dim).zero_()

    def build_edge_index(self, type):
        if type == "line": 
            edges = [[i, i + 1] for i in range(self.N - 1)]  # # arrange agents in a line 
        elif type == "full": 
            edges = [[(j, i + j + 1) for i in range(self.N - j - 1)] for j in range(self.N - 1)]
            edges = [e for l in edges for e in l] 
        elif type == 'cycle':    # arrange agents in a circle
            edges = [(i, i + 1) for i in range(self.N - 1)] + [(self.N - 1, 0)] 
        elif type == 'star':     # arrange all agents in a star around agent 0
            edges = [(0, i + 1) for i in range(self.N - 1)] 
        edge_index = th.tensor(edges).T.cuda() # # arrange agents in a line 
        return edge_index

    def forward(self, inputs, hidden_state):
        x = F.relu(self.fc1(inputs), inplace=True)
        x = self.conv1(x, self.edge_index)
        h_in = hidden_state.reshape(-1, self.args.rnn_hidden_dim)
        hh = self.rnn(x, h_in)
        if getattr(self.args, "use_layer_norm", False):
            q = self.fc2(self.layer_norm(hh))
        else:
            q = self.fc2(hh)
        return q, hh