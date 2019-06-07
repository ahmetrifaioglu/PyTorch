bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 64 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_128_128_0.005_16_PDBBind.out "python cnn_playground.py 256_256 64 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_128_128_0.005_16_PDBBind.out "python cnn_playground.py 512_256 64 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_128_128_0.005_16_PDBBind.out "python cnn_playground.py 512_512 64 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 64 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 64 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 64 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_128_128_0.001_16_PDBBind.out "python cnn_playground.py 256_256 64 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_128_128_0.001_16_PDBBind.out "python cnn_playground.py 512_256 64 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_128_128_0.001_16_PDBBind.out "python cnn_playground.py 512_512 64 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 64 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 64 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 64 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_128_128_0.01_16_PDBBind.out "python cnn_playground.py 256_256 64 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_128_128_0.01_16_PDBBind.out "python cnn_playground.py 512_256 64 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_128_128_0.01_16_PDBBind.out "python cnn_playground.py 512_512 64 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 64 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 64 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 64 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 64 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 64 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 64 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 64 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 64 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 64 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_256_256_0.005_16_PDBBind.out "python cnn_playground.py 256_256 64 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_256_256_0.005_16_PDBBind.out "python cnn_playground.py 512_256 64 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_256_256_0.005_16_PDBBind.out "python cnn_playground.py 512_512 64 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 64 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 64 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 64 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_256_256_0.001_16_PDBBind.out "python cnn_playground.py 256_256 64 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_256_256_0.001_16_PDBBind.out "python cnn_playground.py 512_256 64 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_256_256_0.001_16_PDBBind.out "python cnn_playground.py 512_512 64 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 64 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 64 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 64 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_256_256_0.01_16_PDBBind.out "python cnn_playground.py 256_256 64 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_256_256_0.01_16_PDBBind.out "python cnn_playground.py 512_256 64 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_256_256_0.01_16_PDBBind.out "python cnn_playground.py 512_512 64 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 64 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 64 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 64 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 64 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 64 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 64 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 64 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 64 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 64 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_512_512_0.005_16_PDBBind.out "python cnn_playground.py 256_256 64 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_512_512_0.005_16_PDBBind.out "python cnn_playground.py 512_256 64 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_512_512_0.005_16_PDBBind.out "python cnn_playground.py 512_512 64 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 64 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 64 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 64 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_512_512_0.001_16_PDBBind.out "python cnn_playground.py 256_256 64 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_512_512_0.001_16_PDBBind.out "python cnn_playground.py 512_256 64 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_512_512_0.001_16_PDBBind.out "python cnn_playground.py 512_512 64 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 64 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 64 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 64 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_512_512_0.01_16_PDBBind.out "python cnn_playground.py 256_256 64 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_512_512_0.01_16_PDBBind.out "python cnn_playground.py 512_256 64 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_512_512_0.01_16_PDBBind.out "python cnn_playground.py 512_512 64 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 64 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 64 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 64 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 64 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 64 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 64 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 64 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 64 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 64 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 256_256 64 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 512_256 64 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 512_512 64 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 64 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 64 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 64 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 256_256 64 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 512_256 64 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 512_512 64 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 64 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 64 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 64 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 256_256 64 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 512_256 64 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 512_512 64 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 64 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 64 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 64 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 128 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 128 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 128 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 128 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 128 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 128 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_128_128_0.005_16_PDBBind.out "python cnn_playground.py 256_256 128 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_128_128_0.005_16_PDBBind.out "python cnn_playground.py 512_256 128 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_128_128_0.005_16_PDBBind.out "python cnn_playground.py 512_512 128 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 128 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 128 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 128 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_128_128_0.001_16_PDBBind.out "python cnn_playground.py 256_256 128 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_128_128_0.001_16_PDBBind.out "python cnn_playground.py 512_256 128 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_128_128_0.001_16_PDBBind.out "python cnn_playground.py 512_512 128 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 128 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 128 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 128 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_128_128_0.01_16_PDBBind.out "python cnn_playground.py 256_256 128 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_128_128_0.01_16_PDBBind.out "python cnn_playground.py 512_256 128 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_128_128_0.01_16_PDBBind.out "python cnn_playground.py 512_512 128 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 128 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 128 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 128 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 128 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 128 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 128 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 128 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 128 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 128 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_256_256_0.005_16_PDBBind.out "python cnn_playground.py 256_256 128 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_256_256_0.005_16_PDBBind.out "python cnn_playground.py 512_256 128 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_256_256_0.005_16_PDBBind.out "python cnn_playground.py 512_512 128 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 128 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 128 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 128 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_256_256_0.001_16_PDBBind.out "python cnn_playground.py 256_256 128 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_256_256_0.001_16_PDBBind.out "python cnn_playground.py 512_256 128 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_256_256_0.001_16_PDBBind.out "python cnn_playground.py 512_512 128 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 128 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 128 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 128 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_256_256_0.01_16_PDBBind.out "python cnn_playground.py 256_256 128 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_256_256_0.01_16_PDBBind.out "python cnn_playground.py 512_256 128 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_256_256_0.01_16_PDBBind.out "python cnn_playground.py 512_512 128 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 128 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 128 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 128 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 128 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 128 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 128 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 128 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 128 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 128 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_512_512_0.005_16_PDBBind.out "python cnn_playground.py 256_256 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_512_512_0.005_16_PDBBind.out "python cnn_playground.py 512_256 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_512_512_0.005_16_PDBBind.out "python cnn_playground.py 512_512 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 128 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_512_512_0.001_16_PDBBind.out "python cnn_playground.py 256_256 128 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_512_512_0.001_16_PDBBind.out "python cnn_playground.py 512_256 128 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_512_512_0.001_16_PDBBind.out "python cnn_playground.py 512_512 128 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 128 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 128 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 128 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_512_512_0.01_16_PDBBind.out "python cnn_playground.py 256_256 128 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_512_512_0.01_16_PDBBind.out "python cnn_playground.py 512_256 128 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_512_512_0.01_16_PDBBind.out "python cnn_playground.py 512_512 128 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 128 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 128 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 128 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 128 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 128 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 128 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 128 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 128 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 128 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 256_256 128 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 512_256 128 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 512_512 128 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 128 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 128 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 128 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 256_256 128 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 512_256 128 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 512_512 128 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 128 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 128 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 128 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 256_256 128 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 512_256 128 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 512_512 128 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 128 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 128 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 128 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 256 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 256 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 256 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 256 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 256 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 256 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_128_128_0.005_16_PDBBind.out "python cnn_playground.py 256_256 256 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_128_128_0.005_16_PDBBind.out "python cnn_playground.py 512_256 256 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_128_128_0.005_16_PDBBind.out "python cnn_playground.py 512_512 256 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 256 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 256 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 256 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_128_128_0.001_16_PDBBind.out "python cnn_playground.py 256_256 256 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_128_128_0.001_16_PDBBind.out "python cnn_playground.py 512_256 256 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_128_128_0.001_16_PDBBind.out "python cnn_playground.py 512_512 256 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 256 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 256 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 256 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_128_128_0.01_16_PDBBind.out "python cnn_playground.py 256_256 256 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_128_128_0.01_16_PDBBind.out "python cnn_playground.py 512_256 256 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_128_128_0.01_16_PDBBind.out "python cnn_playground.py 512_512 256 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 256 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 256 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 256 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 256 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 256 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 256 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 256 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 256 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 256 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_256_256_0.005_16_PDBBind.out "python cnn_playground.py 256_256 256 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_256_256_0.005_16_PDBBind.out "python cnn_playground.py 512_256 256 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_256_256_0.005_16_PDBBind.out "python cnn_playground.py 512_512 256 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 256 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 256 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 256 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_256_256_0.001_16_PDBBind.out "python cnn_playground.py 256_256 256 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_256_256_0.001_16_PDBBind.out "python cnn_playground.py 512_256 256 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_256_256_0.001_16_PDBBind.out "python cnn_playground.py 512_512 256 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 256 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 256 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 256 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_256_256_0.01_16_PDBBind.out "python cnn_playground.py 256_256 256 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_256_256_0.01_16_PDBBind.out "python cnn_playground.py 512_256 256 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_256_256_0.01_16_PDBBind.out "python cnn_playground.py 512_512 256 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 256 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 256 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 256 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 256 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 256 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 256 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 256 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 256 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 256 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_512_512_0.005_16_PDBBind.out "python cnn_playground.py 256_256 256 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_512_512_0.005_16_PDBBind.out "python cnn_playground.py 512_256 256 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_512_512_0.005_16_PDBBind.out "python cnn_playground.py 512_512 256 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 256 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 256 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 256 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_512_512_0.001_16_PDBBind.out "python cnn_playground.py 256_256 256 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_512_512_0.001_16_PDBBind.out "python cnn_playground.py 512_256 256 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_512_512_0.001_16_PDBBind.out "python cnn_playground.py 512_512 256 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 256 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 256 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 256 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_512_512_0.01_16_PDBBind.out "python cnn_playground.py 256_256 256 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_512_512_0.01_16_PDBBind.out "python cnn_playground.py 512_256 256 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_512_512_0.01_16_PDBBind.out "python cnn_playground.py 512_512 256 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 256 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 256 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 256 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 256 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 256 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 256 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 256 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 256 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 256 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 256_256 256 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 512_256 256 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 512_512 256 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 256 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 256 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 256 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 256_256 256 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 512_256 256 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 512_512 256 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 256 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 256 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 256 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 256_256 256 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 512_256 256 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 512_512 256 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 256 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 256 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 256 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 512 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 512 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 512 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 512 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 512 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 512 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_128_128_0.005_16_PDBBind.out "python cnn_playground.py 256_256 512 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_128_128_0.005_16_PDBBind.out "python cnn_playground.py 512_256 512 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_128_128_0.005_16_PDBBind.out "python cnn_playground.py 512_512 512 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 512 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 512 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 512 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_128_128_0.001_16_PDBBind.out "python cnn_playground.py 256_256 512 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_128_128_0.001_16_PDBBind.out "python cnn_playground.py 512_256 512 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_128_128_0.001_16_PDBBind.out "python cnn_playground.py 512_512 512 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 512 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 512 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 512 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_128_128_0.01_16_PDBBind.out "python cnn_playground.py 256_256 512 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_128_128_0.01_16_PDBBind.out "python cnn_playground.py 512_256 512 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_128_128_0.01_16_PDBBind.out "python cnn_playground.py 512_512 512 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 512 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 512 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 512 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 512 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 512 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 512 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 512 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 512 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 512 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_256_256_0.005_16_PDBBind.out "python cnn_playground.py 256_256 512 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_256_256_0.005_16_PDBBind.out "python cnn_playground.py 512_256 512 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_256_256_0.005_16_PDBBind.out "python cnn_playground.py 512_512 512 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 512 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 512 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 512 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_256_256_0.001_16_PDBBind.out "python cnn_playground.py 256_256 512 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_256_256_0.001_16_PDBBind.out "python cnn_playground.py 512_256 512 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_256_256_0.001_16_PDBBind.out "python cnn_playground.py 512_512 512 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 512 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 512 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 512 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_256_256_0.01_16_PDBBind.out "python cnn_playground.py 256_256 512 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_256_256_0.01_16_PDBBind.out "python cnn_playground.py 512_256 512 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_256_256_0.01_16_PDBBind.out "python cnn_playground.py 512_512 512 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 512 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 512 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 512 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 512 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 512 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 512 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 512 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 512 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 512 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_512_512_0.005_16_PDBBind.out "python cnn_playground.py 256_256 512 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_512_512_0.005_16_PDBBind.out "python cnn_playground.py 512_256 512 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_512_512_0.005_16_PDBBind.out "python cnn_playground.py 512_512 512 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 512 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 512 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 512 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_512_512_0.001_16_PDBBind.out "python cnn_playground.py 256_256 512 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_512_512_0.001_16_PDBBind.out "python cnn_playground.py 512_256 512 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_512_512_0.001_16_PDBBind.out "python cnn_playground.py 512_512 512 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 512 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 512 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 512 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_512_512_0.01_16_PDBBind.out "python cnn_playground.py 256_256 512 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_512_512_0.01_16_PDBBind.out "python cnn_playground.py 512_256 512 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_512_512_0.01_16_PDBBind.out "python cnn_playground.py 512_512 512 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 512 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 512 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 512 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 512 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 512 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 512 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 512 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 512 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 512 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 256_256 512 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 512_256 512 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 512_512 512 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 512 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 512 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 512 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 256_256 512 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 512_256 512 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 512_512 512 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 512 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 512 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 512 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 256_256 512 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 512_256 512 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 512_512 512 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 512 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 512 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 512 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 1024 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 1024 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 1024 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 1024 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 1024 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_128_128_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 128_128 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_128_128_0.005_16_PDBBind.out "python cnn_playground.py 256_256 1024 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_128_128_0.005_16_PDBBind.out "python cnn_playground.py 512_256 1024 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_128_128_0.005_16_PDBBind.out "python cnn_playground.py 512_512 1024 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 1024 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 1024 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_128_128_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 128_128 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_128_128_0.001_16_PDBBind.out "python cnn_playground.py 256_256 1024 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_128_128_0.001_16_PDBBind.out "python cnn_playground.py 512_256 1024 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_128_128_0.001_16_PDBBind.out "python cnn_playground.py 512_512 1024 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 1024 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 1024 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_128_128_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 128_128 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_128_128_0.01_16_PDBBind.out "python cnn_playground.py 256_256 1024 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_128_128_0.01_16_PDBBind.out "python cnn_playground.py 512_256 1024 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_128_128_0.01_16_PDBBind.out "python cnn_playground.py 512_512 1024 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 1024 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 1024 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_128_128_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 128_128 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 1024 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 1024 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 1024 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 1024 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 1024 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_256_256_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 256_256 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_256_256_0.005_16_PDBBind.out "python cnn_playground.py 256_256 1024 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_256_256_0.005_16_PDBBind.out "python cnn_playground.py 512_256 1024 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_256_256_0.005_16_PDBBind.out "python cnn_playground.py 512_512 1024 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 1024 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 1024 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_256_256_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 256_256 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_256_256_0.001_16_PDBBind.out "python cnn_playground.py 256_256 1024 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_256_256_0.001_16_PDBBind.out "python cnn_playground.py 512_256 1024 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_256_256_0.001_16_PDBBind.out "python cnn_playground.py 512_512 1024 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 1024 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 1024 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_256_256_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 256_256 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_256_256_0.01_16_PDBBind.out "python cnn_playground.py 256_256 1024 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_256_256_0.01_16_PDBBind.out "python cnn_playground.py 512_256 1024 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_256_256_0.01_16_PDBBind.out "python cnn_playground.py 512_512 1024 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 1024 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 1024 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_256_256_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 256_256 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 1024 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 1024 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 1024 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 1024 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 1024 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_512_512_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 512_512 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_512_512_0.005_16_PDBBind.out "python cnn_playground.py 256_256 1024 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_512_512_0.005_16_PDBBind.out "python cnn_playground.py 512_256 1024 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_512_512_0.005_16_PDBBind.out "python cnn_playground.py 512_512 1024 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 1024 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 1024 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_512_512_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 512_512 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_512_512_0.001_16_PDBBind.out "python cnn_playground.py 256_256 1024 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_512_512_0.001_16_PDBBind.out "python cnn_playground.py 512_256 1024 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_512_512_0.001_16_PDBBind.out "python cnn_playground.py 512_512 1024 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 1024 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 1024 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_512_512_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 512_512 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_512_512_0.01_16_PDBBind.out "python cnn_playground.py 256_256 1024 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_512_512_0.01_16_PDBBind.out "python cnn_playground.py 512_256 1024 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_512_512_0.01_16_PDBBind.out "python cnn_playground.py 512_512 1024 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 1024 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 1024 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_512_512_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 512_512 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 256_256 1024 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 512_256 1024 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 512_512 1024 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_512 1024 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_256 1024 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_1024_1024_0.0001_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 1024_1024 0.0001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 256_256 1024 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 512_256 1024 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 512_512 1024 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_512 1024 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_256 1024 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_1024_1024_0.005_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 1024_1024 0.005 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 256_256 1024 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 512_256 1024 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 512_512 1024 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_512 1024 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_256 1024 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_1024_1024_0.001_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 1024_1024 0.001 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 256_256 1024 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 512_256 1024 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 512_512 1024 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_512 1024 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_256 1024 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_1024_1024_0.01_16_PDBBind.out "python cnn_playground.py 1024_1024 1024 1024_1024 0.01 16 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 64 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 64 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 64 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 64 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 64 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 64 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_128_128_0.005_32_PDBBind.out "python cnn_playground.py 256_256 64 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_128_128_0.005_32_PDBBind.out "python cnn_playground.py 512_256 64 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_128_128_0.005_32_PDBBind.out "python cnn_playground.py 512_512 64 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 64 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 64 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 64 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_128_128_0.001_32_PDBBind.out "python cnn_playground.py 256_256 64 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_128_128_0.001_32_PDBBind.out "python cnn_playground.py 512_256 64 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_128_128_0.001_32_PDBBind.out "python cnn_playground.py 512_512 64 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 64 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 64 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 64 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_128_128_0.01_32_PDBBind.out "python cnn_playground.py 256_256 64 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_128_128_0.01_32_PDBBind.out "python cnn_playground.py 512_256 64 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_128_128_0.01_32_PDBBind.out "python cnn_playground.py 512_512 64 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 64 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 64 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 64 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 64 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 64 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 64 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 64 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 64 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 64 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_256_256_0.005_32_PDBBind.out "python cnn_playground.py 256_256 64 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_256_256_0.005_32_PDBBind.out "python cnn_playground.py 512_256 64 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_256_256_0.005_32_PDBBind.out "python cnn_playground.py 512_512 64 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 64 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 64 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 64 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_256_256_0.001_32_PDBBind.out "python cnn_playground.py 256_256 64 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_256_256_0.001_32_PDBBind.out "python cnn_playground.py 512_256 64 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_256_256_0.001_32_PDBBind.out "python cnn_playground.py 512_512 64 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 64 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 64 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 64 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_256_256_0.01_32_PDBBind.out "python cnn_playground.py 256_256 64 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_256_256_0.01_32_PDBBind.out "python cnn_playground.py 512_256 64 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_256_256_0.01_32_PDBBind.out "python cnn_playground.py 512_512 64 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 64 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 64 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 64 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 64 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 64 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 64 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 64 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 64 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 64 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_512_512_0.005_32_PDBBind.out "python cnn_playground.py 256_256 64 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_512_512_0.005_32_PDBBind.out "python cnn_playground.py 512_256 64 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_512_512_0.005_32_PDBBind.out "python cnn_playground.py 512_512 64 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 64 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 64 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 64 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_512_512_0.001_32_PDBBind.out "python cnn_playground.py 256_256 64 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_512_512_0.001_32_PDBBind.out "python cnn_playground.py 512_256 64 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_512_512_0.001_32_PDBBind.out "python cnn_playground.py 512_512 64 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 64 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 64 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 64 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_512_512_0.01_32_PDBBind.out "python cnn_playground.py 256_256 64 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_512_512_0.01_32_PDBBind.out "python cnn_playground.py 512_256 64 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_512_512_0.01_32_PDBBind.out "python cnn_playground.py 512_512 64 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 64 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 64 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 64 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 64 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 64 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 64 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 64 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 64 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 64 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 256_256 64 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 512_256 64 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 512_512 64 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 64 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 64 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 64 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 256_256 64 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 512_256 64 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 512_512 64 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 64 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 64 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 64 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_64_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 256_256 64 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_64_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 512_256 64 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_64_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 512_512 64 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_64_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 64 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_64_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 64 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_64_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 64 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 128 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 128 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 128 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 128 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 128 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 128 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_128_128_0.005_32_PDBBind.out "python cnn_playground.py 256_256 128 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_128_128_0.005_32_PDBBind.out "python cnn_playground.py 512_256 128 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_128_128_0.005_32_PDBBind.out "python cnn_playground.py 512_512 128 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 128 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 128 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 128 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_128_128_0.001_32_PDBBind.out "python cnn_playground.py 256_256 128 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_128_128_0.001_32_PDBBind.out "python cnn_playground.py 512_256 128 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_128_128_0.001_32_PDBBind.out "python cnn_playground.py 512_512 128 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 128 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 128 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 128 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_128_128_0.01_32_PDBBind.out "python cnn_playground.py 256_256 128 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_128_128_0.01_32_PDBBind.out "python cnn_playground.py 512_256 128 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_128_128_0.01_32_PDBBind.out "python cnn_playground.py 512_512 128 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 128 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 128 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 128 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 128 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 128 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 128 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 128 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 128 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 128 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_256_256_0.005_32_PDBBind.out "python cnn_playground.py 256_256 128 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_256_256_0.005_32_PDBBind.out "python cnn_playground.py 512_256 128 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_256_256_0.005_32_PDBBind.out "python cnn_playground.py 512_512 128 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 128 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 128 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 128 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_256_256_0.001_32_PDBBind.out "python cnn_playground.py 256_256 128 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_256_256_0.001_32_PDBBind.out "python cnn_playground.py 512_256 128 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_256_256_0.001_32_PDBBind.out "python cnn_playground.py 512_512 128 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 128 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 128 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 128 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_256_256_0.01_32_PDBBind.out "python cnn_playground.py 256_256 128 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_256_256_0.01_32_PDBBind.out "python cnn_playground.py 512_256 128 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_256_256_0.01_32_PDBBind.out "python cnn_playground.py 512_512 128 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 128 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 128 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 128 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 128 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 128 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 128 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 128 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 128 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 128 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_512_512_0.005_32_PDBBind.out "python cnn_playground.py 256_256 128 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_512_512_0.005_32_PDBBind.out "python cnn_playground.py 512_256 128 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_512_512_0.005_32_PDBBind.out "python cnn_playground.py 512_512 128 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 128 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 128 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 128 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_512_512_0.001_32_PDBBind.out "python cnn_playground.py 256_256 128 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_512_512_0.001_32_PDBBind.out "python cnn_playground.py 512_256 128 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_512_512_0.001_32_PDBBind.out "python cnn_playground.py 512_512 128 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 128 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 128 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 128 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_512_512_0.01_32_PDBBind.out "python cnn_playground.py 256_256 128 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_512_512_0.01_32_PDBBind.out "python cnn_playground.py 512_256 128 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_512_512_0.01_32_PDBBind.out "python cnn_playground.py 512_512 128 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 128 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 128 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 128 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 128 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 128 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 128 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 128 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 128 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 128 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 256_256 128 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 512_256 128 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 512_512 128 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 128 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 128 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 128 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 256_256 128 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 512_256 128 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 512_512 128 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 128 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 128 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 128 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_128_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 256_256 128 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_128_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 512_256 128 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_128_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 512_512 128 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_128_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 128 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_128_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 128 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_128_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 128 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 256 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 256 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 256 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 256 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 256 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 256 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_128_128_0.005_32_PDBBind.out "python cnn_playground.py 256_256 256 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_128_128_0.005_32_PDBBind.out "python cnn_playground.py 512_256 256 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_128_128_0.005_32_PDBBind.out "python cnn_playground.py 512_512 256 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 256 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 256 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 256 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_128_128_0.001_32_PDBBind.out "python cnn_playground.py 256_256 256 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_128_128_0.001_32_PDBBind.out "python cnn_playground.py 512_256 256 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_128_128_0.001_32_PDBBind.out "python cnn_playground.py 512_512 256 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 256 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 256 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 256 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_128_128_0.01_32_PDBBind.out "python cnn_playground.py 256_256 256 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_128_128_0.01_32_PDBBind.out "python cnn_playground.py 512_256 256 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_128_128_0.01_32_PDBBind.out "python cnn_playground.py 512_512 256 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 256 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 256 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 256 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 256 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 256 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 256 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 256 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 256 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 256 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_256_256_0.005_32_PDBBind.out "python cnn_playground.py 256_256 256 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_256_256_0.005_32_PDBBind.out "python cnn_playground.py 512_256 256 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_256_256_0.005_32_PDBBind.out "python cnn_playground.py 512_512 256 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 256 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 256 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 256 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_256_256_0.001_32_PDBBind.out "python cnn_playground.py 256_256 256 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_256_256_0.001_32_PDBBind.out "python cnn_playground.py 512_256 256 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_256_256_0.001_32_PDBBind.out "python cnn_playground.py 512_512 256 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 256 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 256 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 256 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_256_256_0.01_32_PDBBind.out "python cnn_playground.py 256_256 256 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_256_256_0.01_32_PDBBind.out "python cnn_playground.py 512_256 256 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_256_256_0.01_32_PDBBind.out "python cnn_playground.py 512_512 256 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 256 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 256 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 256 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 256 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 256 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 256 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 256 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 256 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 256 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_512_512_0.005_32_PDBBind.out "python cnn_playground.py 256_256 256 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_512_512_0.005_32_PDBBind.out "python cnn_playground.py 512_256 256 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_512_512_0.005_32_PDBBind.out "python cnn_playground.py 512_512 256 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 256 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 256 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 256 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_512_512_0.001_32_PDBBind.out "python cnn_playground.py 256_256 256 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_512_512_0.001_32_PDBBind.out "python cnn_playground.py 512_256 256 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_512_512_0.001_32_PDBBind.out "python cnn_playground.py 512_512 256 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 256 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 256 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 256 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_512_512_0.01_32_PDBBind.out "python cnn_playground.py 256_256 256 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_512_512_0.01_32_PDBBind.out "python cnn_playground.py 512_256 256 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_512_512_0.01_32_PDBBind.out "python cnn_playground.py 512_512 256 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 256 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 256 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 256 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 256 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 256 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 256 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 256 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 256 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 256 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 256_256 256 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 512_256 256 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 512_512 256 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 256 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 256 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 256 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 256_256 256 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 512_256 256 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 512_512 256 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 256 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 256 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 256 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_256_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 256_256 256 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_256_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 512_256 256 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_256_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 512_512 256 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_256_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 256 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_256_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 256 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_256_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 256 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 512 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 512 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 512 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 512 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 512 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 512 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_128_128_0.005_32_PDBBind.out "python cnn_playground.py 256_256 512 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_128_128_0.005_32_PDBBind.out "python cnn_playground.py 512_256 512 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_128_128_0.005_32_PDBBind.out "python cnn_playground.py 512_512 512 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 512 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 512 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 512 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_128_128_0.001_32_PDBBind.out "python cnn_playground.py 256_256 512 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_128_128_0.001_32_PDBBind.out "python cnn_playground.py 512_256 512 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_128_128_0.001_32_PDBBind.out "python cnn_playground.py 512_512 512 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 512 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 512 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 512 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_128_128_0.01_32_PDBBind.out "python cnn_playground.py 256_256 512 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_128_128_0.01_32_PDBBind.out "python cnn_playground.py 512_256 512 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_128_128_0.01_32_PDBBind.out "python cnn_playground.py 512_512 512 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 512 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 512 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 512 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 512 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 512 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 512 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 512 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 512 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 512 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_256_256_0.005_32_PDBBind.out "python cnn_playground.py 256_256 512 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_256_256_0.005_32_PDBBind.out "python cnn_playground.py 512_256 512 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_256_256_0.005_32_PDBBind.out "python cnn_playground.py 512_512 512 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 512 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 512 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 512 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_256_256_0.001_32_PDBBind.out "python cnn_playground.py 256_256 512 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_256_256_0.001_32_PDBBind.out "python cnn_playground.py 512_256 512 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_256_256_0.001_32_PDBBind.out "python cnn_playground.py 512_512 512 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 512 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 512 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 512 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_256_256_0.01_32_PDBBind.out "python cnn_playground.py 256_256 512 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_256_256_0.01_32_PDBBind.out "python cnn_playground.py 512_256 512 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_256_256_0.01_32_PDBBind.out "python cnn_playground.py 512_512 512 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 512 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 512 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 512 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 512 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 512 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 512 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 512 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 512 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 512 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_512_512_0.005_32_PDBBind.out "python cnn_playground.py 256_256 512 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_512_512_0.005_32_PDBBind.out "python cnn_playground.py 512_256 512 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_512_512_0.005_32_PDBBind.out "python cnn_playground.py 512_512 512 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 512 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 512 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 512 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_512_512_0.001_32_PDBBind.out "python cnn_playground.py 256_256 512 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_512_512_0.001_32_PDBBind.out "python cnn_playground.py 512_256 512 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_512_512_0.001_32_PDBBind.out "python cnn_playground.py 512_512 512 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 512 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 512 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 512 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_512_512_0.01_32_PDBBind.out "python cnn_playground.py 256_256 512 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_512_512_0.01_32_PDBBind.out "python cnn_playground.py 512_256 512 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_512_512_0.01_32_PDBBind.out "python cnn_playground.py 512_512 512 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 512 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 512 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 512 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 512 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 512 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 512 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 512 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 512 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 512 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 256_256 512 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 512_256 512 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 512_512 512 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 512 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 512 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 512 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 256_256 512 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 512_256 512 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 512_512 512 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 512 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 512 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 512 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_512_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 256_256 512 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_512_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 512_256 512 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_512_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 512_512 512 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_512_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 512 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_512_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 512 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_512_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 512 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 1024 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 1024 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 1024 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 1024 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 1024 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_128_128_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 128_128 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_128_128_0.005_32_PDBBind.out "python cnn_playground.py 256_256 1024 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_128_128_0.005_32_PDBBind.out "python cnn_playground.py 512_256 1024 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_128_128_0.005_32_PDBBind.out "python cnn_playground.py 512_512 1024 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 1024 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 1024 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_128_128_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 128_128 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_128_128_0.001_32_PDBBind.out "python cnn_playground.py 256_256 1024 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_128_128_0.001_32_PDBBind.out "python cnn_playground.py 512_256 1024 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_128_128_0.001_32_PDBBind.out "python cnn_playground.py 512_512 1024 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 1024 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 1024 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_128_128_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 128_128 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_128_128_0.01_32_PDBBind.out "python cnn_playground.py 256_256 1024 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_128_128_0.01_32_PDBBind.out "python cnn_playground.py 512_256 1024 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_128_128_0.01_32_PDBBind.out "python cnn_playground.py 512_512 1024 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 1024 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 1024 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_128_128_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 128_128 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 1024 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 1024 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 1024 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 1024 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 1024 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_256_256_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 256_256 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_256_256_0.005_32_PDBBind.out "python cnn_playground.py 256_256 1024 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_256_256_0.005_32_PDBBind.out "python cnn_playground.py 512_256 1024 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_256_256_0.005_32_PDBBind.out "python cnn_playground.py 512_512 1024 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 1024 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 1024 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_256_256_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 256_256 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_256_256_0.001_32_PDBBind.out "python cnn_playground.py 256_256 1024 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_256_256_0.001_32_PDBBind.out "python cnn_playground.py 512_256 1024 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_256_256_0.001_32_PDBBind.out "python cnn_playground.py 512_512 1024 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 1024 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 1024 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_256_256_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 256_256 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_256_256_0.01_32_PDBBind.out "python cnn_playground.py 256_256 1024 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_256_256_0.01_32_PDBBind.out "python cnn_playground.py 512_256 1024 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_256_256_0.01_32_PDBBind.out "python cnn_playground.py 512_512 1024 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 1024 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 1024 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_256_256_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 256_256 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 1024 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 1024 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 1024 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 1024 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 1024 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_512_512_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 512_512 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_512_512_0.005_32_PDBBind.out "python cnn_playground.py 256_256 1024 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_512_512_0.005_32_PDBBind.out "python cnn_playground.py 512_256 1024 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_512_512_0.005_32_PDBBind.out "python cnn_playground.py 512_512 1024 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 1024 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 1024 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_512_512_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 512_512 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_512_512_0.001_32_PDBBind.out "python cnn_playground.py 256_256 1024 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_512_512_0.001_32_PDBBind.out "python cnn_playground.py 512_256 1024 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_512_512_0.001_32_PDBBind.out "python cnn_playground.py 512_512 1024 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 1024 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 1024 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_512_512_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 512_512 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_512_512_0.01_32_PDBBind.out "python cnn_playground.py 256_256 1024 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_512_512_0.01_32_PDBBind.out "python cnn_playground.py 512_256 1024 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_512_512_0.01_32_PDBBind.out "python cnn_playground.py 512_512 1024 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 1024 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 1024 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_512_512_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 512_512 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 256_256 1024 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 512_256 1024 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 512_512 1024 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_512 1024 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_256 1024 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_1024_1024_0.0001_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 1024_1024 0.0001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 256_256 1024 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 512_256 1024 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 512_512 1024 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_512 1024 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_256 1024 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_1024_1024_0.005_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 1024_1024 0.005 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 256_256 1024 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 512_256 1024 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 512_512 1024 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_512 1024 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_256 1024 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_1024_1024_0.001_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 1024_1024 0.001 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_256_256_1024_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 256_256 1024 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_256_1024_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 512_256 1024 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_512_512_1024_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 512_512 1024 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_512_1024_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_512 1024 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_256_1024_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_256 1024 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
bsub -g /my_small_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 20480 -R 'rusage[mem=20480]' -o ../log_files/pdbbind_experiment_07062019/500_1024_1024_1024_1024_1024_0.01_32_PDBBind.out "python cnn_playground.py 1024_1024 1024 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix500"
sleep 1
