bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/out.1 "python ../../cnn_playground.py 1024_1024 256 512_256 0.0001 32 kinome ecfp4 sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 0 CompFCNNTarCNNModuleInception 0.25 kinome_dataset_ebi_gpu_only_combined_best_encoding 0"
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/out.2 "python ../../cnn_playground.py 1024_1024 256 512_256 0.0001 32 kinome ecfp4 sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 0 CompFCNNTarCNNModuleInception 0.25 kinome_dataset_ebi_gpu_only_combined_best_encoding 1"
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/out.3 "python ../../cnn_playground.py 1024_1024 256 512_256 0.0001 32 kinome ecfp4 sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 0 CompFCNNTarCNNModuleInception 0.25 kinome_dataset_ebi_gpu_only_combined_best_encoding 2"
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/out.4 "python ../../cnn_playground.py 1024_1024 256 512_256 0.0001 32 kinome ecfp4 sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 0 CompFCNNTarCNNModuleInception 0.25 kinome_dataset_ebi_gpu_only_combined_best_encoding 3"
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/out.5 "python ../../cnn_playground.py 1024_1024 256 512_256 0.0001 32 kinome ecfp4 sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 0 CompFCNNTarCNNModuleInception 0.25 kinome_dataset_ebi_gpu_only_combined_best_encoding 4"
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/out.6 "python ../../cnn_playground.py 1024_1024 256 512_256 0.0001 32 kinome ecfp4 sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 0 CompFCNNTarCNNModuleInception 0.1 kinome_dataset_ebi_gpu_only_combined_best_encoding 0"
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/out.7 "python ../../cnn_playground.py 1024_1024 256 512_256 0.0001 32 kinome ecfp4 sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 0 CompFCNNTarCNNModuleInception 0.1 kinome_dataset_ebi_gpu_only_combined_best_encoding 1"
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/out.8 "python ../../cnn_playground.py 1024_1024 256 512_256 0.0001 32 kinome ecfp4 sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 0 CompFCNNTarCNNModuleInception 0.1 kinome_dataset_ebi_gpu_only_combined_best_encoding 2"
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/out.9 "python ../../cnn_playground.py 1024_1024 256 512_256 0.0001 32 kinome ecfp4 sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 0 CompFCNNTarCNNModuleInception 0.1 kinome_dataset_ebi_gpu_only_combined_best_encoding 3"
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/out.10 "python ../../cnn_playground.py 1024_1024 256 512_256 0.0001 32 kinome ecfp4 sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000 0 CompFCNNTarCNNModuleInception 0.1 kinome_dataset_ebi_gpu_only_combined_best_encoding 4"