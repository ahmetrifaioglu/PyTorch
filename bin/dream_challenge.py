from __future__ import print_function, division
import os
import torch
import pandas as pd
import numpy as np
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from torch.autograd import Variable
import torch.nn.functional as F
import sys
from dream_challenge_metrics import rmse, pearson, spearman, ci, f1, average_AUC
from torchvision import datasets
import torchvision.transforms as transforms
import itertools
import warnings
from dream_challenge_models import FCModel1, FCModel2, FCPINNModel1, FCModel_3_Hidden_with_Modules, FCModel_3_Hidden, FCModel1_M
from dream_challenge_data_processing import TrainingValidationShuffledDataLoader, get_nfold_data_loader_dict

warnings.filterwarnings("ignore")

modeltype = sys.argv[1]
learn_rate = 0.0001
#learn_rate = sys.argv[2]
n_epoch = int(sys.argv[2])
num_of_folds = 5
batch_size = 32

use_gpu = torch.cuda.is_available()

device = "cpu"

if use_gpu:
    print("GPU is available on this device!")
    device = "cuda"
else:
    print("CPU is available on this device!")

datasets_path = "../trainingFiles/IDGDreamChallenge"
comp_feature_list = ["comp_dummy_feat_1", "comp_dummy_feat_2"]
tar_feature_list = ["prot_dummy_feat_1", "prot_dummy_feat_2"]
# comp_feature_list = ["comp_dummy_feat_1"]
# tar_feature_list = ["prot_dummy_feat_1"]
comp_feature_list = ["ecfp4"]
tar_feature_list = ["tri_gram"]

# comp_tar_pair_dataset = "dummy_Dtc_comp_targ_uniq_inter_filtered_onlykinase.txt"
comp_tar_pair_dataset = "Dtc_comp_targ_uniq_inter_filtered_onlykinase.txt"
loader_fold_dict, number_of_comp_features, number_of_target_features = get_nfold_data_loader_dict(num_of_folds, 32, comp_feature_list, tar_feature_list, comp_tar_pair_dataset)



original_number_of_comp_features = int(number_of_comp_features)
original_number_of_target_features = int(number_of_target_features)


total_number_of_features = number_of_comp_features+number_of_target_features
# feature_lst = ["tri_gram", "spmap", "pfam", "k_sep_bigrams", "DDE", "APAAC"]
# feature_lst = ["k_sep_bigrams", "APAAC"]

concat_models = ["FC1", "FC1M", "FC2" , "FC3", "FC3M"]
rmse_fold_lst = [-100000.0 for i in range(num_of_folds)]
pearson_fold_lst = [-100000.0 for i in range(num_of_folds)]
spearman_fold_lst = [-100000.0 for i in range(num_of_folds)]
ci_fold_lst = [-100000.0 for i in range(num_of_folds)]
f1_fold_lst = [-100000.0 for i in range(num_of_folds)]
auc_fold_lst = [-100000.0 for i in range(num_of_folds)]



