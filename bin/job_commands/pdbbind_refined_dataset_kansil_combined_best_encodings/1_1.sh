#!/bin/sh
mkdir ../../../log_files/pdbbind_refined_dataset_kansil_combined_best_encodings
mkdir ../../../result_files/pdbbind_refined_dataset_kansil_combined_best_encodings
python ../../cnn_playground.py 1024_512 128 256_128 0.0001 32 PDBBind_Refined ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500 1 CompFCNNTarCNNModuleInception 0.1 pdbbind_refined_dataset_kansil_combined_best_encodings
sleep 1
