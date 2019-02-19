# Original Code here:
# https://github.com/pytorch/examples/blob/master/mnist/main.py
from __future__ import print_function, division

import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms

import os
import torch
import pandas as pd
import numpy as np
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from torch.autograd import Variable
import torch.nn.functional as F
import sys
from dream_challenge_metrics import rmse, pearson, ci, f1, average_AUC
from torchvision import datasets
import torchvision.transforms as transforms
import itertools
import warnings
import math
from sklearn.metrics import f1_score, accuracy_score
from sklearn import preprocessing,metrics
import sklearn
import argparse
from ray.tune import Trainable
import torch.optim as optim
# from dream_challenge_models import FCModel1, FCModel2, FCPINNModel1, FCModel_3_Hidden_with_Modules, FCModel_3_Hidden, FCModel1_M
#from dream_challenge_models import FCModel1, FCModel2, FCPINNModel1, FCModel_3_Hidden_with_Modules, FCModel_3_Hidden, FCModel1_M
from dream_challenge_data_processing import TrainingValidationShuffledDataLoader, get_nfold_data_loader_dict
from dream_challenge_PINN_models import FC_PINNModel_2_2_2, FC_PINNModel_2_2_2_Modules, FC_PINNModel_2_3_2_Modules, FC_PINNModel_3_5_2_Modules#, FC_PINNModel_4_4_2,  FC_PINNModel_3_3_2



# Training settings
parser = argparse.ArgumentParser(description='Dream Challenge Ray Test 2')
parser.add_argument(
    '--batch-size',
    type=int,
    default=64,
    metavar='N',
    help='input batch size for training (default: 64)')
parser.add_argument(
    '--test-batch-size',
    type=int,
    default=1000,
    metavar='N',
    help='input batch size for testing (default: 1000)')
parser.add_argument(
    '--epochs',
    type=int,
    default=50,
    metavar='N',
    help='number of epochs to train (default: 10)')
parser.add_argument(
    '--lr',
    type=float,
    default=0.01,
    metavar='LR',
    help='learning rate (default: 0.01)')
parser.add_argument(
    '--momentum',
    type=float,
    default=0.5,
    metavar='M',
    help='SGD momentum (default: 0.5)')
parser.add_argument(
    '--no-cuda',
    action='store_true',
    default=False,
    help='disables CUDA training')
parser.add_argument(
    '--seed',
    type=int,
    default=1,
    metavar='S',
    help='random seed (default: 1)')
parser.add_argument(
    '--first-comp-layer',
    type=int,
    default=1024,
    metavar='F_COMP_LAYER',
    help='number of neurons in the first compound layer (default: 1024)')
parser.add_argument(
    '--second-comp-layer',
    type=int,
    default=1024,
    metavar='S_COMP_LAYER',
    help='number of neurons in the second compound layer (default: 1024)')
parser.add_argument(
    '--first-tar-layer',
    type=int,
    default=1024,
    metavar='F_TAR_LAYER',
    help='number of neurons in the first target layer (default: 1024)')
parser.add_argument(
    '--second-tar-layer',
    type=int,
    default=1024,
    metavar='S_TAR_LAYER',
    help='number of neurons in the second target layer (default: 1024)')
parser.add_argument(
    '--first-comb-layer',
    type=int,
    default=1024,
    metavar='F_COMB_LAYER',
    help='number of neurons in the first combined layer (default: 1024)')
parser.add_argument(
    '--second-comb-layer',
    type=int,
    default=1024,
    metavar='S_COMB_LAYER',
    help='number of neurons in the second combined layer (default: 1024)')
parser.add_argument(
    '--smoke-test', action="store_true", help="Finish quickly for testing")


