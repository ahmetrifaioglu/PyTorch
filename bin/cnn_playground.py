from __future__ import print_function, division
import os
import sys
import math
import torch
import warnings
import itertools
import numpy as np
import pandas as pd
import subprocess
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from torch.autograd import Variable
import torch.nn.functional as F
from evaluation_metrics import rmse, pearson, spearman, ci, prec_rec_f1_acc_mcc, average_AUC, mse
from torchvision import datasets
import torchvision.transforms as transforms
from sklearn.metrics import f1_score, accuracy_score
from sklearn import preprocessing,metrics
import sklearn
from cnn_models import CompFCNNTarCNNModuleInception, CompFCNNTarCNN4Layers, CompFCNNTarCNNModule2Layers, CompFCNNTarCNN4LayersStride
from evaluation_metrics import r_squared_error, get_rm2, squared_error_zero, get_k, get_cindex, get_aupr, get_list_of_scores
from cnn_data_processing import get_cnn_test_val_folds_train_data_loader, get_cnn_train_test_full_training_data_loader, get_aa_match_encodings_max_value

warnings.filterwarnings(action='ignore')

cwd = os.getcwd()
project_file_path = "{}PyTorch".format(cwd.split("PyTorch")[0])

n_epoch = 100
num_of_folds = 5

def get_model(model_name, tar_feature_list, num_of_com_features, tar_num_of_last_neurons, comp_hidden_first, comp_hidden_second, fc1, fc2, dropout):
    model=None
    if model_name == "CompFCNNTarCNNModuleInception":
        model = CompFCNNTarCNNModuleInception(tar_feature_list, num_of_com_features, tar_num_of_last_neurons, comp_hidden_first, comp_hidden_second,
                                fc1, fc2, dropout)
    elif model_name=="CompFCNNTarCNN4Layers":
        model = CompFCNNTarCNN4Layers(tar_feature_list, num_of_com_features, tar_num_of_last_neurons, comp_hidden_first, comp_hidden_second,
                            fc1, fc2, dropout)
    elif model_name=="CompFCNNTarCNNModule2Layers":
        model = CompFCNNTarCNNModule2Layers(tar_feature_list, num_of_com_features, tar_num_of_last_neurons, comp_hidden_first, comp_hidden_second,
                            fc1, fc2, dropout)
    elif model_name=="CompFCNNTarCNN4LayersStride":
        model = CompFCNNTarCNN4LayersStride(tar_feature_list, num_of_com_features, tar_num_of_last_neurons, comp_hidden_first, comp_hidden_second,
                            fc1, fc2, dropout)
    return model


