#!/bin/sh
python ../../cnn_playground.py 1024_1024 512 512_256 0.001 32 PDBBind_Refined ecfp4 sequencematrix500_blosum62LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.1 pdbbind_refined_dataset_kansil_combined_best_encodings
sleep 1
