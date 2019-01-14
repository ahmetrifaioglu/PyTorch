import torch
import torch.nn.functional as F


class FC_1_Layer(torch.nn.Module):

    def __init__(self, number_of_inputs):
        # In the constructor we instantiate two nn.Linear module
        super(FC_1_Layer, self).__init__()

        self.l1 = torch.nn.Linear(number_of_inputs, 1024)
        self.bn1 = torch.nn.BatchNorm1d(num_features=1024)
        self.relu = torch.nn.ReLU()
        self.drop_rate = 0.5

    def forward(self, x):

        # In the forward function we accept a Variable of input data and we must return
        # a Variable of output data. We can use Modules defined in the constructor as
        # well as arbitrary operators on Variables.

        out1 = F.dropout(self.relu(self.bn1(self.l1(x))), self.drop_rate)
        # print("BURAYA ")
        return out1

class FCModel1_M(torch.nn.Module):

    def __init__(self, number_of_features):
        # In the constructor we instantiate two nn.Linear module
        super(FCModel1_M, self).__init__()

        self.first_layer = FC_1_Layer(number_of_features)
        self.l2 = torch.nn.Linear(1024, 400)
        self.bn2 = torch.nn.BatchNorm1d(num_features=400)
        self.l3 = torch.nn.Linear(400, 1)
        self.relu = torch.nn.ReLU()

    def forward(self, x):

        # In the forward function we accept a Variable of input data and we must return
        # a Variable of output data. We can use Modules defined in the constructor as
        # well as arbitrary operators on Variables.

        out1 = self.first_layer(x)
        out2 = self.l2(out1)
        out2 = self.bn2(out2)
        out2 = self.relu(out2)
        out2 = F.dropout(out2, 0.5)
        y_pred = self.l3(out2)
        # print(y_pred)
        return y_pred


class FCModel1(torch.nn.Module):

    def __init__(self, number_of_features):
        # In the constructor we instantiate two nn.Linear module
        super(FCModel1, self).__init__()

        self.l1 = torch.nn.Linear(number_of_features, 1024)
        self.bn1 = torch.nn.BatchNorm1d(num_features=1024)
        self.l2 = torch.nn.Linear(1024, 400)
        self.bn2 = torch.nn.BatchNorm1d(num_features=400)
        self.l3 = torch.nn.Linear(400, 1)
        self.relu = torch.nn.ReLU()

    def forward(self, x):

        # In the forward function we accept a Variable of input data and we must return
        # a Variable of output data. We can use Modules defined in the constructor as
        # well as arbitrary operators on Variables.

        out1 = self.l1(x)
        out1 = self.bn1(out1)
        out1 = self.relu(out1)
        out1 = F.dropout(out1, 0.5)

        out2 = self.l2(out1)
        out2 = self.bn2(out2)
        out2 = self.relu(out2)
        out2 = F.dropout(out2, 0.5)

        # out1 = self.relu(self.l1(x))
        # out1 = F.dropout(out1,0.2)
        # out2 = self.relu(self.l2(out1))
        # out2 = F.dropout(out2, 0.2)
        y_pred = self.l3(out2)
        # print(y_pred)
        return y_pred

class FC_2_Layer(torch.nn.Module):

    def __init__(self, number_of_inputs, neuron_l1, neuron_l2, drop_rate):
        # In the constructor we instantiate two nn.Linear module
        super(FC_2_Layer, self).__init__()

        self.l1 = torch.nn.Linear(number_of_inputs, neuron_l1)
        self.bn1 = torch.nn.BatchNorm1d(num_features=neuron_l1)
        self.l2 = torch.nn.Linear(neuron_l1, neuron_l2)
        self.bn2 = torch.nn.BatchNorm1d(num_features=neuron_l2)
        self.relu = torch.nn.ReLU()
        self.drop_rate = drop_rate

    def forward(self, x):

        # In the forward function we accept a Variable of input data and we must return
        # a Variable of output data. We can use Modules defined in the constructor as
        # well as arbitrary operators on Variables.

        out1 = F.dropout(self.relu(self.bn1(self.l1(x))), self.drop_rate)
        out2 = F.dropout(self.relu(self.bn2(self.l2(out1))), self.drop_rate)
        # print("BURAYA ")
        return out2

