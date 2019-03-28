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

def getChEMBLTargetIDUniProtMapping():
    chembl_uniprot_dict = dict()

    with open("{}/{}".format(training_files_path, "chembl24_uniprot_mapping.txt")) as f:
        for line in f:
            if not line.startswith("#") and line != "":
                line=line.split("\n")[0]
                #print(line.split("\t"))
                u_id, chembl_id, defin, target_type = line.split("\t")

                if target_type=='SINGLE PROTEIN':

                    try:
                        chembl_uniprot_dict[chembl_id].append(u_id)
                        #print("varmis", comp_id, uniprot_id)
                    except:
                        chembl_uniprot_dict[chembl_id] = [u_id]
    #for key in chembl_uniprot_dict.keys():
    #    if len(chembl_uniprot_dict[key])!=1:
    #        print(key, chembl_uniprot_dict[key])

    return chembl_uniprot_dict

def getSMILEsForChEMBLIDList(rep_fl, lst_chembl_ids):
    isFirst = True
    prob_count = 0
    dict_ids = dict()
    for id in lst_chembl_ids:
        dict_ids[id] = 0
    # there should be a header in the smiles file
    compound_smiles_dict = dict()
    # print("DENEME../trainingFiles/{}".format(rep_fl))
    with open("../all_trainingFiles/{}".format(rep_fl)) as f:
        for line in f:
            if isFirst:
                isFirst = False
            else:
                #print(line)
                line = line.split("\n")[0]
                temp_parts = line.split("\t")
                # print(temp_parts)
                chembl_id, smiles = temp_parts[0], temp_parts[1]
                try:
                    dict_ids[chembl_id]
                    compound_smiles_dict[chembl_id] = smiles
                except:
                    pass

    return compound_smiles_dict

def getChEMBL24KDBioactivities():

    dict_chembl_uniprot_mapping = getChEMBLTargetIDUniProtMapping()
    df_chembl24_activities = pd.read_csv("/Users/trman/OneDrive/Projects/DEEPScreen/inputDatasets/ChEMBL24_preprocessed_activities_sp_b_pchembl.txt", sep="\t", index_col=False)
    df_only_kd = df_chembl24_activities[df_chembl24_activities["standard_type"]=="Kd"]
    df_only_kd_actives = df_only_kd[df_only_kd["pchembl_value"] > 7.0]

    df_dti_original_dataset = pd.read_csv("{}/{}".format(idg_training_dataset_path, "idg_comp_targ_uniq_inter_filtered.csv"), header=None)

    original_comp_tar_pair_set = set()
    for ind, data in df_dti_original_dataset.iterrows():
        comp_id, uniprot_id = data[0], data[1]
        original_comp_tar_pair_set.add("{}_{}".format(comp_id, uniprot_id))



    new_chembl24_comp_tar_pair_dict = dict()
    for ind, data in df_only_kd_actives.iterrows():
        new_chembl24_comp_tar_pair_dict["{}_{}".format(data["Compound_CHEMBL_ID"], dict_chembl_uniprot_mapping[data["Target_CHEMBL_ID"]][0])] = data["pchembl_value"]

    new_data_comp_tar_pairs = set(new_chembl24_comp_tar_pair_dict.keys()) - original_comp_tar_pair_set
    # print(df_dti_original_dataset)

    new_data_points = []
    for pair in new_data_comp_tar_pairs:
        comp_id, uniprot_id = pair.split("_")
        new_data_points.append([comp_id, uniprot_id, new_chembl24_comp_tar_pair_dict[pair]])


    headers = df_dti_original_dataset.columns
    df_new_data_points = pd.DataFrame(new_data_points, columns=headers)

    df_dti_original_dataset = df_dti_original_dataset.append(df_new_data_points)

    df_dti_original_dataset.to_csv(
        "{}/{}".format(idg_training_dataset_path, "idg_comp_targ_uniq_inter_filtered_chembl24.csv"), header=False, index=False)


# getChEMBL24KDBioactivities()

def get_dict_combined_feature_vectors(target_or_compound, feature_lst):
    sorted(feature_lst)
    feat_vec_path = prot_feature_vector_path if target_or_compound=="target" else comp_feature_vector_path
    common_column = "target id" if target_or_compound=="target" else "compound id"
    # print("{}/{}_normalized.tsv".format(feat_vec_path, feature_lst[0]))
    df_combined_features = pd.read_csv("{}/{}_normalized.tsv".format(feat_vec_path, feature_lst[0]), sep="\t")
    # print(df_combined_features.columns)
    for feat in feature_lst[1:]:
        df_temp_features =  pd.read_csv("{}/{}_normalized.tsv".format(feat_vec_path, feat), sep="\t")
        df_combined_features = pd.merge(df_combined_features, df_temp_features, on=[common_column])
    # print(df_combined_features)
    df_combined_features = df_combined_features.set_index(common_column).T.to_dict('list')
    #print(df_combined_features)
    # print(df_combined_features.keys())

    #print(df_combined_features.columns)
    return df_combined_features


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
            #feat_vec = torch.from_numpy(np.asarray(line[1:], dtype=float)).view(500,500)
            feat_vec = np.asarray([line[1:]], dtype=float).reshape(1, 500,500)
            # print(feat_vec.shape)
            # print(count, len(line))
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
            df_combined_features[target_id] = feat_vec
            count+=1
    return df_combined_features


