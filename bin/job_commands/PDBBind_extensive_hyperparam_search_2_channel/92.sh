bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_512_256_128_512_512_0.005_16_PDBBind_sequencematrix500_1_CompFCNNTarCNN_0.5.out "python cnn_playground.py 512_256 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.5"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_512_256_128_512_512_0.005_16_PDBBind_sequencematrix500_1_CompFCNNTarCNN2_0.5.out "python cnn_playground.py 512_256 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.5"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_512_512_128_512_512_0.005_16_PDBBind_sequencematrix500_1_CompFCNNTarCNN_0.2.out "python cnn_playground.py 512_512 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_512_512_128_512_512_0.005_16_PDBBind_sequencematrix500_1_CompFCNNTarCNN2_0.2.out "python cnn_playground.py 512_512 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_512_512_128_512_512_0.005_16_PDBBind_sequencematrix500_1_CompFCNNTarCNN_0.3.out "python cnn_playground.py 512_512 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.3"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_512_512_128_512_512_0.005_16_PDBBind_sequencematrix500_1_CompFCNNTarCNN2_0.3.out "python cnn_playground.py 512_512 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.3"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_512_512_128_512_512_0.005_16_PDBBind_sequencematrix500_1_CompFCNNTarCNN_0.5.out "python cnn_playground.py 512_512 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.5"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_512_512_128_512_512_0.005_16_PDBBind_sequencematrix500_1_CompFCNNTarCNN2_0.5.out "python cnn_playground.py 512_512 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.5"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_1024_512_128_512_512_0.005_16_PDBBind_sequencematrix500_1_CompFCNNTarCNN_0.2.out "python cnn_playground.py 1024_512 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN 0.2"
sleep 1
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 10240 -R 'rusage[mem=10240]' -o ../../../log_files/PDBBind_extensive_hyperparam_search_2_channel/normalized_1024_512_128_512_512_0.005_16_PDBBind_sequencematrix500_1_CompFCNNTarCNN2_0.2.out "python cnn_playground.py 1024_512 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500 1 CompFCNNTarCNN2 0.2"
sleep 1
