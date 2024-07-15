import os 

def baselines(): 
    CONFIGS = ["qmix", "vdn", "iql", "qtran", "dcg", "cg"]
    SEEDS = 3 
    PARALLEL = False 
    CG_EDGES = ["full", "cycle", "line", "star"]
    UNITS=["5v5", "10v10", "10v11", "20v20", "20v23"] 

    for s in range(SEEDS): 
        for cg_edges in CG_EDGES: 
            for unit in UNITS: 
                for a in CONFIGS: 
                    u = unit.split('v') 
                    command = f"python3 src/main.py --config={a} --env-config=sc2_gen_protoss with use_cuda=False env_args.capability_config.n_units={u[0]} env_args.capability_config.n_enemies={u[1]} seed={s} cg_edges={cg_edges}" 
                    if PARALLEL: command += " &" 
                    os.system(command) 
baselines() 