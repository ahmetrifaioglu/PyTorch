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

parser = argparse.ArgumentParser(description='Dream  Example')
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
    default=10,
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


warnings.filterwarnings("ignore")


class TrainDream(Trainable):
    def _setup(self, config):
        args = config.pop("args")
        vars(args).update(config)
        args.cuda = not args.no_cuda and torch.cuda.is_available()
        print(args.cuda)
        torch.manual_seed(args.seed)
        if args.cuda:
            torch.cuda.manual_seed(args.seed)
        self.device = "cpu"
        use_gpu = torch.cuda.is_available()
        if use_gpu:
            print("GPU is available on this device!")
            self.device = "cuda"
        else:
            print("CPU is available on this device!")

        kwargs = {'num_workers': 1, 'pin_memory': True} if args.cuda else {}

        loader_fold_dict, number_of_comp_features, number_of_target_features = get_nfold_data_loader_dict(1,
                                                                                                          args.batch_size,
                                                                                                          ["ecfp4"],
                                                                                                          ["k-sep-bigrams"],
                                                                                                          "idg_comp_targ_uniq_inter_filtered_chembl24.csv",
                                                                                                          #"idg_comp_targ_uniq_inter_filtered.csv",
                                                                                                          "r")
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




if __name__ == '__main__':
    args = parser.parse_args()

    import numpy as np
    import ray
    from ray import tune
    from ray.tune.schedulers import HyperBandScheduler

    ray.init(num_gpus=1)
    sched = HyperBandScheduler(
        time_attr="training_iteration")#, reward_attr="neg_mean_loss")
    tune.run_experiments(
        {
            "exp": {
                "stop": {
                    #"neg_mean_loss": 0.0,
                    "training_iteration": 20 if args.smoke_test else 20,
                },
                "resources_per_trial": {
                    "cpu": 1,
                    "gpu": 1
                },
                "run": TrainDream,
                "num_samples": 1 if args.smoke_test else 20,
                # "checkpoint_at_end": True,
                "config": {
                    "args": args,
                    "lr": tune.sample_from(
                        lambda spec: np.random.uniform(0.001, 0.1)),
                    "momentum": tune.sample_from(
                        lambda spec: np.random.uniform(0.1, 0.9)),

                    "first-comp-layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048, 4096])),
                    "second-comp-layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048, 4096])),
                    "first-tar-layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048, 4096])),
                    "second-tar-layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048, 4096])),
                    "first-comb-layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048, 4096])),
                    "second-comb-layer": tune.sample_from(
                        lambda spec: np.random.choice([32, 64, 128, 256, 512, 1024, 2048, 4096])),

                }

            }
        },
        verbose=0,
        scheduler=sched)