class TrainingValidationShuffledDataLoader(Dataset):

    def __init__(self, comp_feature_list, target_feature_lst, comp_target_pair_dataset, regression_classifier):

        comp_target_pair_dataset_path = "{}/{}".format(idg_training_dataset_path, comp_target_pair_dataset)
        dict_compound_features = get_dict_combined_feature_vectors("compound", comp_feature_list)
        dict_target_features = get_dict_combined_feature_vectors("target", target_feature_lst)

        training_dataset = pd.read_csv(comp_target_pair_dataset_path, header=None)
        # https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows
        # The frac keyword argument specifies the fraction of rows to return in the random sample,
        # so frac=1 means return all rows (in random order).
        training_dataset = training_dataset.sample(frac=1).reset_index(drop=True)
        self.compound_ids = training_dataset.iloc[:, 0]
        self.target_ids = training_dataset.iloc[:, 1]
        self.labels = training_dataset.iloc[:, 2]


        valid_compound_ids = []
        valid_target_ids = []
        self.comp_feature_vectors = []
        self.target_feature_vectors = []
        valid_labels = []

        invalid_data_points = 0
        total_number_of_data_points = 0
        for ind  in range(len(self.labels)):
            total_number_of_data_points += 1
            #print(dict_compound_features[comp_id])
            try:
                comp_id = self.compound_ids[ind]
                tar_id = self.target_ids[ind]
                lbl = self.labels[ind]
                comp_features = dict_compound_features[comp_id]
                tar_features = dict_target_features[tar_id]
                self.comp_feature_vectors.append(comp_features)
                self.target_feature_vectors.append(tar_features)
                # valid_labels.append(-math.log10(10e-10*float(lbl)))
                # valid_labels.append(10**(9-float(lbl))) # dogru olan bu
                if regression_classifier=="r":
                    valid_labels.append(float(lbl))
                else:
                    #print(lbl)
                    valid_labels.append([1, 0] if int(lbl)==1 else [0, 1])
                valid_compound_ids.append(comp_id)
                valid_target_ids.append(tar_id)
            except:
                invalid_data_points+=1
                # print(tar_id)
                pass

        print("{} data points are invalid out of {}!".format(invalid_data_points, total_number_of_data_points))

        self.comp_feature_vectors = np.asarray(self.comp_feature_vectors)
        self.comp_feature_vectors = torch.tensor(self.comp_feature_vectors).type(torch.FloatTensor)

        self.target_feature_vectors = np.asarray(self.target_feature_vectors)
        self.target_feature_vectors = torch.tensor(self.target_feature_vectors).type(torch.FloatTensor)

        self.labels = torch.tensor(valid_labels).type(torch.FloatTensor)
        self.compound_ids = valid_compound_ids
        self.target_ids = valid_target_ids

        self.number_of_comp_features = int(self.comp_feature_vectors.shape[1])
        self.number_of_target_features = int(self.target_feature_vectors.shape[1])

    def __getitem__(self, index):
        return self.comp_feature_vectors[index], self.target_feature_vectors[index], self.labels[index], self.compound_ids[index], self.target_ids[index], self.number_of_comp_features, self.number_of_target_features

    def __len__(self):
        return len(self.compound_ids)


