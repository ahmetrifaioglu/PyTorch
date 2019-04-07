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
from dream_challenge_metrics import rmse, pearson, spearman, ci, f1, average_AUC, mse
from torchvision import datasets
import torchvision.transforms as transforms
import itertools
import warnings
import math
from sklearn.metrics import f1_score, accuracy_score
from sklearn import preprocessing,metrics
import sklearn
from dream_challenge_PINN_models import FC_PINNModel_2_2_2, FC_PINNModel_2_2_2_Modules, FC_PINNModel_2_3_2_Modules, FC_PINNModel_3_5_2_Modules#, FC_PINNModel_4_4_2,  FC_PINNModel_3_3_2
from cnn_models import CompFCNNTarCNN, CompFCNNTarCNN2
from emetrics import r_squared_error, get_rm2, squared_error_zero, get_k, get_cindex, get_aupr
from cnn_data_processing import get_cnn_test_val_folds_train_data_loader, get_cnn_train_test_full_training_data_loader
import sys
# import statistics

n_epoch = 100
num_of_folds = 5

def get_scores(labels, predictions, validation_test, total_training_loss, total_validation_test_loss, fold, epoch, comp_tar_pair_dataset, fold_epoch_results):
    deep_dta_rm2 = get_rm2(np.asarray(labels), np.asarray(
        predictions))
    # deep_dta_aupr = get_aupr(np.asarray(labels), np.asarray(
    #    predictions))
    deep_dta_cindex = get_cindex(np.asarray(labels), np.asarray(
        predictions))
    deep_dta_mse = mse(np.asarray(labels), np.asarray(
        predictions))

    #rmse_score = rmse(np.asarray(labels), np.asarray(
    #    predictions))
    pearson_score = pearson(np.asarray(labels), np.asarray(predictions))
    spearman_score = spearman(np.asarray(labels), np.asarray(predictions))
    ci_score = ci(np.asarray(labels), np.asarray(predictions))
    f1_score = f1(np.asarray(labels), np.asarray(predictions))
    ave_auc_score = average_AUC(np.asarray(labels), np.asarray(predictions))
    fold_epoch_results[-1].append([deep_dta_rm2, deep_dta_cindex, deep_dta_mse, pearson_score, spearman_score, ci_score, f1_score, ave_auc_score])
    print("Fold:{}\tEpoch:{}\tTraining Loss:{}\t{} Loss:{}".format(fold + 1, epoch, total_training_loss, validation_test, total_validation_test_loss))
    # print("{} RMSE:\t{}".format(validation_test, rmse_score))  # rmse, pearson, spearman, ci, ci, average_AUC
    print("{} DeepDTA RM2:\t{}".format(validation_test, deep_dta_rm2))
    print("{} DeepDTA MSE\t{}".format(validation_test, deep_dta_mse))
    print("{} DeepDTA c-index\t{}".format(validation_test, deep_dta_cindex))
    print("{} Pearson:\t{}".format(validation_test, pearson_score))
    print("{} Spearman:\t{}".format(validation_test, spearman_score))
    print("{} Ci:\t{}".format(validation_test, ci_score))
    print("{} F1-Score:\t{}".format(validation_test, f1_score))
    print("{} Average_AUC:\t{}".format(validation_test, ave_auc_score))
    # print("{} IDG File:\t{}".format(validation_test, comp_tar_pair_dataset))
    # print("{} Number of training samples:\t{}".format(validation_test, total_training_count))
    # print("{} Number of validation samples:\t{}".format(validation_test, total_validation_count))

