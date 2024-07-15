import os 

def baselines(): 
    CONFIGS = ["qmix", "vdn", "iql", "qtran", "dcg", "cg"]
    ENVS = ["gather", "hallway", "pursuit", "disperse", "sensor", "aloha"] 
    SEEDS = 3 
    PARALLEL = False 

    for s in range(SEEDS): 
        for e in ENVS:
            for a in CONFIGS: 
                command = f"python3 src/main.py --config={a} --env-config={e} with use_cuda=False seed={s}" 
                if PARALLEL: command += " &" 
                os.system(command) 
baselines() 