class TrainingValidationShuffledDataLoaderCNN(Dataset):

    def __init__(self, comp_feature_list, target_feature_lst, comp_target_pair_dataset, fasta_fl_path, regression_classifier):
        comp_target_pair_dataset_path = "{}/{}".format(idg_training_dataset_path, comp_target_pair_dataset)
        dict_compound_features = get_dict_combined_feature_vectors("compound", comp_feature_list)

        dict_target_features = get_list_target_dict_combined_feature_vectors("target", target_feature_lst)
        prot_id_seq_dict = get_prot_id_seq_dict_from_fasta_fl(fasta_fl_path)
        training_dataset = pd.read_csv(comp_target_pair_dataset_path, header=None)

        training_dataset = training_dataset.sample(frac=1).reset_index(drop=True)
        self.compound_ids = training_dataset.iloc[:, 0]
        self.target_ids = training_dataset.iloc[:, 1]
        self.labels = training_dataset.iloc[:, 2]


        valid_compound_ids = []
        valid_target_ids = []
        self.comp_feature_vectors = []
        self.target_feature_vectors = []

        valid_labels = []

        invalid_data_points = 0
        total_number_of_data_points = 0
        for ind in range(len(self.labels)):
            total_number_of_data_points += 1
            try:
                #if len(prot_id_seq_dict[self.target_ids[ind]])<=500:
                comp_id = self.compound_ids[ind]
                tar_id = self.target_ids[ind]
                lbl = self.labels[ind]
                comp_features = dict_compound_features[comp_id]
                tar_features = dict_target_features[tar_id]
                #tar_features = get_sequence_matrix(prot_id_seq_dict[tar_id], size)
                self.comp_feature_vectors.append(comp_features)
                self.target_feature_vectors.append(tar_features)
                # valid_labels.append(-math.log10(10e-10*float(lbl)))
                # valid_labels.append(10**(9-float(lbl))) # dogru olan bu
                if regression_classifier=="r":
                    valid_labels.append(float(lbl))
                else:
                    #print(lbl)
                    valid_labels.append([1, 0] if int(lbl)==1 else [0, 1])
                valid_compound_ids.append(comp_id)
                valid_target_ids.append(tar_id)
            except:
                invalid_data_points+=1
                # print(tar_id)
                pass

        print("{} data points are invalid out of {}!".format(invalid_data_points, total_number_of_data_points))

        self.comp_feature_vectors = np.asarray(self.comp_feature_vectors)
        self.comp_feature_vectors = torch.tensor(self.comp_feature_vectors).type(torch.FloatTensor)

        self.target_feature_vectors = np.asarray(self.target_feature_vectors)
        # print(self.target_feature_vectors.shape)
        self.target_feature_vectors = torch.tensor(self.target_feature_vectors).type(torch.FloatTensor)
        # print("cikti")
        self.labels = torch.tensor(valid_labels).type(torch.FloatTensor)
        self.compound_ids = valid_compound_ids
        self.target_ids = valid_target_ids

        self.number_of_comp_features = int(self.comp_feature_vectors.shape[1])
        self.number_of_target_features = int(self.target_feature_vectors.shape[1])

    def __getitem__(self, index):
        return self.comp_feature_vectors[index], self.target_feature_vectors[index], self.labels[index], self.compound_ids[index], self.target_ids[index], self.number_of_comp_features, self.number_of_target_features

    def __len__(self):
        return len(self.compound_ids)

def get_training_validation_data_loaders_for_cnn(num_of_folds, batch_size, comp_feature_list, target_feature_lst, comp_target_pair_dataset, fasta_fl_path, regression_classifier):
    # from random import choices
    import numpy as np
    loader_fold_dict = dict()
    valid_size = 0.2
    if num_of_folds > 1:
        valid_size = round(1.0 / float(num_of_folds), 1)
    train_val_data = TrainingValidationShuffledDataLoaderCNN(comp_feature_list, target_feature_lst, comp_target_pair_dataset, fasta_fl_path, regression_classifier)

    number_of_comp_features = train_val_data.number_of_comp_features
    number_of_target_features = train_val_data.number_of_target_features

    total_number_of_samples = len(train_val_data)

    num_of_valid_samples = int(np.floor(valid_size * total_number_of_samples))
    num_of_training_samples = total_number_of_samples - num_of_valid_samples

    print("Number of training samples:\t{}".format(num_of_training_samples))
    print("Number of validation samples:\t{}".format(num_of_valid_samples))

    for fold_id in range(num_of_folds):
        val_starting_index = fold_id * num_of_valid_samples
        val_end_index = val_starting_index + num_of_valid_samples
        val_indices = list(range(val_starting_index, val_end_index))
        train_indices = list(set(range(total_number_of_samples)) - set(val_indices))
        # define samplers for obtaining training and validation batches
        train_sampler = SubsetRandomSampler(train_indices)
        valid_sampler = SubsetRandomSampler(val_indices)
        train_loader = torch.utils.data.DataLoader(train_val_data, batch_size=batch_size,
                                                   sampler=train_sampler)

        valid_loader = torch.utils.data.DataLoader(train_val_data, batch_size=batch_size,
                                                   sampler=valid_sampler)

        loader_fold_dict[fold_id] = [train_loader, valid_loader]
    return loader_fold_dict, number_of_comp_features, number_of_target_features


def get_full_training_data_loader(batch_size, comp_feature_list, target_feature_lst, comp_target_pair_dataset, regression_classifier):


    train_val_data = TrainingValidationShuffledDataLoader(comp_feature_list, target_feature_lst, comp_target_pair_dataset, regression_classifier)

    number_of_comp_features = train_val_data.number_of_comp_features
    number_of_target_features = train_val_data.number_of_target_features

    # print(train_val_data.compound_ids)
    # print(train_val_data.target_ids)
    total_number_of_samples = len(train_val_data)
    train_loader = torch.utils.data.DataLoader(train_val_data, batch_size=batch_size, shuffle=True)
    #print(total_number_of_samples)
    #self.number_of_comp_features, self.number_of_target_features
    return train_loader, number_of_comp_features, number_of_target_features


