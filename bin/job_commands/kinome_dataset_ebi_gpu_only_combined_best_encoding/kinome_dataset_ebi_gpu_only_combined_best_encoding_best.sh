chmod +x ./3_1.sh
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/3_1.out "./3_1.sh"
chmod +x ./4_1.sh
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/4_1.out "./4_1.sh"
chmod +x ./7_1.sh
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/7_1.out "./7_1.sh"
chmod +x ./8_1.sh
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/8_1.out "./8_1.sh"
chmod +x ./23_1.sh
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/23_1.out "./23_1.sh"
chmod +x ./39_1.sh
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/39_1.out "./39_1.sh"
chmod +x ./40_1.sh
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/40_1.out "./40_1.sh"
chmod +x ./55_1.sh
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 15360 -R 'rusage[mem=15360]' -o ../../../log_files/kinome_dataset_ebi_gpu_only_combined_best_encoding/55_1.out "./55_1.sh"
