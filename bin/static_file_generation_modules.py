import os
from cnn_common_modules import get_prot_id_seq_dict_from_fasta_fl
import itertools
import torch
import numpy as np
import torch.nn as nn
import subprocess
import pandas as pd

cwd = os.getcwd()
training_files_path = "{}PyTorch/trainingFiles".format(cwd.split("PyTorch")[0])



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
                try:
                    dist = float(col_values[col_ind])
                    if dist>max_dist:
                        max_dist = dist
                    np_dist_matrix[row_ind,col_ind] = round(dist, 3)
                    np_dist_matrix[col_ind, row_ind] = round(dist, 3)
                except:
                    print("Houston we have a problem", prot_id, row_ind, col_ind)
    # print(max_dist)
    normalized_np_arr = np.around(np_dist_matrix/max_dist, decimals=4)
    # print(len(normalized_np_arr[450]))
    seq_torch_matrix = get_padded_sequence_matrix(normalized_np_arr, size)
    #print(len(seq_torch_matrix[450]))

    # print(seq_torch_matrix)
    flattened_seq_matrix_arr = np.array(seq_torch_matrix.contiguous().view(-1))
    #print(flattened_seq_matrix_arr)
    #print(prot_id + "\t" + "\t".join([str(val) for val in flattened_seq_matrix_arr]))
    # if not os.path.exists("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/target_feature_vectors/aadistancematrix500/{}.tsv".format(prot_id)):
    prot_aa_fl = open("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/target_feature_vectors/aadistancematrix500/{}.tsv".format(prot_id), "w")
    prot_aa_fl.write(prot_id + "\t" + "\t".join([str(val) for val in flattened_seq_matrix_arr]))
    prot_aa_fl.close()


def save_all_aa_distance_matrices(dist_folder_path, size):
    import os
    #str_header = "target id\t" + "\t".join([str(num) for num in list(range(size * size))])
    #print(str_header)
    count = 0

    for fl in os.listdir(dist_folder_path):
        # print(fl)
        count += 1
        eprint(count)
        normalize_and_print_flattened_aa_distance_matrices(dist_folder_path, fl, size)


# save_all_aa_distance_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/target_feature_vectors/PBDbind_residue_distance_maps_4001_8000", 500)
# python dream_challenge_data_processing.py > ../trainingFiles/PDBBind/target_feature_vectors/aadistancematrix500_normalized_1_4000.tsv
#save_all_aa_distance_matrices("/Users/trman/Downloads/PBDbind_residue_distance_maps_1_4000", 1000 )
# python dream_challenge_data_processing.py > ../trainingFiles/PDBBind/target_feature_vectors/aadistancematrix1000_normalized_1_4000.tsv
# save_all_aa_distance_matrices("/Users/trman/Downloads/PBDbind_residue_distance_maps_4001_8000", 500)
# python dream_challenge_data_processing.py > ../trainingFiles/PDBBind/target_feature_vectors/aadistancematrix500_normalized_4001_8000.tsv
# save_all_aa_distance_matrices("/Users/trman/Downloads/PBDbind_residue_distance_maps_4001_8000", 1000)
# python dream_challenge_data_processing.py > ../trainingFiles/PDBBind/target_feature_vectors/aadistancematrix1000_normalized_4001_8000.tsv

#save_all_aa_distance_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/target_feature_vectors/PBDbind_residue_distance_maps_8001_11918", 500)
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


