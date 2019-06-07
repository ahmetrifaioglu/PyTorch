import os
from cnn_common_modules import get_prot_id_seq_dict_from_fasta_fl, eprint
import itertools
# import torch
import numpy as np
# import torch.nn as nn



def remove_nonstandard_aas(prot_seq):
    aa_list = get_aa_list()
    prot_seq_list = [aa for aa in prot_seq if aa in aa_list]
    prot_seq = ''.join(prot_seq_list)
    return prot_seq


def convert_pdbbind_sequences_into_fasta_format():
    files_path = "/Users/trman/Downloads/PBDbind_sequences"
    for fl in os.listdir(files_path):
        #print(fl)
        if fl.endswith("fasta"):
            seq_fl = open("{}/{}".format(files_path, fl), "r")
            lst_seq_fl = seq_fl.read().split("\n")
            seq_fl.close()
            print(">XXX|{}|XXX".format(lst_seq_fl[0][1:]))
            print(lst_seq_fl[1])
            #print(lst_seq_fl)

# python static_file_generation_modules.py > ../trainingFiles/PDBBind/helper_files/targets.fasta
# convert_pdbbind_sequences_into_fasta_format()


def get_padded_sequence_matrix(np_arr, size):
    torch_arr = torch.from_numpy(np_arr)
    size_of_tensor = torch_arr.shape[0]
    # print(torch_list)
    # print(torch_list.shape[0])
    if size_of_tensor < size:
        padding_size = int((size - size_of_tensor) / 2)
        m = nn.ZeroPad2d(padding_size)
        if size_of_tensor % 2 != 0:
            m = nn.ZeroPad2d((padding_size, padding_size + 1, padding_size, padding_size + 1))
        torch_arr = m(torch_arr)
    else:
        torch_arr = torch_arr[:size, :size]

    # print(torch_arr.shape)
    return torch_arr


def normalize_and_print_flattened_aa_distance_matrices(dist_folder_path, dist_fl_name, size):
    prot_id = dist_fl_name.split(".")[0]
    dist_fl = open("{}/{}".format(dist_folder_path, dist_fl_name), "r")
    lst_dist_fl = dist_fl.read().split("\n")
    dist_fl.close()
    lst_dist_fl = lst_dist_fl[:-1]
    max_dist = 0.0
    np_dist_matrix = np.zeros((len(lst_dist_fl), len(lst_dist_fl)), dtype=float)
    # print(len(lst_dist_fl))
    for row_ind in range(len(lst_dist_fl)):
        col_values = lst_dist_fl[row_ind].split("\t")
        for col_ind in range(len(lst_dist_fl)):
            dist = 0
            if col_ind>row_ind:
                #print(col_values[col_ind])
                dist = float(col_values[col_ind])
                if dist>max_dist:
                    max_dist = dist
                np_dist_matrix[row_ind,col_ind] = round(dist, 3)
                np_dist_matrix[col_ind, row_ind] = round(dist, 3)
    # print(max_dist)
    normalized_np_arr = np.around(np_dist_matrix/max_dist, decimals=4)
    # print(len(normalized_np_arr[450]))
    seq_torch_matrix = get_padded_sequence_matrix(normalized_np_arr, size)
    #print(len(seq_torch_matrix[450]))

    # print(seq_torch_matrix)
    flattened_seq_matrix_arr = np.array(seq_torch_matrix.contiguous().view(-1))
    #print(flattened_seq_matrix_arr)
    print(prot_id + "\t" + "\t".join([str(val) for val in flattened_seq_matrix_arr]))


def save_all_aa_distance_matrices(dist_folder_path, size):
    import os
    str_header = "target id\t" + "\t".join([str(num) for num in list(range(size * size))])
    print(str_header)
    count = 0
    for fl in os.listdir(dist_folder_path):
        #print(fl)
        count += 1
        eprint(count)
        normalize_and_print_flattened_aa_distance_matrices(dist_folder_path, fl, size)

# save_all_aa_distance_matrices("/Users/trman/Downloads/PBDbind_residue_distance_maps_1_4000", 500)
# python dream_challenge_data_processing.py > ../trainingFiles/PDBBind/target_feature_vectors/aadistancematrix500_normalized_1_4000.tsv
# save_all_aa_distance_matrices("/Users/trman/Downloads/PBDbind_residue_distance_maps_1_4000", 1000)
# python dream_challenge_data_processing.py > ../trainingFiles/PDBBind/target_feature_vectors/aadistancematrix1000_normalized_1_4000.tsv
# save_all_aa_distance_matrices("/Users/trman/Downloads/PBDbind_residue_distance_maps_4001_8000", 500)
# python dream_challenge_data_processing.py > ../trainingFiles/PDBBind/target_feature_vectors/aadistancematrix500_normalized_4001_8000.tsv
# save_all_aa_distance_matrices("/Users/trman/Downloads/PBDbind_residue_distance_maps_4001_8000", 1000)
# python dream_challenge_data_processing.py > ../trainingFiles/PDBBind/target_feature_vectors/aadistancematrix1000_normalized_4001_8000.tsv



def get_aa_list():
    aa_list = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
    return aa_list


