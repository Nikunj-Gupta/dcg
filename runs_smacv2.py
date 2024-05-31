import os 

configs=["dcg", "qmix", "iql", "vdn"] 
maps = ["sc2_gen_protoss"] 
units=["20v20"] 
GPU = 0
seed_max=1

parallel = True 

for map in maps: 
    for unit in units: 
        for config in configs: 
            for _ in range(seed_max): 
                u = unit.split('v') 
                command = f"CUDA_VISIBLE_DEVICES={GPU} python3 src/main.py --config={config} --env-config={map} with env_args.capability_config.n_units={u[0]} env_args.capability_config.n_enemies={u[1]}" 
                if parallel: command += " &"
                os.system(command)

