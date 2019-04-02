bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_256_256_0.0001_16_DeepDTA_davis.out "python cnn_playground.py 1000_64 256_256 0.0001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_256_256_0.0001_32_DeepDTA_davis.out "python cnn_playground.py 1000_64 256_256 0.0001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_256_256_0.005_16_DeepDTA_davis.out "python cnn_playground.py 1000_64 256_256 0.005 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_256_256_0.005_32_DeepDTA_davis.out "python cnn_playground.py 1000_64 256_256 0.005 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_256_256_0.001_16_DeepDTA_davis.out "python cnn_playground.py 1000_64 256_256 0.001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_256_256_0.001_32_DeepDTA_davis.out "python cnn_playground.py 1000_64 256_256 0.001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_1024_1024_0.0001_16_DeepDTA_davis.out "python cnn_playground.py 1000_64 1024_1024 0.0001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_1024_1024_0.0001_32_DeepDTA_davis.out "python cnn_playground.py 1000_64 1024_1024 0.0001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_1024_1024_0.005_16_DeepDTA_davis.out "python cnn_playground.py 1000_64 1024_1024 0.005 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_1024_1024_0.005_32_DeepDTA_davis.out "python cnn_playground.py 1000_64 1024_1024 0.005 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_1024_1024_0.001_16_DeepDTA_davis.out "python cnn_playground.py 1000_64 1024_1024 0.001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_1024_1024_0.001_32_DeepDTA_davis.out "python cnn_playground.py 1000_64 1024_1024 0.001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_512_512_0.0001_16_DeepDTA_davis.out "python cnn_playground.py 1000_64 512_512 0.0001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_512_512_0.0001_32_DeepDTA_davis.out "python cnn_playground.py 1000_64 512_512 0.0001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_512_512_0.005_16_DeepDTA_davis.out "python cnn_playground.py 1000_64 512_512 0.005 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_512_512_0.005_32_DeepDTA_davis.out "python cnn_playground.py 1000_64 512_512 0.005 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_512_512_0.001_16_DeepDTA_davis.out "python cnn_playground.py 1000_64 512_512 0.001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_64_512_512_0.001_32_DeepDTA_davis.out "python cnn_playground.py 1000_64 512_512 0.001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_256_256_0.0001_16_DeepDTA_davis.out "python cnn_playground.py 1000_128 256_256 0.0001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_256_256_0.0001_32_DeepDTA_davis.out "python cnn_playground.py 1000_128 256_256 0.0001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_256_256_0.005_16_DeepDTA_davis.out "python cnn_playground.py 1000_128 256_256 0.005 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_256_256_0.005_32_DeepDTA_davis.out "python cnn_playground.py 1000_128 256_256 0.005 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_256_256_0.001_16_DeepDTA_davis.out "python cnn_playground.py 1000_128 256_256 0.001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_256_256_0.001_32_DeepDTA_davis.out "python cnn_playground.py 1000_128 256_256 0.001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_1024_1024_0.0001_16_DeepDTA_davis.out "python cnn_playground.py 1000_128 1024_1024 0.0001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_1024_1024_0.0001_32_DeepDTA_davis.out "python cnn_playground.py 1000_128 1024_1024 0.0001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_1024_1024_0.005_16_DeepDTA_davis.out "python cnn_playground.py 1000_128 1024_1024 0.005 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_1024_1024_0.005_32_DeepDTA_davis.out "python cnn_playground.py 1000_128 1024_1024 0.005 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_1024_1024_0.001_16_DeepDTA_davis.out "python cnn_playground.py 1000_128 1024_1024 0.001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_1024_1024_0.001_32_DeepDTA_davis.out "python cnn_playground.py 1000_128 1024_1024 0.001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_512_512_0.0001_16_DeepDTA_davis.out "python cnn_playground.py 1000_128 512_512 0.0001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_512_512_0.0001_32_DeepDTA_davis.out "python cnn_playground.py 1000_128 512_512 0.0001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_512_512_0.005_16_DeepDTA_davis.out "python cnn_playground.py 1000_128 512_512 0.005 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_512_512_0.005_32_DeepDTA_davis.out "python cnn_playground.py 1000_128 512_512 0.005 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_512_512_0.001_16_DeepDTA_davis.out "python cnn_playground.py 1000_128 512_512 0.001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_128_512_512_0.001_32_DeepDTA_davis.out "python cnn_playground.py 1000_128 512_512 0.001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_256_256_0.0001_16_DeepDTA_davis.out "python cnn_playground.py 1000_256 256_256 0.0001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_256_256_0.0001_32_DeepDTA_davis.out "python cnn_playground.py 1000_256 256_256 0.0001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_256_256_0.005_16_DeepDTA_davis.out "python cnn_playground.py 1000_256 256_256 0.005 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_256_256_0.005_32_DeepDTA_davis.out "python cnn_playground.py 1000_256 256_256 0.005 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_256_256_0.001_16_DeepDTA_davis.out "python cnn_playground.py 1000_256 256_256 0.001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_256_256_0.001_32_DeepDTA_davis.out "python cnn_playground.py 1000_256 256_256 0.001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_1024_1024_0.0001_16_DeepDTA_davis.out "python cnn_playground.py 1000_256 1024_1024 0.0001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_1024_1024_0.0001_32_DeepDTA_davis.out "python cnn_playground.py 1000_256 1024_1024 0.0001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_1024_1024_0.005_16_DeepDTA_davis.out "python cnn_playground.py 1000_256 1024_1024 0.005 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_1024_1024_0.005_32_DeepDTA_davis.out "python cnn_playground.py 1000_256 1024_1024 0.005 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_1024_1024_0.001_16_DeepDTA_davis.out "python cnn_playground.py 1000_256 1024_1024 0.001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_1024_1024_0.001_32_DeepDTA_davis.out "python cnn_playground.py 1000_256 1024_1024 0.001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_512_512_0.0001_16_DeepDTA_davis.out "python cnn_playground.py 1000_256 512_512 0.0001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_512_512_0.0001_32_DeepDTA_davis.out "python cnn_playground.py 1000_256 512_512 0.0001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_512_512_0.005_16_DeepDTA_davis.out "python cnn_playground.py 1000_256 512_512 0.005 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_512_512_0.005_32_DeepDTA_davis.out "python cnn_playground.py 1000_256 512_512 0.005 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_512_512_0.001_16_DeepDTA_davis.out "python cnn_playground.py 1000_256 512_512 0.001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_256_512_512_0.001_32_DeepDTA_davis.out "python cnn_playground.py 1000_256 512_512 0.001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_256_256_0.0001_16_DeepDTA_davis.out "python cnn_playground.py 1000_512 256_256 0.0001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_256_256_0.0001_32_DeepDTA_davis.out "python cnn_playground.py 1000_512 256_256 0.0001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_256_256_0.005_16_DeepDTA_davis.out "python cnn_playground.py 1000_512 256_256 0.005 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_256_256_0.005_32_DeepDTA_davis.out "python cnn_playground.py 1000_512 256_256 0.005 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_256_256_0.001_16_DeepDTA_davis.out "python cnn_playground.py 1000_512 256_256 0.001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_256_256_0.001_32_DeepDTA_davis.out "python cnn_playground.py 1000_512 256_256 0.001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_1024_1024_0.0001_16_DeepDTA_davis.out "python cnn_playground.py 1000_512 1024_1024 0.0001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_1024_1024_0.0001_32_DeepDTA_davis.out "python cnn_playground.py 1000_512 1024_1024 0.0001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_1024_1024_0.005_16_DeepDTA_davis.out "python cnn_playground.py 1000_512 1024_1024 0.005 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_1024_1024_0.005_32_DeepDTA_davis.out "python cnn_playground.py 1000_512 1024_1024 0.005 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_1024_1024_0.001_16_DeepDTA_davis.out "python cnn_playground.py 1000_512 1024_1024 0.001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_1024_1024_0.001_32_DeepDTA_davis.out "python cnn_playground.py 1000_512 1024_1024 0.001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_512_512_0.0001_16_DeepDTA_davis.out "python cnn_playground.py 1000_512 512_512 0.0001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_512_512_0.0001_32_DeepDTA_davis.out "python cnn_playground.py 1000_512 512_512 0.0001 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_512_512_0.005_16_DeepDTA_davis.out "python cnn_playground.py 1000_512 512_512 0.005 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_512_512_0.005_32_DeepDTA_davis.out "python cnn_playground.py 1000_512 512_512 0.005 32 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_512_512_0.001_16_DeepDTA_davis.out "python cnn_playground.py 1000_512 512_512 0.001 16 DeepDTA_davis"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 20480 -R 'rusage[mem=20480]' -o 1000_512_512_512_0.001_32_DeepDTA_davis.out "python cnn_playground.py 1000_512 512_512 0.001 32 DeepDTA_davis"
sleep 1