def get_all_aa_word_list(word_size):
    aa_list = get_aa_list()
    # all_n_gram_list = list(itertools.permutations(aa_list, word_size))
    all_n_gram_list = list(itertools.product(aa_list, repeat=word_size))
    all_n_gram_list = [''.join(n_gram_tuple) for n_gram_tuple in all_n_gram_list]
    return all_n_gram_list


def get_aa_match_encodings():
    all_aa_matches = get_all_aa_word_list(2)
    aa_match_encoding_dict = dict()
    encod_int = 1
    for aa_pair in all_aa_matches:
        if aa_pair not in aa_match_encoding_dict.keys():
            aa_match_encoding_dict[aa_pair] = encod_int
            aa_match_encoding_dict[aa_pair[::-1]] = encod_int
            encod_int += 1
    return aa_match_encoding_dict


def get_sequence_matrix(seq, size):
    aa_match_encoding_dict = get_aa_match_encodings()
    # print(aa_match_encoding_dict)

    seq = remove_nonstandard_aas(seq)
    lst = []
    for i in range(len(seq)):
        lst.append([])
        for j in range(len(seq)):
            lst[-1].append(aa_match_encoding_dict[seq[i] + seq[j]])

    torch_arr = torch.from_numpy(np.asarray(lst))
    size_of_tensor = torch_arr.shape[0]
    # print(torch_list)
    # print(torch_list.shape[0])
    if size_of_tensor < size:
        padding_size = int((size - size_of_tensor) / 2)
        m = nn.ZeroPad2d(padding_size)
        if size_of_tensor % 2 != 0:
            m = nn.ZeroPad2d((padding_size, padding_size + 1, padding_size, padding_size + 1))
        torch_arr = m(torch_arr)
    else:
        torch_arr = torch_arr[:size, :size]

    # print(torch_arr.shape)
    return torch_arr


def save_all_flattened_sequence_matrices(fasta_fl_path, size):
    prot_id_seq_dict = get_prot_id_seq_dict_from_fasta_fl(fasta_fl_path)
    str_header = "target id\t" + "\t".join([str(num) for num in list(range(size*size))])
    count = 0
    print(str_header)
    for prot_id, seq in prot_id_seq_dict.items():
        count += 1
        eprint(count)
        seq_torch_matrix = get_sequence_matrix(seq, size)
        # print(seq_torch_matrix)
        flattened_seq_matrix_arr = np.array(seq_torch_matrix.contiguous().view(-1))
        # print(flattened_seq_matrix_arr)
        print(prot_id + "\t" + "\t".join([str(val) for val in flattened_seq_matrix_arr]))

# python static_file_generation_modules.py > ../trainingFiles/PDBBind/target_feature_vectors/sequencematrix500_normalized.tsv
# save_all_flattened_sequence_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/helper_files/targets.fasta", 500)

# python static_file_generation_modules.py > ../trainingFiles/PDBBind/target_feature_vectors/sequencematrix1000_normalized.tsv
# save_all_flattened_sequence_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/helper_files/targets.fasta", 1000)



# Components-smiles-stereo-oe.smi and Components-inchi.ich.txt were downloaded from  http://ligand-expo.rcsb.org/ld-download.html
def create_ecfp4_feature_file_for_pdbbind_ligands():
    from operator import itemgetter
    import math
    import numpy as np
    from rdkit import Chem
    from rdkit.Chem import AllChem

    dict_ligand_inchi = dict()
    dict_ligand_smiles = dict()

    inchi_fl = open(
        "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/helper_files/Components-inchi.ich.txt", "r")
    lst_inchi_fl = inchi_fl.read().split("\n")
    inchi_fl.close()
    if "" in lst_inchi_fl:
        lst_inchi_fl.remove("")

    for line in lst_inchi_fl:
        # print(line.split("\t"))
        inchi, pdb_id, _ = line.split("\t")
        dict_ligand_inchi[pdb_id] = inchi

    smiles_fl = open(
        "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/helper_files/Components-smiles-stereo-oe.smi", "r")
    lst_smiles_fl = smiles_fl.read().split("\n")
    smiles_fl.close()
    lst_smiles_fl.remove("")

    for line in lst_smiles_fl:
        # print(line.split("\t"))
        smiles, pdb_id, _ = line.split("\t")
        dict_ligand_smiles[pdb_id] = smiles


    dataset_fl = open("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/helper_files/INDEX_refined_data.2015","r")
    lst_dataset_fl = dataset_fl.read().split("\n")
    dataset_fl.close()


    all_count = 0
    true_count = 0
    all_set = set()
    true_set = set()
    for line in lst_dataset_fl:
        if not line.startswith("#") and line!="":
            all_count += 1
            ligand_pdb_id = line.split("(")[-1][:-1]
            all_set.add(ligand_pdb_id)
            is_inchi = True
            try:
                dict_ligand_inchi[ligand_pdb_id]
                true_set.add(ligand_pdb_id)
                true_count+=1
            except:

                is_inchi=False

            if not is_inchi:
                try:
                    dict_ligand_smiles[ligand_pdb_id]
                    true_set.add(ligand_pdb_id)
                    true_count += 1
                except:
                    pass

            failureCount = 0


    str_header = "compound id\t" + "\t".join([str(num) for num in range(1024)])
    print(str_header)
    for comp in true_set:

        isInChiFailed = False

        try:
            m = Chem.MolFromInchi(dict_ligand_inchi[comp])
            fp = AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=1024).ToBitString()
            print(comp + "\t" + "\t".join([str(float(dim)) for dim in fp]))
        except:
            eprint("inhci error")
            isInChiFailed = True


        isSmilesFailed = False
        if isInChiFailed:
            fp = ""
            try:
                m = Chem.MolFromSmiles(dict_ligand_smiles[comp])
                fp = AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=1024).ToBitString()
                print(comp + "\t" + "\t".join([str(float(dim)) for dim in fp]))
            except:
                isSmilesFailed = True

        if isSmilesFailed:
            eprint("%s\tBoth Failed" % (comp))
            failureCount += 1

    # print(all_set - true_set)
    # print(len(all_set), len(true_set), len(all_set-true_set))

    # print(all_count, true_count)