def get_nfold_data_loader_dict(num_of_folds, batch_size, comp_feature_list, target_feature_lst, comp_target_pair_dataset, regression_classifier):
    # from random import choices
    import numpy as np
    loader_fold_dict = dict()
    valid_size = 0.2
    if num_of_folds > 1:
        valid_size = round(1.0 / float(num_of_folds), 1)
    #print(comp_feature_list)
    train_val_data = TrainingValidationShuffledDataLoader(comp_feature_list, target_feature_lst, comp_target_pair_dataset, regression_classifier)
    # print(train_val_data)

    number_of_comp_features = train_val_data.number_of_comp_features
    number_of_target_features = train_val_data.number_of_target_features

    # print(train_val_data.compound_ids)
    # print(train_val_data.target_ids)
    total_number_of_samples = len(train_val_data)
    #print(total_number_of_samples)
    #self.number_of_comp_features, self.number_of_target_features


    num_of_valid_samples = int(np.floor(valid_size * total_number_of_samples))
    num_of_training_samples = total_number_of_samples - num_of_valid_samples

    print("Number of training samples:\t{}".format(num_of_training_samples))
    print("Number of validation samples:\t{}".format(num_of_valid_samples))

    for fold_id in range(num_of_folds):
        val_starting_index = fold_id * num_of_valid_samples
        val_end_index = val_starting_index + num_of_valid_samples
        val_indices = list(range(val_starting_index, val_end_index))
        train_indices = list(set(range(total_number_of_samples)) - set(val_indices))

        # burada train datayi yeni bir liste al
        # print(len(train_indices))
        # print(len(val_indices))
        # print(train_indices)
        #print(val_indices)
        """
        # this code block is to make positive and negative dataset balanced
        # by sampling (with replacement) more data from active class until the datasets are balanced
        active_indeces = []
        inactive_indeces = []

        for ind in train_indices:
            if float(train_val_data[ind][-5])>7.0:
                active_indeces.append(ind)
            else:
                inactive_indeces.append(ind)

        # print(len(active_indeces))
        # print(len(inactive_indeces))
        sample_count = len(inactive_indeces) - len(active_indeces)
        new_sampled_active_indices = np.random.choice(active_indeces, sample_count)

        for new_ind in new_sampled_active_indices:
            train_indices.append(new_ind)
        """
        # choices(colors, k=4)
        # for ind in range(len(train_val_data)):
        #    print(train_val_data[ind][-5])

        # define samplers for obtaining training and validation batches
        train_sampler = SubsetRandomSampler(train_indices)
        valid_sampler = SubsetRandomSampler(val_indices)

        # print(fold_id, len(train_sampler.indices))
        # print(fold_id, valid_sampler.indices)
        train_loader = torch.utils.data.DataLoader(train_val_data, batch_size=batch_size,
                                                   sampler=train_sampler)

        valid_loader = torch.utils.data.DataLoader(train_val_data, batch_size=batch_size,
                                                   sampler=valid_sampler)

        loader_fold_dict[fold_id] = [train_loader, valid_loader]


        """
        # Just to check if everything is OK. 
        # Remove this when you finish testing.
        print("-----FOLD {} -------".format(fold_id+1))
        print("Training dataset:")
        # dataiter = iter(train_loader)
        for i, data in enumerate(train_loader):
            print("Training Batch")
            comp_feature_vectors, target_feature_vectors, labels, comp_ids, target_ids, number_of_comp_features, number_of_target_features = data
            for ind in range(len(labels)):
                print(comp_ids[ind], target_ids[ind], labels[ind], comp_feature_vectors[ind], target_feature_vectors[ind])

        for i, data in enumerate(valid_loader):
            print("Validation dataset:")
            #dataiter = iter(valid_loader)
            print("Validation Batch")
            comp_feature_vectors, target_feature_vectors, labels, comp_ids, target_ids, number_of_comp_features, number_of_target_features = data
            for ind in range(len(labels)):
                print(comp_ids[ind], target_ids[ind], labels[ind], comp_feature_vectors[ind], target_feature_vectors[ind])
        """

    # print(loader_fold_dict, number_of_comp_features, number_of_target_features)
    return loader_fold_dict, number_of_comp_features, number_of_target_features