def get_aa_match_encodings_generic(aaindex_enconding, full_matrix=False):
    aa_list = get_aa_list()
    encoding_fl = open("../trainingFiles/encodings/{}".format(aaindex_enconding))
    lst_encoding_fl = encoding_fl.read().split("\n")
    encoding_fl.close()
    aa_match_encoding_dict = dict()
    starting_ind = -1
    for row_ind in range(len(lst_encoding_fl)-1):
        str_line = lst_encoding_fl[row_ind]
        if str_line.startswith("M rows"):
            starting_ind = row_ind + 1

        if  not str_line.startswith("//") and starting_ind != -1 and row_ind >= starting_ind:
            row_aa_ind = row_ind - starting_ind
            str_line = str_line.split(" ")

            while "" in str_line:
                str_line.remove("")

            # print(len(str_line))
            for col_ind in range(len(str_line)):
                # print(str_line)
                # print(row_aa_ind, col_ind, aa_list[row_aa_ind], aa_list[col_ind], str_line[col_ind] )
                if not full_matrix:
                    aa_match_encoding_dict["{}{}".format(aa_list[row_aa_ind], aa_list[col_ind])] = round(float(str_line[col_ind]),3)
                    aa_match_encoding_dict["{}{}".format(aa_list[col_ind], aa_list[row_aa_ind])] = round(float(str_line[col_ind]),3)
                else:
                    aa_match_encoding_dict["{}{}".format(aa_list[row_aa_ind], aa_list[col_ind])] = round(
                        float(str_line[col_ind]), 3)
    #print(aa_match_encoding_dict)
    return aa_match_encoding_dict

# get_aa_match_encodings_generic("ZHAC000103.txt", True)

def get_sequence_matrix(seq, size, aaindex_enconding=None):
    aa_match_encoding_dict = None
    if aaindex_enconding==None:
        aa_match_encoding_dict = get_aa_match_encodings()
    elif aaindex_enconding=="ZHAC000103":
        aa_match_encoding_dict = get_aa_match_encodings_generic(aaindex_enconding, full_matrix=True)
    else:
        aa_match_encoding_dict = get_aa_match_encodings_generic(aaindex_enconding)
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


def save_all_flattened_sequence_matrices(dataset_name, size, aaindex_enconding=None):
    print(dataset_name, size, aaindex_enconding)
    fasta_fl_path = "../trainingFiles/{}/helper_files/targets.fasta".format(dataset_name)
    prot_id_seq_dict = get_prot_id_seq_dict_from_fasta_fl(fasta_fl_path)

    feature_name = ""
    if aaindex_enconding:
        feature_name = "{}LEQ{}".format(aaindex_enconding.split(".")[0], size)
    else:
        feature_name = "sequencematrix"

    str_header = "target id\t" + "\t".join([str(num) for num in list(range(size*size))])
    count = 0
    output_fl_name = ""
    if feature_name=="sequencematrix":
        output_fl_name = "{}{}_normalized.tsv".format(feature_name, size)
    else:
        output_fl_name = "{}.tsv".format(feature_name, size)

    output_fl =open("../trainingFiles/{}/target_feature_vectors/{}".format(dataset_name, output_fl_name),"w")
    output_fl.write(str_header+"\n")
    for prot_id, seq in prot_id_seq_dict.items():
        count += 1
        if count %100 == 0:
            print(count)
        seq_torch_matrix = None
        if aaindex_enconding==None:
            seq_torch_matrix = get_sequence_matrix(seq, size)
        else:
            seq_torch_matrix = get_sequence_matrix(seq, size, aaindex_enconding)

        # print(seq_torch_matrix)
        flattened_seq_matrix_arr = np.array(seq_torch_matrix.contiguous().view(-1))
        # print(flattened_seq_matrix_arr)
        #print(prot_id + "\t" + "\t".join([str(val) for val in flattened_seq_matrix_arr]))
        output_fl.write(prot_id + "\t" + "\t".join([str(val) for val in flattened_seq_matrix_arr]))

    output_fl.close()

save_all_flattened_sequence_matrices("Davis", 1000, "ZHAC000103.txt")
save_all_flattened_sequence_matrices("Davis", 1000, "GRAR740104.txt")
save_all_flattened_sequence_matrices("Davis", 1000, "SIMK990101.txt")
save_all_flattened_sequence_matrices("Davis", 1000, "blosum62.txt")

save_all_flattened_sequence_matrices("PDBBind_Refined", 1000, "ZHAC000103.txt")
save_all_flattened_sequence_matrices("PDBBind_Refined", 1000, "GRAR740104.txt")
save_all_flattened_sequence_matrices("PDBBind_Refined", 1000, "SIMK990101.txt")
save_all_flattened_sequence_matrices("PDBBind_Refined", 1000, "blosum62.txt")



# save_all_flattened_sequence_matrices("PDBBind_Refined", 500, "ZHAC000106.txt")



