#!/bin/sh
python ../../cnn_playground.py 1024_256 128 256_128 0.0001 32 PDBBind_Refined ecfp4 sequencematrix500_GRAR740104LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 pdbbind_refined_dataset_kansil_combined_best_encodings
sleep 1