class TestDataLoader(Dataset):

    def __init__(self, comp_feature_list, target_feature_lst, comp_target_pair_dataset):

        comp_target_pair_dataset_path = "{}/{}".format(idg_training_dataset_path, comp_target_pair_dataset)

        dict_compound_features = get_dict_combined_feature_vectors("compound", comp_feature_list)
        dict_target_features = get_dict_combined_feature_vectors("target", target_feature_lst)

        training_dataset = pd.read_csv(comp_target_pair_dataset_path, header=None)
        # https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows
        # The frac keyword argument specifies the fraction of rows to return in the random sample,
        # so frac=1 means return all rows (in random order).
        # training_dataset = training_dataset.sample(frac=1).reset_index(drop=True)
        self.compound_ids = training_dataset.iloc[:, 0]
        self.target_ids = training_dataset.iloc[:, 1]
        # self.labels = training_dataset.iloc[:, 2]


        valid_compound_ids = []
        valid_target_ids = []
        self.comp_feature_vectors = []
        self.target_feature_vectors = []
        valid_labels = []

        invalid_data_points = 0
        total_number_of_data_points = 0
        for ind  in range(len(self.compound_ids)):
            total_number_of_data_points += 1
            #print(dict_compound_features[comp_id])
            #try:
            comp_id = self.compound_ids[ind]
            tar_id = self.target_ids[ind]
            #lbl = self.labels[ind]
            comp_features = dict_compound_features[comp_id]
            tar_features = dict_target_features[tar_id]
            self.comp_feature_vectors.append(comp_features)
            self.target_feature_vectors.append(tar_features)
            #valid_labels.append(-math.log10(10e-10*float(lbl)))
            #valid_labels.append(float(lbl))
            valid_compound_ids.append(comp_id)
            valid_target_ids.append(tar_id)
            #except:
            #    invalid_data_points+=1
            #    print()
            #    pass

        print("{} data points are invalid out of {}!".format(invalid_data_points, total_number_of_data_points))

        self.comp_feature_vectors = np.asarray(self.comp_feature_vectors)
        self.comp_feature_vectors = torch.tensor(self.comp_feature_vectors).type(torch.FloatTensor)

        self.target_feature_vectors = np.asarray(self.target_feature_vectors)
        self.target_feature_vectors = torch.tensor(self.target_feature_vectors).type(torch.FloatTensor)

        #self.labels = torch.tensor(valid_labels).type(torch.FloatTensor)
        self.compound_ids = valid_compound_ids
        self.target_ids = valid_target_ids

        self.number_of_comp_features = int(self.comp_feature_vectors.shape[1])
        self.number_of_target_features = int(self.target_feature_vectors.shape[1])

    def __getitem__(self, index):
        return self.comp_feature_vectors[index], self.target_feature_vectors[index], self.compound_ids[index], self.target_ids[index], self.number_of_comp_features, self.number_of_target_features

    def __len__(self):
        return len(self.compound_ids)


def get_test_loader(comp_feature_list, target_feature_lst, comp_target_pair_dataset):#batch_size, comp_feature_list, target_feature_lst, comp_target_pair_dataset):

    test_data = TestDataLoader(comp_feature_list, target_feature_lst, comp_target_pair_dataset)
    total_number_of_samples = len(test_data)

    print("Number of test samples:\t{}".format(total_number_of_samples))

    test_loader = torch.utils.data.DataLoader(test_data) #, batch_size=batch_size)

    # print(loader_fold_dict, number_of_comp_features, number_of_target_features)
    return test_loader

# get_nfold_data_loader_dict(5, 32, ["comp_dummy_feat_1", "comp_dummy_feat_2"], ["prot_dummy_feat_1", "prot_dummy_feat_2"], "dummy_Dtc_comp_targ_uniq_inter_filtered_onlykinase.txt")



# get_df_combined_feature_vectors("target", ["k_sep_bigrams", "APAAC", "pfam"])

# comp_dummy_features = ["comp_dummy_feat_1", "comp_dummy_feat_2"]
# prot_dummy_features = ["prot_dummy_feat_1", "prot_dummy_feat_2"]

# print(get_dict_combined_feature_vectors("compound", comp_dummy_features))
# print(get_dict_combined_feature_vectors("target", prot_dummy_features))



def create_normalized_feature_vector_files(target_or_compound):


    # feature_types = ["tri_gram", "spmap", "pfam", "k_sep_bigrams", "DDE", "APAAC"]
    feature_types = None
    if target_or_compound=="target":
        #feature_types = ["tri_gram", "spmap", "pfam", "k_sep_bigrams", "DDE", "APAAC"]
        #feature_types = ["spmap_final", "pfam", "k-sep-bigrams", "DDE", "APAAC"]
        feature_types = ["k-sep-bigrams", "trigram"]
    elif target_or_compound == "compound":
        feature_types = ["ecfp4", "fcfp4", "rdk5"]

    for feat in feature_types:
        dataset_path = None
        if target_or_compound =="target":
            dataset_path = "{}/{}.tsv".format(tar_feature_vector_path, feat)
        elif target_or_compound=="compound":
            dataset_path = "{}/{}.tsv".format(comp_feature_vector_path, feat)
        print(dataset_path)
        training_dataset = pd.read_csv(dataset_path, sep="\t")
        columns = training_dataset.columns
        target_column = training_dataset.iloc[:, 0]
        for ind in range(len(target_column)):
            if "|" in target_column[ind]:
                target_column[ind] = target_column[ind].split("|")[1]

        feature_vectors = training_dataset.iloc[:, 1:].values  # returns a numpy array
        min_max_scaler = preprocessing.MinMaxScaler()
        feature_vectors = min_max_scaler.fit_transform(feature_vectors)
        feature_vectors = feature_vectors


        df_normalized = pd.DataFrame(data=feature_vectors, columns=columns[1:])

        if target_or_compound == "target":
            df_normalized.insert(loc=0, column="target id", value=target_column)
            df_normalized.to_csv("{}/{}_normalized.tsv".format(prot_feature_vector_path, feat), sep='\t', index=False)

        elif target_or_compound == "compound":
            df_normalized.insert(loc=0, column="compound id", value=target_column)
            df_normalized.to_csv("{}/{}_normalized.tsv".format(comp_feature_vector_path, feat), sep='\t', index=False)

