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
from sklearn import preprocessing, metrics
import sklearn
from cnn_models import CompFCNNTarCNNModuleInception, CompFCNNTarCNN4Layers, CompFCNNTarCNNModule2Layers, \
    CompFCNNTarCNN4LayersStride
from evaluation_metrics import r_squared_error, get_rm2, squared_error_zero, get_k, get_cindex, get_aupr, \
    get_list_of_scores
from cnn_data_processing import get_cnn_test_val_folds_train_data_loader, get_cnn_train_test_full_training_data_loader, \
    get_aa_match_encodings_max_value, get_cnn_test_data_loader

warnings.filterwarnings(action='ignore')

cwd = os.getcwd()
project_file_path = "{}PyTorch".format(cwd.split("PyTorch")[0])

n_epoch = 100
num_of_folds = 5


def get_model(model_name, tar_feature_list, num_of_com_features, tar_num_of_last_neurons, comp_hidden_first,
              comp_hidden_second, fc1, fc2, dropout):
    model = None
    if model_name == "CompFCNNTarCNNModuleInception":
        model = CompFCNNTarCNNModuleInception(tar_feature_list, num_of_com_features, tar_num_of_last_neurons,
                                              comp_hidden_first, comp_hidden_second,
                                              fc1, fc2, dropout)
    elif model_name == "CompFCNNTarCNN4Layers":
        model = CompFCNNTarCNN4Layers(tar_feature_list, num_of_com_features, tar_num_of_last_neurons, comp_hidden_first,
                                      comp_hidden_second,
                                      fc1, fc2, dropout)
    elif model_name == "CompFCNNTarCNNModule2Layers":
        model = CompFCNNTarCNNModule2Layers(tar_feature_list, num_of_com_features, tar_num_of_last_neurons,
                                            comp_hidden_first, comp_hidden_second,
                                            fc1, fc2, dropout)
    elif model_name == "CompFCNNTarCNN4LayersStride":
        model = CompFCNNTarCNN4LayersStride(tar_feature_list, num_of_com_features, tar_num_of_last_neurons,
                                            comp_hidden_first, comp_hidden_second,
                                            fc1, fc2, dropout)
    return model


def load_model(model_fl):
    torch.manual_seed(123)
    np.random.seed(123)
    use_gpu = torch.cuda.is_available()

    device = "cpu"

    if use_gpu:
        print("GPU is available on this device!")
        device = "cuda"
    else:
        print("CPU is available on this device!")
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
    fold_num = int(sys.argv[13])
    """
    #model_fl = "kinome_best_val_1024_1024-256-512_256-0.0001-32-kinome-ecfp4-sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000-0-CompFCNNTarCNNModuleInception-0.25-kinome_dataset_ebi_gpu_only_combined_best_encoding-4_state_dict.pth"
    params = model_fl.split("kinome_best_val_")[1].split("-")
    comp_h_1 = int(params[0].split("_")[0])
    comp_h_2 = int(params[0].split("_")[1])
    tar_after_flat = int(params[1])
    last_h_1 = int(params[2].split("_")[0])
    last_h_2 = int(params[2].split("_")[1])
    tar_feats = params[7]
    dropout = float(params[10])
    #print()
    #kinome_best_val_1024_1024-256-512_256-0.0001-32-kinome-ecfp4-sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000-0-CompFCNNTarCNNModuleInception-0.25-kinome_dataset_ebi_gpu_only_combined_best_encoding-4_state_dict.pth
    #print("CompFCNNTarCNNModuleInception", tar_feats.split("_"), 1024, tar_after_flat, comp_h_1, comp_h_2,last_h_1,last_h_2, dropout)
    #print("CompFCNNTarCNNModuleInception", "sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000".split("_"), 1024, 256, 1024, 1024, 512, 256, 0.25)
    model = get_model("CompFCNNTarCNNModuleInception", tar_feats.split("_"), 1024, tar_after_flat, comp_h_1, comp_h_2,last_h_1,last_h_2, dropout)
    # model = get_model("CompFCNNTarCNNModuleInception", "sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000".split("_"), 1024, 256, 1024, 1024, 512, 256, 0.25)
    #print(model.state_dict())
    model.load_state_dict(torch.load("{}/trained_models/kinome/{}".format(project_file_path, model_fl)))
    model = model.to(device)
    model.eval()
    #print("================================================================================")
    #print("================================================================================")
    #print("================================================================================")
    #print(model.state_dict())
    #model = torch.load(model_fl)
    # print(model.state_dict())
    #torch.save(model.state_dict(), "{}/trained_models/kinome/kinome_state_dict.pth".format(project_file_path))

    test_loader = get_cnn_test_data_loader("kinome", ["ecfp4"], "sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000".split("_"), "aacr_test_comp_targ_affinity.csv")
    print("loader gecti")
    test_predictions, test_labels, test_all_comp_ids, test_all_tar_ids = [], [], [], []
    total_test_count = 0
    total_test_loss = 0.0

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


import sys
model_fl = sys.argv[1]
load_model(model_fl)
# load_model("kinome_best_val_1024_1024-256-512_256-0.0001-32-kinome-ecfp4-sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000-0-CompFCNNTarCNNModuleInception-0.25-kinome_dataset_ebi_gpu_only_combined_best_encoding-4_state_dict.pth")
# 1024_1024-256-512_256-0.0001-32-kinome-ecfp4-sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000-1-CompFCNNTarCNNModuleInception-0.1-kinome_dataset_ebi_gpu_only_combined_best_encoding-98
# load_model("../../1024_1024-256-512_256-0.0001-32-kinome-ecfp4-sequencematrix1000_ZHAC000103LEQ1000_GRAR740104LEQ1000_SIMK990101LEQ1000_blosum62LEQ1000-1-CompFCNNTarCNNModuleInception-0.1-kinome_dataset_ebi_gpu_only_combined_best_encoding-98")