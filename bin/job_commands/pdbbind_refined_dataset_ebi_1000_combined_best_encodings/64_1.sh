#!/bin/sh
python ../../cnn_playground.py 1024_1024 64 1024_512 0.001 32 PDBBind_Refined ecfp4 sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 1 CompFCNNTarCNNModuleInception 0.25 pdbbind_refined_dataset_ebi_1000_combined_best_encodings
sleep 1
