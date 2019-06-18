bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_1024_1024_256_1024_1024_0.001_64_PDBBind_sequencematrix500_1_CompFCNNTarCNN_0.5.out "python cnn_playground.py 1024_1024 256 1024_1024 0.001 64 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.5"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_1024_1024_256_1024_1024_0.001_64_PDBBind_sequencematrix500_1_CompFCNNTarCNN2_0.5.out "python cnn_playground.py 1024_1024 256 1024_1024 0.001 64 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.5"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_256_256_256_1024_1024_0.01_64_PDBBind_sequencematrix500_1_CompFCNNTarCNN_0.2.out "python cnn_playground.py 256_256 256 1024_1024 0.01 64 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_256_256_256_1024_1024_0.01_64_PDBBind_sequencematrix500_1_CompFCNNTarCNN2_0.2.out "python cnn_playground.py 256_256 256 1024_1024 0.01 64 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_256_256_256_1024_1024_0.01_64_PDBBind_sequencematrix500_1_CompFCNNTarCNN_0.3.out "python cnn_playground.py 256_256 256 1024_1024 0.01 64 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.3"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_256_256_256_1024_1024_0.01_64_PDBBind_sequencematrix500_1_CompFCNNTarCNN2_0.3.out "python cnn_playground.py 256_256 256 1024_1024 0.01 64 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.3"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_256_256_256_1024_1024_0.01_64_PDBBind_sequencematrix500_1_CompFCNNTarCNN_0.5.out "python cnn_playground.py 256_256 256 1024_1024 0.01 64 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.5"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_256_256_256_1024_1024_0.01_64_PDBBind_sequencematrix500_1_CompFCNNTarCNN2_0.5.out "python cnn_playground.py 256_256 256 1024_1024 0.01 64 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.5"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_512_256_256_1024_1024_0.01_64_PDBBind_sequencematrix500_1_CompFCNNTarCNN_0.2.out "python cnn_playground.py 512_256 256 1024_1024 0.01 64 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_512_256_256_1024_1024_0.01_64_PDBBind_sequencematrix500_1_CompFCNNTarCNN2_0.2.out "python cnn_playground.py 512_256 256 1024_1024 0.01 64 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.2"
sleep 1
