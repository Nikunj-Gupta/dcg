import os 

configs=["dcg", "dcg_noshare", "cg"] 
configs=["dcg_noshare"] 
all_cg_edges = ["full", "cycle", "line", "star", "vdn"]
maps = ["sc2_gen_protoss"] 
units=["20v20"] 
GPU = 0
seed_max=1

parallel = True 

for map in maps: 
    for unit in units: 
        for config in configs: 
            for cg_edges in all_cg_edges: 
                for _ in range(seed_max): 
                    u = unit.split('v') 
                    command = f"CUDA_VISIBLE_DEVICES={GPU} python3 src/main.py --config={config} --env-config={map} with env_args.capability_config.n_units={u[0]} env_args.capability_config.n_enemies={u[1]}" 
                    if cg_edges: command += f" cg_edges={cg_edges}" 
                    if parallel: command += " &"
                    os.system(command) 

