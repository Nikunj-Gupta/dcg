GPU=0
all: 
	clear 
	CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=dcg --env-config=sc2_gen_protoss