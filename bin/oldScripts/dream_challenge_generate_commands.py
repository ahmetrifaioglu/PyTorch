
from itertools import permutations, combinations
import subprocess
def generateFirstCommands(n_of_comp_h_layers, n_of_tar_h_layers):
    comp_feature_list = ["ecfp4"] #, "fcfp4", "rdk5"]
    #comp_feature_list = ["ecfp4",]
    #tar_feature_list = ["k-sep-bigrams", "APAAC", "DDE", "pfam"]
    tar_feature_list = ["k-sep-bigrams", "trigram"]#, "DDE", "pfam"]
    #tar_feature_list = ["k-sep-bigrams", "APAAC", "DDE", "pfam"]

    lst_idg_files = ["idg_comp_targ_uniq_inter_filtered_AGC.csv", "idg_comp_targ_uniq_inter_filtered_CAMK.csv",
                     "idg_comp_targ_uniq_inter_filtered_CMGC.csv", "idg_comp_targ_uniq_inter_filtered_other.csv",
                     "idg_comp_targ_uniq_inter_filtered_STE.csv", "idg_comp_targ_uniq_inter_filtered_TK.csv",
                     "idg_comp_targ_uniq_inter_filtered_TKL.csv"]

    lst_idg_files = ["idg_comp_targ_uniq_inter_filtered.csv"]

    lst_learning_rate = [0.0001, 0.005, 0.001, 0.0005]
    comb_comp_feat_list = []
    comb_tar_feat_list = []

    for i in range(3):
        lst_cand_comp_list = list(combinations(comp_feature_list,i+1))

        for cand in lst_cand_comp_list:
            str_comp_feat = ""
            for feat in cand:
                str_comp_feat += "{}_".format(feat)
            str_comp_feat =str_comp_feat[:-1]

            comb_comp_feat_list.append(str_comp_feat)

    for i in range(2):
        lst_cand_tar_list = list(combinations(tar_feature_list, i + 1))

        for cand in lst_cand_tar_list:
            str_tar_feat = ""
            for feat in cand:
                str_tar_feat += "{}_".format(feat)
            str_tar_feat = str_tar_feat[:-1]

            comb_tar_feat_list.append(str_tar_feat)


    # print(comb_comp_feat_list)
    # print(comb_tar_feat_list)
    n_of_neuron_list_h = [2048, 1536, 1024, 512, 128]
    n_of_neuron_list_fc = [1024, 512, 256, 64]
    model_types = ["PINN_{}_{}".format(n_of_comp_h_layers, n_of_tar_h_layers)]
    # n_of_h_comp_layers = n_of_comp_h_layers
    # n_of_h_tar_layers = n_of_tar_h_layers
    n_of_fc_layers = 2

    lst_n_comp_permutations = list(permutations(n_of_neuron_list_h, n_of_comp_h_layers))


    lst_comp_decreasing_permutations = []
    for perm in lst_n_comp_permutations:
        is_decreasing = True
        perm_ind = 0

        while perm_ind+1<(len(perm)):
            if perm[perm_ind]<perm[perm_ind+1]:
                is_decreasing = False
                break
            perm_ind += 1

        if is_decreasing:
            str_decreasing = ""
            for neur in perm:
                str_decreasing += "{}_".format(neur)
                #print(str_decreasing)
            str_decreasing = str_decreasing[:-1]
            lst_comp_decreasing_permutations.append(str_decreasing)

    lst_n_tar_permutations = list(permutations(n_of_neuron_list_h, n_of_tar_h_layers))
    lst_tar_decreasing_permutations = []
    for perm in lst_n_tar_permutations:
        is_decreasing = True
        perm_ind = 0

        while perm_ind + 1 < (len(perm)):
            if perm[perm_ind] < perm[perm_ind + 1]:
                is_decreasing = False
                break
            perm_ind += 1

        if is_decreasing:
            str_decreasing = ""
            for neur in perm:
                str_decreasing += "{}_".format(neur)
                # print(str_decreasing)
            str_decreasing = str_decreasing[:-1]
            lst_tar_decreasing_permutations.append(str_decreasing)
    print(lst_comp_decreasing_permutations)
    print(lst_tar_decreasing_permutations)


    lst_commands = []
    count = 0
    cmd_fl_count = 1
    for mod in model_types:
        for comp_feat in comb_comp_feat_list:
            for tar_feat in comb_tar_feat_list:
                for hidden_comp in lst_comp_decreasing_permutations:
                    for hidden_tar in lst_tar_decreasing_permutations:

                        for fc in n_of_neuron_list_fc:
                            for lr in lst_learning_rate:
                                for idg_fl in lst_idg_files:
                                    count += 1
                                    # if count ==3:
                                    #    break
                                    # print(count)
                                    # print(mod, comp_feat, tar_feat, hidden, hidden, fc, fc, lr)
                                    if count%100 == 0:
                                        fl_command = open("./pinn_ecfp4ksep_{}_{}_classifier_commands_{}_r.py".format(n_of_comp_h_layers, n_of_tar_h_layers, cmd_fl_count), "w")
                                        fl_command.write("import subprocess\n")
                                        cmd_fl_count += 1
                                        for cmd in lst_commands:

                                            fl_command.write("{}\n".format(cmd))
                                        fl_command.close()
                                        lst_commands = []


                                    lst_commands.append("subprocess.call(\"python dream_challenge.py {} {} {} {} {} {} {} {} {} r\", shell=True)".format(mod, comp_feat, tar_feat, hidden_comp, hidden_tar, fc, fc, lr, idg_fl))
                                    #print(
                                    #    "subprocess.call(\"python dream_challenge.py {} {} {} {} {} {} {} {}\".format(mod, comp_feat, tar_feat, hidden, hidden, fc, fc, lr), shell=True)")
                                    #subprocess.call("python dream_challenge.py {} {} {} {} {} {} {} {}".format("PINN2", "ecfp4_fcfp4_rdk5", "k-sep-bigrams_pfam_APAAC", "4096_4096", "4096_4096", "1024", "1024", "0.05"), shell=True)
    fl_command = open("./pinn_ecfp4ksep_{}_{}_classifier_commands_{}_r.py".format(n_of_comp_h_layers, n_of_tar_h_layers, cmd_fl_count), "w")
    fl_command.write("import subprocess\n")
    cmd_fl_count += 1
    for cmd in lst_commands:
        fl_command.write("{}\n".format(cmd))
    fl_command.close()

