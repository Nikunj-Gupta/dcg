GPU=1
all: 
	clear 
	# CUDA_VISIBLE_DEVICES=$(GPU) python3 src/main.py --config=qmix --env-config=sc2_gen_protoss with use_cuda=True env_args.capability_config.n_units=10 env_args.capability_config.n_enemies=10 seed=0 cg_edges=full 
	# python3 src/main.py --config=dcg --env-config=sc2_gen_protoss with use_cuda=False env_args.capability_config.n_units=20 env_args.capability_config.n_enemies=20 seed=0 cg_edges=full 

runall: 
	for f in runs_discovery_smacv2_baselines/*.job; do sbatch $$f; done 