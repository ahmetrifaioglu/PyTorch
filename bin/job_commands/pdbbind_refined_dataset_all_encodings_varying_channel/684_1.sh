#!/bin/sh
python ../../cnn_playground.py 1024_512 1024 1024_512 0.0001 32 PDBBind_Refined ecfp4 sequencematrix500_blosum62LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.25 pdbbind_refined_dataset_all_encodings_varying_channel
sleep 1