def get_scores_full(labels, predictions, validation_test, total_training_loss, total_validation_test_loss, epoch, comp_tar_pair_dataset, fold_epoch_results):
    deep_dta_rm2 = get_rm2(np.asarray(labels), np.asarray(
        predictions))
    # deep_dta_aupr = get_aupr(np.asarray(labels), np.asarray(
    #    predictions))
    deep_dta_cindex = get_cindex(np.asarray(labels), np.asarray(
        predictions))
    deep_dta_mse = mse(np.asarray(labels), np.asarray(
        predictions))

    #rmse_score = rmse(np.asarray(labels), np.asarray(
    #    predictions))
    pearson_score = pearson(np.asarray(labels), np.asarray(predictions))
    spearman_score = spearman(np.asarray(labels), np.asarray(predictions))
    ci_score = ci(np.asarray(labels), np.asarray(predictions))
    f1_score = f1(np.asarray(labels), np.asarray(predictions))
    ave_auc_score = average_AUC(np.asarray(labels), np.asarray(predictions))
    fold_epoch_results[-1].append([deep_dta_rm2, deep_dta_cindex, deep_dta_mse, pearson_score, spearman_score, ci_score, f1_score, ave_auc_score])
    print("Epoch:{}\tTraining Loss:{}\t{} Loss:{}".format(epoch, total_training_loss, validation_test, total_validation_test_loss))
    # print("{} RMSE:\t{}".format(validation_test, rmse_score))  # rmse, pearson, spearman, ci, ci, average_AUC
    print("{} DeepDTA RM2:\t{}".format(validation_test, deep_dta_rm2))
    print("{} DeepDTA MSE\t{}".format(validation_test, deep_dta_mse))
    print("{} DeepDTA c-index\t{}".format(validation_test, deep_dta_cindex))
    print("{} Pearson:\t{}".format(validation_test, pearson_score))
    print("{} Spearman:\t{}".format(validation_test, spearman_score))
    print("{} Ci:\t{}".format(validation_test, ci_score))
    print("{} F1-Score:\t{}".format(validation_test, f1_score))
    print("{} Average_AUC:\t{}".format(validation_test, ave_auc_score))
    # print("{} IDG File:\t{}".format(validation_test, comp_tar_pair_dataset))
    # print("{} Number of training samples:\t{}".format(validation_test, total_training_count))
    # print("{} Number of validation samples:\t{}".format(validation_test, total_validation_count))