for fold in range(num_of_folds):
    train_loader, valid_loader = loader_fold_dict[fold]
    # Just to check if everything is OK.
    # Remove this when you finish testing.
    print("FOLD : {}".format(fold+1))
    #print(len(train_loader), len(valid_loader))
    number_of_comp_features = original_number_of_comp_features
    number_of_target_features = original_number_of_target_features
    model = None
    if modeltype == "FC1":
        model = FCModel1(total_number_of_features).to(device)
    elif modeltype == "FC1M":
        model = FCModel1_M(total_number_of_features).to(device)
    elif modeltype == "FC2":
        model = FCModel2(total_number_of_features).to(device)
    elif modeltype == "FC3":
        model = FCModel_3_Hidden(total_number_of_features, 1024, 400, 200, 0.5).to(device)
    elif modeltype == "FC3M":
        model = FCModel_3_Hidden_with_Modules(total_number_of_features, 1024, 400, 200, 0.5).to(device)
    else:
        model = FCPINNModel1(number_of_comp_features, number_of_target_features).to(device)
    # print(model.parameters)
    optimizer = torch.optim.Adam(model.parameters(), lr=learn_rate)
    criterion = torch.nn.MSELoss()

    for epoch in range(n_epoch):

        total_training_loss = 0.0
        total_validation_loss = 0.0
        total_training_count = 0
        total_validation_count = 0
        validation_predictions = []
        validation_labels = []
        batch_number = 0
        model.train()
        for i, data in enumerate(train_loader):

            batch_number += 1
            # get the inputs
            comp_feature_vectors, target_feature_vectors, labels, compound_ids, target_ids, number_of_comp_features, number_of_target_features = data
            # wrap them in Variable
            comp_feature_vectors, target_feature_vectors, labels = Variable(comp_feature_vectors).to(device), Variable(target_feature_vectors).to(device), Variable(labels).to(device)
            inputs = None
            y_pred = None

            total_training_count += comp_feature_vectors.shape[0]
            if modeltype in concat_models:
                inputs = torch.cat((comp_feature_vectors, target_feature_vectors), 1)
                y_pred = model(inputs)
            else:
            # Forward pass: Compute predicted y by passing x to the model
                y_pred = model(comp_feature_vectors, target_feature_vectors)
            # Compute and print loss
            loss = criterion(y_pred.squeeze(), labels)
            total_training_loss += float(loss.data[0])

            loss.backward()
            optimizer.step()
            # clear gradient DO NOT forget you fool!
            optimizer.zero_grad()


        model.eval()
        with torch.no_grad(): # torch.set_grad_enabled(False):
            for i, data in enumerate(valid_loader):
                #print("Validation")
                val_comp_feature_vectors, val_target_feature_vectors, val_labels, val_compound_ids, val_target_ids, val_number_of_comp_features, val_number_of_target_features = data
                val_comp_feature_vectors, val_target_feature_vectors, val_labels = Variable(val_comp_feature_vectors).to(
                    device), Variable(val_target_feature_vectors).to(device), Variable(val_labels).to(device)
                # val_inputs = torch.cat((val_comp_feature_vectors, val_target_feature_vectors), 1)
                total_validation_count += val_comp_feature_vectors.shape[0]

                val_inputs = None
                val_y_pred = None

                if modeltype in concat_models:
                    val_inputs = torch.cat((val_comp_feature_vectors, val_target_feature_vectors), 1)
                    val_y_pred = model(val_inputs)
                else:
                    # Forward pass: Compute predicted y by passing x to the model
                    val_y_pred = model(val_comp_feature_vectors, val_target_feature_vectors)

                # print(val_y_pred)
                loss_val = criterion(val_y_pred.squeeze(), val_labels)
                total_validation_loss += float(loss_val.data[0])

                for item in val_y_pred:
                    validation_predictions.append(float(item.data[0]))
                for item in val_labels:
                    validation_labels.append(float(item.data[0]))

        
        rmse_score = rmse(np.asarray(validation_labels), np.asarray(
            validation_predictions))
        pearson_score = pearson(np.asarray(validation_labels), np.asarray(validation_predictions))
        spearman_score = spearman(np.asarray(validation_labels), np.asarray(validation_predictions))
        ci_score = ci(np.asarray(validation_labels), np.asarray(validation_predictions))
        f1_score = f1(np.asarray(validation_labels), np.asarray(validation_predictions))
        ave_auc_score = average_AUC(np.asarray(validation_labels), np.asarray(validation_predictions))
        print("================================================================================")
        print("Fold:{}, Epoch:{}, Training Loss:{}, Validation Loss:{}".format(fold, epoch, total_training_loss, total_validation_loss))
        print("RMSE:\t{}".format(rmse_score))  # rmse, pearson, spearman, ci, ci, average_AUC
        print("Pearson:\t{}".format(pearson_score))
        print("Spearman:\t{}".format(spearman_score))
        print("Ci:\t{}".format(ci_score))
        print("F1-Score:\t{}".format(f1_score))
        print("Average_AUC:\t{}".format(ave_auc_score))
        print("Number of training samples:\t{}".format(total_training_count))
        print("Number of validation samples:\t{}".format(total_validation_count))

        rmse_fold_lst[fold] = rmse_score
        pearson_fold_lst[fold] = pearson_score
        spearman_fold_lst[fold] = spearman_score
        ci_fold_lst[fold] = ci_score
        f1_fold_lst[fold] = f1_score
        auc_fold_lst[fold] = ave_auc_score


average_rmse_fold = sum(rmse_fold_lst)/num_of_folds
average_pearson_fold = sum(pearson_fold_lst)/num_of_folds
average_spearman_fold = sum(spearman_fold_lst)/num_of_folds
average_ci_fold = sum(ci_fold_lst)/num_of_folds
average_f1_fold = sum(f1_fold_lst)/num_of_folds
average_auc_fold = sum(auc_fold_lst)/num_of_folds

print("Average RMSE:\t{}".format(average_rmse_fold))  # rmse, pearson, spearman, ci, ci, average_AUC
print("Average Pearson:\t{}".format(average_pearson_fold))
print("Average Spearman:\t{}".format(average_spearman_fold))
print("Average Ci:\t{}".format(average_ci_fold))
print("Average F1-Score:\t{}".format(average_f1_fold))
print("Average Average_AUC:\t{}".format(average_auc_fold))