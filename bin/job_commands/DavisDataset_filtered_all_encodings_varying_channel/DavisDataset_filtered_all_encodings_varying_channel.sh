chmod +x ./1_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/1_20.out "./1_20.sh"
chmod +x ./2_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/2_20.out "./2_20.sh"
chmod +x ./3_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/3_20.out "./3_20.sh"
chmod +x ./4_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/4_20.out "./4_20.sh"
chmod +x ./5_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/5_20.out "./5_20.sh"
chmod +x ./6_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/6_20.out "./6_20.sh"
chmod +x ./7_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/7_20.out "./7_20.sh"
chmod +x ./8_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/8_20.out "./8_20.sh"
chmod +x ./9_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/9_20.out "./9_20.sh"
chmod +x ./10_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/10_20.out "./10_20.sh"
chmod +x ./11_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/11_20.out "./11_20.sh"
chmod +x ./12_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/12_20.out "./12_20.sh"
chmod +x ./13_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/13_20.out "./13_20.sh"
chmod +x ./14_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/14_20.out "./14_20.sh"
chmod +x ./15_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/15_20.out "./15_20.sh"
chmod +x ./16_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/16_20.out "./16_20.sh"
chmod +x ./17_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/17_20.out "./17_20.sh"
chmod +x ./18_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/18_20.out "./18_20.sh"
chmod +x ./19_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/19_20.out "./19_20.sh"
chmod +x ./20_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/20_20.out "./20_20.sh"
chmod +x ./21_20.sh
bsub -q research-rh74 -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/21_20.out "./21_20.sh"
chmod +x ./22_20.sh
bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 5120 -R 'rusage[mem=5120]' -o ../../../log_files/DavisDataset_filtered_all_encodings_varying_channel/22.out "./22.sh"