# save_all_flattened_sequence_matrices("PDBBind_Refined", 500, "ZHAC000103.txt")
# save_all_flattened_sequence_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/helper_files/targets.fasta", 500)

# python static_file_generation_modules.py > ../trainingFiles/PDBBind/target_feature_vectors/sequencematrix1000_normalized.tsv
# save_all_flattened_sequence_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/helper_files/targets.fasta", 1000)

# python static_file_generation_modules.py > ../trainingFiles/PDBBind/target_feature_vectors/blosum62LEQ500.tsv
# save_all_flattened_sequence_matrices("../trainingFiles/PDBBind/helper_files/targets.fasta", 500, "blosum62.txt")

# python static_file_generation_modules.py > ../trainingFiles/PDBBind/target_feature_vectors/SIMK990101.tsv
# save_all_flattened_sequence_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/helper_files/targets.fasta", 500, "SIMK990101.txt")

# python static_file_generation_modules.py > ../trainingFiles/DeepDTA_davis/target_feature_vectors/SIMK990101500.tsv
# save_all_flattened_sequence_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/DeepDTA_davis/helper_files/targets.fasta", 500, "SIMK990101.txt")

# python static_file_generation_modules.py > ../trainingFiles/DeepDTA_davis/target_feature_vectors/blosum62500_normalized.tsv
# save_all_flattened_sequence_matrices("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/DeepDTA_davis/helper_files/targets.fasta", 500, "blosum62.txt")

# python static_file_generation_modules.py > ../trainingFiles/PDBBind_Refined/target_feature_vectors/KESO980101LEQ500.tsv
# save_all_flattened_sequence_matrices("../trainingFiles/PDBBind_Refined/helper_files/targets.fasta", 500, "KESO980101.txt")

# python static_file_generation_modules.py > ../trainingFiles/PDBBind_Refined/target_feature_vectors/GRAR740104LEQ500.tsv
# save_all_flattened_sequence_matrices("../trainingFiles/PDBBind_Refined/helper_files/targets.fasta", 500, "GRAR740104.txt")

# python static_file_generation_modules.py > ../trainingFiles/PDBBind_Refined/target_feature_vectors/MIYS850102LEQ500.tsv
# save_all_flattened_sequence_matrices("../trainingFiles/PDBBind_Refined/helper_files/targets.fasta", 500, "MIYS850102.txt")

# python static_file_generation_modules.py > ../trainingFiles/PDBBind_Refined/target_feature_vectors/ZHAC000106LEQ500.tsv
#save_all_flattened_sequence_matrices("../trainingFiles/PDBBind_Refined/helper_files/targets.fasta", 500, "ZHAC000106.txt")

# python static_file_generation_modules.py > ../trainingFiles/PDBBind_Refined/target_feature_vectors/SIMK990101LEQ500.tsv
#save_all_flattened_sequence_matrices("../trainingFiles/PDBBind_Refined/helper_files/targets.fasta", 500, "SIMK990101.txt")

# python static_file_generation_modules.py > ../trainingFiles/PDBBind_Refined/target_feature_vectors/ZHAC000103LEQ500.tsv
# save_all_flattened_sequence_matrices("../trainingFiles/PDBBind_Refined/helper_files/targets.fasta", 500, "ZHAC000103.txt")

# ====================================================

# python static_file_generation_modules.py > ../trainingFiles/Davis/target_feature_vectors/KESO980101LEQ500.tsv
# save_all_flattened_sequence_matrices("../trainingFiles/Davis/helper_files/targets.fasta", 500, "KESO980101.txt")

# python static_file_generation_modules.py > ../trainingFiles/Davis/target_feature_vectors/GRAR740104LEQ500.tsv
# save_all_flattened_sequence_matrices("../trainingFiles/Davis/helper_files/targets.fasta", 500, "GRAR740104.txt")

# python static_file_generation_modules.py > ../trainingFiles/Davis/target_feature_vectors/MIYS850102LEQ500.tsv
# save_all_flattened_sequence_matrices("../trainingFiles/Davis/helper_files/targets.fasta", 500, "MIYS850102.txt")

