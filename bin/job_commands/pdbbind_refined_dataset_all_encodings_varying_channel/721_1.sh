#!/bin/sh
python ../../cnn_playground.py 1024_512 1024 1024_512 0.001 32 PDBBind_Refined ecfp4 sequencematrix500 1 CompFCNNTarCNNModuleInception 0.1 pdbbind_refined_dataset_all_encodings_varying_channel
sleep 1