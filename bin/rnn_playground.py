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
# from dream_challenge_models import FCModel1, FCModel2, FCPINNModel1, FCModel_3_Hidden_with_Modules, FCModel_3_Hidden, FCModel1_M
#from dream_challenge_models import FCModel1, FCModel2, FCPINNModel1, FCModel_3_Hidden_with_Modules, FCModel_3_Hidden, FCModel1_M
from dream_challenge_PINN_models import FC_PINNModel_2_2_2, FC_PINNModel_2_2_2_Modules, FC_PINNModel_2_3_2_Modules, FC_PINNModel_3_5_2_Modules#, FC_PINNModel_4_4_2,  FC_PINNModel_3_3_2
from dream_challenge_data_processing import TrainingValidationShuffledDataLoader, get_nfold_data_loader_dict
from rnn_playground_models import CompFCNNTarRNN



# number_of_comp_features, comp_l1, comp_l2, vocab_size, output_size, embedding_dim, hidden_dim, n_layers, drop_prob=0.5


# learn_rate = sys.argv[2]
n_epoch = 2
num_of_folds = 5
batch_size = 45
comp_feature_list = "ecfp4".split("_")
tar_feature_list = "trigramencodings1000".split("_")
comp_tar_pair_dataset = "idg_comp_targ_uniq_inter_filtered.csv"
regression_classifier = "r"
learn_rate = 0.001
use_gpu = torch.cuda.is_available()

device = "cpu"

if use_gpu:
    print("GPU is available on this device!")
    device = "cuda"
else:
    print("CPU is available on this device!")

loader_fold_dict, number_of_comp_features, number_of_target_features = get_nfold_data_loader_dict(num_of_folds,
                                                                                                  batch_size,
                                                                                                  comp_feature_list,
                                                                                                  tar_feature_list,
                                                                                                  comp_tar_pair_dataset,
                                                                                                  regression_classifier)

original_number_of_comp_features = int(number_of_comp_features)
original_number_of_target_features = int(number_of_target_features)

print(original_number_of_comp_features, original_number_of_target_features)


torch.manual_seed(1)
vocab_size = 8000 + 1  # +1 for the 0 padding + our word tokens
output_size = 100
embedding_dim = 400
hidden_dim = 256
n_layers = 2


for fold in range(num_of_folds):
    train_loader, valid_loader = loader_fold_dict[fold]
    # Just to check if everything is OK.
    # Remove this when you finish testing.
    print("FOLD : {}".format(fold + 1))
    # print(len(train_loader), len(valid_loader))
    number_of_comp_features = original_number_of_comp_features
    number_of_target_features = original_number_of_target_features
    model = CompFCNNTarRNN(1024, 100, 100, vocab_size, output_size, embedding_dim, hidden_dim, n_layers, 300, 300).to(device)
    # print(model)

    optimizer = torch.optim.SGD(
        model.parameters(), lr=learn_rate, momentum=0.507344802825)
    criterion = torch.nn.MSELoss()
    optimizer.zero_grad()

    for epoch in range(n_epoch):
        total_training_loss, total_validation_loss = 0.0, 0.0
        total_training_count, total_validation_count = 0, 0
        validation_predictions, validation_labels = [], []
        batch_number = 0

        h = model.init_hidden(batch_size)
        # print(h)
        model.train()
        for i, data in enumerate(train_loader):
            print(i)
            batch_number += 1
            h = tuple([each.data for each in h])
            # clear gradient DO NOT forget you fool!
            optimizer.zero_grad()

            # get the inputs
            comp_feature_vectors, target_feature_vectors, labels, compound_ids, target_ids, number_of_comp_features, number_of_target_features = data
            # wrap them in Variable
            comp_feature_vectors, target_feature_vectors, labels = Variable(comp_feature_vectors).to(device), Variable(
                target_feature_vectors).to(device), Variable(labels).to(device)
            # print(labels)
            inputs = None
            y_pred = None

            total_training_count += comp_feature_vectors.shape[0]

            y_pred, h = model(comp_feature_vectors, target_feature_vectors, h)


            loss = criterion(y_pred.squeeze(), labels)

            total_training_loss += float(loss.data[0])
            loss.backward()
            optimizer.step()


        model.eval()
        with torch.no_grad():  # torch.set_grad_enabled(False):
            for i, data in enumerate(valid_loader):

                val_comp_feature_vectors, val_target_feature_vectors, val_labels, val_compound_ids, val_target_ids, val_number_of_comp_features, val_number_of_target_features = data
                val_comp_feature_vectors, val_target_feature_vectors, val_labels = Variable(
                    val_comp_feature_vectors).to(
                    device), Variable(val_target_feature_vectors).to(device), Variable(val_labels).to(device)
                total_validation_count += val_comp_feature_vectors.shape[0]

                val_inputs = None
                val_y_pred = None

                if modeltype in concat_models:
                    val_inputs = torch.cat((val_comp_feature_vectors, val_target_feature_vectors), 1)
                    val_y_pred = model(val_inputs)
                else:
                    val_y_pred = model(val_comp_feature_vectors, val_target_feature_vectors)

                loss_val = criterion(val_y_pred.squeeze(), val_labels)
                total_validation_loss += float(loss_val.data[0])

                for item in val_y_pred:
                    validation_predictions.append(float(item.data[0]))

        if regression_classifier == "r":
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
