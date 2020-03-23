bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.1_1 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 0"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.1_2 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.1_3 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.1_4 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 3"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.1_5 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 4"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.2_1 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 0"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.2_2 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.2_3 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.2_4 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 3"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.2_5 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 4"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.3_1 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 0"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.3_2 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.3_3 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.3_4 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 3"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.3_5 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 4"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.4_1 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 0"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.4_2 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.4_3 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.4_4 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 3"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.4_5 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 4"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.5_1 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 0"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.5_2 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.5_3 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.5_4 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 3"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.5_5 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 4"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.6_1 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 0"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.6_2 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.6_3 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.6_4 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 3"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.6_5 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 4"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.7_1 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 0"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.7_2 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.7_3 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.7_4 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 3"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.7_5 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 4"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.8_1 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 0"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.8_2 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.8_3 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.8_4 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 3"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.8_5 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 4"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.9_1 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 0"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.9_2 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.9_3 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.9_4 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 3"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.9_5 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 4"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.10_1 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 0"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.10_2 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 1"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.10_3 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.10_4 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 3"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o out.10_5 "python ../../cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 Davis ecfp4 sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500 1 CompFCNNTarCNNModuleInception 0.1 davis_dataset_ebi_gpu_only_combined_best_encoding_final 4"