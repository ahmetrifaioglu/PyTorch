#!/bin/sh
python ../../cnn_playground.py 1024_256 1024 1024_1024 0.0001 32 PDBBind_Refined ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.25 pdbbind_refined_dataset_ebi_gpu_only_combined_best_encoding
sleep 1
