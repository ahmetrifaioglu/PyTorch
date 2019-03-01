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




class TrainDream(Trainable):
    def _setup(self, config):
        args = config.pop("args")
        vars(args).update(config)
        args.cuda = not args.no_cuda and torch.cuda.is_available()
        print(args.cuda)

        torch.manual_seed(1)
        use_gpu = torch.cuda.is_available()

        device = "cpu"

        if use_gpu:
            print("GPU is available on this device!")
            device = "cuda"
        else:
            print("CPU is available on this device!")

        kwargs = {'num_workers': 1, 'pin_memory': True} if args.cuda else {}

        loader_fold_dict, number_of_comp_features, number_of_target_features = get_nfold_data_loader_dict(num_of_folds,
                                                                                                          batch_size,
                                                                                                          comp_feature_list,
                                                                                                          tar_feature_list,
                                                                                                          comp_tar_pair_dataset,
                                                                                                          regression_classifier)

        original_number_of_comp_features = int(number_of_comp_features)
        original_number_of_target_features = int(number_of_target_features)

        print(original_number_of_comp_features, original_number_of_target_features)

        self.train_loader = loader_fold_dict[0][0]
        self.test_loader = loader_fold_dict[0][1]

        self.model = FC_PINNModel_2_2_2_Modules(number_of_comp_features, args.first_comp_layer, args.second_comp_layer, number_of_target_features, args.first_tar_layer, args.second_tar_layer, args.first_comb_layer, args.second_comb_layer, "r").to(self.device)
        if args.cuda:
            self.model.cuda()

        self.optimizer = optim.SGD(
            self.model.parameters(), lr=args.lr, momentum=args.momentum)
        self.args = args

    def _train_iteration(self):
        self.model.train()

        total_training_loss = 0.0
        total_training_count = 0

        batch_number = 0
        for i, data in enumerate(self.train_loader):

            batch_number += 1
            # get the inputs
            comp_feature_vectors, target_feature_vectors, labels, compound_ids, target_ids, number_of_comp_features, number_of_target_features = data
            # wrap them in Variable
            comp_feature_vectors, target_feature_vectors, labels = Variable(comp_feature_vectors).to(self.device), Variable(
                target_feature_vectors).to(self.device), Variable(labels).to(self.device)
            # print(labels)
            # clear gradient DO NOT forget you fool!
            self.optimizer.zero_grad()
            inputs = None
            y_pred = None
            concat_models = [""]
            modeltype = None
            total_training_count += comp_feature_vectors.shape[0]
            if modeltype in concat_models:
                inputs = torch.cat((comp_feature_vectors, target_feature_vectors), 1)
                y_pred = self.model(inputs)
            else:
                # Forward pass: Compute predicted y by passing x to the model
                y_pred = self.model(comp_feature_vectors, target_feature_vectors)

            # Compute and print loss
            # loss = criterion(y_pred.squeeze(), labels)
            # print(y_pred)

            # print(len(weights), len(labels))

            regression_classifier = "r"
            loss = None
            criterion = torch.nn.MSELoss()
            if regression_classifier == "r":
                loss = criterion(y_pred.squeeze(), labels)
            else:
                loss = criterion(y_pred.squeeze(), labels)

            total_training_loss += float(loss.item())
            # print(y_pred)
            loss.backward()
            self.optimizer.step()
        print(total_training_loss)
        return {"neg_mean_loss": -1*total_training_loss}

    def _test(self):
        self.model.eval()
        regression_classifier = "r"
        total_validation_loss = 0.0
        total_validation_count = 0
        validation_predictions = []
        validation_labels = []

        with torch.no_grad():  # torch.set_grad_enabled(False):
            for i, data in enumerate(self.test_loader):
                # print("Validation")
                val_comp_feature_vectors, val_target_feature_vectors, val_labels, val_compound_ids, val_target_ids, val_number_of_comp_features, val_number_of_target_features = data
                val_comp_feature_vectors, val_target_feature_vectors, val_labels = Variable(
                    val_comp_feature_vectors).to(
                    self.device), Variable(val_target_feature_vectors).to(self.device), Variable(val_labels).to(self.device)
                # val_inputs = torch.cat((val_comp_feature_vectors, val_target_feature_vectors), 1)
                total_validation_count += val_comp_feature_vectors.shape[0]
                # print(val_comp_feature_vectors)
                # print(val_labels)
                val_inputs = None
                val_y_pred = None
                concat_models = [""]
                # print(self.model.parameters)
                modeltype = None
                if modeltype in concat_models:
                    val_inputs = torch.cat((val_comp_feature_vectors, val_target_feature_vectors), 1)
                    val_y_pred = self.model(val_inputs)
                else:
                    # Forward pass: Compute predicted y by passing x to the model
                    # print("girdi")
                    val_y_pred = self.model(val_comp_feature_vectors, val_target_feature_vectors)

                # print(val_y_pred)
                criterion = torch.nn.MSELoss()
                loss_val = criterion(val_y_pred.squeeze(), val_labels)
                total_validation_loss += float(loss_val.item())

                for item in val_y_pred:
                    # regression icin
                    # validation_predictions.append(float(item.data[0]))
                    # classification icin
                    if regression_classifier == "r":
                        validation_predictions.append(float(item.data[0]))
                    else:
                        validation_predictions.append(int(float(item.data[0]) >= 0.5))
                    # print(item.data[0], int(float(item.data[0])>=0.5))
                    # print("real pred", float(item.data[0]))
                    # print("loggedpred", -math.log10(10e-10*float(item.data[0])))
                    # validation_predictions.append(-math.log10(10e-10*float(item.data[0])))
                for item in val_labels:
                    # regression icin
                    # validation_labels.append(float(item.data[0]))
                    # classification icin
                    if regression_classifier == "r":
                        validation_labels.append(float(item.item()))
                    else:
                        validation_labels.append(int(item.data[0]))

                    # validation_labels.append(-math.log10(10e-10*float(item.data[0])))
        # print("validation predictions", validation_predictions)
        # print("validation labels", validation_labels)
        if regression_classifier == "r":
            rmse_score = rmse(np.asarray(validation_labels), np.asarray(
                validation_predictions))
            pearson_score = pearson(np.asarray(validation_labels), np.asarray(validation_predictions))
            # spearman_score = spearman(np.asarray(validation_labels), np.asarray(validation_predictions))
            # ci_score = ci(np.asarray(validation_labels), np.asarray(validation_predictions))
            f1_score = f1(np.asarray(validation_labels), np.asarray(validation_predictions))
            ave_auc_score = average_AUC(np.asarray(validation_labels), np.asarray(validation_predictions))
            print("================================================================================")
            print("Fold:{}\tEpoch:{}\tTest RMSE:{}\tValidation Loss:{}".format(0 + 1, 0,
                                                                                                 rmse_score,
                                                                                                 total_validation_loss))
            print("RMSE:\t{}".format(rmse_score))  # rmse, pearson, spearman, ci, ci, average_AUC
            #print("Pearson:\t{}".format(pearson_score))
            #print("Spearman:\t{}".format(spearman_score))
            #print("Ci:\t{}".format(ci_score))
            print("F1-Score:\t{}".format(f1_score))
            print("Average_AUC:\t{}".format(ave_auc_score))
            # print("IDG File:\t{}".format(comp_tar_pair_dataset))
            #print("Number of training samples:\t{}".format(total_training_count))
            # print("Number of validation samples:\t{}".format(total_validation_count))


            return {"RMSE": rmse_score, "F1-Score": f1_score}
        else:
            f1_score = sklearn.metrics.f1_score(validation_labels, validation_predictions)
            accuracy_score = sklearn.metrics.accuracy_score(validation_labels, validation_predictions)
            print("================================================================================")
            print("Fold:{}\tEpoch:{}\tTest F1:{}\tValidation Loss:{}".format(0 + 1, 0,
                                                                                               f1_score,
                                                                                               total_validation_loss))

            print("F1 Score:\t{}".format(f1_score))
            print("Accuracy:\t{}.".format(accuracy_score))

        return {"neg_mean_loss": -1*total_validation_loss, "mean_accuracy": accuracy_score}
    def _train(self):
        self._train_iteration()
        return self._test()

    def _save(self, checkpoint_dir):
        checkpoint_path = os.path.join(checkpoint_dir, "model.pth")
        torch.save(self.model.state_dict(), checkpoint_path)
        return checkpoint_path

    def _restore(self, checkpoint_path):
        self.model.load_state_dict(checkpoint_path)



