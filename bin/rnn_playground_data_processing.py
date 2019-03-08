import numpy as np
import torch
from torch.utils.data import TensorDataset, DataLoader
import itertools
helper_fl_path = "../trainingFiles/IDGDreamChallenge/helper_files"

def get_prot_id_seq_dict_from_fasta_fl(fasta_fl):
    prot_id_seq_dict = dict()

    prot_id = ""
    with open("{}/{}".format(helper_fl_path, fasta_fl)) as f:
        for line in f:
            line = line.split("\n")[0]
            if line.startswith(">"):
                prot_id = line.split("|")[1]
                prot_id_seq_dict[prot_id] = ""
            else:
                prot_id_seq_dict[prot_id] = prot_id_seq_dict[prot_id] + line

    return prot_id_seq_dict

def get_aa_list():
    aa_list = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
    return aa_list


def get_all_aa_word_list(word_size):
    aa_list = get_aa_list()
    #all_n_gram_list = list(itertools.permutations(aa_list, word_size))
    all_n_gram_list = list(itertools.product(aa_list, repeat=word_size))
    all_n_gram_list = [''.join(n_gram_tuple) for n_gram_tuple in all_n_gram_list]
    return all_n_gram_list


def get_int2aaword_aaword2int_dicts(word_size):
    aa_word_list = get_all_aa_word_list(word_size)
    int2aaword_dict = dict(enumerate(aa_word_list, 1))
    aaword2int_dict = {ch: ii for ii, ch in int2aaword_dict.items()}
    return int2aaword_dict, aaword2int_dict


def get_overlapping_n_grams_list(prot_seq, word_size, skip_size):
    prot_seq_overlapping_ngram_list = None
    if skip_size!=0:
        prot_seq_overlapping_ngram_list =[prot_seq[ind:ind + word_size] for ind in range(0, (len(prot_seq) - (word_size - 1)), skip_size)]
    else:
        prot_seq_overlapping_ngram_list = [prot_seq[ind:ind + word_size] for ind in
                                           range(len(prot_seq) - (word_size - 1))]
    return prot_seq_overlapping_ngram_list

def remove_nonstandard_aas(prot_seq):
    aa_list = get_aa_list()
    prot_seq_list = [aa for aa in prot_seq if aa in aa_list]
    prot_seq = ''.join(prot_seq_list)
    return prot_seq

'''
Gets a sequence as an input whose nonstandard aminoacids removed
'''
def encode_protein_sequence(prot_seq, word_size, skip_size, aaword2int_dict):
    prot_seq_overlapping_ngram_list = get_overlapping_n_grams_list(prot_seq, word_size, skip_size)
    prot_seq_encoded = [aaword2int_dict[aa_word] for aa_word in prot_seq_overlapping_ngram_list]
    return prot_seq_encoded


def get_int_encodings_of_proteins_sequences(fasta_fl, word_size, skip_size):
    int2aaword_dict, aaword2int_dict = get_int2aaword_aaword2int_dicts(word_size)
    # print(aaword2int_dict)
    prot_id_list, seq_encoding_list  = [], []
    prot_id_seq_dict = get_prot_id_seq_dict_from_fasta_fl(fasta_fl)
    for prot_id, seq in prot_id_seq_dict.items():
        # first remove nonstandard aminoacids
        # print(seq)
        seq = remove_nonstandard_aas(seq)
        prot_id_list.append(prot_id)
        seq_encoding_list.append(encode_protein_sequence(seq, word_size, skip_size, aaword2int_dict))
    return prot_id_list, seq_encoding_list


def pad_encoded_features(seq_encoding_list, seq_length=1000):
    '''
    Return features of review_ints, where each review is padded with 0's
    or truncated to the input seq_length.
    '''

    # getting the correct rows x cols shape
    padded_features = np.zeros((len(seq_encoding_list), seq_length), dtype=int)


    for i, row in enumerate(seq_encoding_list):
        # padding before
        # padded_features[i, -len(row):] = np.array(row)[:seq_length]
        # padding after
        padded_features[i,:len(row)] = np.array(row)[:seq_length]

    return padded_features

def save_encoded_features(fasta_fl, word_size, skip_size, seq_length):

    prot_id_list, seq_encoding_list = get_int_encodings_of_proteins_sequences(fasta_fl, word_size, skip_size)
    padded_features = pad_encoded_features(seq_encoding_list, seq_length)

    str_header = "target id\t"+"\t".join([str(num) for num in list(range(seq_length))])
    print(str_header)
    for idx, prot_id in enumerate(prot_id_list):
        # print(idx, prot_id)
        print(prot_id+"\t"+"\t".join([str(num) for num in padded_features[idx]]))




def get_data_lists():
    split_frac = 0.8

    ## split data into training, validation, and test data (features and labels, x and y)

    split_idx = int(len(features) * split_frac)
    train_x, remaining_x = features[:split_idx], features[split_idx:]
    train_y, remaining_y = encoded_labels[:split_idx], encoded_labels[split_idx:]

    test_idx = int(len(remaining_x) * 0.5)
    val_x, test_x = remaining_x[:test_idx], remaining_x[test_idx:]
    val_y, test_y = remaining_y[:test_idx], remaining_y[test_idx:]

    ## print out the shapes of your resultant feature data
    print("\t\t\tFeature Shapes:")
    print("Train set: \t\t{}".format(train_x.shape),
          "\nValidation set: \t{}".format(val_x.shape),
          "\nTest set: \t\t{}".format(test_x.shape))
    return train_x, train_y, val_x, val_y, test_x, test_y


def get_train_test_val_data_loaders(batch_size):
    # create Tensor datasets
    train_data = TensorDataset(torch.from_numpy(train_x), torch.from_numpy(train_y))
    valid_data = TensorDataset(torch.from_numpy(val_x), torch.from_numpy(val_y))
    test_data = TensorDataset(torch.from_numpy(test_x), torch.from_numpy(test_y))

    # make sure the SHUFFLE your training data
    train_loader = DataLoader(train_data, shuffle=True, batch_size=batch_size)
    valid_loader = DataLoader(valid_data, shuffle=True, batch_size=batch_size)
    test_loader = DataLoader(test_data, shuffle=True, batch_size=batch_size)

    return train_loader, valid_loader, test_loader

"""
# LEGACY CODE

def create_onehot_aa_vector(aa_index):
    int2aa_dict, aa2int_dict = get_int2aa_aa2int_dicts()
    # create a zero array and assign 1 to corresponding index
    aa_onehot_arr = np.zeros(len(aa2int_dict))
    np.put(aa_onehot_arr, aa_index, 1)
    return aa_onehot_arr
    

def convert_protein_sequence_into_onehot(prot_seq):
    lst_encoded_seq = encode_protein_sequence(prot_seq)
    prot_seq_onehot = [create_onehot_aa_vector(aa_ind) for aa_ind in lst_encoded_seq]
    return prot_seq_onehot

    
"""