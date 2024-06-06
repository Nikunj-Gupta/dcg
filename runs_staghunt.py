import os 

maps = ["rel_overgen"] 
configs=["dcg", "cg", "vdn", "qmix", "iql"] 
miscapture_punishments=[0, -1, -1.25, -1.5, -2] 
miscapture_punishments=[0] 
GPU = 1
seed_max=1

parallel = True 

for map in maps: 
    for config in configs: 
        for miscapture_punishment in miscapture_punishments: 
            for _ in range(seed_max): 
                command = f"CUDA_VISIBLE_DEVICES={GPU} python3 src/main.py --config={config} --env-config={map} with env_args.miscapture_punishment={miscapture_punishment}" 
                if parallel: command += " &"
                os.system(command) 