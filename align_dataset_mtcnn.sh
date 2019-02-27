#!/usr/bin/env python
#require tf12py27 env
#export PYTHONPATH=`pwd`/src
python src/align/align_dataset_mtcnn.py ./data/images/ ./data/images_align --image_size 182  --margin=44 --gpu_memory_fraction 0.8
