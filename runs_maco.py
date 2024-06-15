import os 

def exps(configs, maps, agents, GPU, seed_max, parallel): 
    for map in maps: 
        for config in configs: 
            for agent in agents: 
                for _ in range(seed_max): 
                    command = f"CUDA_VISIBLE_DEVICES={GPU} python3 src/main.py --config={config} --env-config={map}  with agent={agent} cg_edges=full" 
                    if parallel: command += " &"
                    os.system(command) 


exps(
    configs=["dcg"], 
    maps=["gather", "hallway", "pursuit", "disperse", "sensor", "aloha"], 
    agents=["gtn_feat"], 
    GPU=0, 
    seed_max=1, 
    parallel=False 
)

exps(
    configs=["dcg"], 
    maps=["gather", "hallway", "pursuit", "disperse", "sensor", "aloha"], 
    agents=["gcn_feat", "gat_feat", "gatv2_feat"], 
    GPU=1, 
    seed_max=1, 
    parallel=False 
) 