def get_scores(labels, predictions, validation_test, total_training_loss, total_validation_test_loss, epoch, fold_epoch_results, fold=None):
    score_dict = {"rm2": None, "CI (DEEPDTA)": None, "MSE": None, "RMSE": None, "Pearson": None,
                  "Spearman": None, "CI (Challenge)": None, "Average AUC": None,
                  "Precision 5.0": None, "Recall 5.0": None, "F1-Score 5.0": None, "Accuracy 5.0": None, "MCC 5.0": None,
                  "Precision 6.0": None, "Recall 6.0": None, "F1-Score 6.0": None, "Accuracy 6.0": None, "MCC 6.0": None,
                  "Precision 7.0": None, "Recall 7.0": None, "F1-Score 7.0": None, "Accuracy 7.0": None, "MCC 7.0": None,
                  }

    score_dict = {"rm2": None, "CI (DEEPDTA)": None, "MSE": None, "RMSE": None, "Pearson": None,
                  "Spearman": None, "CI (Challenge)": None, "Average AUC": None,
                  "Precision 10uM": None, "Recall 10uM": None, "F1-Score 10uM": None, "Accuracy 10uM": None, "MCC 10uM": None,
                  "Precision 1uM": None, "Recall 1uM": None, "F1-Score 1uM": None, "Accuracy 1uM": None, "MCC 1uM": None,
                  "Precision 100nM": None, "Recall 100nM": None, "F1-Score 100nM": None, "Accuracy 100nM": None, "MCC 100nM": None,
                  "Precision 30nM": None, "Recall 30nM": None, "F1-Score 30nM": None, "Accuracy 30nM": None, "MCC 30nM": None,}
    score_list = get_list_of_scores()

    score_dict["rm2"] = get_rm2(np.asarray(labels), np.asarray(
        predictions))
    score_dict["CI (DEEPDTA)"] = get_cindex(np.asarray(labels), np.asarray(
        predictions))
    score_dict["MSE"] = mse(np.asarray(labels), np.asarray(
        predictions))
    score_dict["RMSE"] = rmse(np.asarray(labels), np.asarray(
        predictions))
    score_dict["Pearson"] = pearson(np.asarray(labels), np.asarray(predictions))
    score_dict["Spearman"] = spearman(np.asarray(labels), np.asarray(predictions))
    score_dict["CI (Challenge)"] = ci(np.asarray(labels), np.asarray(predictions))
    score_dict["Average AUC"] = average_AUC(np.asarray(labels), np.asarray(predictions))

    prec_rec_f1_acc_mcc_threshold_dict = prec_rec_f1_acc_mcc(np.asarray(labels), np.asarray(predictions))
    for key in prec_rec_f1_acc_mcc_threshold_dict.keys():
        score_dict[key] = prec_rec_f1_acc_mcc_threshold_dict[key]

    """
    lst_calculated_scores = []
    for scr in score_list:
        lst_calculated_scores.append(score_dict[scr])
    """

    if fold!=None:
        fold_epoch_results[-1].append(score_dict)
        print("Fold:{}\tEpoch:{}\tTraining Loss:{}\t{} Loss:{}".format(fold + 1, epoch, total_training_loss,
                                                                       validation_test, total_validation_test_loss))
    else:
        fold_epoch_results.append(score_dict)
        print("Epoch:{}\tTraining Loss:{}\t{} Loss:{}".format(epoch, total_training_loss, validation_test,
                                                              total_validation_test_loss))
    for scr in score_list:
        print("{} {}:\t{}".format(validation_test, scr, score_dict[scr]))
    """
    print("{} RM2:\t{}".format(validation_test, deep_dta_rm2))
    print("{} MSE\t{}".format(validation_test, deep_dta_mse))
    print("{} RMSE\t{}".format(validation_test, rmse_score))
    print("{} c-index\t{}".format(validation_test, deep_dta_cindex))
    print("{} Pearson:\t{}".format(validation_test, pearson_score))
    print("{} Spearman:\t{}".format(validation_test, spearman_score))
    print("{} Ci:\t{}".format(validation_test, ci_score))
    print("{} Average_AUC:\t{}".format(validation_test, ave_auc_score))

    for key in prec_rec_f1_acc_mcc_threshold_dict.keys():
        
    """






