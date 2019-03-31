bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.0001_16_DeepDTA_kiba.out "python cnn_playground.py 64 256_256 0.0001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.0001_32_DeepDTA_kiba.out "python cnn_playground.py 64 256_256 0.0001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.005_16_DeepDTA_kiba.out "python cnn_playground.py 64 256_256 0.005 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.005_32_DeepDTA_kiba.out "python cnn_playground.py 64 256_256 0.005 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.001_16_DeepDTA_kiba.out "python cnn_playground.py 64 256_256 0.001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.001_32_DeepDTA_kiba.out "python cnn_playground.py 64 256_256 0.001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.0001_16_DeepDTA_kiba.out "python cnn_playground.py 64 1024_1024 0.0001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.0001_32_DeepDTA_kiba.out "python cnn_playground.py 64 1024_1024 0.0001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.005_16_DeepDTA_kiba.out "python cnn_playground.py 64 1024_1024 0.005 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.005_32_DeepDTA_kiba.out "python cnn_playground.py 64 1024_1024 0.005 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.001_16_DeepDTA_kiba.out "python cnn_playground.py 64 1024_1024 0.001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.001_32_DeepDTA_kiba.out "python cnn_playground.py 64 1024_1024 0.001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.0001_16_DeepDTA_kiba.out "python cnn_playground.py 64 512_512 0.0001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.0001_32_DeepDTA_kiba.out "python cnn_playground.py 64 512_512 0.0001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.005_16_DeepDTA_kiba.out "python cnn_playground.py 64 512_512 0.005 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.005_32_DeepDTA_kiba.out "python cnn_playground.py 64 512_512 0.005 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.001_16_DeepDTA_kiba.out "python cnn_playground.py 64 512_512 0.001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.001_32_DeepDTA_kiba.out "python cnn_playground.py 64 512_512 0.001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.0001_16_DeepDTA_kiba.out "python cnn_playground.py 128 256_256 0.0001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.0001_32_DeepDTA_kiba.out "python cnn_playground.py 128 256_256 0.0001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.005_16_DeepDTA_kiba.out "python cnn_playground.py 128 256_256 0.005 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.005_32_DeepDTA_kiba.out "python cnn_playground.py 128 256_256 0.005 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.001_16_DeepDTA_kiba.out "python cnn_playground.py 128 256_256 0.001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.001_32_DeepDTA_kiba.out "python cnn_playground.py 128 256_256 0.001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.0001_16_DeepDTA_kiba.out "python cnn_playground.py 128 1024_1024 0.0001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.0001_32_DeepDTA_kiba.out "python cnn_playground.py 128 1024_1024 0.0001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.005_16_DeepDTA_kiba.out "python cnn_playground.py 128 1024_1024 0.005 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.005_32_DeepDTA_kiba.out "python cnn_playground.py 128 1024_1024 0.005 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.001_16_DeepDTA_kiba.out "python cnn_playground.py 128 1024_1024 0.001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.001_32_DeepDTA_kiba.out "python cnn_playground.py 128 1024_1024 0.001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.0001_16_DeepDTA_kiba.out "python cnn_playground.py 128 512_512 0.0001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.0001_32_DeepDTA_kiba.out "python cnn_playground.py 128 512_512 0.0001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.005_16_DeepDTA_kiba.out "python cnn_playground.py 128 512_512 0.005 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.005_32_DeepDTA_kiba.out "python cnn_playground.py 128 512_512 0.005 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.001_16_DeepDTA_kiba.out "python cnn_playground.py 128 512_512 0.001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.001_32_DeepDTA_kiba.out "python cnn_playground.py 128 512_512 0.001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.0001_16_DeepDTA_kiba.out "python cnn_playground.py 256 256_256 0.0001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.0001_32_DeepDTA_kiba.out "python cnn_playground.py 256 256_256 0.0001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.005_16_DeepDTA_kiba.out "python cnn_playground.py 256 256_256 0.005 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.005_32_DeepDTA_kiba.out "python cnn_playground.py 256 256_256 0.005 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.001_16_DeepDTA_kiba.out "python cnn_playground.py 256 256_256 0.001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.001_32_DeepDTA_kiba.out "python cnn_playground.py 256 256_256 0.001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.0001_16_DeepDTA_kiba.out "python cnn_playground.py 256 1024_1024 0.0001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.0001_32_DeepDTA_kiba.out "python cnn_playground.py 256 1024_1024 0.0001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.005_16_DeepDTA_kiba.out "python cnn_playground.py 256 1024_1024 0.005 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.005_32_DeepDTA_kiba.out "python cnn_playground.py 256 1024_1024 0.005 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.001_16_DeepDTA_kiba.out "python cnn_playground.py 256 1024_1024 0.001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.001_32_DeepDTA_kiba.out "python cnn_playground.py 256 1024_1024 0.001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.0001_16_DeepDTA_kiba.out "python cnn_playground.py 256 512_512 0.0001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.0001_32_DeepDTA_kiba.out "python cnn_playground.py 256 512_512 0.0001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.005_16_DeepDTA_kiba.out "python cnn_playground.py 256 512_512 0.005 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.005_32_DeepDTA_kiba.out "python cnn_playground.py 256 512_512 0.005 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.001_16_DeepDTA_kiba.out "python cnn_playground.py 256 512_512 0.001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.001_32_DeepDTA_kiba.out "python cnn_playground.py 256 512_512 0.001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.0001_16_DeepDTA_kiba.out "python cnn_playground.py 512 256_256 0.0001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.0001_32_DeepDTA_kiba.out "python cnn_playground.py 512 256_256 0.0001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.005_16_DeepDTA_kiba.out "python cnn_playground.py 512 256_256 0.005 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.005_32_DeepDTA_kiba.out "python cnn_playground.py 512 256_256 0.005 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.001_16_DeepDTA_kiba.out "python cnn_playground.py 512 256_256 0.001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.001_32_DeepDTA_kiba.out "python cnn_playground.py 512 256_256 0.001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.0001_16_DeepDTA_kiba.out "python cnn_playground.py 512 1024_1024 0.0001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.0001_32_DeepDTA_kiba.out "python cnn_playground.py 512 1024_1024 0.0001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.005_16_DeepDTA_kiba.out "python cnn_playground.py 512 1024_1024 0.005 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.005_32_DeepDTA_kiba.out "python cnn_playground.py 512 1024_1024 0.005 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.001_16_DeepDTA_kiba.out "python cnn_playground.py 512 1024_1024 0.001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.001_32_DeepDTA_kiba.out "python cnn_playground.py 512 1024_1024 0.001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.0001_16_DeepDTA_kiba.out "python cnn_playground.py 512 512_512 0.0001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.0001_32_DeepDTA_kiba.out "python cnn_playground.py 512 512_512 0.0001 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.005_16_DeepDTA_kiba.out "python cnn_playground.py 512 512_512 0.005 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.005_32_DeepDTA_kiba.out "python cnn_playground.py 512 512_512 0.005 32 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.001_16_DeepDTA_kiba.out "python cnn_playground.py 512 512_512 0.001 16 DeepDTA_kiba"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.001_32_DeepDTA_kiba.out "python cnn_playground.py 512 512_512 0.001 32 DeepDTA_kiba"
sleep 1
