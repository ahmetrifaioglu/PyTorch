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
import sys


cwd = os.getcwd()
training_files_path = "{}/../trainingFiles".format(cwd)
compound_target_pair_dataset = "comp_targ_affinity.csv"

def get_numpy_target_dict_combined_feature_vectors(training_data_name, target_or_compound, feature_lst):
    sorted(feature_lst)
    training_dataset_path = "{}/{}".format(training_files_path, training_data_name)
    comp_feature_vector_path = "{}/compound_feature_vectors".format(training_dataset_path)
    tar_feature_vector_path = "{}/target_feature_vectors".format(training_dataset_path)
    feat_vec_path = tar_feature_vector_path if target_or_compound == "target" else comp_feature_vector_path
    common_column = "target id" if target_or_compound=="target" else "compound id"
    df_combined_features = dict()
    count = 0
    with open("{}/{}_normalized.tsv".format(feat_vec_path, feature_lst[0])) as f:
        for line in f:
            line = line.split("\n")[0]
            line = line.split("\t")
            target_id = line[0]
            # feat_vec = torch.tensor(np.asarray([line[1:]], dtype=float).reshape(1, 1000,1000)).type(torch.FloatTensor)
            feat_vec = torch.tensor(np.asarray([line[1:]], dtype=float).reshape(1, 500, 500)).type(torch.FloatTensor)
            df_combined_features[target_id] = feat_vec
            count+=1
    return df_combined_features

def get_list_target_dict_combined_feature_vectors(training_data_name, target_or_compound, feature_lst):
    sorted(feature_lst)
    training_dataset_path = "{}/{}".format(training_files_path, training_data_name)
    comp_feature_vector_path = "{}/compound_feature_vectors".format(training_dataset_path)
    tar_feature_vector_path = "{}/target_feature_vectors".format(training_dataset_path)
    feat_vec_path = tar_feature_vector_path if target_or_compound == "target" else comp_feature_vector_path
    common_column = "target id" if target_or_compound=="target" else "compound id"
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



# training_dataset = pd.read_csv('{}/{}'.format(comp_tar_training_dataset_path, compound_target_pair_dataset), header=None)



class CNNBioactivityDataset(Dataset):
    def __init__(self, training_data_name, comp_target_pair_dataset, compound_feature_list, target_feature_list):
        training_dataset_path = "{}/{}".format(training_files_path, training_data_name)
        comp_tar_training_dataset_path = "{}/dti_datasets".format(training_dataset_path)
        comp_target_pair_dataset_path = "{}/{}".format(comp_tar_training_dataset_path, comp_target_pair_dataset)
        self.dict_compound_features = get_list_target_dict_combined_feature_vectors(training_data_name, "compound", compound_feature_list)
        self.dict_target_features = get_numpy_target_dict_combined_feature_vectors(training_data_name, "target", target_feature_list)
        self.training_dataset = pd.read_csv(comp_target_pair_dataset_path, header=None)
        #print(self.training_dataset)
    def __len__(self):
        return len(self.training_dataset)

    def __getitem__(self, idx):
        row = self.training_dataset.iloc[idx]

        comp_id, tar_id, biact_val = str(row[0]), str(row[1]), str(row[2])
        comp_feats = self.dict_compound_features[comp_id]
        tar_feats = self.dict_target_features[tar_id]
        label = torch.tensor(float(biact_val)).type(torch.FloatTensor)
        return comp_feats, tar_feats, label, comp_id, tar_id



def get_cnn_test_val_folds_train_data_loader(training_data_name, comp_feature_list, tar_feature_list, batch_size=32):
    import numpy as np
    import json

    training_dataset_path = "{}/{}".format(training_files_path, training_data_name)
    folds_path = "{}/data/folds".format(training_dataset_path)

    folds = json.load(open("{}/train_fold_setting1.txt".format(folds_path)))
    test = json.load(open("{}/test_fold_setting1.txt".format(folds_path)))

    bioactivity_dataset = CNNBioactivityDataset(training_data_name, compound_target_pair_dataset, comp_feature_list, tar_feature_list)
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

        train_loader = torch.utils.data.DataLoader(bioactivity_dataset, batch_size=batch_size,
                                                   sampler=train_sampler)

        valid_loader = torch.utils.data.DataLoader(bioactivity_dataset, batch_size=batch_size,
                                                   sampler=valid_sampler)

        loader_fold_dict[fold_id] = [train_loader, valid_loader]

    test_sampler = SubsetRandomSampler(test)
    test_loader = torch.utils.data.DataLoader(bioactivity_dataset, batch_size=batch_size,
                                                   sampler=test_sampler)
    return loader_fold_dict, test_loader



def get_cnn_train_test_full_training_data_loader(training_data_name, batch_size=32, train_test_val=False):
    import numpy as np
    import json

    training_dataset_path = "{}/{}".format(training_files_path, training_data_name)
    folds_path = "{}/data/folds".format(training_dataset_path)

    folds = json.load(open("{}/train_fold_setting1.txt".format(folds_path)))
    test = json.load(open("{}/test_fold_setting1.txt".format(folds_path)))
    #print(test)
    #print("{}/train_fold_setting1.txt".format(folds_path))
    #print("{}/test_fold_setting1.txt".format(folds_path))
    #print(compound_target_pair_dataset)
    bioactivity_dataset = CNNBioactivityDataset(training_data_name, compound_target_pair_dataset, comp_feature_list, tar_feature_list)
    # print(len(bioactivity_dataset))
    train_indices = []
    validation_indices = []

    if train_test_val:
        train_indices = folds[0]
        validation_indices = folds[1]
    else:
        for fold_id in range(len(folds)):
            train_indices.extend(folds[fold_id])

    train_sampler = SubsetRandomSampler(train_indices)

    train_loader = torch.utils.data.DataLoader(bioactivity_dataset, batch_size=batch_size,
                                               sampler=train_sampler)

    validation_sampler, validation_loader = None, None
    if train_test_val:
        validation_sampler = SubsetRandomSampler(validation_indices)
        validation_loader = torch.utils.data.DataLoader(bioactivity_dataset, batch_size=batch_size,
                                                   sampler=validation_sampler)


    test_sampler = SubsetRandomSampler(test)
    test_loader = torch.utils.data.DataLoader(bioactivity_dataset, batch_size=batch_size,
                                                   sampler=test_sampler)
    if train_test_val:
        return train_loader, validation_loader, test_loader

    return train_loader, test_loader