# python static_file_generation_modules.py > ../trainingFiles/Davis/target_feature_vectors/ZHAC000106LEQ500.tsv
# save_all_flattened_sequence_matrices("../trainingFiles/Davis/helper_files/targets.fasta", 500, "ZHAC000106.txt")

# python static_file_generation_modules.py > ../trainingFiles/Davis/target_feature_vectors/SIMK990101LEQ500.tsv
# save_all_flattened_sequence_matrices("../trainingFiles/Davis/helper_files/targets.fasta", 500, "SIMK990101.txt")

# python static_file_generation_modules.py > ../trainingFiles/Davis/target_feature_vectors/ZHAC000103LEQ500.tsv
# save_all_flattened_sequence_matrices("../trainingFiles/Davis/helper_files/targets.fasta", 500, "ZHAC000103.txt")

# ====================================================


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


    # dataset_fl = open("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/helper_files/INDEX_refined_data.2015","r")
    dataset_fl = open(
        "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/helper_files/INDEX_general_PL_data.2015", "r")
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

# python static_file_generation_modules.py > ../trainingFiles/PDBBind/compound_feature_vectors/ecfp4_normalized_general.tsv
# create_ecfp4_feature_file_for_pdbbind_ligands()

def create_dti_dataset_for_pdbbind():
    import math

    dataset_fl = open("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/helper_files/INDEX_general_PL_data.2015","r")
    lst_dataset_fl = dataset_fl.read().split("\n")
    dataset_fl.close()

    dict_ligand_inchi = dict()

    ecfp4_fl = open(
        "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/PDBBind/compound_feature_vectors/ecfp4_normalized_general.tsv", "r")
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
    print(len(train_val_indices[0]), len(train_val_indices[1]), len(test_indices))
    # then print this
    # print(train_val_indices)
    # finally print this
    # print(test_indices)

# 2 asamali once dti datasini yazdirdim sonra train test val datasini
# python static_file_generation_modules.py > ../trainingFiles/PDBBind/dti_datasets/comp_targ_affinity_general.csv
# python static_file_generation_modules.py > ../trainingFiles/PDBBind/data/folds/train_fold_setting1_general.txt
# python static_file_generation_modules.py > ../trainingFiles/PDBBind/data/folds/test_fold_setting1_general.txt
# create_dti_dataset_for_pdbbind()

def create_single_target_feature_vector_files_using_combined(feature_name, dataset):
    # feature_name = "blosum62LEQ500"
    print(feature_name)
    input_path = "../trainingFiles/{}/target_feature_vectors".format(dataset)
    output_path = "../trainingFiles/{}/target_feature_vectors/{}".format(dataset, feature_name)
    subprocess.call("mkdir {}".format(output_path), shell=True)
    with open("{}/{}.tsv".format(input_path, feature_name)) as f:
        for line in f:
            line = line.split("\n")[0]
            target_id = line.split("\t")[0]
            output_fl = open("{}/{}.tsv".format(output_path, target_id), "w")
            output_fl.write(line)
            output_fl.close()

# create_single_target_feature_vector_files_using_combined("MIYS850102LEQ500", "PDBBind_Refined")
# create_single_target_feature_vector_files_using_combined("KESO980101LEQ500", "Davis_Filtered")
# create_single_target_feature_vector_files_using_combined("ZHAC000106LEQ500", "Davis_Filtered")
# create_single_target_feature_vector_files_using_combined("SIMK990101LEQ500", "Davis_Filtered")
# sequencematrix500_ZHAC000103LEQ500_GRAR740104LEQ500_SIMK990101LEQ500_blosum62LEQ500
def get_single_protein_family_associated_compounds(dataset_name, family_name):
    import numpy as np
    family_target_fl = "{}_target_ids.tsv".format(family_name)
    helper_fl_path = os.path.join(training_files_path, dataset_name, "helper_files")
    family_target_fl = os.path.join(helper_fl_path, family_target_fl)
    filtered_interaction_dataset_fl = os.path.join(helper_fl_path, "chembl25_preprocessed_sp_b_pchembl_data.txt")

    # print(family_target_fl)
    df_family_chembl_targets = pd.read_csv(family_target_fl, sep="\t")
    df_family_chembl_targets = df_family_chembl_targets.loc[df_family_chembl_targets['Type'] == "SINGLE PROTEIN"]
    # df_family_chembl_targets = df_family_chembl_targets["ChEMBL ID"]
    # list_family_chembl_ids = df_family_chembl_targets["ChEMBL ID"].tolist()
    # dict_of_chembl_ids = {chembl_id: None for chembl_id in list_family_chembl_ids}

    # print(dict_of_chembl_ids)
    df_filtered_association = pd.read_csv(filtered_interaction_dataset_fl, sep="\t", index_col=False)
    df_only_family_associations = pd.merge(df_family_chembl_targets, df_filtered_association, how="inner", left_on="ChEMBL ID", right_on="Target_CHEMBL_ID")
    unique_compound_ids = set(df_only_family_associations["Compound_CHEMBL_ID"].tolist())
    #print(len(unique_compound_ids))
    compound_fl = open(os.path.join(helper_fl_path, "{}_compound_ids.txt".format(family_name)), "w")
    for comp in unique_compound_ids:
        compound_fl.write("{}\n".format(comp))
    compound_fl.close()

