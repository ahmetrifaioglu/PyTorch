#!/bin/sh
python ../../cnn_playground.py 1024_256 512 1024_1024 0.001 32 kinome ecfp4 sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 1 CompFCNNTarCNNModuleInception 0.25 kinome_dataset_ebi_gpu_only_combined_best_encoding
sleep 1
