#!/bin/sh
mkdir ../../../log_files/davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
mkdir ../../../result_files/davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
python ../../cnn_playground.py 1024_512 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_512 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_512 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_512 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_blosum62LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_512 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500 1 CompFCNNTarCNNModuleInception 0.25 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_512 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.25 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_512 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.25 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_512 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_blosum62LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.25 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_256 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_256 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_256 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_256 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_blosum62LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_256 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500 1 CompFCNNTarCNNModuleInception 0.25 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_256 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.25 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_256 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.25 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_256 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_blosum62LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.25 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_1024 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_1024 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_1024 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
python ../../cnn_playground.py 1024_1024 128 256_128512_256 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_blosum62LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_filtered_ebi_gpu_encoding_blosum62_SIMK990101
sleep 1