# python static_file_generation_modules.py > ../trainingFiles/PDBBind/compound_feature_vectors/ecfp4_normalized.tsv
# create_ecfp4_feature_file_for_pdbbind_ligands()

def create_dti_dataset_for_pdbbind():
    import math

    dataset_fl = open("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/helper_files/INDEX_refined_data.2015","r")
    lst_dataset_fl = dataset_fl.read().split("\n")
    dataset_fl.close()

    dict_ligand_inchi = dict()

    ecfp4_fl = open(
        "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/compound_feature_vectors/ecfp4_normalized.tsv", "r")
    lst_ecfp4_fl = ecfp4_fl.read().split("\n")
    ecfp4_fl.close()

    if "" in lst_ecfp4_fl:
        lst_ecfp4_fl.remove("")

    for line in lst_ecfp4_fl:
        # print(line.split("\t"))
        pdb_id = line.split("\t")[0]
        dict_ligand_inchi[pdb_id] = ""

    # first list holds train and the other one holds validation
    train_val_indices = [[],[]]
    test_indices = []
    index = 0
    all_count = 0
    true_count = 0
    all_set = set()
    true_set = set()
    for line in lst_dataset_fl:
        if not line.startswith("#") and line!="":
            all_count += 1
            ligand_pdb_id = line.split("(")[-1][:-1]
            all_set.add(ligand_pdb_id)
            is_inchi = True
            # print(ligand_pdb_id)
            try:
                dict_ligand_inchi[ligand_pdb_id]
                true_set.add(ligand_pdb_id)
                true_count+=1
                fields = line.split("  ")
                prot_pdb_id = fields[0]
                year = fields[2]
                affinity_val = float(fields[4].split("=")[1][:-2])
                affinity_unit = fields[4].split("=")[1][-2:]
                if affinity_unit=="fM":
                    affinity_val =  -math.log10(affinity_val * 10**-15)
                elif affinity_unit=="pM":
                    affinity_val =  -math.log10(affinity_val * 10**-12)
                elif affinity_unit=="nM":
                    affinity_val =  -math.log10(affinity_val * 10**-9)
                elif affinity_unit=="uM":
                    affinity_val =  -math.log10(affinity_val * 10**-6)
                elif affinity_unit == "mM":
                    affinity_val = -math.log10(affinity_val * 10**-3)
                else:
                    print("WTF!", affinity_unit, line, affinity_val)

                if year == "2012":
                    train_val_indices[1].append(index)
                elif year== "2013" or year== "2014":
                    test_indices.append(index)
                else:
                    train_val_indices[0].append(index)
                index += 1
                # first print this
                # print("{},{},{}".format(ligand_pdb_id, prot_pdb_id, affinity_val))
                # print("{},{},{},{}".format(ligand_pdb_id,prot_pdb_id,affinity_val,year))

            except Exception as e:
                pass
                # print("Exception:", str(e))
    # then print this
    # print(train_val_indices)
    # finally print this
    # print(test_indices)
# 2 asamali once dti datasini yazdirdim sonra train test val datasini
# python static_file_generation_modules.py > ../trainingFiles/PDBBind/dti_datasets/comp_targ_affinity.csv
# python static_file_generation_modules.py > ../trainingFiles/PDBBind/data/folds/train_fold_setting1.txt
# python static_file_generation_modules.py > ../trainingFiles/PDBBind/data/folds/test_fold_setting1.txt
# create_dti_dataset_for_pdbbind()

def create_single_target_feature_vector_files_using_combined():
    feature_name = "sequencematrix500_normalized"
    input_path = "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/target_feature_vectors"
    output_path = "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/target_feature_vectors/{}".format(feature_name)
    with open("{}/{}.tsv".format(input_path, feature_name)) as f:
        for line in f:
            line = line.split("\n")[0]
            target_id = line.split("\t")[0]
            output_fl = open("{}/{}.tsv".format(output_path, target_id), "w")
            output_fl.write(line)
            output_fl.close()

# create_single_target_feature_vector_files_using_combined()

