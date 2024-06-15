REGISTRY = {}

from .rnn_agent import RNNAgent
REGISTRY["rnn"] = RNNAgent

from .rnn_feature_agent import RNNFeatureAgent
REGISTRY["rnn_feat"] = RNNFeatureAgent

from .gnn_agent import GNNAgent
REGISTRY["gat"] = GNNAgent
REGISTRY["gatv2"] = GNNAgent
REGISTRY["gcn"] = GNNAgent

from .gnn_agent_feat import GNNFeatureAgent
REGISTRY["gat_feat"] = GNNFeatureAgent
REGISTRY["gatv2_feat"] = GNNFeatureAgent
REGISTRY["gcn_feat"] = GNNFeatureAgent