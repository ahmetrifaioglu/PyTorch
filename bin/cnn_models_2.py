import torch
import torch.nn as nn
import torch.nn.functional as F
from operator import itemgetter

use_gpu = torch.cuda.is_available()
import numpy as np
device = "cpu"
if use_gpu:
    device = "cuda"

class FC_2_Layer(torch.nn.Module):

    def __init__(self, number_of_inputs, neuron_l1, neuron_l2, drop_rate):
        super(FC_2_Layer, self).__init__()
        self.l1 = torch.nn.Linear(number_of_inputs, neuron_l1)
        self.bn1 = torch.nn.BatchNorm1d(num_features=neuron_l1)
        self.l2 = torch.nn.Linear(neuron_l1, neuron_l2)
        self.bn2 = torch.nn.BatchNorm1d(num_features=neuron_l2)
        self.relu = torch.nn.ReLU()
        self.drop_rate = drop_rate


    def forward(self, x):
        out1 = F.dropout(self.relu(self.bn1(self.l1(x))), self.drop_rate)
        out2 = F.dropout(self.relu(self.bn2(self.l2(out1))), self.drop_rate)
        return out2

class CNNModule(torch.nn.Module):

    def __init__(self, num_of_neurons):
        super(CNNModule, self).__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=2, out_channels=8, kernel_size=5)
        self.conv2 = torch.nn.Conv2d(in_channels=8, out_channels=16, kernel_size=5)
        self.conv3 = torch.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3)
        self.conv4 = torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3)
        self.pool = torch.nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc1 = torch.nn.Linear(53824, num_of_neurons)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = F.relu(self.conv3(x))
        x = self.pool(x)
        x = F.relu(self.conv4(x))
        x = self.pool(x)
        x = x.view(-1, 53824)
        x = F.relu(self.fc1(x))
        return x


class CompFCNNTarCNN(nn.Module):
    def __init__(self, number_of_comp_features, num_of_tar_neurons, comp_l1, comp_l2, fc_l1, fc_l2, drop_prob=0.5):
        super(CompFCNNTarCNN, self).__init__()
        self.layer_2_comp = FC_2_Layer(number_of_comp_features, comp_l1, comp_l2, drop_prob)
        self.cnn_flattened_layer = CNNModule(num_of_tar_neurons)
        # dropout layer
        self.dropout = nn.Dropout(0.3)
        self.layer_2_combined = FC_2_Layer(comp_l2 + num_of_tar_neurons, fc_l1, fc_l2, drop_prob)
        self.output = None

        self.output = torch.nn.Linear(fc_l2, 1)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()
        self.softmax = torch.nn.Softmax()
        # self.drop_rate = drop_rate
        self.r_c = "r"


    def forward(self, x_comp, x_tar):
        out2_comp = self.layer_2_comp.forward(x_comp)
        out_tar = self.cnn_flattened_layer(x_tar)
        combined_layer = torch.cat((out2_comp, out_tar), 1)
        out_combined = self.layer_2_combined.forward(combined_layer)
        y_pred = None

        if self.r_c == "r":
            y_pred = self.output(out_combined)
        else:
            y_pred = self.softmax(self.output(out_combined))

        return y_pred
