import os 

configs=["cg", "dcg"]
maps = ["aloha", "disperse", "gather", "hallway", "pursuit"] 
GPU = 1 
seed_max=1 

parallel = True 

for map in maps: 
    for config in configs: 
        for _ in range(seed_max): 
            command = f"CUDA_VISIBLE_DEVICES={GPU} python3 src/main.py --config={config} --env-config={map}" 
            if parallel: command += " &"
            os.system(command) 