# generateFirstCommands(2, 2)
#print(len(lst_decreasing_permutations))

# model_type, comp_feat_type, tar_feat_type, num_comp_lay, num_of_prot_la, h1, h2 ,learn rate

def generateECFPKSEPCommands():
    comp_feature_list = ["ecfp4"]
    # comp_feature_list = ["ecfp4",]
    tar_feature_list = ["k-sep-bigrams", "trigram"]
    # tar_feature_list = ["k-sep-bigrams", "APAAC", "DDE", "pfam"]
    lst_learning_rate = [0.0001, 0.005, 0.001, 0.05]
    comb_comp_feat_list = []
    comb_tar_feat_list = []
    fl_command = open("./PINN_ECFPKSEPTRIGRAM_commands.py", "w")
    fl_command.write("import subprocess\n")

    for i in range(3):
        lst_cand_comp_list = list(combinations(comp_feature_list, i + 1))

        for cand in lst_cand_comp_list:
            str_comp_feat = ""
            for feat in cand:
                str_comp_feat += "{}_".format(feat)
            str_comp_feat = str_comp_feat[:-1]

            comb_comp_feat_list.append(str_comp_feat)

    for i in range(2):
        lst_cand_tar_list = list(combinations(tar_feature_list, i + 1))

        for cand in lst_cand_tar_list:
            str_tar_feat = ""
            for feat in cand:
                str_tar_feat += "{}_".format(feat)
            str_tar_feat = str_tar_feat[:-1]

            comb_tar_feat_list.append(str_tar_feat)

    print(comb_comp_feat_list)
    print(comb_tar_feat_list)
    n_of_neuron_list_h = [4096, 2048, 1536, 1024, 512, 128]
    n_of_neuron_list_fc = [1024, 512, 256, 64]
    model_types = ["PINN2"]
    n_of_h_layers = 2
    n_of_fc_layers = 2

    lst_n_permutations = list(permutations(n_of_neuron_list_h, n_of_h_layers))

    lst_decreasing_permutations = []
    for perm in lst_n_permutations:
        is_decreasing = True
        perm_ind = 0

        while perm_ind + 1 < (len(perm)):
            if perm[perm_ind] < perm[perm_ind + 1]:
                is_decreasing = False
                break
            perm_ind += 1

        if is_decreasing:
            str_decreasing = ""
            for neur in perm:
                str_decreasing += "{}_".format(neur)
                # print(str_decreasing)
            str_decreasing = str_decreasing[:-1]
            lst_decreasing_permutations.append(str_decreasing)

    lst_commands = []
    count = 0
    cmd_fl_count = 1
    for mod in model_types:
        for comp_feat in comb_comp_feat_list:
            for tar_feat in comb_tar_feat_list:
                for hidden in lst_decreasing_permutations:
                    for fc in n_of_neuron_list_fc:
                        for lr in lst_learning_rate:
                            count += 1
                            # if count ==3:
                            #    break
                            # print(count)
                            # print(mod, comp_feat, tar_feat, hidden, hidden, fc, fc, lr)

                            lst_commands.append(
                                "subprocess.call(\"python dream_challenge.py {} {} {} {} {} {} {} {}\", shell=True)".format(
                                    mod, comp_feat, tar_feat, hidden, hidden, fc, fc, lr))
                            # print(
                            #    "subprocess.call(\"python dream_challenge.py {} {} {} {} {} {} {} {}\".format(mod, comp_feat, tar_feat, hidden, hidden, fc, fc, lr), shell=True)")
                            # subprocess.call("python dream_challenge.py {} {} {} {} {} {} {} {}".format("PINN2", "ecfp4_fcfp4_rdk5", "k-sep-bigrams_pfam_APAAC", "4096_4096", "4096_4096", "1024", "1024", "0.05"), shell=True)
    for cmd in lst_commands:
        fl_command.write("{}\n".format(cmd))
    fl_command.close()