# create_normalized_feature_vector_files("target")

def create_comp_tar_inter_dataset_nM():
    dataset_fl = open("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/IDGDreamChallenge/dti_datasets/idg_comp_targ_uniq_inter_filtered.csv", "r")
    lst_dataset_fl = dataset_fl.read().split("\n")
    dataset_fl.close()
    nm_dataset_fl = open(
        "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/IDGDreamChallenge/dti_datasets/idg_comp_targ_uniq_inter_filtered_nm.csv",
        "w")
    if "" in lst_dataset_fl:
        lst_dataset_fl.remove("")

    for line in lst_dataset_fl:
        comp_id, uniprot_id, value = line.split(",")
        value = 10**(9-float(value))
        nm_dataset_fl.write("{},{},{}\n".format(comp_id, uniprot_id, value))
    nm_dataset_fl.close()

def create_comp_tar_inter_dataset_label():
    import numpy as np
    from sklearn import preprocessing

    dataset_fl = open("/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/IDGDreamChallenge/dti_datasets/idg_comp_targ_uniq_inter_filtered.csv", "r")
    lst_dataset_fl = dataset_fl.read().split("\n")
    dataset_fl.close()

    lst_values = []
    if "" in lst_dataset_fl:
        lst_dataset_fl.remove("")

    for line in lst_dataset_fl:
        comp_id, uniprot_id, value = line.split(",")
        lst_values.append(float(value))

    labels = preprocessing.binarize(np.array(lst_values).reshape(1, -1), threshold=7.0, copy=False)[0]
    label_dataset_fl = open(
        "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/IDGDreamChallenge/dti_datasets/idg_comp_targ_uniq_inter_filtered_labels.csv",
        "w")


    for line_ind in range(len(lst_dataset_fl)):

        comp_id, uniprot_id, value = lst_dataset_fl[line_ind].split(",")
        value = int(labels[line_ind])
        label_dataset_fl.write("{},{},{}\n".format(comp_id, uniprot_id, value))
    label_dataset_fl.close()

# create_comp_tar_inter_dataset_label()





# create_comp_tar_inter_dataset_nM()

def get_prot_id_seq_dict_from_fasta_fl(fasta_fl_path):
    prot_id_seq_dict = dict()

    prot_id = ""
    with open("{}".format(fasta_fl_path)) as f:
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
    # all_n_gram_list = list(itertools.permutations(aa_list, word_size))
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
    if skip_size != 0:
        prot_seq_overlapping_ngram_list = [prot_seq[ind:ind + word_size] for ind in
                                           range(0, (len(prot_seq) - (word_size - 1)), skip_size)]
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


def get_int_encodings_of_proteins_sequences(fasta_fl_path, word_size, skip_size):
    int2aaword_dict, aaword2int_dict = get_int2aaword_aaword2int_dicts(word_size)
    # print(aaword2int_dict)
    prot_id_list, seq_encoding_list = [], []
    prot_id_seq_dict = get_prot_id_seq_dict_from_fasta_fl(fasta_fl_path)
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
        padded_features[i, :len(row)] = np.array(row)[:seq_length]

    return padded_features


def save_encoded_features(fasta_fl, word_size, skip_size, seq_length):
    prot_id_list, seq_encoding_list = get_int_encodings_of_proteins_sequences(fasta_fl, word_size, skip_size)
    padded_features = pad_encoded_features(seq_encoding_list, seq_length)

    str_header = "target id\t" + "\t".join([str(num) for num in list(range(seq_length))])
    print(str_header)
    for idx, prot_id in enumerate(prot_id_list):
        # print(idx, prot_id)
        print(prot_id + "\t" + "\t".join([str(num) for num in padded_features[idx]]))


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
    print(str_header)
    for prot_id, seq in prot_id_seq_dict.items():

        seq_torch_matrix = get_sequence_matrix(seq, size)
        # print(seq_torch_matrix)
        flattened_seq_matrix_arr = np.array(seq_torch_matrix.contiguous().view(-1))
        # print(flattened_seq_matrix_arr)
        print(prot_id + "\t" + "\t".join([str(val) for val in flattened_seq_matrix_arr]))


