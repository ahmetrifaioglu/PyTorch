import pandas as pd
from torch.utils.data import Dataset, DataLoader, TensorDataset
import torch
import numpy as np
from torch.utils.data.sampler import SubsetRandomSampler, BatchSampler, SequentialSampler
import sklearn
from sklearn import preprocessing
import math
import os
import itertools
import torch.nn as nn

cwd = os.getcwd()

training_files_path = "{}/../trainingFiles".format(cwd)
davis_dataset_path = "{}/DeepDTA".format(training_files_path)
davis_comp_tar_training_dataset = "{}/dti_datasets".format(davis_dataset_path)

# print(training_files_path)
# training_files_path = "/hps/nobackup/production/uniprot/rahmet/PyTorch/trainingFiles"
idg_training_dataset_path = "{}/IDGDreamChallenge/dti_datasets".format(training_files_path)
prot_feature_vector_path = "{}/IDGDreamChallenge/protein_feature_vectors".format(training_files_path)
heval_prot_feature_vector_path = "{}/IDGDreamChallenge/DreamChallengeHeval/feature_vectors".format(training_files_path)
comp_feature_vector_path = "{}/IDGDreamChallenge/compound_feature_vectors".format(training_files_path)
comp_feature_vector_path = "{}/IDGDreamChallenge/compound_feature_vectors".format(training_files_path)
tar_feature_vector_path = "{}/IDGDreamChallenge/protein_feature_vectors".format(training_files_path)
helper_fl_path = "../trainingFiles/IDGDreamChallenge/helper_files"


idg_training_dataset_path = "{}/DeepDTA/dti_datasets".format(training_files_path)
prot_feature_vector_path = "{}/DeepDTA/protein_feature_vectors".format(training_files_path)
# heval_prot_feature_vector_path = "{}/DeepDTA/DreamChallengeHeval/feature_vectors".format(training_files_path)
comp_feature_vector_path = "{}/DeepDTA/compound_feature_vectors".format(training_files_path)
tar_feature_vector_path = "{}/DeepDTA/protein_feature_vectors".format(training_files_path)
helper_fl_path = "../trainingFiles/DeepDTA/helper_files"





def get_numpy_target_dict_combined_feature_vectors(target_or_compound, feature_lst):
    sorted(feature_lst)
    feat_vec_path = prot_feature_vector_path if target_or_compound=="target" else comp_feature_vector_path
    common_column = "target id" if target_or_compound=="target" else "compound id"
    # print("{}/{}_normalized.tsv".format(feat_vec_path, feature_lst[0]))
    df_combined_features = dict()
    count = 0
    with open("{}/{}_normalized.tsv".format(feat_vec_path, feature_lst[0])) as f:
        for line in f:
            line = line.split("\n")[0]
            line = line.split("\t")
            target_id = line[0]
            feat_vec = torch.tensor(np.asarray([line[1:]], dtype=float).reshape(1, 500,500)).type(torch.FloatTensor)
            df_combined_features[target_id] = feat_vec
            count+=1
    return df_combined_features

def get_list_target_dict_combined_feature_vectors(target_or_compound, feature_lst):
    sorted(feature_lst)
    feat_vec_path = prot_feature_vector_path if target_or_compound=="target" else comp_feature_vector_path
    common_column = "target id" if target_or_compound=="target" else "compound id"
    # print("{}/{}_normalized.tsv".format(feat_vec_path, feature_lst[0]))
    df_combined_features = dict()
    count = 0
    with open("{}/{}_normalized.tsv".format(feat_vec_path, feature_lst[0])) as f:
        for line in f:
            line = line.split("\n")[0]
            line = line.split("\t")
            target_id = line[0]
            feat_vec = line[1:]
            df_combined_features[target_id] = torch.tensor(np.asarray(feat_vec, dtype=float)).type(torch.FloatTensor)
            count+=1
    return df_combined_features


