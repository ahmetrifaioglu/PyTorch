#!/bin/sh
python ../../cnn_playground.py 1024_256 256 256_128512_256 0.001 32 PDBBind_Refined ecfp4 sequencematrix500_blosum62LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNN4LayersStride 0.1 pdbbind_refined_dataset_all_encodings_varying_channel
sleep 1