def generate2_3_Commands():
    comp_feature_list = ["ecfp4"] #, "fcfp4", "rdk5"]
    #comp_feature_list = ["ecfp4",]
    #tar_feature_list = ["k-sep-bigrams", "APAAC", "DDE", "pfam"]
    tar_feature_list = ["k-sep-bigrams", "trigram"]#, "DDE", "pfam"]
    #tar_feature_list = ["k-sep-bigrams", "APAAC", "DDE", "pfam"]
    lst_learning_rate = [0.0001, 0.005, 0.001, 0.05]
    comb_comp_feat_list = []
    comb_tar_feat_list = []

    for i in range(3):
        lst_cand_comp_list = list(combinations(comp_feature_list, i+1))

        for cand in lst_cand_comp_list:
            str_comp_feat = ""
            for feat in cand:
                str_comp_feat += "{}_".format(feat)
            str_comp_feat =str_comp_feat[:-1]

            comb_comp_feat_list.append(str_comp_feat)

    for i in range(2):
        lst_cand_tar_list = list(combinations(tar_feature_list, i+1))

        for cand in lst_cand_tar_list:
            str_tar_feat = ""
            for feat in cand:
                str_tar_feat += "{}_".format(feat)
            str_tar_feat = str_tar_feat[:-1]

            comb_tar_feat_list.append(str_tar_feat)


    print(comb_comp_feat_list)
    print(comb_tar_feat_list)
    n_of_neuron_list_h = [4096, 2048, 1536, 1024, 512, 128]
    n_of_neuron_list_fc = [1024, 512, 256, 64]
    model_types = ["PINN2"]
    n_of_h_layers = 2
    n_of_fc_layers = 2

    lst_n_permutations = list(permutations(n_of_neuron_list_h, n_of_h_layers))

    lst_decreasing_permutations = []
    for perm in lst_n_permutations:
        is_decreasing = True
        perm_ind = 0

        while perm_ind+1<(len(perm)):
            if perm[perm_ind]<perm[perm_ind+1]:
                is_decreasing = False
                break
            perm_ind += 1

        if is_decreasing:
            str_decreasing = ""
            for neur in perm:
                str_decreasing += "{}_".format(neur)
                #print(str_decreasing)
            str_decreasing = str_decreasing[:-1]
            lst_decreasing_permutations.append(str_decreasing)

    lst_commands = []
    count = 0
    cmd_fl_count = 1
    for mod in model_types:
        for comp_feat in comb_comp_feat_list:
            for tar_feat in comb_tar_feat_list:
                for hidden in lst_decreasing_permutations:
                    for fc in n_of_neuron_list_fc:
                        for lr in lst_learning_rate:
                            count += 1
                            # if count ==3:
                            #    break
                            # print(count)
                            # print(mod, comp_feat, tar_feat, hidden, hidden, fc, fc, lr)
                            if count%50 == 0:
                                fl_command = open("./PINN_ECFP4KSEPTRIGRAMfirst_commands_{}.py".format(cmd_fl_count), "w")
                                fl_command.write("import subprocess\n")
                                cmd_fl_count += 1
                                for cmd in lst_commands:

                                    fl_command.write("{}\n".format(cmd))
                                fl_command.close()
                                lst_commands = []


                            lst_commands.append("subprocess.call(\"python dream_challenge.py {} {} {} {} {} {} {} {}\", shell=True)".format(mod, comp_feat, tar_feat, hidden, hidden, fc, fc, lr))
                            #print(
                            #    "subprocess.call(\"python dream_challenge.py {} {} {} {} {} {} {} {}\".format(mod, comp_feat, tar_feat, hidden, hidden, fc, fc, lr), shell=True)")
                            #subprocess.call("python dream_challenge.py {} {} {} {} {} {} {} {}".format("PINN2", "ecfp4_fcfp4_rdk5", "k-sep-bigrams_pfam_APAAC", "4096_4096", "4096_4096", "1024", "1024", "0.05"), shell=True)
    fl_command = open("./PINN_ECFP4KSEPTRIGRAMfirst_commands_{}.py".format(cmd_fl_count), "w")
    fl_command.write("import subprocess\n")
    cmd_fl_count += 1
    for cmd in lst_commands:
        fl_command.write("{}\n".format(cmd))
    fl_command.close()