"""
get_single_protein_family_associated_compounds("ChEMBL25", "gpcr")
get_single_protein_family_associated_compounds("ChEMBL25", "nuclearreceptor")
get_single_protein_family_associated_compounds("ChEMBL25", "ionchannel")
get_single_protein_family_associated_compounds("ChEMBL25", "kinase")
"""


def deepdta_create_filtered_fold_file(davis_kiba):
    import pickle
    import numpy as np
    import math
    import json
    from random import shuffle

    dataset_path = "../trainingFiles/DeepDTA_original/data/{}".format(davis_kiba)

    prot_id_seq_dict = json.load(open("{}/proteins.txt".format(dataset_path)))
    comp_id_smiles_dict = json.load(open("{}/ligands_can.txt".format(dataset_path)))
    ind_prot_id_dict, ind_comp_id_dict = dict(), dict()
    ind = 0
    for prot_id, seq in prot_id_seq_dict.items():
        ind_prot_id_dict[ind] = prot_id
        ind += 1

    ind = 0
    for comp_id, smiles in comp_id_smiles_dict.items():
        ind_comp_id_dict[ind] = comp_id
        ind += 1

    affinity_matrix  = pickle.load(open("{}/Y".format(dataset_path),"rb"), encoding='latin1')
    n_of_rows, n_of_cols = affinity_matrix.shape
    label_row_inds, label_col_inds = np.where(affinity_matrix!=1.0e+04)
    # print(label_row_inds[0], label_col_inds[0])
    shuffled_indices = list(range(len(label_row_inds)))
    shuffle(shuffled_indices)
    # print(shuffled_indices)
    """
    count = 0
    training_test_val_indices = []
    for ind in shuffled_indices:
        # print(ind)
        training_test_val_indices.append((label_row_inds[ind]*n_of_cols+label_col_inds[ind]))
        # print((label_row_inds[ind]*n_of_cols+label_col_inds[ind]))
        count += 1
        #if count>=100:
        #    break

    #print(len(training_test_val_indices))
    #print(len(set(training_test_val_indices)))
    """
    train_folds = []
    number_of_samples_each_fold = int(len(shuffled_indices)/6)
    for i in range(5):

        train_folds.append(shuffled_indices[i*number_of_samples_each_fold:(i+1)*number_of_samples_each_fold])


    test_folds = shuffled_indices[5*number_of_samples_each_fold:]

    train_folds_fl = open("/Users/trman/Downloads/DeepDTA-master/data/davis/folds/train_fold_setting1.txt", "w")
    train_folds_fl.write(str(train_folds))
    train_folds_fl.close()

    test_folds_fl = open("/Users/trman/Downloads/DeepDTA-master/data/davis/folds/test_fold_setting1.txt", "w")
    test_folds_fl.write(str(test_folds))
    test_folds_fl.close()

    assert [ind for fold in train_folds for ind in fold]+test_folds == shuffled_indices

    """
    # training_test_val_indices

    # print(sorted([ind for fold in train_folds for ind in fold]+test_folds, reverse=True))
    # print(affinity_matrix[2,16])
    # print(affinity_matrix.flatten()[900])
    """