def train_networks(training_dataset, comp_feature_list, tar_feature_list, comp_hidden_lst, tar_num_of_last_neurons, fc1, fc2, learn_rate, regression_classifier, batch_size, train_val_test, model_nm, dropout, experiment_name):
    arguments = [str(argm) for argm in sys.argv[1:]]
    print("Arguments::", "-".join(arguments))
    torch.manual_seed(123)
    np.random.seed(123)

    use_gpu = torch.cuda.is_available()

    device = "cpu"

    if use_gpu:
        print("GPU is available on this device!")
        device = "cuda"
    else:
        print("CPU is available on this device!")

    loader_fold_dict, test_loader = get_cnn_test_val_folds_train_data_loader(training_dataset, comp_feature_list, tar_feature_list, batch_size)

    validation_fold_epoch_results, test_fold_epoch_results = [], []

    for fold in range(num_of_folds):
        test_fold_epoch_results.append([])
        validation_fold_epoch_results.append([])
        train_loader, valid_loader = loader_fold_dict[fold]

        print("FOLD : {}".format(fold + 1))

        model = get_model(model_nm, tar_feature_list, 1024, tar_num_of_last_neurons, comp_hidden_lst[0],
                          comp_hidden_lst[1], fc1, fc2, dropout).to(device)
        optimizer = torch.optim.Adam(model.parameters(), lr=learn_rate)
        criterion = torch.nn.MSELoss()
        optimizer.zero_grad()

        for epoch in range(n_epoch):
            print("Epoch :{}".format(epoch))
            total_training_loss, total_validation_loss, total_test_loss = 0.0, 0.0, 0.0
            total_training_count, total_validation_count, total_test_count = 0, 0, 0
            validation_predictions, validation_labels, test_predictions, test_labels = [], [], [], []
            test_all_comp_ids, test_all_tar_ids =  [], []
            batch_number = 0
            model.train()
            for i, data in enumerate(train_loader):
                batch_number += 1
                # clear gradient DO NOT forget you fool!
                optimizer.zero_grad()

                comp_feature_vectors, target_feature_vectors, labels, compound_ids, target_ids = data
                comp_feature_vectors, target_feature_vectors, labels = Variable(comp_feature_vectors).to(device), Variable(
                    target_feature_vectors).to(device), Variable(labels).to(device)

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
                    val_comp_feature_vectors, val_target_feature_vectors, val_labels, val_compound_ids, val_target_ids = data
                    val_comp_feature_vectors, val_target_feature_vectors, val_labels = Variable(val_comp_feature_vectors).to(
                        device), Variable(
                        val_target_feature_vectors).to(device), Variable(val_labels).to(device)

                    total_validation_count += val_comp_feature_vectors.shape[0]
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

                    test_y_pred  = model(test_comp_feature_vectors, test_target_feature_vectors)
                    loss_test = criterion(test_y_pred.squeeze(), tst_labels)
                    total_test_loss += float(loss_test.item())
                    for item in tst_labels:
                        test_labels.append(float(item.item()))

                    for item in test_y_pred:
                        test_predictions.append(float(item.item()))

                    test_all_comp_ids.extend(test_compound_ids)
                    test_all_tar_ids.extend(test_target_ids)
                # test_predictions, test_labels
                print_predictions = True
                if print_predictions:
                    print("=====PREDICTIONS=====")
                    for ind in range(len(test_all_tar_ids)):
                        print("{}\t{}\t{}\t{}".format(test_all_comp_ids[ind], test_all_tar_ids[ind], test_labels[ind],
                                                      test_predictions[ind]))
                    print("=====PREDICTIONS=====")

            if regression_classifier == "r":
                print("==============================================================================")
                get_scores(validation_labels, validation_predictions, "Validation", total_training_loss, total_validation_loss, epoch, validation_fold_epoch_results, fold)
                print("------------------------------------------------------------------------------")
                get_scores(test_labels, test_predictions, "Test", total_training_loss,
                           total_test_loss, epoch, test_fold_epoch_results, fold)


                if epoch==n_epoch-1:
                    #print(len(test_fold_epoch_results[-1]))
                    mse_results = [epoch_score_dict["MSE"] for epoch_score_dict in test_fold_epoch_results[-1]]
                    if training_dataset=="Davis":
                        if min(mse_results) >= 0.30:
                            sys.exit("Terminating training since minimum MSE is higher than the threshold!")
                    elif training_dataset=="Davis_Filtered":
                        if min(mse_results) >= 0.60:
                            sys.exit("Terminating training since minimum MSE is higher than the threshold!")


    if not os.path.exists("{}/result_files/{}".format(project_file_path, experiment_name)):
        subprocess.call("mkdir {}".format("{}/result_files/{}".format(project_file_path, experiment_name)), shell=True)

    result_fl = open("{}/result_files/{}/{}.tsv".format(project_file_path, experiment_name, "-".join(sys.argv[1:])), "w")
    score_list = get_list_of_scores()
    header = "test {}\tvalidation {}".format("\ttest ".join(score_list), "\tvalidation ".join(score_list))
    result_fl.write(header+"\n")
    for epoch_ind in range(n_epoch):

        epoch_test_combined_rslt_lst = []
        epoch_val_combined_rslt_lst = []
        for rslt_ind in range(len(score_list)):
            fold_combined_test_result_list = []
            fold_combined_val_result_list = []
            for fold_num in range(num_of_folds):
                fold_combined_test_result_list.append(test_fold_epoch_results[fold_num][epoch_ind][score_list[rslt_ind]])
                fold_combined_val_result_list.append(validation_fold_epoch_results[fold_num][epoch_ind][score_list[rslt_ind]])

            str_test_fold_combined_list = ",".join([str(item) for item in fold_combined_test_result_list])
            str_val_fold_combined_list = ",".join([str(item) for item in fold_combined_val_result_list])

            epoch_test_combined_rslt_lst.append(str_test_fold_combined_list)
            epoch_val_combined_rslt_lst.append(str_val_fold_combined_list)

        result_line = "\t".join(["\t".join(epoch_test_combined_rslt_lst), "\t".join(epoch_val_combined_rslt_lst)])
        result_fl.write(result_line + "\n")


    result_fl.close()


