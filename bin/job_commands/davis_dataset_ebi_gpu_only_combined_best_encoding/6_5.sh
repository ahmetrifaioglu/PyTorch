#!/bin/sh
python ../../cnn_playground.py 512_512 64 512_256 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.25 davis_dataset_ebi_gpu_only_combined_best_encoding
sleep 1
python ../../cnn_playground.py 1024_512 64 512_256 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding
sleep 1
python ../../cnn_playground.py 1024_512 64 512_256 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.25 davis_dataset_ebi_gpu_only_combined_best_encoding
sleep 1
python ../../cnn_playground.py 1024_256 64 512_256 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding
sleep 1
python ../../cnn_playground.py 1024_256 64 512_256 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.25 davis_dataset_ebi_gpu_only_combined_best_encoding
sleep 1
