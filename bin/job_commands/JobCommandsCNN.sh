bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.0001_32.out "python cnn_playground.py 64 256_256 0.0001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.0001_64.out "python cnn_playground.py 64 256_256 0.0001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.0001_128.out "python cnn_playground.py 64 256_256 0.0001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.005_32.out "python cnn_playground.py 64 256_256 0.005 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.005_64.out "python cnn_playground.py 64 256_256 0.005 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.005_128.out "python cnn_playground.py 64 256_256 0.005 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.001_32.out "python cnn_playground.py 64 256_256 0.001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.001_64.out "python cnn_playground.py 64 256_256 0.001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_256_256_0.001_128.out "python cnn_playground.py 64 256_256 0.001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.0001_32.out "python cnn_playground.py 64 1024_1024 0.0001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.0001_64.out "python cnn_playground.py 64 1024_1024 0.0001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.0001_128.out "python cnn_playground.py 64 1024_1024 0.0001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.005_32.out "python cnn_playground.py 64 1024_1024 0.005 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.005_64.out "python cnn_playground.py 64 1024_1024 0.005 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.005_128.out "python cnn_playground.py 64 1024_1024 0.005 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.001_32.out "python cnn_playground.py 64 1024_1024 0.001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.001_64.out "python cnn_playground.py 64 1024_1024 0.001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_1024_1024_0.001_128.out "python cnn_playground.py 64 1024_1024 0.001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.0001_32.out "python cnn_playground.py 64 512_512 0.0001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.0001_64.out "python cnn_playground.py 64 512_512 0.0001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.0001_128.out "python cnn_playground.py 64 512_512 0.0001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.005_32.out "python cnn_playground.py 64 512_512 0.005 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.005_64.out "python cnn_playground.py 64 512_512 0.005 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.005_128.out "python cnn_playground.py 64 512_512 0.005 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.001_32.out "python cnn_playground.py 64 512_512 0.001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.001_64.out "python cnn_playground.py 64 512_512 0.001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 64_512_512_0.001_128.out "python cnn_playground.py 64 512_512 0.001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.0001_32.out "python cnn_playground.py 128 256_256 0.0001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.0001_64.out "python cnn_playground.py 128 256_256 0.0001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.0001_128.out "python cnn_playground.py 128 256_256 0.0001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.005_32.out "python cnn_playground.py 128 256_256 0.005 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.005_64.out "python cnn_playground.py 128 256_256 0.005 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.005_128.out "python cnn_playground.py 128 256_256 0.005 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.001_32.out "python cnn_playground.py 128 256_256 0.001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.001_64.out "python cnn_playground.py 128 256_256 0.001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_256_256_0.001_128.out "python cnn_playground.py 128 256_256 0.001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.0001_32.out "python cnn_playground.py 128 1024_1024 0.0001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.0001_64.out "python cnn_playground.py 128 1024_1024 0.0001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.0001_128.out "python cnn_playground.py 128 1024_1024 0.0001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.005_32.out "python cnn_playground.py 128 1024_1024 0.005 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.005_64.out "python cnn_playground.py 128 1024_1024 0.005 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.005_128.out "python cnn_playground.py 128 1024_1024 0.005 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.001_32.out "python cnn_playground.py 128 1024_1024 0.001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.001_64.out "python cnn_playground.py 128 1024_1024 0.001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_1024_1024_0.001_128.out "python cnn_playground.py 128 1024_1024 0.001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.0001_32.out "python cnn_playground.py 128 512_512 0.0001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.0001_64.out "python cnn_playground.py 128 512_512 0.0001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.0001_128.out "python cnn_playground.py 128 512_512 0.0001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.005_32.out "python cnn_playground.py 128 512_512 0.005 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.005_64.out "python cnn_playground.py 128 512_512 0.005 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.005_128.out "python cnn_playground.py 128 512_512 0.005 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.001_32.out "python cnn_playground.py 128 512_512 0.001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.001_64.out "python cnn_playground.py 128 512_512 0.001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 128_512_512_0.001_128.out "python cnn_playground.py 128 512_512 0.001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.0001_32.out "python cnn_playground.py 256 256_256 0.0001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.0001_64.out "python cnn_playground.py 256 256_256 0.0001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.0001_128.out "python cnn_playground.py 256 256_256 0.0001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.005_32.out "python cnn_playground.py 256 256_256 0.005 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.005_64.out "python cnn_playground.py 256 256_256 0.005 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.005_128.out "python cnn_playground.py 256 256_256 0.005 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.001_32.out "python cnn_playground.py 256 256_256 0.001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.001_64.out "python cnn_playground.py 256 256_256 0.001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_256_256_0.001_128.out "python cnn_playground.py 256 256_256 0.001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.0001_32.out "python cnn_playground.py 256 1024_1024 0.0001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.0001_64.out "python cnn_playground.py 256 1024_1024 0.0001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.0001_128.out "python cnn_playground.py 256 1024_1024 0.0001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.005_32.out "python cnn_playground.py 256 1024_1024 0.005 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.005_64.out "python cnn_playground.py 256 1024_1024 0.005 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.005_128.out "python cnn_playground.py 256 1024_1024 0.005 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.001_32.out "python cnn_playground.py 256 1024_1024 0.001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.001_64.out "python cnn_playground.py 256 1024_1024 0.001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_1024_1024_0.001_128.out "python cnn_playground.py 256 1024_1024 0.001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.0001_32.out "python cnn_playground.py 256 512_512 0.0001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.0001_64.out "python cnn_playground.py 256 512_512 0.0001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.0001_128.out "python cnn_playground.py 256 512_512 0.0001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.005_32.out "python cnn_playground.py 256 512_512 0.005 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.005_64.out "python cnn_playground.py 256 512_512 0.005 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.005_128.out "python cnn_playground.py 256 512_512 0.005 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.001_32.out "python cnn_playground.py 256 512_512 0.001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.001_64.out "python cnn_playground.py 256 512_512 0.001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 256_512_512_0.001_128.out "python cnn_playground.py 256 512_512 0.001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.0001_32.out "python cnn_playground.py 512 256_256 0.0001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.0001_64.out "python cnn_playground.py 512 256_256 0.0001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.0001_128.out "python cnn_playground.py 512 256_256 0.0001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.005_32.out "python cnn_playground.py 512 256_256 0.005 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.005_64.out "python cnn_playground.py 512 256_256 0.005 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.005_128.out "python cnn_playground.py 512 256_256 0.005 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.001_32.out "python cnn_playground.py 512 256_256 0.001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.001_64.out "python cnn_playground.py 512 256_256 0.001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_256_256_0.001_128.out "python cnn_playground.py 512 256_256 0.001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.0001_32.out "python cnn_playground.py 512 1024_1024 0.0001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.0001_64.out "python cnn_playground.py 512 1024_1024 0.0001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.0001_128.out "python cnn_playground.py 512 1024_1024 0.0001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.005_32.out "python cnn_playground.py 512 1024_1024 0.005 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.005_64.out "python cnn_playground.py 512 1024_1024 0.005 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.005_128.out "python cnn_playground.py 512 1024_1024 0.005 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.001_32.out "python cnn_playground.py 512 1024_1024 0.001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.001_64.out "python cnn_playground.py 512 1024_1024 0.001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_1024_1024_0.001_128.out "python cnn_playground.py 512 1024_1024 0.001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.0001_32.out "python cnn_playground.py 512 512_512 0.0001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.0001_64.out "python cnn_playground.py 512 512_512 0.0001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.0001_128.out "python cnn_playground.py 512 512_512 0.0001 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.005_32.out "python cnn_playground.py 512 512_512 0.005 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.005_64.out "python cnn_playground.py 512 512_512 0.005 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.005_128.out "python cnn_playground.py 512 512_512 0.005 128"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.001_32.out "python cnn_playground.py 512 512_512 0.001 32"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.001_64.out "python cnn_playground.py 512 512_512 0.001 64"
sleep 1
bsub -q research-rh74 -P gpu -gpu - -M 5120 -R 'rusage[mem=5120]' -o 512_512_512_0.001_128.out "python cnn_playground.py 512 512_512 0.001 128"
sleep 1