# number_of_comp_features, comp_l1, comp_l2, vocab_size, output_size, embedding_dim, hidden_dim, n_layers, drop_prob=0.5


# learn_rate = sys.argv[2]
n_epoch = 10
num_of_folds = 5
batch_size = 45
comp_feature_list = "ecfp4".split("_")
tar_feature_list = "trigramencodings1000".split("_")
comp_tar_pair_dataset = "idg_comp_targ_uniq_inter_filtered.csv"
regression_classifier = "r"
learn_rate = 0.001



torch.manual_seed(1)
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
            # print(i)
            # print(len(data))
            batch_number += 1
            h = tuple([each.data for each in h])
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

                y_pred, h = model(comp_feature_vectors, target_feature_vectors, h)
                #print(y_pred)

                loss = criterion(y_pred.squeeze(), labels)

                total_training_loss += float(loss.item())
                loss.backward()
                optimizer.step()
        print("Epoch {} training loss:".format(epoch), total_training_loss)

        h = model.init_hidden(batch_size)
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


                    val_y_pred, h = model(val_comp_feature_vectors, val_target_feature_vectors, h)
                    #print(val_y_pred)
                    loss_val = criterion(val_y_pred.squeeze(), val_labels)
                    total_validation_loss += float(loss_val.item())
                    for item in val_labels:
                        validation_labels.append(float(item.data[0]))

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

