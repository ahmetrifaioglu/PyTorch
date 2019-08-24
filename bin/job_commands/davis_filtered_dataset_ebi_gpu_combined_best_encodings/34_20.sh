#!/bin/sh
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_1024_512_1024_512_0.001_32_Davis_Filtered_sequencematrix500_ZHAC000103LEQ500_SIMK990101LEQ500_1_CompFCNNTarCNNModuleInception_0.1.out "python cnn_playground.py 1024_1024 512 1024_512 0.001 32 Davis_Filtered ecfp4 sequencematrix500_ZHAC000103LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_1024_512_1024_512_0.001_32_Davis_Filtered_sequencematrix500_GRAR740104LEQ500_blosum62LEQ500_1_CompFCNNTarCNNModuleInception_0.1.out "python cnn_playground.py 1024_1024 512 1024_512 0.001 32 Davis_Filtered ecfp4 sequencematrix500_GRAR740104LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_1024_512_1024_512_0.001_32_Davis_Filtered_sequencematrix500_GRAR740104LEQ500_SIMK990101LEQ500_1_CompFCNNTarCNNModuleInception_0.1.out "python cnn_playground.py 1024_1024 512 1024_512 0.001 32 Davis_Filtered ecfp4 sequencematrix500_GRAR740104LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_1024_512_1024_512_0.001_32_Davis_Filtered_sequencematrix500_blosum62LEQ500_SIMK990101LEQ500_1_CompFCNNTarCNNModuleInception_0.1.out "python cnn_playground.py 1024_1024 512 1024_512 0.001 32 Davis_Filtered ecfp4 sequencematrix500_blosum62LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_1024_512_1024_512_0.001_32_Davis_Filtered_sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500_1_CompFCNNTarCNNModuleInception_0.1.out "python cnn_playground.py 1024_1024 512 1024_512 0.001 32 Davis_Filtered ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_1024_512_1024_512_0.001_32_Davis_Filtered_sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_1_CompFCNNTarCNNModuleInception_0.25.out "python cnn_playground.py 1024_1024 512 1024_512 0.001 32 Davis_Filtered ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500 1 CompFCNNTarCNNModuleInception 0.25"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_1024_512_1024_512_0.001_32_Davis_Filtered_sequencematrix500_ZHAC000103LEQ500_blosum62LEQ500_1_CompFCNNTarCNNModuleInception_0.25.out "python cnn_playground.py 1024_1024 512 1024_512 0.001 32 Davis_Filtered ecfp4 sequencematrix500_ZHAC000103LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.25"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_1024_512_1024_512_0.001_32_Davis_Filtered_sequencematrix500_ZHAC000103LEQ500_SIMK990101LEQ500_1_CompFCNNTarCNNModuleInception_0.25.out "python cnn_playground.py 1024_1024 512 1024_512 0.001 32 Davis_Filtered ecfp4 sequencematrix500_ZHAC000103LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.25"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_1024_512_1024_512_0.001_32_Davis_Filtered_sequencematrix500_GRAR740104LEQ500_blosum62LEQ500_1_CompFCNNTarCNNModuleInception_0.25.out "python cnn_playground.py 1024_1024 512 1024_512 0.001 32 Davis_Filtered ecfp4 sequencematrix500_GRAR740104LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.25"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_1024_512_1024_512_0.001_32_Davis_Filtered_sequencematrix500_GRAR740104LEQ500_SIMK990101LEQ500_1_CompFCNNTarCNNModuleInception_0.25.out "python cnn_playground.py 1024_1024 512 1024_512 0.001 32 Davis_Filtered ecfp4 sequencematrix500_GRAR740104LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.25"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_1024_512_1024_512_0.001_32_Davis_Filtered_sequencematrix500_blosum62LEQ500_SIMK990101LEQ500_1_CompFCNNTarCNNModuleInception_0.25.out "python cnn_playground.py 1024_1024 512 1024_512 0.001 32 Davis_Filtered ecfp4 sequencematrix500_blosum62LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.25"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_1024_512_1024_512_0.001_32_Davis_Filtered_sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500_1_CompFCNNTarCNNModuleInception_0.25.out "python cnn_playground.py 1024_1024 512 1024_512 0.001 32 Davis_Filtered ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.25"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_512_512_1024_1024_0.0001_32_Davis_Filtered_sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_1_CompFCNNTarCNNModuleInception_0.1.out "python cnn_playground.py 1024_512 512 1024_1024 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500 1 CompFCNNTarCNNModuleInception 0.1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_512_512_1024_1024_0.0001_32_Davis_Filtered_sequencematrix500_ZHAC000103LEQ500_blosum62LEQ500_1_CompFCNNTarCNNModuleInception_0.1.out "python cnn_playground.py 1024_512 512 1024_1024 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_ZHAC000103LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_512_512_1024_1024_0.0001_32_Davis_Filtered_sequencematrix500_ZHAC000103LEQ500_SIMK990101LEQ500_1_CompFCNNTarCNNModuleInception_0.1.out "python cnn_playground.py 1024_512 512 1024_1024 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_ZHAC000103LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_512_512_1024_1024_0.0001_32_Davis_Filtered_sequencematrix500_GRAR740104LEQ500_blosum62LEQ500_1_CompFCNNTarCNNModuleInception_0.1.out "python cnn_playground.py 1024_512 512 1024_1024 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_GRAR740104LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_512_512_1024_1024_0.0001_32_Davis_Filtered_sequencematrix500_GRAR740104LEQ500_SIMK990101LEQ500_1_CompFCNNTarCNNModuleInception_0.1.out "python cnn_playground.py 1024_512 512 1024_1024 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_GRAR740104LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_512_512_1024_1024_0.0001_32_Davis_Filtered_sequencematrix500_blosum62LEQ500_SIMK990101LEQ500_1_CompFCNNTarCNNModuleInception_0.1.out "python cnn_playground.py 1024_512 512 1024_1024 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_blosum62LEQ500_SIMK990101LEQ500 1 CompFCNNTarCNNModuleInception 0.1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_512_512_1024_1024_0.0001_32_Davis_Filtered_sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500_1_CompFCNNTarCNNModuleInception_0.1.out "python cnn_playground.py 1024_512 512 1024_1024 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/davis_filtered_dataset_ebi_gpu_combined_best_encodings/normalized_1024_512_512_1024_1024_0.0001_32_Davis_Filtered_sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_1_CompFCNNTarCNNModuleInception_0.25.out "python cnn_playground.py 1024_512 512 1024_1024 0.0001 32 Davis_Filtered ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500 1 CompFCNNTarCNNModuleInception 0.25"
sleep 1