def convert_deepdta_davis_dataset_into_our_format():
    import json
    import math
    import os
    david_dataset_path = "../trainingFiles/DeepDTA/data/davis"
    helper_fl_path = "../trainingFiles/DeepDTA/helper_files"

    prot_id_seq_dict = json.load(open("{}/proteins.txt".format(david_dataset_path)))
    comp_id_smiles_dict = json.load(open("{}/ligands_can.txt".format(david_dataset_path)))


    prot_fasta_file = open(os.path.join(helper_fl_path, "davis_prots.fasta"), "w")
    ind_prot_id_dict = dict()
    ind = 0
    for prot_id, seq in prot_id_seq_dict.items():
        prot_fasta_file.write(">xxx|{}|xxxx\n".format(prot_id))
        prot_fasta_file.write("{}\n".format(seq))
        ind_prot_id_dict[ind] = prot_id
        ind += 1
    prot_fasta_file.close()

    comp_smiles_file = open("{}/davis_comp_smiles.fasta".format(helper_fl_path), "w")
    ind_comp_id_dict = dict()
    ind = 0
    for comp_id, smiles in comp_id_smiles_dict.items():
        comp_smiles_file.write("{}\t{}\n".format(comp_id,smiles))
        ind_comp_id_dict[ind] = comp_id
        ind += 1
    comp_smiles_file.close()

    affinity_matrix_fl = open("{}/drug-target_interaction_affinities_Kd__Davis_et_al.2011v1.txt".format(david_dataset_path),"r")
    lst_affinity_matrix_fl = affinity_matrix_fl.read().split("\n")
    affinity_matrix_fl.close()


    for row_ind in range(len(lst_affinity_matrix_fl[:-1])):
        affinity_val_list = lst_affinity_matrix_fl[row_ind].split(" ")
        for col_ind in range(len(affinity_val_list)):
            print("{},{},{}".format(ind_comp_id_dict[row_ind], ind_prot_id_dict[col_ind],  -1*math.log10(float(affinity_val_list[col_ind])*1e-9)))
    # print(lst_affinity_matrix_fl)
    # print(prot_id_seq_dict)
    # print(ind_prot_id_dict)
    # print(comp_id_smiles_dict)
    # print(ind_comp_id_dict)
# convert_deepdta_davis_dataset_into_our_format()

def convert_deepdta_dataset_into_our_format_using_deepdta_pickle(davis_kiba):
    import pickle
    import numpy as np
    import math
    import json

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
    label_row_inds, label_col_inds = np.where(np.isnan(affinity_matrix)==False)

    for id in range(len(label_row_inds)):
        row, col = label_row_inds[id], label_col_inds[id]
        # print(row, col)
        if davis_kiba=="davis":
            print("{},{},{}".format(ind_comp_id_dict[row], ind_prot_id_dict[col], -1*math.log10(affinity_matrix[row, col]*1e-9)))
        else:
            print("{},{},{}".format(ind_comp_id_dict[row], ind_prot_id_dict[col], affinity_matrix[row, col]))
    # row = floor((441+442*2)/ 442)
    # column = (441+442*2)% 442
    # print(row ,column)
# convert_deepdta_dataset_into_our_format_using_deepdta_pickle("davis")
convert_deepdta_dataset_into_our_format_using_deepdta_pickle("kiba")




# create_ecfp4_fingerprint_file()

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

# this script run in another file
def create_ecfp4_fingerprint_file():
    from operator import itemgetter
    import math
    import numpy as np
    from rdkit import Chem
    from rdkit.Chem import AllChem
    path = "../trainingFiles/DeepDTA/helper_files/"
    fl_name = "davis_comp_smiles.txt"

    rep_fl = open("%s/%s" % (path, fl_name), "r")
    lst_rep_fl = rep_fl.read().split("\n")
    rep_fl.close()
    if "" in lst_rep_fl:
        lst_rep_fl.remove("")

    compound_smiles_inchi_dict = dict()
    for line in lst_rep_fl:
        # compund_id, smiles, inchi = line.split("\t")
        compund_id, smiles = line.split("\t")
        # compound_smiles_inchi_dict[compund_id] = [smiles, inchi]
        compound_smiles_inchi_dict[compund_id] = smiles

    # compound_ecfp4_vectors = open("../compound_ecfp4_vectors.tsv", "w")
    failureCount = 0
    str_header = "compound id\t" + "\t".join([str(num) for num in range(1024)])
    print(str_header)
    for comp in compound_smiles_inchi_dict.keys():
        isSmilesFailed = False
        fp = ""
        #try:
        m = Chem.MolFromSmiles(compound_smiles_inchi_dict[comp])
        fp = AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=1024).ToBitString()
        #except:
        #    isSmilesFailed = True
        """
        isInChiFailed = False
        if isSmilesFailed:
            try:
                m = Chem.MolFromInchi(compound_smiles_inchi_dict[comp][1])
                fp = AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=1024).ToBitString()
            except:
                isInChiFailed = True
        if isInChiFailed:
            print("%s\tBoth Failed" % (comp))
            failureCount += 1
        else:
            compound_ecfp4_vectors.write("%s\t%s\n" % (comp, fp))
        """

        if not isSmilesFailed:
            print(comp + "\t" + "\t".join([str(float(dim)) for dim in fp]))
            #print("{}\t{}".format(comp, fp))
            #print("")
        else:
            print("Failed")

