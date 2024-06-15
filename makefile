GPU=0
all: 
	clear 
	# pip install -r req.txt 
	# CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=dcg --env-config=sc2_gen_protoss with env_args.capability_config.n_units=5 env_args.capability_config.n_enemies=5 cg_edges=vdn
	# CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=dcg --env-config=rel_overgen 
	# CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=dcg --env-config=aloha
	# CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=dcg --env-config=sensor
	# CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=cg --env-config=sensor 

	CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=dcg --env-config=gather with agent=gcn_feat cg_edges=full
	CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=dcg --env-config=gather with agent=gat_feat cg_edges=full
	CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=dcg --env-config=gather with agent=gatv2_feat cg_edges=full
	CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=cg --env-config=gather with agent=gcn_feat cg_edges=full
	CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=cg --env-config=gather with agent=gat_feat cg_edges=full
	CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=cg --env-config=gather with agent=gatv2_feat cg_edges=full 