class FCModel_3_Hidden_with_Modules(torch.nn.Module):

    def __init__(self, number_of_features, neuron_l1, neuron_l2, neuron_l3, drop_rate):
        # In the constructor we instantiate two nn.Linear module
        super(FCModel_3_Hidden_with_Modules, self).__init__()

        self.first_2_layer = FC_2_Layer(number_of_features, neuron_l1, neuron_l2, drop_rate)
        self.l3 = torch.nn.Linear(neuron_l2, neuron_l3)
        self.bn3 = torch.nn.BatchNorm1d(num_features=neuron_l3)

        self.lout = torch.nn.Linear(neuron_l3, 1)
        self.relu = torch.nn.ReLU()
        self.drop_rate = drop_rate

    def forward(self, x):

        # In the forward function we accept a Variable of input data and we must return
        # a Variable of output data. We can use Modules defined in the constructor as
        # well as arbitrary operators on Variables.

        out2 = self.first_2_layer(x)
        out3 = F.dropout(self.relu(self.bn3(self.l3(out2))), self.drop_rate)

        y_pred = self.lout(out3)

        return y_pred


class FCModel_2_Hidden(torch.nn.Module):

    def __init__(self, number_of_features, neuron_l1, neuron_l2, drop_rate):
        # In the constructor we instantiate two nn.Linear module
        super(FCModel_2_Hidden, self).__init__()

        self.l1 = torch.nn.Linear(number_of_features, neuron_l1)
        self.bn1 = torch.nn.BatchNorm1d(num_features=neuron_l1)
        self.l2 = torch.nn.Linear(neuron_l1, neuron_l2)
        self.bn2 = torch.nn.BatchNorm1d(num_features=neuron_l2)
        self.l3 = torch.nn.Linear(neuron_l2, 1)
        self.relu = torch.nn.ReLU()
        self.drop_rate = drop_rate

    def forward(self, x):

        # In the forward function we accept a Variable of input data and we must return
        # a Variable of output data. We can use Modules defined in the constructor as
        # well as arbitrary operators on Variables.

        out1 = F.dropout(self.relu(self.bn1(self.l1(x))), self.drop_rate)
        out2 = F.dropout(self.relu(self.bn2(self.l2(out1))), self.drop_rate)

        y_pred = self.l3(out2)

        return y_pred

class FCModel_3_Hidden(torch.nn.Module):

    def __init__(self, number_of_features, neuron_l1, neuron_l2, neuron_l3, drop_rate):
        # In the constructor we instantiate two nn.Linear module
        super(FCModel_3_Hidden, self).__init__()

        self.l1 = torch.nn.Linear(number_of_features, neuron_l1)
        self.bn1 = torch.nn.BatchNorm1d(num_features=neuron_l1)
        self.l2 = torch.nn.Linear(neuron_l1, neuron_l2)
        self.bn2 = torch.nn.BatchNorm1d(num_features=neuron_l2)
        self.l3 = torch.nn.Linear(neuron_l2, neuron_l3)
        self.bn3 = torch.nn.BatchNorm1d(num_features=neuron_l3)

        self.lout = torch.nn.Linear(neuron_l3, 1)
        self.relu = torch.nn.ReLU()
        self.drop_rate = drop_rate

    def forward(self, x):

        # In the forward function we accept a Variable of input data and we must return
        # a Variable of output data. We can use Modules defined in the constructor as
        # well as arbitrary operators on Variables.

        out1 = F.dropout(self.relu(self.bn1(self.l1(x))), self.drop_rate)
        out2 = F.dropout(self.relu(self.bn2(self.l2(out1))), self.drop_rate)
        out3 = F.dropout(self.relu(self.bn3(self.l3(out2))), self.drop_rate)

        y_pred = self.lout(out3)

        return y_pred


class FCModel_4_Hidden(torch.nn.Module):

    def __init__(self, number_of_features, neuron_l1, neuron_l2, drop_rate):
        # In the constructor we instantiate two nn.Linear module
        super(FCModel_4_Hidden, self).__init__()

        self.l1 = torch.nn.Linear(number_of_features, neuron_l1)
        self.bn1 = torch.nn.BatchNorm1d(num_features=neuron_l1)
        self.l2 = torch.nn.Linear(neuron_l1, neuron_l2)
        self.bn2 = torch.nn.BatchNorm1d(num_features=neuron_l2)
        self.l3 = torch.nn.Linear(neuron_l2, neuron_l3)
        self.bn3 = torch.nn.BatchNorm1d(num_features=neuron_l3)
        self.l4 = torch.nn.Linear(neuron_l3, neuron_l4)
        self.bn4 = torch.nn.BatchNorm1d(num_features=neuron_l4)

        self.lout = torch.nn.Linear(neuron_l4, 1)
        self.relu = torch.nn.ReLU()
        self.drop_rate = drop_rate

    def forward(self, x):
        # In the forward function we accept a Variable of input data and we must return
        # a Variable of output data. We can use Modules defined in the constructor as
        # well as arbitrary operators on Variables.

        out1 = F.dropout(self.relu(self.bn1(self.l1(x))), self.drop_rate)
        out2 = F.dropout(self.relu(self.bn2(self.l2(out1))), self.drop_rate)
        out3 = F.dropout(self.relu(self.bn3(self.l3(out2))), self.drop_rate)
        out4 = F.dropout(self.relu(self.bn4(self.l4(out3))), self.drop_rate)

        y_pred = self.lout(out4)

        return y_pred