def train_networks(comp_feature_list, tar_feature_list, comp_hidden_lst, tar_num_of_last_neurons, fc1, fc2, learn_rate, comp_tar_pair_dataset, regression_classifier, batch_size):
    torch.manual_seed(1)
    use_gpu = torch.cuda.is_available()

    device = "cpu"

    if use_gpu:
        print("GPU is available on this device!")
        device = "cuda"
    else:
        print("CPU is available on this device!")

    loader_fold_dict, test_loader = get_cnn_test_val_folds_train_data_loader(batch_size)

    test_fold_epoch_results = []
    validation_fold_epoch_results = []
    for fold in range(num_of_folds):
        test_fold_epoch_results.append([])
        validation_fold_epoch_results.append([])
        train_loader, valid_loader = loader_fold_dict[fold]
        print("FOLD : {}".format(fold + 1))

        model = CompFCNNTarCNN2(1024, tar_num_of_last_neurons, comp_hidden_lst[0], comp_hidden_lst[1], fc1, fc2, drop_prob=0.5).to(device)
        optimizer = torch.optim.Adam(model.parameters(), lr=learn_rate)
        criterion = torch.nn.MSELoss()
        optimizer.zero_grad()

        for epoch in range(n_epoch):
            #print("Epoch :{}".format(epoch))
            total_training_loss, total_validation_loss, total_test_loss = 0.0, 0.0, 0.0
            total_training_count, total_validation_count, total_test_count = 0, 0, 0
            validation_predictions, validation_labels, test_predictions, test_labels = [], [], [], []
            batch_number = 0
            model.train()
            for i, data in enumerate(train_loader):
                batch_number += 1
                # clear gradient DO NOT forget you fool!
                optimizer.zero_grad()

                # get the inputs
                #comp_feature_vectors, target_feature_vectors, labels, compound_ids, target_ids, number_of_comp_features, number_of_target_features = data
                comp_feature_vectors, target_feature_vectors, labels, compound_ids, target_ids = data
                # wrap them in Variable
                comp_feature_vectors, target_feature_vectors, labels = Variable(comp_feature_vectors).to(device), Variable(
                    target_feature_vectors).to(device), Variable(labels).to(device)
                # if comp_feature_vectors.shape[0]==batch_size:
                inputs = None
                y_pred = None

                total_training_count += comp_feature_vectors.shape[0]

                y_pred = model(comp_feature_vectors, target_feature_vectors).to(device)

                loss = criterion(y_pred.squeeze(), labels)

                total_training_loss += float(loss.item())
                loss.backward()
                optimizer.step()

            #print("Epoch {} training loss:".format(epoch), total_training_loss)

            model.eval()
            with torch.no_grad():  # torch.set_grad_enabled(False):
                for i, data in enumerate(valid_loader):
                    val_comp_feature_vectors, val_target_feature_vectors, val_labels, val_compound_ids, val_target_ids = data
                    val_comp_feature_vectors, val_target_feature_vectors, val_labels = Variable(val_comp_feature_vectors).to(
                        device), Variable(
                        val_target_feature_vectors).to(device), Variable(val_labels).to(device)

                    total_validation_count += val_comp_feature_vectors.shape[0]

                    # if val_comp_feature_vectors.shape[0] == batch_size:
                    val_inputs = None
                    val_y_pred = None
                    val_y_pred  = model(val_comp_feature_vectors, val_target_feature_vectors)
                    loss_val = criterion(val_y_pred.squeeze(), val_labels)
                    total_validation_loss += float(loss_val.item())
                    for item in val_labels:
                        validation_labels.append(float(item.item()))

                    for item in val_y_pred:
                        validation_predictions.append(float(item.item()))

                for i, data in enumerate(test_loader):
                    test_comp_feature_vectors, test_target_feature_vectors, tst_labels, test_compound_ids, test_target_ids = data
                    test_comp_feature_vectors, test_target_feature_vectors, tst_labels = Variable(test_comp_feature_vectors).to(
                        device), Variable(
                        test_target_feature_vectors).to(device), Variable(tst_labels).to(device)

                    total_test_count += test_comp_feature_vectors.shape[0]

                    # if test_comp_feature_vectors.shape[0] == batch_size:
                    test_inputs = None
                    test_y_pred = None
                    test_y_pred  = model(test_comp_feature_vectors, test_target_feature_vectors)
                    loss_test = criterion(test_y_pred.squeeze(), tst_labels)
                    total_test_loss += float(loss_test.item())
                    for item in tst_labels:
                        test_labels.append(float(item.item()))

                    for item in test_y_pred:
                        test_predictions.append(float(item.item()))


            if regression_classifier == "r":
                print("==============================================================================")
                get_scores(validation_labels, validation_predictions, "Validation", total_training_loss, total_validation_loss, fold, epoch, comp_tar_pair_dataset, validation_fold_epoch_results)
                print("------------------------------------------------------------------------------")
                get_scores(test_labels, test_predictions, "Test", total_training_loss,
                           total_test_loss, fold, epoch, comp_tar_pair_dataset, test_fold_epoch_results)
    # deep_dta_rm2, deep_dta_cindex, deep_dta_mse, pearson_score, spearman_score, ci_score, f1_score, ave_auc_score
    result_fl = open("../result_files/{}.tsv".format("_".join(sys.argv[1:])), "w")
    header = "test_deep_dta_rm2\ttest_deep_dta_cindex\ttest_deep_dta_mse\ttest_pearson_score\ttest_spearman_score\ttest_ci_score\ttest_f1_score\ttest_ave_auc_score\tval_deep_dta_rm2\tval_deep_dta_cindex\tval_deep_dta_mse\tval_pearson_score\tval_spearman_score\tval_ci_score\tval_f1_score\tval_ave_auc_score"
    #print(header)
    #print(test_fold_epoch_results)
    result_fl.write(header+"\n")
    for epoch_ind in range(n_epoch):

        epoch_test_combined_rslt_lst = []
        epoch_val_combined_rslt_lst = []
        for rslt_ind in range(len(test_fold_epoch_results[0][epoch_ind])):
            fold_combined_test_result_list = []
            fold_combined_val_result_list = []
            for fold_num in range(num_of_folds):
                fold_combined_test_result_list.append(test_fold_epoch_results[fold_num][epoch_ind][rslt_ind])
                fold_combined_val_result_list.append(validation_fold_epoch_results[fold_num][epoch_ind][rslt_ind])

            str_test_fold_combined_list = ",".join([str(item) for item in fold_combined_test_result_list])
            str_val_fold_combined_list = ",".join([str(item) for item in fold_combined_val_result_list])
            epoch_test_combined_rslt_lst.append(str_test_fold_combined_list)
            #epoch_test_combined_rslt_lst.append(str(statistics.mean(fold_combined_test_result_list)))
            #epoch_test_combined_rslt_lst.append(str(statistics.pstdev(fold_combined_test_result_list)))
            epoch_val_combined_rslt_lst.append(str_val_fold_combined_list)
            #epoch_val_combined_rslt_lst.append(str(statistics.mean(fold_combined_val_result_list)))
            #epoch_val_combined_rslt_lst.append(str(statistics.pstdev(fold_combined_val_result_list)))
            #epoch_combined_rslt_lst.append(str_val_fold_combined_list)

        result_line = "\t".join(["\t".join(epoch_test_combined_rslt_lst), "\t".join(epoch_val_combined_rslt_lst)])
        result_fl.write(result_line + "\n")
        #print(result_line)

    result_fl.close()
