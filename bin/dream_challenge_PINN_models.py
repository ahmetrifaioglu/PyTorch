import torch
import torch.nn.functional as F
from dream_challenge_models import FC_1_Layer, FC_2_Layer, FC_3_Layer, FC_5_Layer

class FC_PINNModel_2_2_2(torch.nn.Module):

    def __init__(self, number_of_comp_features, comp_l1, comp_l2, number_of_target_features, tar_l1, tar_l2, fc_l1, fc_l2):
        # In the constructor we instantiate two nn.Linear module

        super(FC_PINNModel_2_2_2, self).__init__()
        # print(type(number_of_comp_features), type(number_of_target_features))
        self.l1_comp = torch.nn.Linear(number_of_comp_features, comp_l1)
        self.bn1_comp = torch.nn.BatchNorm1d(num_features=comp_l1)
        self.l2_comp = torch.nn.Linear(comp_l1, comp_l2)
        self.bn2_comp = torch.nn.BatchNorm1d(num_features=comp_l2)


        self.l1_tar = torch.nn.Linear(int(number_of_target_features), tar_l1)
        self.bn1_tar = torch.nn.BatchNorm1d(num_features=tar_l1)
        self.l2_tar = torch.nn.Linear(tar_l1, tar_l2)
        self.bn2_tar = torch.nn.BatchNorm1d(num_features=tar_l2)


        self.fc1 = torch.nn.Linear(comp_l2+tar_l2, fc_l1)
        self.fc2 = torch.nn.Linear(fc_l1, fc_l2)

        self.output = torch.nn.Linear(fc_l2, 1)
        self.relu = torch.nn.ReLU()

    def forward(self, x_comp, x_tar):
        # Compound part
        out1_comp = F.dropout(self.relu(self.bn1_comp(self.l1_comp(x_comp))), 0.5)
        out2_comp = F.dropout(self.relu(self.bn2_comp(self.l2_comp(out1_comp))), 0.5)

        # Target part
        out1_tar = F.dropout(self.relu(self.bn1_tar(self.l1_tar(x_tar))), 0.5)
        out2_tar = F.dropout(self.relu(self.bn2_tar(self.l2_tar(out1_tar))), 0.5)

        combined_layer = torch.cat((out2_comp, out2_tar), 1)
        out_fc1 = self.fc1(combined_layer)
        out_fc2 = self.fc2(out_fc1)
        y_pred = self.output(out_fc2)

        return y_pred

class FC_PINNModel_2_2_2_Modules(torch.nn.Module):

    def __init__(self, number_of_comp_features, comp_l1, comp_l2, number_of_target_features, tar_l1, tar_l2, fc_l1, fc_l2, regression_classifier):
        # In the constructor we instantiate two nn.Linear module

        super(FC_PINNModel_2_2_2_Modules, self).__init__()
        # print(type(number_of_comp_features), type(number_of_target_features))
        print(comp_l1, comp_l2, tar_l1, tar_l2, fc_l1, fc_l2,)
        self.layer_2_comp = FC_2_Layer(number_of_comp_features, comp_l1, comp_l2, 0.5)
        self.layer_2_tar = FC_2_Layer(number_of_target_features, tar_l1, tar_l2, 0.5)

        self.layer_2_combined = FC_2_Layer(comp_l2+tar_l2, fc_l1, fc_l2, 0.5)

        self.output = None
        if regression_classifier=="r":
            self.output = torch.nn.Linear(fc_l2, 1)
        else:
            self.output = torch.nn.Linear(fc_l2, 2)

        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()
        self.softmax = torch.nn.Softmax()
        #self.drop_rate = drop_rate
        self.r_c = regression_classifier

    def forward(self, x_comp, x_tar):
        # Compound part

        out2_comp = self.layer_2_comp.forward(x_comp)
        out2_tar = self.layer_2_tar.forward(x_tar)


        combined_layer = torch.cat((out2_comp, out2_tar), 1)

        out_combined = self.layer_2_combined.forward(combined_layer)

        y_pred = None

        if self.r_c=="r":
            y_pred = self.output(out_combined)
        else:
            y_pred = self.softmax(self.output(out_combined))

        return y_pred


class FC_PINNModel_2_3_2_Modules(torch.nn.Module):

    def __init__(self, number_of_comp_features, comp_l1, comp_l2, number_of_target_features, tar_l1, tar_l2, tar_l3, fc_l1, fc_l2):
        # In the constructor we instantiate two nn.Linear module

        super(FC_PINNModel_2_3_2_Modules, self).__init__()
        # print(type(number_of_comp_features), type(number_of_target_features))
        self.layer_2_comp = FC_2_Layer(number_of_comp_features, comp_l1, comp_l2, 0.5)
        self.layer_3_tar = FC_3_Layer(number_of_target_features, tar_l1, tar_l2, tar_l3, 0.5)

        self.layer_2_combined = FC_2_Layer(comp_l2+tar_l3, fc_l1, fc_l2, 0.5)
        self.output = torch.nn.Linear(fc_l2, 1)

        self.relu = torch.nn.ReLU()
        #self.drop_rate = drop_rate

    def forward(self, x_comp, x_tar):
        # Compound part

        out2_comp = self.layer_2_comp.forward(x_comp)
        out3_tar = self.layer_3_tar.forward(x_tar)


        combined_layer = torch.cat((out2_comp, out3_tar), 1)

        out_combined = self.layer_2_combined.forward(combined_layer)
        y_pred = self.output(out_combined)

        return y_pred