class FCModel_5_Hidden(torch.nn.Module):

    def __init__(self, number_of_features, neuron_l1, neuron_l2, drop_rate):
        # In the constructor we instantiate two nn.Linear module
        super(FCModel_5_Hidden, self).__init__()

        self.l1 = torch.nn.Linear(number_of_features, neuron_l1)
        self.bn1 = torch.nn.BatchNorm1d(num_features=neuron_l1)
        self.l2 = torch.nn.Linear(neuron_l1, neuron_l2)
        self.bn2 = torch.nn.BatchNorm1d(num_features=neuron_l2)
        self.l3 = torch.nn.Linear(neuron_l2, neuron_l3)
        self.bn3 = torch.nn.BatchNorm1d(num_features=neuron_l3)
        self.l4 = torch.nn.Linear(neuron_l3, neuron_l4)
        self.bn4 = torch.nn.BatchNorm1d(num_features=neuron_l4)
        self.l5 = torch.nn.Linear(neuron_l4, neuron_l5)
        self.bn5 = torch.nn.BatchNorm1d(num_features=neuron_l5)

        self.lout = torch.nn.Linear(neuron_l5, 1)
        self.relu = torch.nn.ReLU()
        self.drop_rate = drop_rate

    def forward(self, x):
        # In the forward function we accept a Variable of input data and we must return
        # a Variable of output data. We can use Modules defined in the constructor as
        # well as arbitrary operators on Variables.

        out1 = F.dropout(self.relu(self.bn1(self.l1(x))), self.drop_rate)
        out2 = F.dropout(self.relu(self.bn2(self.l2(out1))), self.drop_rate)
        out3 = F.dropout(self.relu(self.bn3(self.l3(out2))), self.drop_rate)
        out4 = F.dropout(self.relu(self.bn4(self.l4(out3))), self.drop_rate)
        out5 = F.dropout(self.relu(self.bn5(self.l5(out4))), self.drop_rate)

        y_pred = self.lout(out5)

        return y_pred

class FCModel_6_Hidden(torch.nn.Module):

    def __init__(self, number_of_features, neuron_l1, neuron_l2, drop_rate):
        # In the constructor we instantiate two nn.Linear module
        super(FCModel_6_Hidden, self).__init__()

        self.l1 = torch.nn.Linear(number_of_features, neuron_l1)
        self.bn1 = torch.nn.BatchNorm1d(num_features=neuron_l1)
        self.l2 = torch.nn.Linear(neuron_l1, neuron_l2)
        self.bn2 = torch.nn.BatchNorm1d(num_features=neuron_l2)
        self.l3 = torch.nn.Linear(neuron_l2, neuron_l3)
        self.bn3 = torch.nn.BatchNorm1d(num_features=neuron_l3)
        self.l4 = torch.nn.Linear(neuron_l3, neuron_l4)
        self.bn4 = torch.nn.BatchNorm1d(num_features=neuron_l4)
        self.l5 = torch.nn.Linear(neuron_l4, neuron_l5)
        self.bn5 = torch.nn.BatchNorm1d(num_features=neuron_l5)
        self.l6 = torch.nn.Linear(neuron_l5, neuron_l6)
        self.bn6 = torch.nn.BatchNorm1d(num_features=neuron_l6)

        self.lout = torch.nn.Linear(neuron_l6, 1)
        self.relu = torch.nn.ReLU()
        self.drop_rate = drop_rate

    def forward(self, x):
        # In the forward function we accept a Variable of input data and we must return
        # a Variable of output data. We can use Modules defined in the constructor as
        # well as arbitrary operators on Variables.

        out1 = F.dropout(self.relu(self.bn1(self.l1(x))), self.drop_rate)
        out2 = F.dropout(self.relu(self.bn2(self.l2(out1))), self.drop_rate)
        out3 = F.dropout(self.relu(self.bn3(self.l3(out2))), self.drop_rate)
        out4 = F.dropout(self.relu(self.bn4(self.l4(out3))), self.drop_rate)
        out5 = F.dropout(self.relu(self.bn5(self.l5(out4))), self.drop_rate)
        out6 = F.dropout(self.relu(self.bn6(self.l6(out5))), self.drop_rate)

        y_pred = self.lout(out6)

        return y_pred




