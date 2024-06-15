GPU=0
all: 
	clear 
	# pip install -r req.txt 
	CUDA_VISIBLE_DEVICES=${GPU} python3 src/main.py --config=dcg --env-config=gather with agent=gtn_feat 