# comp_feature_list, tar_feature_list, comp_hidden_lst, tar_num_of_last_neurons, fc1, fc2, learn_rate, comp_tar_pair_dataset, regression_classifier, batch_size


def full_training(comp_feature_list, tar_feature_list, comp_hidden_lst, tar_num_of_last_neurons, fc1, fc2, learn_rate, comp_tar_pair_dataset, regression_classifier, batch_size):
    torch.manual_seed(1)
    use_gpu = torch.cuda.is_available()

    device = "cpu"

    if use_gpu:
        print("GPU is available on this device!")
        device = "cuda"
    else:
        print("CPU is available on this device!")

    train_loader, test_loader = get_cnn_train_test_full_training_data_loader(batch_size)

    test_epoch_results = []
    test_epoch_results.append([])

    model = CompFCNNTarCNN2(1024, tar_num_of_last_neurons, comp_hidden_lst[0], comp_hidden_lst[1], fc1, fc2, drop_prob=0.5).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=learn_rate)
    criterion = torch.nn.MSELoss()
    optimizer.zero_grad()

    for epoch in range(n_epoch):
        #print("Epoch :{}".format(epoch))
        total_training_loss, total_test_loss = 0.0, 0.0
        total_training_count, total_test_count = 0, 0
        test_predictions, test_labels, test_all_comp_ids, test_all_tar_ids = [], [],[] ,[]
        batch_number = 0
        model.train()
        for i, data in enumerate(train_loader):
            batch_number += 1
            # clear gradient DO NOT forget you fool!
            optimizer.zero_grad()

            # get the inputs
            #comp_feature_vectors, target_feature_vectors, labels, compound_ids, target_ids, number_of_comp_features, number_of_target_features = data
            comp_feature_vectors, target_feature_vectors, labels, compound_ids, target_ids = data
            # wrap them in Variable
            comp_feature_vectors, target_feature_vectors, labels = Variable(comp_feature_vectors).to(device), Variable(
                target_feature_vectors).to(device), Variable(labels).to(device)
            # if comp_feature_vectors.shape[0]==batch_size:
            inputs = None
            y_pred = None

            total_training_count += comp_feature_vectors.shape[0]

            y_pred = model(comp_feature_vectors, target_feature_vectors).to(device)

            loss = criterion(y_pred.squeeze(), labels)

            total_training_loss += float(loss.item())
            loss.backward()
            optimizer.step()

        #print("Epoch {} training loss:".format(epoch), total_training_loss)

        model.eval()
        with torch.no_grad():  # torch.set_grad_enabled(False):

            for i, data in enumerate(test_loader):
                test_comp_feature_vectors, test_target_feature_vectors, tst_labels, test_compound_ids, test_target_ids = data
                test_comp_feature_vectors, test_target_feature_vectors, tst_labels = Variable(test_comp_feature_vectors).to(
                    device), Variable(
                    test_target_feature_vectors).to(device), Variable(tst_labels).to(device)

                total_test_count += test_comp_feature_vectors.shape[0]

                # if test_comp_feature_vectors.shape[0] == batch_size:
                test_inputs = None
                test_y_pred = None
                test_y_pred  = model(test_comp_feature_vectors, test_target_feature_vectors)
                loss_test = criterion(test_y_pred.squeeze(), tst_labels)
                total_test_loss += float(loss_test.item())
                for item in tst_labels:
                    test_labels.append(float(item.item()))

                for item in test_y_pred:
                    test_predictions.append(float(item.item()))

                for item in test_compound_ids:
                    test_all_comp_ids.append(item)

                for item in test_target_ids:
                    test_all_tar_ids.append(item)

        if regression_classifier == "r":
            print("==============================================================================")
            get_scores_full(test_labels, test_predictions, "Test", total_training_loss,
                       total_test_loss, epoch, comp_tar_pair_dataset, test_epoch_results)
        if epoch==n_epoch-1:
            pred_fl = open("../result_files/{}_full_prediction.tsv".format("_".join(sys.argv[1:])), "w")
            header = "Comp_ID\tTar_ID\tLabel\tPrediction"
            pred_fl.write(header + "\n")
            for ind in range(len(test_all_tar_ids)):
                pred_fl.write("{}\t{}\t{}\t{}\n".format(test_all_comp_ids[ind], test_all_tar_ids[ind], test_labels[ind], test_predictions[ind]))
            pred_fl.close()
    # deep_dta_rm2, deep_dta_cindex, deep_dta_mse, pearson_score, spearman_score, ci_score, f1_score, ave_auc_score
    result_fl = open("../result_files/{}_full.tsv".format("_".join(sys.argv[1:])), "w")
    header = "test_deep_dta_rm2\ttest_deep_dta_cindex\ttest_deep_dta_mse\ttest_pearson_score\ttest_spearman_score\ttest_ci_score\ttest_f1_score\ttest_ave_auc_score"
    #print(header)
    #print(test_fold_epoch_results)
    result_fl.write(header+"\n")
    for epoch_ind in range(n_epoch):
        test_epoch_results = [str(rslt) for rslt in test_epoch_results[epoch_ind]]
        result_line = "\t".join(test_epoch_results)
        result_fl.write(result_line + "\n")
        #print(result_line)

    result_fl.close()
# comp_feature_list, tar_feature_list, comp_hidden_lst, tar_num_of_last_neurons, fc1, fc2, learn_rate, comp_tar_pair_dataset, regression_classifier, batch_size

after_flattened_conv_layer_neurons = sys.argv[1]
last_2_hidden_layer_list = sys.argv[2].split("_")
learn_rate = sys.argv[3]
batch_size = sys.argv[4]
training_dataset = sys.argv[5]

# train_networks(["ecfp4"], ["sequencematrix500"], [1024, 512], 64, 256, 256, 0.001, "davis_comp_targ_affinity.csv", "r", 32)
# full_training(["ecfp4"], ["sequencematrix1000"], [1024, 512], int(after_flattened_conv_layer_neurons), int(last_2_hidden_layer_list[0]), int(last_2_hidden_layer_list[1]), float(learn_rate), "davis_comp_targ_affinity.csv", "r", int(batch_size))
full_training(["ecfp4"], ["sequencematrix500"], [1024, 512], int(after_flattened_conv_layer_neurons), int(last_2_hidden_layer_list[0]), int(last_2_hidden_layer_list[1]), float(learn_rate), "davis_comp_targ_affinity.csv", "r", int(batch_size))