def full_training(training_dataset, comp_feature_list, tar_feature_list, comp_hidden_lst, tar_num_of_last_neurons, fc1, fc2, learn_rate, regression_classifier, batch_size, train_val_test, model_nm, dropout, experiment_name):
    arguments = [str(argm) for argm in sys.argv[1:]]
    print("Arguments:", "-".join(arguments))

    torch.manual_seed(123)
    np.random.seed(123)
    use_gpu = torch.cuda.is_available()

    device = "cpu"

    if use_gpu:
        print("GPU is available on this device!")
        device = "cuda"
    else:
        print("CPU is available on this device!")

    train_loader, validation_loader, test_loader = None, None, None
    if train_val_test:
        train_loader, validation_loader, test_loader = get_cnn_train_test_full_training_data_loader(training_dataset, comp_feature_list, tar_feature_list, batch_size, train_val_test)
    else:
        train_loader, test_loader = get_cnn_train_test_full_training_data_loader(training_dataset,
                                                                                                 comp_feature_list,
                                                                                                 tar_feature_list,
                                                                                                 batch_size,
                                                                                                 train_val_test)
    validation_epoch_results, test_epoch_results = [], []
    validation_epoch_results.append([])
    test_epoch_results.append([])

    model = get_model(model_nm, tar_feature_list, 1024, tar_num_of_last_neurons, comp_hidden_lst[0], comp_hidden_lst[1], fc1, fc2, dropout).to(device)

    optimizer = torch.optim.Adam(model.parameters(), lr=learn_rate)
    criterion = torch.nn.MSELoss()
    optimizer.zero_grad()

    for epoch in range(n_epoch):
        print("Epoch :{}".format(epoch))
        total_training_loss, total_test_loss, total_validation_loss = 0.0, 0.0, 0.0
        total_training_count, total_test_count, total_validation_count = 0, 0, 0
        test_predictions, test_labels, test_all_comp_ids, test_all_tar_ids = [], [], [], []
        validation_predictions, validation_labels, validation_all_comp_ids, validation_all_tar_ids = [], [], [], []

        batch_number = 0

        model.train()
        for i, data in enumerate(train_loader):
            batch_number += 1
            # clear gradient DO NOT forget you fool!
            optimizer.zero_grad()

            # get the inputs
            comp_feature_vectors, target_feature_vectors, labels, compound_ids, target_ids = data
            comp_feature_vectors, target_feature_vectors, labels = Variable(comp_feature_vectors).to(device), Variable(
                target_feature_vectors).to(device), Variable(labels).to(device)

            total_training_count += comp_feature_vectors.shape[0]
            y_pred = model(comp_feature_vectors, target_feature_vectors).to(device)
            loss = criterion(y_pred.squeeze(), labels)
            total_training_loss += float(loss.item())
            loss.backward()
            optimizer.step()

        print("Epoch {} training loss:".format(epoch), total_training_loss)

        if train_val_test:
            model.eval()
            with torch.no_grad():  # torch.set_grad_enabled(False):

                for i, data in enumerate(validation_loader):
                    validation_comp_feature_vectors, validation_target_feature_vectors, val_labels, validation_compound_ids, validation_target_ids = data
                    validation_comp_feature_vectors, validation_target_feature_vectors, val_labels = Variable(
                        validation_comp_feature_vectors).to(
                        device), Variable(
                        validation_target_feature_vectors).to(device), Variable(val_labels).to(device)

                    total_validation_count += validation_comp_feature_vectors.shape[0]

                    validation_y_pred = model(validation_comp_feature_vectors, validation_target_feature_vectors)
                    loss_validation = criterion(validation_y_pred.squeeze(), val_labels)
                    total_validation_loss += float(loss_validation.item())

                    for item in val_labels:
                        validation_labels.append(float(item.item()))

                    for item in validation_y_pred:
                        validation_predictions.append(float(item.item()))

                    for item in validation_compound_ids:
                        validation_all_comp_ids.append(item)

                    for item in validation_target_ids:
                        validation_all_tar_ids.append(item)

            if regression_classifier == "r":
                print("==============================================================================")
                get_scores(validation_labels, validation_predictions, "validation", total_training_loss,
                                total_validation_loss, epoch, validation_epoch_results)

            print("Epoch {} validation loss:".format(epoch), total_validation_loss)

        model.eval()
        with torch.no_grad():  # torch.set_grad_enabled(False):

            for i, data in enumerate(test_loader):
                test_comp_feature_vectors, test_target_feature_vectors, tst_labels, test_compound_ids, test_target_ids = data
                test_comp_feature_vectors, test_target_feature_vectors, tst_labels = Variable(test_comp_feature_vectors).to(
                    device), Variable(
                    test_target_feature_vectors).to(device), Variable(tst_labels).to(device)

                total_test_count += test_comp_feature_vectors.shape[0]

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
            # print(test_all_tar_ids)
            print_predictions = True
            if print_predictions:
                print("=====PREDICTIONS=====")
                for ind in range(len(test_all_tar_ids)):
                    print("{}\t{}\t{}\t{}".format(test_all_comp_ids[ind], test_all_tar_ids[ind], test_labels[ind], test_predictions[ind]))
                print("=====PREDICTIONS=====")

        if regression_classifier == "r":
            print("==============================================================================")
            get_scores(test_labels, test_predictions, "test", total_training_loss,
                       total_test_loss, epoch, test_epoch_results)
        """
        if epoch==n_epoch-1:
            pred_fl = open("../result_files/{}_full_prediction_500.tsv".format("_".join(sys.argv[1:])), "w")
            header = "Comp_ID\tTar_ID\tLabel\tPrediction"
            pred_fl.write(header + "\n")
            for ind in range(len(test_all_tar_ids)):
                pred_fl.write("{}\t{}\t{}\t{}\n".format(test_all_comp_ids[ind], test_all_tar_ids[ind], test_labels[ind], test_predictions[ind]))
            pred_fl.close()
        """
    # deep_dta_rm2, deep_dta_cindex, deep_dta_mse, pearson_score, spearman_score, ci_score, f1_score, ave_auc_score
    """
    result_fl = open("../result_files/{}_full_500.tsv".format("_".join(sys.argv[1:])), "w")
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
    """