# print(len(lst_decreasing_permutations))
# generateECFPKSEPCommands()


def generate_protein_rnn_commands():
    name_of_the_experiment = "last_rnn_out_experiment_1"
    comp_feature_list = ["ecfp4"]
    tar_feature_list = ["trigramencodings1000"]#, "DDE", "pfam"]
    batch_size = [32, 64, 128]
    lst_learning_rate = [0.0001, 0.005, 0.001]
    vocab_size = [8000]
    n_of_neuron_list_h = [1024, 512, 256]
    n_of_neuron_list_fc = [1024, 512, 256]
    rnn_output_size = [128, 256, 512]
    embedding_dim = [100, 200, 400]
    hidden_dim = [128, 256, 512, 1024]
    rnn_layers = [2, 3]
    n_of_h_layers = 2

    lst_n_permutations = list(permutations(n_of_neuron_list_h, n_of_h_layers))
    lst_decreasing_permutations = []
    for perm in lst_n_permutations:
        is_decreasing = True
        perm_ind = 0

        while perm_ind+1<(len(perm)):
            if perm[perm_ind]<perm[perm_ind+1]:
                is_decreasing = False
                break
            perm_ind += 1

        if is_decreasing:
            str_decreasing = ""
            for neur in perm:
                str_decreasing += "{}_".format(neur)
                #print(str_decreasing)
            str_decreasing = str_decreasing[:-1]
            lst_decreasing_permutations.append(str_decreasing)
    comp_tar_pair_dataset_fl = ["idg_comp_targ_uniq_inter_filtered.csv"]
    regress_class = ["r"]


    """
    comp_feature_list = sys.argv[1].split("_")
    tar_feature_list = sys.argv[2].split("_")
    comp_hidden_lst = sys.argv[3].split("_")
    vocab_size = int(sys.argv[4]) + 1 # 8000 + 1  # +1 for the 0 padding + our word tokens
    output_size = int(sys.argv[5]) # 100
    embedding_dim = int(sys.argv[6]) # 400
    hidden_dim = int(sys.argv[7]) # 256
    n_rnn_layers = int(sys.argv[8]) # 2
    fc1 = int(sys.argv[9])
    fc2 = int(sys.argv[10])
    learn_rate = float(sys.argv[11])
    comp_tar_pair_dataset_fl = sys.argv[12]
    regress_classifier = sys.argv[13]
    """
    lst_commands = []
    count = 0
    cmd_fl_count = 1
    for btch in batch_size:
        for comp_feat in comp_feature_list:
            for tar_feat in tar_feature_list:
                for hidden in lst_decreasing_permutations:
                    for v_s in vocab_size:
                        for o_s in rnn_output_size:
                            for e_d in embedding_dim:
                                for h_d in hidden_dim:
                                    for r_l in rnn_layers:
                                        for fc in n_of_neuron_list_fc:
                                            for lr in lst_learning_rate:
                                                for fl in comp_tar_pair_dataset_fl:
                                                    for r_c in regress_class:
                                                        count += 1
                                                        # if count ==3:
                                                        #    break
                                                        # print(count)
                                                        # print(mod, comp_feat, tar_feat, hidden, hidden, fc, fc, lr)
                                                        if count%50 == 0:
                                                            fl_command = open("./{}_{}.py".format(name_of_the_experiment, cmd_fl_count), "w")
                                                            fl_command.write("import subprocess\n")
                                                            cmd_fl_count += 1
                                                            for cmd in lst_commands:

                                                                fl_command.write("{}\n".format(cmd))
                                                            fl_command.close()
                                                            lst_commands = []


                                                        lst_commands.append("subprocess.call(\"python rnn_playground.py {} {} {} {} {} {} {} {} {} {} {} {} {} {}\", shell=True)".format(comp_feat, tar_feat, hidden, v_s, o_s, e_d, h_d, r_l, fc, fc, lr, fl, r_c, btch))
                                                        #print(
                                                        #    "subprocess.call(\"python dream_challenge.py {} {} {} {} {} {} {} {}\".format(mod, comp_feat, tar_feat, hidden, hidden, fc, fc, lr), shell=True)")
                                                        #subprocess.call("python dream_challenge.py {} {} {} {} {} {} {} {}".format("PINN2", "ecfp4_fcfp4_rdk5", "k-sep-bigrams_pfam_APAAC", "4096_4096", "4096_4096", "1024", "1024", "0.05"), shell=True)
    fl_command = open("./{}_{}.py".format(name_of_the_experiment, cmd_fl_count), "w")
    fl_command.write("import subprocess\n")
    cmd_fl_count += 1
    for cmd in lst_commands:
        fl_command.write("{}\n".format(cmd))
    fl_command.close()
