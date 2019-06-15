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

    train_loader, validation_loader, test_loader = None, None, None
    if train_val_test:
        train_loader, validation_loader, test_loader = get_cnn_train_test_full_training_data_loader(training_dataset, comp_feature_list, tar_feature_list, batch_size, train_val_test)
    else:
        train_loader, test_loader = get_cnn_train_test_full_training_data_loader(training_dataset,
                                                                                                 comp_feature_list,
                                                                                                 tar_feature_list,
                                                                                                 batch_size,
                                                                                                 train_val_test)

    model = CompFCNNTarCNN2(tar_feature_list, 1024, tar_num_of_last_neurons, comp_hidden_lst[0], comp_hidden_lst[1], fc1, fc2, drop_prob=0.5).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=learn_rate)

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
        total_training_loss,  = 0.0
        total_training_count = 0

        batch_number = 0

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
            y_pred = None
            target_feature_vectors = target_feature_vectors/210.0
            total_training_count += comp_feature_vectors.shape[0]

            y_pred = model(comp_feature_vectors, target_feature_vectors).to(device)

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
        total_test_loss= 0.0
        total_test_count = 0

        total_test_loss = 0.0
        total_test_count = 0
        test_predictions = []
        test_labels = []

        with torch.no_grad():  # torch.set_grad_enabled(False):
            for i, data in enumerate(test_loader):
                test_comp_feature_vectors, test_target_feature_vectors, tst_labels, test_compound_ids, test_target_ids = data
                test_comp_feature_vectors, test_target_feature_vectors, tst_labels = Variable(
                    test_comp_feature_vectors).to(
                    device), Variable(
                    test_target_feature_vectors).to(device), Variable(tst_labels).to(device)

                test_target_feature_vectors = test_target_feature_vectors / 210.0
                total_test_count += test_comp_feature_vectors.shape[0]

                # if test_comp_feature_vectors.shape[0] == batch_size:
                test_inputs = None
                test_y_pred = None
                test_y_pred = model(test_comp_feature_vectors, test_target_feature_vectors)
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
        reporter(mean_loss=total_test_loss)

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