dict_compound_features = get_list_target_dict_combined_feature_vectors("compound", ["ecfp4"])
dict_target_features = get_numpy_target_dict_combined_feature_vectors("target", ["sequencematrix500"])
training_dataset = pd.read_csv('{}/davis_comp_targ_affinity.csv'.format(idg_training_dataset_path), header=None)


class CNNBioactivityDataset(Dataset):
    def __init__(self, comp_target_pair_dataset, root_dir):
        comp_target_pair_dataset_path = "{}/{}".format(idg_training_dataset_path, comp_target_pair_dataset)
        self.training_dataset = pd.read_csv(comp_target_pair_dataset_path, header=None)
        self.root_dir = root_dir

    def __len__(self):
        return len(self.training_dataset)

    def __getitem__(self, idx):

        #print(idx)
        row = self.training_dataset.iloc[idx]

        comp_id, tar_id, biact_val = str(row[0]), str(row[1]), str(row[2])
        # print(comp_id, tar_id, biact_val)
        """
        data_point_fl = open("{}/deepdta_data/{}_{}_{}.tsv".format(davis_dataset_path, idx, comp_id, tar_id), "r")
        fl_comp_id, fl_tar_id, fl_biact_val, comp_feats, tar_feats = data_point_fl.read().split("\t")
        data_point_fl.close()
        """
        comp_feats = dict_compound_features[comp_id]
        tar_feats = dict_target_features[tar_id]
        label = torch.tensor(float(biact_val)).type(torch.FloatTensor)
        return comp_feats, tar_feats, label, comp_id, tar_id



def get_cnn_test_val_folds_train_data_loader(batch_size=32):
    # from random import choices
    import numpy as np
    import json

    folds = json.load(open("{}/data/davis/folds/train_fold_setting1.txt".format(davis_dataset_path)))
    test = json.load(open("{}/data/davis/folds/test_fold_setting1.txt".format(davis_dataset_path)))
    # print(test)

    davis_bioactivity_dataset = CNNBioactivityDataset(comp_target_pair_dataset='davis_comp_targ_affinity.csv',
                                         root_dir='{}/deepdta_data'.format(idg_training_dataset_path))
    loader_fold_dict = dict()
    for fold_id in range(len(folds)):
        folds_id_list = list(range(len(folds)))
        val_indices = folds[fold_id]
        folds_id_list.remove(fold_id)
        train_indices  = []
        for tr_fold_in in folds_id_list:
            train_indices.extend(folds[tr_fold_in])

        train_sampler = SubsetRandomSampler(train_indices)
        valid_sampler = SubsetRandomSampler(val_indices)

        train_loader = torch.utils.data.DataLoader(davis_bioactivity_dataset, batch_size=batch_size,
                                                   sampler=train_sampler)

        valid_loader = torch.utils.data.DataLoader(davis_bioactivity_dataset, batch_size=batch_size,
                                                   sampler=valid_sampler)

        loader_fold_dict[fold_id] = [train_loader, valid_loader]

    # test_sampler = BatchSampler(SequentialSampler(test), batch_size=batch_size, drop_last=False)
    test_sampler = SequentialSampler(test)
    test_loader = torch.utils.data.DataLoader(davis_bioactivity_dataset, batch_size=batch_size,
                                                   sampler=test_sampler)
    return loader_fold_dict, test_loader





"""
for i, data in enumerate(train_loader):
    # get the inputs
    print(i)
    comp_feature_vectors, target_feature_vectors, labels, comp_ids, tar_ids = data
    print(target_feature_vectors.shape)
    print(comp_feature_vectors.shape)
"""
"""
loader_fold_dict, test_loader = get_cnn_test_val_folds_train_data_loader()
train_loader = loader_fold_dict[0][1]
for i, data in enumerate(train_loader):
    # get the inputs
    print(i)
    comp_feature_vectors, target_feature_vectors, labels, comp_ids, tar_ids = data
    print(target_feature_vectors.shape)
    print(comp_feature_vectors.shape)
"""