def train_dream(args, config, reporter):
    vars(args).update(config)
    device = "cpu"
    use_gpu = torch.cuda.is_available()
    if use_gpu:
        print("GPU is available on this device!")
        device = "cuda"

    args.cuda = not args.no_cuda and torch.cuda.is_available()

    torch.manual_seed(args.seed)
    #if args.cuda:
    #    torch.cuda.manual_seed(args.seed)

    """
    train_loader = torch.utils.data.DataLoader(
        datasets.MNIST(
            '~/data',
            train=True,
            download=False,
            transform=transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize((0.1307, ), (0.3081, ))
            ])),
        batch_size=args.batch_size,
        shuffle=True,
        **kwargs)
    test_loader = torch.utils.data.DataLoader(
        datasets.MNIST(
            '~/data',
            train=False,
            transform=transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize((0.1307, ), (0.3081, ))
            ])),
        batch_size=args.test_batch_size,
        shuffle=True,
        **kwargs)
    """
    loader_fold_dict, number_of_comp_features, number_of_target_features = get_nfold_data_loader_dict(1,
                                                                                                      args.batch_size,
                                                                                                      ["ecfp4"],
                                                                                                      ["k-sep-bigrams"],
                                                                                                      "idg_comp_targ_uniq_inter_filtered_chembl24.csv",
                                                                                                      # "idg_comp_targ_uniq_inter_filtered.csv",
                                                                                                      "r")
    train_loader = loader_fold_dict[0][0]
    test_loader = loader_fold_dict[0][1]



    """

    model = Net()
    if args.cuda:
        model.cuda()

    optimizer = optim.SGD(
        model.parameters(), lr=args.lr, momentum=args.momentum)
    """
    # print(args)
    # print("Arguments:", args.first_comp_layer, args.second_comp_layer, args.first_tar_layer, args.second_tar_layer,
    #                                   args.first_comb_layer, args.second_comb_layer, args.lr, args.momentum)
    model = FC_PINNModel_2_2_2_Modules(number_of_comp_features, args.first_comp_layer, args.second_comp_layer,
                                       number_of_target_features, args.first_tar_layer, args.second_tar_layer,
                                       args.first_comb_layer, args.second_comb_layer, "r").to(device)
    optimizer = optim.SGD(
        model.parameters(), lr=args.lr, momentum=args.momentum)

    def train(epoch):
        """
        model.train()
        for batch_idx, (data, target) in enumerate(train_loader):
            if args.cuda:
                data, target = data.cuda(), target.cuda()
            optimizer.zero_grad()
            output = model(data)
            loss = F.nll_loss(output, target)
            loss.backward()
            optimizer.step()
        """
        model.train()

        total_training_loss = 0.0
        total_training_count = 0
        batch_number = 0

        for i, data in enumerate(train_loader):

            batch_number += 1
            # clear gradient DO NOT forget you fool!
            optimizer.zero_grad()

            # get the inputs
            comp_feature_vectors, target_feature_vectors, labels, compound_ids, target_ids, number_of_comp_features, number_of_target_features = data
            # wrap them in Variable
            comp_feature_vectors, target_feature_vectors, labels = Variable(comp_feature_vectors).to(
                device), Variable(
                target_feature_vectors).to(device), Variable(labels).to(device)
            # print(labels)

            inputs = None
            y_pred = None
            concat_models = [""]
            modeltype = None
            total_training_count += comp_feature_vectors.shape[0]
            if modeltype in concat_models:
                inputs = torch.cat((comp_feature_vectors, target_feature_vectors), 1)
                y_pred = model(inputs)
            else:
                # Forward pass: Compute predicted y by passing x to the model
                y_pred = model(comp_feature_vectors, target_feature_vectors)

            regression_classifier = "r"
            loss = None
            criterion = torch.nn.MSELoss()
            if regression_classifier == "r":
                loss = criterion(y_pred.squeeze(), labels)
            else:
                loss = criterion(y_pred.squeeze(), labels)

            total_training_loss += float(loss.item())
            loss.backward()
            optimizer.step()
        print("Total training loss:\t{}".format(total_training_loss))


    def test():
        """
        model.eval()
        test_loss = 0
        correct = 0
        with torch.no_grad():
            for data, target in test_loader:
                if args.cuda:
                    data, target = data.cuda(), target.cuda()
                output = model(data)
                # sum up batch loss
                test_loss += F.nll_loss(output, target, reduction='sum').item()
                # get the index of the max log-probability
                pred = output.argmax(dim=1, keepdim=True)
                correct += pred.eq(
                    target.data.view_as(pred)).long().cpu().sum()

        test_loss = test_loss / len(test_loader.dataset)
        accuracy = float(correct.item()) / len(test_loader.dataset)
        print(test_loss, accuracy)
        reporter(mean_loss=test_loss, mean_accuracy=accuracy)
        """
        model.eval()
        regression_classifier = "r"
        total_validation_loss = 0.0
        total_validation_count = 0
        validation_predictions = []
        validation_labels = []

        with torch.no_grad():  # torch.set_grad_enabled(False):
            for i, data in enumerate(test_loader):
                # print("Validation")
                val_comp_feature_vectors, val_target_feature_vectors, val_labels, val_compound_ids, val_target_ids, val_number_of_comp_features, val_number_of_target_features = data
                val_comp_feature_vectors, val_target_feature_vectors, val_labels = Variable(
                    val_comp_feature_vectors).to(
                    device), Variable(val_target_feature_vectors).to(device), Variable(val_labels).to(
                    device)
                # val_inputs = torch.cat((val_comp_feature_vectors, val_target_feature_vectors), 1)
                total_validation_count += val_comp_feature_vectors.shape[0]
                val_inputs = None
                val_y_pred = None
                concat_models = [""]
                # print(self.model.parameters)
                modeltype = None
                if modeltype in concat_models:
                    val_inputs = torch.cat((val_comp_feature_vectors, val_target_feature_vectors), 1)
                    val_y_pred = model(val_inputs)
                else:
                    val_y_pred = model(val_comp_feature_vectors, val_target_feature_vectors)

                # print(val_y_pred)
                criterion = torch.nn.MSELoss()
                loss_val = criterion(val_y_pred.squeeze(), val_labels)
                total_validation_loss += float(loss_val.item())

                for item in val_y_pred:
                    if regression_classifier == "r":
                        validation_predictions.append(float(item.data[0]))
                    else:
                        validation_predictions.append(int(float(item.data[0]) >= 0.5))
                for item in val_labels:
                    if regression_classifier == "r":
                        validation_labels.append(float(item.item()))
                    else:
                        validation_labels.append(int(item.data[0]))

        if regression_classifier == "r":
            rmse_score = rmse(np.asarray(validation_labels), np.asarray(
                validation_predictions))
            pearson_score = pearson(np.asarray(validation_labels), np.asarray(validation_predictions))
            # spearman_score = spearman(np.asarray(validation_labels), np.asarray(validation_predictions))
            # ci_score = ci(np.asarray(validation_labels), np.asarray(validation_predictions))
            f1_score = f1(np.asarray(validation_labels), np.asarray(validation_predictions))
            ave_auc_score = average_AUC(np.asarray(validation_labels), np.asarray(validation_predictions))

            print("Test RMSE:{}\tF1-Score:{}\tAverage_AUC:{}\tValidation Loss:{}".format(rmse_score, f1_score, ave_auc_score, total_validation_loss))
            # print("F1-Score:\t{}".format(f1_score))
            #print("Average_AUC:\t{}".format(ave_auc_score))

            #return {"RMSE": rmse_score, "F1-Score": f1_score}
        else:
            f1_score = sklearn.metrics.f1_score(validation_labels, validation_predictions)
            accuracy_score = sklearn.metrics.accuracy_score(validation_labels, validation_predictions)
            print("================================================================================")
            print("Fold:{}\tEpoch:{}\tTest F1:{}\tValidation Loss:{}".format(0 + 1, 0,
                                                                             f1_score,
                                                                             total_validation_loss))

            print("F1 Score:\t{}".format(f1_score))
            print("Accuracy:\t{}.".format(accuracy_score))
        reporter(mean_loss=total_validation_loss, mean_accuracy=f1_score)
    for epoch in range(1, args.epochs + 1):
        print("================================================================================")
        print("Epoch number:\t{}".format(epoch))
        print("Arguments:", args.first_comp_layer, args.second_comp_layer, args.first_tar_layer, args.second_tar_layer,
              args.first_comb_layer, args.second_comb_layer, args.lr, args.momentum)
        train(epoch)
        test()


