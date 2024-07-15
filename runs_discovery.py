import os
RUNS_DIRECTORY = "runs_discovery_smacv2_baselines/" 
PARTITION = "main"

def write_run_file(content, num): 
    os.makedirs(RUNS_DIRECTORY, exist_ok=True)    
    f = open(f"{RUNS_DIRECTORY}/run_{num}.job", "a")
    f.write(content)
    f.close()

file = f"""#!/bin/bash

#SBATCH --account=prasanna_1363
#SBATCH --partition={PARTITION}
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=64
#SBATCH --mem=128G
#SBATCH --time=10:00:00

conda activate dcg 
module load gcc/11.3.0 git/2.36.1 

""" 

# command = f"""
# python3 src/main.py --config=qmix --env-config=sc2_gen_protoss with use_cuda=False env_args.capability_config.n_units=20 env_args.capability_config.n_enemies=20 seed=0 cg_edges=full 
# """

# print(file+command)

CONFIGS = ["qmix", "vdn", "iql", "q_tran", "dcg", "cg"] 
ENVS = ["sc2_gen_protoss", "sc2_gen_terran", "sc2_gen_zerg"] 
UNITS = ["5v5", "10v10", "10v11", "20v20", "20v23"] 
SEEDS = 3 

"""
Baselines 
"""
count = 0 
for s in range(SEEDS): 
    for e in ENVS:
        for units in UNITS:
            for a in CONFIGS:
                count+=1
                u = units.split("v") 
                command = f"""python src/main.py --config={a} --env-config={e} with env_args.capability_config.n_units={u[0]} env_args.capability_config.n_enemies={u[1]} use_cuda=False seed={s}""" 
                write_run_file(file+command, count)