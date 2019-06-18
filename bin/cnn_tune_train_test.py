# Original Code here:
# https://github.com/pytorch/examples/blob/master/mnist/main.py
from __future__ import print_function, division
import os
import sys
import argparse
import pandas as pd
import numpy as np
import itertools
import warnings
import math
import sklearn
from sklearn import preprocessing,metrics
from sklearn.metrics import f1_score, accuracy_score
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torch.autograd import Variable
from torchvision import datasets
import torchvision.transforms as transforms
from ray.tune import Trainable
from evaluation_metrics import rmse, pearson, spearman, ci, f1, average_AUC, mse
from cnn_models import CompFCNNTarCNN2, CompFCNNTarCNN
from evaluation_metrics import r_squared_error, get_rm2, squared_error_zero, get_k, get_cindex, get_aupr
from cnn_data_processing import get_cnn_test_val_folds_train_data_loader, get_cnn_train_test_full_training_data_loader



# Training settings
parser = argparse.ArgumentParser(description='dasdsa')
parser.add_argument(
    '--chln',
    type=list,
    default=[512, 512],
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
    type=list,
    default=[256, 256],
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
    type=bool,
    default=True,
    metavar='TVT',
    help='Determines if data is divided into train-validation-test (default: True)')

parser.add_argument(
    '--seed',
    type=int,
    default=1,
    metavar='S',
    help='random seed (default: 1)')

parser.add_argument(
    '--epochs',
    type=int,
    default=100,
    metavar='E',
    help='num of epochs (default: 100)')

parser.add_argument(
    '--smoke-test', action="store_true", help="Finish quickly for testing")

args = parser.parse_args()
print(args)
train_loader, validation_loader, test_loader = None, None, None
if args.tvt:
    train_loader, validation_loader, test_loader = get_cnn_train_test_full_training_data_loader(args.td, [args.cf],
                                                                                                [args.tf], args.bs,
                                                                                                args.tvt)
else:
    train_loader, test_loader = get_cnn_train_test_full_training_data_loader(args.td, [args.cf], [args.tf], args.bs,
                                                                             args.tvt)

def train_dream(args, config, reporter):
    vars(args).update(config)
    device = "cpu"
    use_gpu = torch.cuda.is_available()
    if use_gpu:
        print("GPU is available on this device!")
        device = "cuda"

    comp_hidden_lst = [int(num) for num in args.chln.split("_")]
    fc1, fc2 = [int(num) for num in args.lhln.split("_")]
    # args.cuda = not args.no_cuda and torch.cuda.is_available()

    torch.manual_seed(args.seed)
    # print(args)


    model = CompFCNNTarCNN2([args.tf], 1024, args.tlnaf, comp_hidden_lst[0], comp_hidden_lst[1], fc1, fc2, drop_prob=0.5).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)

    def train(epoch):
        model.train()
        total_training_loss  = 0.0
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
            criterion = torch.nn.MSELoss()
            loss = criterion(y_pred.squeeze(), labels)

            total_training_loss += float(loss.item())
            loss.backward()
            optimizer.step()

        print("Total training loss:\t{}".format(total_training_loss))


    def test():
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
                criterion = torch.nn.MSELoss()
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
        # print("Arguments:", args)
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
        max_t=100)
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
                    "gpu": 0
                },
                "run": "train_dream",
                "num_samples": 1 if args.smoke_test else 20,
                # "checkpoint_at_end": True,
                "config": {
                    "args": args,

                    "chln": tune.sample_from(
                        lambda spec: np.random.choice(["256_256", "512_256", "512_512", "1024_512", "1024_256", "1024_1024"])),

                    "tlnaf": tune.sample_from(
                        lambda spec: np.random.choice([64, 128, 256, 512, 1024])),

                    "lhln": tune.sample_from(
                        lambda spec: np.random.choice(["128_128", "256_256", "512_512", "1024_1024"])),

                    "lr": tune.sample_from(
                        lambda spec: np.random.uniform(0.0001, 0.1)),

                    "bs": tune.sample_from(
                        lambda spec: np.random.choice([16, 32])),

                    "td": tune.sample_from(
                        lambda spec: np.random.choice(["PDBBind"])),

                    "cf": tune.sample_from(
                        lambda spec: np.random.choice(["ecfp4"])),

                    "tf": tune.sample_from(
                        lambda spec: np.random.choice(["sequencematrix500"])),

                    "tvt": tune.sample_from(
                        lambda spec: np.random.choice([True])),
                }

            }
        },
        verbose=0,
        scheduler=sched)
