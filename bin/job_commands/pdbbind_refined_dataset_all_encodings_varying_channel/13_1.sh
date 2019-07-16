#!/bin/sh
python ../../cnn_playground.py 1024_512 128 256_128512_256 0.0001 32 PDBBind_Refined ecfp4 sequencematrix500 1 CompFCNNTarCNN4LayersStride 0.25 pdbbind_refined_dataset_all_encodings_varying_channel
sleep 1