# print(len(lst_decreasing_permutations))
# generateECFPKSEPCommands()
# generate_protein_rnn_commands()

def generate_protein_cnn_commands():
    batch_size = [16, 32]
    lst_learning_rate = [0.0001, 0.005, 0.001, 0.01]
    after_flattened_conv_layer_neurons = [64, 128, 256, 512, 1024]
    comp_2_hidden_layer_list = ["256_256", "512_256", "512_512", "1024_512", "1024_256", "1024_1024"]
    last_2_hidden_layer_list = ["128_128", "256_256", "512_512", "1024_1024"]
    training_dataset_list = ["DeepDTA_davis", "DeepDTA_kiba"]
    training_dataset_list = ["DeepDTA_kiba"]
    training_dataset_list = ["DeepDTA_davis_filtered"]
    training_dataset_list = ["PDBBind"]
    # target_feature = "sequencematrix1000"
    target_feature = "sequencematrix500"
    for b_s in batch_size:
        for tr_data in training_dataset_list:
            for conv_flat in after_flattened_conv_layer_neurons:
                for last_fcc in last_2_hidden_layer_list:
                    for l_r in lst_learning_rate:
                        for comp_hid in comp_2_hidden_layer_list:

                            # lst_params = []
                            print("bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu \"num=1:j_exclusive=yes\" -M 10240 -R 'rusage[mem=10240]' -o ../log_files/pdbbind_experiment_12062019/normalized_{}_{}_{}_{}_{}_{}_{}.out \"python cnn_playground.py {} {} {} {} {} {} ecfp4 {}\"".format(comp_hid, conv_flat, last_fcc, l_r, b_s, tr_data, target_feature, comp_hid, conv_flat, last_fcc, l_r, b_s, tr_data, target_feature))
                            #print(
                            #    "bsub -q research-rh74 -P gpu -M 15360 -R 'rusage[mem=15360]' -o ../log_files/pdbbind_experiment_12062019/normalized_{}_{}_{}_{}_{}_{}_{}.out \"python cnn_playground.py {} {} {} {} {} {} ecfp4 {}\"".format(
                            #        comp_hid, conv_flat, last_fcc, l_r, b_s, tr_data, target_feature, comp_hid,
                            #        conv_flat, last_fcc, l_r, b_s, tr_data, target_feature))
                            print("sleep 1")

generate_protein_cnn_commands()
# python cnn_playground.py 1024_1024 1024 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix1000
# bsub -g /my_gpu_group -q research-rh74 -P gpu -gpu "num=1:j_exclusive=yes" -M 40960 -R 'rusage[mem=40960]' -o ../log_files/pdbbind_experiment_07062019/1000_Deneme.out "python cnn_playground.py 1024_1024 1024 1024_1024 0.01 32 PDBBind ecfp4 sequencematrix1000"
# comp_hid, conv_flat, last_fcc, l_r, b_s, tr_data comp_hid, conv_flat, last_fcc, l_r, b_s, tr_data

"""

comp_hidden_layer_neurons = [int(num) for num in sys.argv[1].split("_")]
after_flattened_conv_layer_neurons = sys.argv[2]
last_2_hidden_layer_list = sys.argv[3].split("_")
learn_rate = sys.argv[4]
batch_size = sys.argv[5]
training_dataset = sys.argv[6]
comp_feature_list = sys.argv[7].split("_")# ["ecfp4"]
tar_feature_list = sys.argv[8].split("_")# ["sequencematrix500"]

"""