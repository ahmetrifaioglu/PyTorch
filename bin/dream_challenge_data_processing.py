import pandas as pd
from torch.utils.data import Dataset, DataLoader
import torch
import numpy as np
from torch.utils.data.sampler import SubsetRandomSampler
import sklearn
from sklearn import preprocessing
import math
idg_training_dataset_path = "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/IDGDreamChallenge/"
prot_feature_vector_path = "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/IDGDreamChallenge/protein_feature_vectors"
comp_feature_vector_path = "/Users/trman/OneDrive/Projects/PyTorch/trainingFiles/IDGDreamChallenge/compound_feature_vectors"

def get_dict_combined_feature_vectors(target_or_compound, feature_lst):

    sorted(feature_lst)
    feat_vec_path = prot_feature_vector_path if target_or_compound=="target" else comp_feature_vector_path
    common_column = "target id" if target_or_compound=="target" else "compound id"
    df_combined_features = pd.read_csv("{}/{}_normalized.tsv".format(feat_vec_path, feature_lst[0]), sep="\t")
    #print(df_combined_features.columns)
    for feat in feature_lst[1:]:
        df_temp_features =  pd.read_csv("{}/{}_normalized.tsv".format(feat_vec_path, feat), sep="\t")
        df_combined_features = pd.merge(df_combined_features, df_temp_features, on=[common_column])
    # print(df_combined_features)
    df_combined_features = df_combined_features.set_index(common_column).T.to_dict('list')
    return df_combined_features


class TrainingValidationShuffledDataLoader(Dataset):

    def __init__(self , comp_feature_list, target_feature_lst, comp_target_pair_dataset):

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
                valid_labels.append(-math.log10(10e-9*float(lbl)))
                valid_compound_ids.append(comp_id)
                valid_target_ids.append(tar_id)
            except:
                invalid_data_points+=1
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


def get_nfold_data_loader_dict(num_of_folds, batch_size, comp_feature_list, target_feature_lst, comp_target_pair_dataset):

    loader_fold_dict = dict()
    valid_size = round(1.0 / float(num_of_folds), 1)

    train_val_data = TrainingValidationShuffledDataLoader(comp_feature_list, target_feature_lst, comp_target_pair_dataset)

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

        # print(len(train_indices))
        # print(len(val_indices))

        # define samplers for obtaining training and validation batches
        train_sampler = SubsetRandomSampler(train_indices)
        valid_sampler = SubsetRandomSampler(val_indices)

        # print(fold_id, train_sampler.indices)
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
        feature_types = ["tri_gram", "spmap", "pfam", "k_sep_bigrams", "DDE", "APAAC"]
    elif target_or_compound == "compound":
        feature_types = ["ecfp4", "fcfp4", "rdk5"]

    for feat in feature_types:
        dataset_path = None
        if target_or_compound =="target":
            dataset_path = "{}/{}.tsv".format(prot_feature_vector_path, feat)
        elif target_or_compound=="compound":
            dataset_path = "{}/{}.tsv".format(comp_feature_vector_path, feat)

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



# create_normalized_feature_vector_files("compound")