comp_hidden_layer_neurons = [int(num) for num in sys.argv[1].split("_")]
after_flattened_conv_layer_neurons = int(sys.argv[2])
last_2_hidden_layer_list = [int(num) for num in sys.argv[3].split("_")]
learn_rate = float(sys.argv[4])
batch_size = int(sys.argv[5])
training_dataset = sys.argv[6]
comp_feature_list = sys.argv[7].split("_")# ["ecfp4"]
tar_feature_list = sys.argv[8].split("_")# ["sequencematrix500"]
train_validation_test = bool(sys.argv[9])
model_name = sys.argv[10]
dropout_prob = float(sys.argv[11])
experiment_name = sys.argv[12]


# train_networks(["ecfp4"], ["sequencematrix500"], [1024, 512], 64, 256, 256, 0.001, "xxx", "r", 32)
# train_networks(["ecfp4"], ["sequencematrix1000"], [1024, 512], int(after_flattened_conv_layer_neurons), int(last_2_hidden_layer_list[0]), int(last_2_hidden_layer_list[1]), float(learn_rate), "xxx.csv", "r", int(batch_size))
# train_networks(training_dataset, comp_feature_list, tar_feature_list, comp_hidden_layer_neurons, int(after_flattened_conv_layer_neurons), int(last_2_hidden_layer_list[0]), int(last_2_hidden_layer_list[1]), float(learn_rate), "xxx.csv", "r", int(batch_size))
# full_training(["ecfp4"], ["sequencematrix1000"], [1024, 512], int(after_flattened_conv_layer_neurons), int(last_2_hidden_layer_list[0]), int(last_2_hidden_layer_list[1]), float(learn_rate), "xxx.csv", "r", int(batch_size))
#train_networks(training_dataset, comp_feature_list, tar_feature_list, comp_hidden_layer_neurons, int(after_flattened_conv_layer_neurons), int(last_2_hidden_layer_list[0]), int(last_2_hidden_layer_list[1]), float(learn_rate), "xxx.csv", "r", int(batch_size))
#            (training_dataset, comp_feature_list, tar_feature_list, comp_hidden_lst, tar_num_of_last_neurons, fc1, fc2, learn_rate, comp_tar_pair_dataset, regression_classifier, batch_size, train_val_test=False)


# full_training(training_dataset, comp_feature_list, tar_feature_list, comp_hidden_layer_neurons, after_flattened_conv_layer_neurons, last_2_hidden_layer_list[0], last_2_hidden_layer_list[1], learn_rate, "r", batch_size, train_validation_test, model_name, dropout_prob, experiment_name)
train_networks(training_dataset, comp_feature_list, tar_feature_list, comp_hidden_layer_neurons, after_flattened_conv_layer_neurons, last_2_hidden_layer_list[0], last_2_hidden_layer_list[1], learn_rate, "r", batch_size, train_validation_test, model_name, dropout_prob, experiment_name)
