GPU=1
all: 
	clear 
	# pip install -r req.txt 
	# CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=dcg --env-config=sc2_gen_protoss with env_args.capability_config.n_units=5 env_args.capability_config.n_enemies=5 cg_edges=vdn
	# CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=dcg --env-config=rel_overgen 
	CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=dcg --env-config=aloha
