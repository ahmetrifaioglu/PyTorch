#!/bin/sh
python ../../cnn_playground.py 1024_512 512 1024_512 0.0001 32 PDBBind_Refined ecfp4 sequencematrix500_SIMK990101LEQ500 1 CompFCNNTarCNN4LayersStride 0.1 pdbbind_refined_dataset_all_encodings_varying_channel
sleep 1
