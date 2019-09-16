#!/bin/sh
python ../../cnn_playground.py 1024_256 1024 1024_1024 0.001 32 PDBBind_Refined ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500 1 CompFCNNTarCNNModuleInception 0.25 pdbbind_refined_dataset_kansil_combined_best_encodings
sleep 1