class FC_PINNModel_3_5_2_Modules(torch.nn.Module):

    def __init__(self, number_of_comp_features, comp_l1, comp_l2, comp_l3, number_of_target_features, tar_l1, tar_l2, tar_l3, tar_l4, tar_l5, fc_l1, fc_l2):
        # In the constructor we instantiate two nn.Linear module

        super(FC_PINNModel_3_5_2_Modules, self).__init__()
        # print(type(number_of_comp_features), type(number_of_target_features))
        self.layer_3_comp = FC_3_Layer(number_of_comp_features, comp_l1, comp_l2, comp_l3, 0.5)
        self.layer_5_tar = FC_5_Layer(number_of_target_features, tar_l1, tar_l2, tar_l3, tar_l4, tar_l5, 0.5)

        self.layer_2_combined = FC_2_Layer(comp_l3 + tar_l5, fc_l1, fc_l2, 0.5)
        self.output = torch.nn.Linear(fc_l2, 1)

        self.relu = torch.nn.ReLU()
        #self.drop_rate = drop_rate

    def forward(self, x_comp, x_tar):
        # Compound part

        out3_comp = self.layer_3_comp.forward(x_comp)
        out5_tar = self.layer_5_tar.forward(x_tar)


        combined_layer = torch.cat((out3_comp, out5_tar), 1)

        out_combined = self.layer_2_combined.forward(combined_layer)
        y_pred = self.output(out_combined)

        return y_pred

class FC_PINNModel_4_4_2(torch.nn.Module):

    def __init__(self, number_of_comp_features, number_of_target_features):

        # In the constructor we instantiate two nn.Linear module

        super(FC_PINNModel_4_4_2, self).__init__()
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


class FC_PINNModel_3_3_2(torch.nn.Module):

    def __init__(self, number_of_comp_features, number_of_target_features):

        # In the constructor we instantiate two nn.Linear module

        super(FC_PINNModel_3_3_2, self).__init__()
        # print(type(number_of_comp_features), type(number_of_target_features))
        self.l1_comp = torch.nn.Linear(number_of_comp_features, 1024)
        self.bn1_comp = torch.nn.BatchNorm1d(num_features=1024)
        self.l2_comp = torch.nn.Linear(1024, 1024)
        self.bn2_comp = torch.nn.BatchNorm1d(num_features=1024)
        self.l3_comp = torch.nn.Linear(1024, 256)
        self.bn3_comp = torch.nn.BatchNorm1d(num_features=256)


        self.l1_tar = torch.nn.Linear(int(number_of_target_features), 1024)
        self.bn1_tar = torch.nn.BatchNorm1d(num_features=1024)
        self.l2_tar = torch.nn.Linear(1024, 1024)
        self.bn2_tar = torch.nn.BatchNorm1d(num_features=1024)
        self.l3_tar = torch.nn.Linear(1024, 256)
        self.bn3_tar = torch.nn.BatchNorm1d(num_features=256)


        self.fc1 = torch.nn.Linear(512, 512)
        self.fc2 = torch.nn.Linear(512, 256)

        self.output = torch.nn.Linear(256, 1)
        self.relu = torch.nn.ReLU()


    def forward(self, x_comp, x_tar):
        # Compound part
        out1_comp = F.dropout(self.relu(self.bn1_comp(self.l1_comp(x_comp))), 0.5)
        out2_comp = F.dropout(self.relu(self.bn2_comp(self.l2_comp(out1_comp))), 0.5)
        out3_comp = F.dropout(self.relu(self.bn3_comp(self.l3_comp(out2_comp))), 0.5)


        # Target part
        out1_tar = F.dropout(self.relu(self.bn1_tar(self.l1_tar(x_tar))), 0.5)
        out2_tar = F.dropout(self.relu(self.bn2_tar(self.l2_tar(out1_tar))), 0.5)
        out3_tar = F.dropout(self.relu(self.bn3_tar(self.l3_tar(out2_tar))), 0.5)


        combined_layer = torch.cat((out3_comp, out3_tar), 1)
        out_fc1 = self.fc1(combined_layer)
        out_fc2 = self.fc2(out_fc1)
        y_pred = self.output(out_fc2)

        return y_pred



