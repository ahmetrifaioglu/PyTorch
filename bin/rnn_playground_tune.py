from __future__ import print_function, division
import argparse
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
from ray.tune import Trainable

parser = argparse.ArgumentParser(description='Dream  Example')

# general hyper-parameters
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
    default=20,
    metavar='N',
    help='number of epochs to train (default: 10)')
parser.add_argument(
    '--lr',
    type=float,
    default=0.01,
    metavar='LR',
    help='learning rate (default: 0.01)')
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

# model specific parameters
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
    '--vocab-size',
    type=int,
    default=8001,
    metavar='VOCAB_SIZE',
    help='vocabulary size (default: 8001)')
parser.add_argument(
    '--output-size',
    type=int,
    default=256,
    metavar='OUTPUT_SIZE',
    help='rnn output size (default: 256)')
parser.add_argument(
    '--embedding-dim',
    type=int,
    default=200,
    metavar='EMBEDDING_DIM',
    help='embedding dim (default: 200)')
parser.add_argument(
    '--hidden-dim',
    type=int,
    default=256,
    metavar='HIDDEN_DIM',
    help='hidden dim (default: 256)')
parser.add_argument(
    '--n-rnn-layers',
    type=int,
    default=2,
    metavar='N-RNN-LAYERS',
    help='number of rnn layers (default: 2)')
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




"""
parser.add_argument(
    '--momentum',
    type=float,
    default=0.5,
    metavar='M',
    help='SGD momentum (default: 0.5)')
"""

warnings.filterwarnings("ignore")


def train_dream(args, config, reporter):
    # print(config)
    vars(args).update(config)
    device = "cpu"
    use_gpu = torch.cuda.is_available()
    if use_gpu:
        print("GPU is available on this device!")
        device = "cuda"
    print(device)
    args.cuda = not args.no_cuda and torch.cuda.is_available()

    torch.manual_seed(args.seed)
    #if args.cuda:
    #    torch.cuda.manual_seed(args.seed)

    loader_fold_dict, number_of_comp_features, number_of_target_features = get_nfold_data_loader_dict(1,
                                                                                                      args.batch_size,
                                                                                                      ["ecfp4"],
                                                                                                      ["trigramencodings1000"],
                                                                                                      "idg_comp_targ_uniq_inter_filtered.csv",
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
    print("Arguments:", number_of_comp_features, args.first_comp_layer, args.second_comp_layer, args.vocab_size,
                                args.output_size, args.embedding_dim, args.hidden_dim, args.n_rnn_layers,
                                args.first_comb_layer, args.second_comb_layer)
    model = CompFCNNTarRNN(number_of_comp_features, args.first_comp_layer, args.second_comp_layer, args.vocab_size,
                           args.output_size, args.embedding_dim, args.hidden_dim, args.n_rnn_layers,
                           args.first_comb_layer, args.second_comb_layer).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)
    criterion = torch.nn.MSELoss()

    def train():
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
        h = model.init_hidden(args.batch_size)
        model.train()

        total_training_loss = 0.0
        total_training_count = 0
        batch_number = 0

        for i, data in enumerate(train_loader):

            batch_number += 1
            h = tuple([each.data for each in h])
            # print(h)
            # clear gradient DO NOT forget you fool!
            optimizer.zero_grad()


            # get the inputs
            comp_feature_vectors, target_feature_vectors, labels, compound_ids, target_ids, number_of_comp_features, number_of_target_features = data
            # wrap them in Variable
            comp_feature_vectors, target_feature_vectors, labels = Variable(comp_feature_vectors).to(device), Variable(
                target_feature_vectors).to(device), Variable(labels).to(device)
            # print(comp_feature_vectors.shape, target_feature_vectors.shape)

            if comp_feature_vectors.shape[0] == args.batch_size:
                inputs = None
                y_pred = None
                # print("gird")
                total_training_count += comp_feature_vectors.shape[0]

                y_pred, h = model(comp_feature_vectors, target_feature_vectors, h)

                loss = criterion(y_pred.squeeze(), labels)

                total_training_loss += float(loss.item())
                loss.backward()
                optimizer.step()

        print("Total training loss:\t{}".format(total_training_loss))

    def test():
        model.eval()
        regression_classifier = "r"
        total_validation_loss = 0.0
        total_validation_count = 0
        validation_predictions = []
        validation_labels = []

        h = model.init_hidden(args.batch_size)

        with torch.no_grad():  # torch.set_grad_enabled(False):
            for i, data in enumerate(test_loader):
                # print("Validation")
                val_comp_feature_vectors, val_target_feature_vectors, val_labels, val_compound_ids, val_target_ids, val_number_of_comp_features, val_number_of_target_features = data
                val_comp_feature_vectors, val_target_feature_vectors, val_labels = Variable(
                    val_comp_feature_vectors).to(device), Variable(val_target_feature_vectors).to(device), Variable(val_labels).to(device)
                total_validation_count += val_comp_feature_vectors.shape[0]

                if val_comp_feature_vectors.shape[0] == args.batch_size:
                    val_inputs = None
                    val_y_pred = None

                    val_y_pred, h = model(val_comp_feature_vectors, val_target_feature_vectors, h)
                    loss_val = criterion(val_y_pred.squeeze(), val_labels)
                    total_validation_loss += float(loss_val.item())

                    for item in val_y_pred:
                        validation_predictions.append(float(item.item()))

        print( len(validation_predictions), len(validation_labels))
        if regression_classifier == "r":
            rmse_score = rmse(np.asarray(validation_labels), np.asarray(
                validation_predictions))
            pearson_score = pearson(np.asarray(validation_labels), np.asarray(validation_predictions))
            f1_score = f1(np.asarray(validation_labels), np.asarray(validation_predictions))
            ave_auc_score = average_AUC(np.asarray(validation_labels), np.asarray(validation_predictions))

            print("Test RMSE:{}\tF1-Score:{}\tAverage_AUC:{}\tValidation Loss:{}".format(rmse_score, f1_score, ave_auc_score, total_validation_loss))

        reporter(mean_loss=total_validation_loss, mean_accuracy=f1_score)
    for epoch in range(1, args.epochs + 1):
        print("================================================================================")
        print("Epoch number:\t{}".format(epoch))
        print("Arguments:", args.batch_size, args.epochs, args.lr, args.first_comp_layer, args.second_comp_layer,
              args.output_size, args.embedding_dim, args.hidden_dim, args.n_rnn_layers, args.first_comp_layer,
              args.second_comb_layer)
        train()
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
                    "training_iteration": 20 if args.smoke_test else 20,
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

                    "batch_size": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256])),
                    "epochs": tune.sample_from(
                        lambda spec: np.random.choice([10, 20, 40])),
                    "lr": tune.sample_from(
                        lambda spec: np.random.uniform(0.001, 0.1)),
                    "first_comp_layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048, 4096])),
                    "second_comp_layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048, 4096])),
                    "output_size": tune.sample_from(
                        lambda spec: np.random.choice([128, 256, 512])),
                    "embedding_dim": tune.sample_from(
                        lambda spec: np.random.choice([100, 200, 400])),
                    "hidden_dim": tune.sample_from(
                        lambda spec: np.random.choice([128, 256, 512, 1024])),
                    "rnn_layers": tune.sample_from(
                        lambda spec: np.random.choice([1, 2, 3])),
                    "first_comb_layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048])),
                    "second_comb_layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048])),

                }

            }
        },
        verbose=0,
        scheduler=sched)

