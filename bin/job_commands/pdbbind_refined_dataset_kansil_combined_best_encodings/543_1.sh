#!/bin/sh
python ../../cnn_playground.py 1024_1024 256 1024_512 0.0001 32 PDBBind_Refined ecfp4 sequencematrix500_GRAR740104LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.25 pdbbind_refined_dataset_kansil_combined_best_encodings
sleep 1
