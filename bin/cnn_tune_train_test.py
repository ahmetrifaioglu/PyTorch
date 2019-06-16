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
parser = argparse.ArgumentParser(description='')
parser.add_argument(
    #'--comp-hidden-layer-neurons',
    '--chln',
    type=str,
    default="512_512",
    metavar='CHLN',
    help='number of neurons in compound hidden layers (default: 512_512)')
parser.add_argument(
    #'--target-layer-neurons-after-flattened',
    '--tlnaf',
    type=int,
    default=512,
    metavar='TFFLAF',
    help='number of neurons after flattening target conv layers (default: 512)')
parser.add_argument(
    '--lhln',
    type=str,
    default="256_256",
    metavar='LHLN',
    help='number of neurons in last two hidden layers before output layer (default: 256_256)')
parser.add_argument(
    '--lr',
    type=float,
    default=0.01,
    metavar='LR',
    help='learning rate (default: 0.01)')
parser.add_argument(
    # '--batch-size',
    '--bs',
    type=int,
    default=32,
    metavar='BS',
    help='batch size (default: 32)')
parser.add_argument(
    # '--training-data',
    '--td',
    type=str,
    default="PDBBind",
    metavar='TD',
    help='the name of the training dataset (default: PDBBind)')

parser.add_argument(
    # '--compound-features',
    '--cf',
    type=str,
    default="ecfp4",
    metavar='CF',
    help='compound features separated by underscore character (default: ecfp4)')
parser.add_argument(
    # '--target-features',
    '--tf',
    type=str,
    default="sequencematrix500",
    metavar='TF',
    help='target features separated by underscore character (default: sequencematrix500)')

parser.add_argument(
    # '--train-validation-test',
    '--tvt',
    type=int,
    default=0,
    metavar='TVT',
    help='Determines if data is divided into train-validation-test (default: 0)')

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
                    "training_iteration": 100 if args.smoke_test else 100,
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
