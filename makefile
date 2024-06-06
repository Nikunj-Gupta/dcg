GPU=1
all: 
	clear 
	# pip install -r req.txt 
	CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=dcg_noshare --env-config=sc2_gen_protoss with env_args.capability_config.n_units=10 env_args.capability_config.n_enemies=10 cg_edges=vdn
