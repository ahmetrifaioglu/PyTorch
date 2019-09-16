#!/bin/sh
python ../../cnn_playground.py 1024_512 512 1024_512 0.001 32 PDBBind_Refined ecfp4 sequencematrix500_blosum62LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.25 pdbbind_refined_dataset_kansil_combined_best_encodings
sleep 1
