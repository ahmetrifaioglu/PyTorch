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
import math
from sklearn.metrics import f1_score, accuracy_score
from sklearn import preprocessing,metrics
import sklearn
from dream_challenge_PINN_models import FC_PINNModel_2_2_2, FC_PINNModel_2_2_2_Modules, FC_PINNModel_2_3_2_Modules, FC_PINNModel_3_5_2_Modules#, FC_PINNModel_4_4_2,  FC_PINNModel_3_3_2
from dream_challenge_data_processing import TrainingValidationShuffledDataLoader, get_nfold_data_loader_dict,get_training_validation_data_loaders_for_cnn
from rnn_playground_models import CompFCNNTarRNN, CompFCNNTarCNN
from emetrics import r_squared_error, get_rm2, squared_error_zero, get_k, get_cindex

n_epoch = 20
num_of_folds = 1

def train_networks(comp_feature_list, tar_feature_list, comp_hidden_lst, fc1, fc2, learn_rate, comp_tar_pair_dataset, regression_classifier, batch_size):
    torch.manual_seed(1)
    use_gpu = torch.cuda.is_available()

    device = "cpu"

    if use_gpu:
        print("GPU is available on this device!")
        device = "cuda"
    else:
        print("CPU is available on this device!")
    davis_prot_fl_path = "../trainingFiles/DeepDTA/helper_files/davis_prots.fasta"
    loader_fold_dict, number_of_comp_features, number_of_target_features = get_training_validation_data_loaders_for_cnn(1, 32, ["ecfp4"], ["sequencematrix500"], "davis_comp_targ_affinity.csv", davis_prot_fl_path, "r")
    original_number_of_comp_features = int(number_of_comp_features)
    original_number_of_target_features = int(number_of_target_features)

    print(original_number_of_comp_features, original_number_of_target_features)

    for fold in range(num_of_folds):
        train_loader, valid_loader = loader_fold_dict[fold]
        print("FOLD : {}".format(fold + 1))
        number_of_comp_features = original_number_of_comp_features
        model = CompFCNNTarCNN(number_of_comp_features, 1024, 512, 256, 256, drop_prob=0.5).to(device)

        optimizer = torch.optim.Adam(model.parameters(), lr=learn_rate)
        criterion = torch.nn.MSELoss()
        optimizer.zero_grad()

        for epoch in range(n_epoch):
            print("Epoch :{}".format(n_epoch))
            total_training_loss, total_validation_loss = 0.0, 0.0
            total_training_count, total_validation_count = 0, 0
            validation_predictions, validation_labels = [], []
            batch_number = 0
            model.train()
            for i, data in enumerate(train_loader):
                batch_number += 1
                # clear gradient DO NOT forget you fool!
                optimizer.zero_grad()

                # get the inputs
                comp_feature_vectors, target_feature_vectors, labels, compound_ids, target_ids, number_of_comp_features, number_of_target_features = data

                # wrap them in Variable
                comp_feature_vectors, target_feature_vectors, labels = Variable(comp_feature_vectors).to(device), Variable(
                    target_feature_vectors).to(device), Variable(labels).to(device)
                if comp_feature_vectors.shape[0]==batch_size:
                    inputs = None
                    y_pred = None

                    total_training_count += comp_feature_vectors.shape[0]

                    y_pred = model(comp_feature_vectors, target_feature_vectors).to(device)

                    loss = criterion(y_pred.squeeze(), labels)

                    total_training_loss += float(loss.item())
                    loss.backward()
                    optimizer.step()

            print("Epoch {} training loss:".format(epoch), total_training_loss)

            model.eval()
            with torch.no_grad():  # torch.set_grad_enabled(False):
                for i, data in enumerate(valid_loader):

                    val_comp_feature_vectors, val_target_feature_vectors, val_labels, val_compound_ids, val_target_ids, val_number_of_comp_features, val_number_of_target_features = data
                    val_comp_feature_vectors, val_target_feature_vectors, val_labels = Variable(
                        val_comp_feature_vectors).to(
                        device), Variable(val_target_feature_vectors).to(device), Variable(val_labels).to(device)
                    total_validation_count += val_comp_feature_vectors.shape[0]

                    if val_comp_feature_vectors.shape[0] == batch_size:
                        val_inputs = None
                        val_y_pred = None


                        val_y_pred  = model(val_comp_feature_vectors, val_target_feature_vectors)
                        loss_val = criterion(val_y_pred.squeeze(), val_labels)
                        total_validation_loss += float(loss_val.item())
                        for item in val_labels:
                            validation_labels.append(float(item.item()))

                        for item in val_y_pred:
                            validation_predictions.append(float(item.item()))

            if regression_classifier == "r":
                deep_dta_rmse = get_rm2(np.asarray(validation_labels), np.asarray(
                    validation_predictions))
                rmse_score = rmse(np.asarray(validation_labels), np.asarray(
                    validation_predictions))
                pearson_score = pearson(np.asarray(validation_labels), np.asarray(validation_predictions))
                spearman_score = spearman(np.asarray(validation_labels), np.asarray(validation_predictions))
                ci_score = ci(np.asarray(validation_labels), np.asarray(validation_predictions))
                f1_score = f1(np.asarray(validation_labels), np.asarray(validation_predictions))
                ave_auc_score = average_AUC(np.asarray(validation_labels), np.asarray(validation_predictions))
                print("================================================================================")
                print("Fold:{}\tEpoch:{}\tTest RMSE:{}\tTraining Loss:{}\tValidation Loss:{}".format(fold + 1, epoch,
                                                                                                     rmse_score,
                                                                                                     total_training_loss,
                                                                                                     total_validation_loss))
                print("RMSE:\t{}".format(rmse_score))  # rmse, pearson, spearman, ci, ci, average_AUC
                print("Pearson:\t{}".format(pearson_score))
                print("Spearman:\t{}".format(spearman_score))
                print("Ci:\t{}".format(ci_score))
                print("F1-Score:\t{}".format(f1_score))
                print("Average_AUC:\t{}".format(ave_auc_score))
                print("IDG File:\t{}".format(comp_tar_pair_dataset))
                print("Number of training samples:\t{}".format(total_training_count))
                print("Number of validation samples:\t{}".format(total_validation_count))
                print("DEEPDTA Validation Labels:\t{}".format(deep_dta_rmse))



train_networks(["ecfp4"], ["sequencematrix500"], [256, 512], 256, 256, 0.001, "davis_comp_targ_affinity.csv", "r", 32)