if __name__ == "__main__":
    # datasets.MNIST('~/data', train=True, download=True)
    args = parser.parse_args()

    import numpy as np
    import ray
    from ray import tune
    from ray.tune.schedulers import HyperBandScheduler

    ray.init()
    sched = HyperBandScheduler(
        time_attr="training_iteration",
        reward_attr="neg_mean_loss",
        max_t=400)
    tune.register_trainable("train_dream",
                            lambda cfg, rprtr: train_dream(args, cfg, rprtr))
    tune.run_experiments(
        {
            "exp": {
                "stop": {
                    # "neg_mean_loss": 0.0,
                    "training_iteration": 50 if args.smoke_test else 50,
                },
                "resources_per_trial": {
                    "cpu": 1,
                    "gpu": 1
                },
                "run": "train_dream",
                "num_samples": 1 if args.smoke_test else 20,
                # "checkpoint_at_end": True,
                "config": {
                    "args": args,
                    "lr": tune.sample_from(
                        lambda spec: np.random.uniform(0.001, 0.1)),
                    "momentum": tune.sample_from(
                        lambda spec: np.random.uniform(0.1, 0.9)),

                    "first_comp_layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048, 4096])),
                    "second_comp_layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048, 4096])),
                    "first_tar_layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048, 4096])),
                    "second_tar_layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048, 4096])),
                    "first_comb_layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048, 4096])),
                    "second_comb_layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048, 4096])),

                }

            }
        },
        verbose=0,
        scheduler=sched)