class FCModel2(torch.nn.Module):

    def __init__(self, number_of_features):

        # In the constructor we instantiate two nn.Linear module

        super(FCModel2, self).__init__()
        self.l1 = torch.nn.Linear(number_of_features, 2048)
        self.bn1 = torch.nn.BatchNorm1d(num_features=2048)
        self.l2 = torch.nn.Linear(2048, 1024)
        self.bn2 = torch.nn.BatchNorm1d(num_features=1024)
        self.l3 = torch.nn.Linear(1024, 256)
        self.bn3 = torch.nn.BatchNorm1d(num_features=256)
        self.l4 = torch.nn.Linear(256, 64)
        self.bn4 = torch.nn.BatchNorm1d(num_features=64)
        self.l5 = torch.nn.Linear(64, 1)
        self.relu = torch.nn.ReLU()

    def forward(self, x):

        # In the forward function we accept a Variable of input data and we must return
        # a Variable of output data. We can use Modules defined in the constructor as
        # well as arbitrary operators on Variables.

        out1 = F.dropout(self.relu(self.bn1(self.l1(x))), 0.5)
        out2 = F.dropout(self.relu(self.bn2(self.l2(out1))), 0.5)
        out3 = F.dropout(self.relu(self.bn3(self.l3(out2))), 0.5)
        out4 = F.dropout(self.relu(self.bn4(self.l4(out3))), 0.5)
        y_pred = self.l5(out4)
        # print(y_pred)
        return y_pred


class FCPINNModel1(torch.nn.Module):

    def __init__(self, number_of_comp_features, number_of_target_features):

        # In the constructor we instantiate two nn.Linear module

        super(FCPINNModel1, self).__init__()
        # print(type(number_of_comp_features), type(number_of_target_features))
        self.l1_comp = torch.nn.Linear(number_of_comp_features, 1024)
        self.bn1_comp = torch.nn.BatchNorm1d(num_features=1024)
        self.l2_comp = torch.nn.Linear(1024, 1024)
        self.bn2_comp = torch.nn.BatchNorm1d(num_features=1024)
        self.l3_comp = torch.nn.Linear(1024, 256)
        self.bn3_comp = torch.nn.BatchNorm1d(num_features=256)
        self.l4_comp = torch.nn.Linear(256, 32)
        self.bn4_comp = torch.nn.BatchNorm1d(num_features=32)

        self.l1_tar = torch.nn.Linear(int(number_of_target_features), 1024)
        self.bn1_tar = torch.nn.BatchNorm1d(num_features=1024)
        self.l2_tar = torch.nn.Linear(1024, 1024)
        self.bn2_tar = torch.nn.BatchNorm1d(num_features=1024)
        self.l3_tar = torch.nn.Linear(1024, 256)
        self.bn3_tar = torch.nn.BatchNorm1d(num_features=256)
        self.l4_tar = torch.nn.Linear(256, 32)
        self.bn4_tar = torch.nn.BatchNorm1d(num_features=32)

        self.fc1 = torch.nn.Linear(64, 64)
        self.fc2 = torch.nn.Linear(64, 32)

        self.output = torch.nn.Linear(32, 1)
        self.relu = torch.nn.ReLU()


    def forward(self, x_comp, x_tar):
        # Compound part
        out1_comp = F.dropout(self.relu(self.bn1_comp(self.l1_comp(x_comp))), 0.5)
        out2_comp = F.dropout(self.relu(self.bn2_comp(self.l2_comp(out1_comp))), 0.5)
        out3_comp = F.dropout(self.relu(self.bn3_comp(self.l3_comp(out2_comp))), 0.5)
        out4_comp = F.dropout(self.relu(self.bn4_comp(self.l4_comp(out3_comp))), 0.5)

        # Target part
        out1_tar = F.dropout(self.relu(self.bn1_tar(self.l1_tar(x_tar))), 0.5)
        out2_tar = F.dropout(self.relu(self.bn2_tar(self.l2_tar(out1_tar))), 0.5)
        out3_tar = F.dropout(self.relu(self.bn3_tar(self.l3_tar(out2_tar))), 0.5)
        out4_tar = F.dropout(self.relu(self.bn4_tar(self.l4_tar(out3_tar))), 0.5)

        combined_layer = torch.cat((out4_comp, out4_tar), 1)
        out_fc1 = self.fc1(combined_layer)
        out_fc2 = self.fc2(out_fc1)
        y_pred = self.output(out_fc2)

        return y_pred