# create_ecfp4_fingerprint_file()

def get_prot_seq_lengths_given_fasta(fasta_fl_path):
    from operator import itemgetter

    prot_id_seq_dict = get_prot_id_seq_dict_from_fasta_fl(fasta_fl_path)
    seq_len_list = []
    for prot_id, seq in prot_id_seq_dict.items():
        seq_len_list.append([prot_id, len(seq)])

    seq_len_list = sorted(seq_len_list, key=itemgetter(1))
    for prot_ind in range(len(seq_len_list)):
        print(prot_ind, seq_len_list[prot_ind])

def create_interaction_data_file(comp_feature_list, target_feature_lst, comp_target_pair_dataset):
    comp_target_pair_dataset_path = "{}/{}".format(idg_training_dataset_path, comp_target_pair_dataset)
    dict_compound_features = get_dict_combined_feature_vectors("compound", comp_feature_list)

    dict_target_features = get_list_target_dict_combined_feature_vectors("target", target_feature_lst)
    #prot_id_seq_dict = get_prot_id_seq_dict_from_fasta_fl(fasta_fl_path)
    training_dataset = pd.read_csv(comp_target_pair_dataset_path, header=None)
    for ind, row in training_dataset.iterrows():
        print(ind)
        comp_id = row[0]
        tar_id = str(row[1])
        biact_val = str(row[2])
        str_comp_feats = ",".join([str(item) for item in dict_compound_features[comp_id]])
        comp_id = str(comp_id)
        str_tar_feats = ",".join(dict_target_features[tar_id])
        # print(len(dict_target_features[tar_id]))
        #print(type(comp_id), type(tar_id), type(biact_val), type(str_comp_feats), type(str_tar_feats))
        final_str_list = [comp_id, tar_id, biact_val, str_comp_feats, str_tar_feats]
        data_point_fl = open("{}/deepdta_data/{}_{}_{}.tsv".format(davis_dataset_path, ind, comp_id, tar_id), "w")
        data_point_fl.write("\t".join(final_str_list))
        data_point_fl.close()

# create_interaction_data_file(["ecfp4"], ["sequencematrix500"], "davis_comp_targ_affinity.csv")

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
        data_point_fl = open("{}/deepdta_data/{}_{}_{}.tsv".format(davis_dataset_path, idx, comp_id, tar_id), "r")
        fl_comp_id, fl_tar_id, fl_biact_val, comp_feats, tar_feats = data_point_fl.read().split("\t")
        data_point_fl.close()

        comp_feats = torch.tensor(np.asarray(comp_feats.split(","), dtype=float)).type(torch.FloatTensor)
        tar_feats = torch.tensor(np.asarray([tar_feats.split(",")], dtype=float).reshape(1, 500,500)).type(torch.FloatTensor)
        label = torch.tensor(float(biact_val)).type(torch.FloatTensor)

        #print(comp_feats.shape, tar_feats.shape, label.shape)

        return comp_feats, tar_feats, label, comp_id, tar_id



def get_cnn_test_val_folds_train_data_loader(batch_size=32):
    # from random import choices
    import numpy as np
    import json

    folds = json.load(open("{}/data/davis/folds/train_fold_setting1.txt".format(davis_dataset_path)))
    test = json.load(open("{}/data/davis/folds/test_fold_setting1.txt".format(davis_dataset_path)))
    #print(folds)

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

    test_sampler = BatchSampler(SequentialSampler(test), batch_size=batch_size, drop_last=False)
    test_loader = torch.utils.data.DataLoader(davis_bioactivity_dataset, batch_size=batch_size,
                                                   sampler=test_sampler)
    return loader_fold_dict, test_loader



"""
loader_fold_dict, test_loader = loader_fold_dict, test_loader = get_cnn_test_val_folds_train_data_loader()
train_loader = loader_fold_dict[0][0]

for i, data in enumerate(train_loader):
    # get the inputs
    print(i)
    comp_feature_vectors, target_feature_vectors, labels, comp_ids, tar_ids = data
    print(target_feature_vectors.shape)
"""
