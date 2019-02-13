import subprocess
subprocess.call("python dream_challenge.py PINN_2_2 ecfp4 k-sep-bigrams_trigram 512_128 512_128 64 64 0.0005 idg_comp_targ_uniq_inter_filtered.csv r", shell=True)