# deepdta_create_filtered_fold_file("davis")

def create_deepdta_non_5_filtered_dataset():
    full_dti_dataset_path = "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/DeepDTA_davis/dti_datasets/comp_targ_affinity.csv"

    dti_data_fl = open(full_dti_dataset_path, "r")
    lst_dti_data_fl = dti_data_fl.read().split("\n")
    dti_data_fl.close()

    while "" in lst_dti_data_fl:
        lst_dti_data_fl.remove("")

    for line in lst_dti_data_fl:
        comp_id , tar_id, binding_affinity = line.split(",")
        if binding_affinity != "5.0":
            print(line)

# create_deepdta_non_5_filtered_dataset()

def create_pdbind_train_validation_test_folds_based_on_their_predictions():
    df_predictions = pd.read_csv("{}/PDBBind_Refined/helper_files/refined_report.csv".format(training_files_path), sep = ",")
    df_dti_dataset = pd.read_csv("{}/PDBBind_Refined/dti_datasets/comp_targ_affinity.csv".format(training_files_path), header=None, sep = ",")
    # print(df_dti_dataset)
    dict_id_traintestval = dict()
    for ind, row in df_predictions.iterrows():
        id = row["id"]
        train_test_val = row["assign"]
        bioact_val = row["-logKd/Ki"]
        dict_id_traintestval[id] = train_test_val
        # print(id, train_test_val, bioact_val)

    training_ids = []
    validation_ids = []
    test_ids = []

    for ind, row in df_dti_dataset.iterrows():
        comp_id = row[0]
        pdb_id = row[1]
        try:
            if dict_id_traintestval[pdb_id]=="train":
                training_ids.append(ind)
            elif dict_id_traintestval[pdb_id]=="valid":
                validation_ids.append(ind)
            elif dict_id_traintestval[pdb_id]=="test":
                test_ids.append(ind)
            else:
                pass
        except:
            training_ids.append(ind)

    # print([training_ids, validation_ids])
    # print(test_ids)
    #print(len(training_ids)+len(validation_ids)+len(test_ids))
        #print(ind, comp_id, pdb_id)


    """
    lst_methods = df_predictions.columns.values[3:]
    for method in lst_methods:

        method_specific_predictions = df_predictions.loc[:,["id", "assign", "-logKd/Ki", method]].dropna()
        method_specific_test_predictions = method_specific_predictions.loc[method_specific_predictions['assign'] == "test"]
        
        print(method)
        print(method_specific_test_predictions)
        break
    """
# create_pdbind_train_validation_test_folds_based_on_their_predictions()

def create_deepdta_train_test_indices_folds_simboost():
    import json
    #indices are starts with 1 in R therefore we increased all indices by 1
    output_path = "/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/trainingFiles/Davis/data/folds_simboost"
    train_validation_fold_lst = json.load(open("/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/trainingFiles/Davis/data/folds/train_fold_setting1.txt"))
    test_fold_lst = json.load(open("/Users/trman/OneDrive - ceng.metu.edu.tr/Projects/PyTorch/trainingFiles/Davis/data/folds/test_fold_setting1.txt"))

    for fold_id in range(len(train_validation_fold_lst)):
        out_validation_fl = open("{}/validation_fold_{}.csv".format(output_path, fold_id + 1), "w")
        out_validation_fl.write("indices\n")

        out_train_fl = open("{}/train_fold_{}.csv".format(output_path, fold_id + 1), "w")
        out_train_fl.write("indices\n")

        for fold_id2 in range(len(train_validation_fold_lst)):
            if fold_id==fold_id2:
                out_validation_fl.write("\n".join([str(ind + 1) for ind in train_validation_fold_lst[fold_id2]]))
            else:
                out_train_fl.write("\n".join([str(ind + 1) for ind in train_validation_fold_lst[fold_id2]])+"\n")
        out_train_fl.close()
        out_validation_fl.close()

    out_test_fl = open("{}/test.csv".format(output_path), "w")
    out_test_fl.write("indices\n")
    out_test_fl.write("\n".join([str(ind + 1) for ind in test_fold_lst]))
    out_test_fl.close()






# create_deepdta_train_test_indices_folds_simboost()
