
class  myCustomTestDataLoader(Dataset):
    def __init__(self):
        test_dataset = pd.read_csv('data/test_dataset.csv', header=None)
        self.compound_ids = test_dataset.iloc[:,0]
        #print(self.compound_ids)
        self.target_ids = test_dataset.iloc[:,1]
        #print(self.target_ids)
        self.labels = torch.tensor(test_dataset.iloc[:,2]).type(torch.FloatTensor)
        #print(self.labels)
        self.feature_vectors = torch.tensor(test_dataset.iloc[:,3:].values).type(torch.FloatTensor)

    def __getitem__(self, index):
        return self.feature_vectors[index], self.labels[index]

    def __len__(self):
        return len(self.compound_ids)

dataset = myCustomDataLoader()
n_of_training_samples = len(dataset)

test_dataset = myCustomTestDataLoader()


train_loader = DataLoader(dataset=dataset, batch_size = 32, shuffle=False)

test_loader = DataLoader(dataset=test_dataset, batch_size = 500, shuffle=True)
#print(train_loader)


import torch

class Model(torch.nn.Module):

    def __init__(self):
        # In the constructor we instantiate two nn.Linear module
        super(Model, self).__init__()

        self.l1 = torch.nn.Linear(9024, 1024)
        self.bn1 = torch.nn.BatchNorm1d(num_features=1024)
        self.l2 = torch.nn.Linear(1024, 400)
        self.bn2 = torch.nn.BatchNorm1d(num_features=400)
        self.l3 = torch.nn.Linear(400, 1)
        self.relu = torch.nn.ReLU()

        """
        if use_gpu:
            self.l1 = torch.nn.Linear(9024, 1024).cuda()
            self.bn1 = torch.nn.BatchNorm1d(num_features=1024).cuda()
            self.l2 = torch.nn.Linear(1024, 400).cuda()
            self.bn2 = torch.nn.BatchNorm1d(num_features=400).cuda()
            self.l3 = torch.nn.Linear(400, 1).cuda()
            self.relu = torch.nn.ReLU().cuda()
        else:
            self.l1 = torch.nn.Linear(9024, 1024)
            self.bn1 = torch.nn.BatchNorm1d(num_features=1024)
            self.l2 = torch.nn.Linear(1024, 400)
            self.bn2 = torch.nn.BatchNorm1d(num_features=400)
            self.l3 = torch.nn.Linear(400, 1)
            self.relu = torch.nn.ReLU()
        """

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


class Model2(torch.nn.Module):

    def __init__(self):

        # In the constructor we instantiate two nn.Linear module

        super(Model2, self).__init__()
        self.l1 = torch.nn.Linear(9024, 2048)
        self.bn1 = torch.nn.BatchNorm1d(num_features=2048)
        self.l2 = torch.nn.Linear(2048, 1024)
        self.bn2 = torch.nn.BatchNorm1d(num_features=1024)
        self.l3 = torch.nn.Linear(1024, 256)
        self.bn3 = torch.nn.BatchNorm1d(num_features=256)
        self.l4 = torch.nn.Linear(256, 64)
        self.bn4 = torch.nn.BatchNorm1d(num_features=64)
        self.l5 = torch.nn.Linear(64, 1)
        self.relu = torch.nn.ReLU()
        """
        else:
            self.l1 = torch.nn.Linear(9024, 2048)
            self.bn1 = torch.nn.BatchNorm1d(num_features=2048)
            self.l2 = torch.nn.Linear(2048, 1024)
            self.bn2 = torch.nn.BatchNorm1d(num_features=1024)
            self.l3 = torch.nn.Linear(1024, 256)
            self.bn3 = torch.nn.BatchNorm1d(num_features=256)
            self.l4 = torch.nn.Linear(256, 64)
            self.bn4 = torch.nn.BatchNorm1d(num_features=64)
            self.l5 = torch.nn.Linear(64, 1)
            self.relu = torch.nn.ReLU()
        """
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

        out3 = self.l3(out2)
        out3 = self.bn3(out3)
        out3 = self.relu(out3)
        out3 = F.dropout(out3, 0.5)

        out4 = self.l4(out3)
        out4 = self.bn4(out4)
        out4 = self.relu(out4)
        out4 = F.dropout(out4, 0.5)

        y_pred = self.l5(out4)
        # print(y_pred)
        return y_pred

class RMSELoss(torch.nn.Module):
    def __init__(self):
        super(RMSELoss, self).__init__()
        self.mse = torch.nn.MSELoss()

    def forward(self, yhat, y):
        return torch.sqrt(self.mse(yhat, y))


criterion = RMSELoss()


"""


# Construct our loss function and an Optimizer. The call to model.parameters()
# in the SGD constructor will contain the learnable parameters of the two
# nn.Linear modules which are members of the model.

# Training loop
for epoch in range(n_epoch):
    total_training_loss = 0.0
    total_validation_loss = 0.0
    total_training_count = 0
    training=True
    validation_predictions = []
    validation_labels = []

    print("TRAINING STARTED")
    for i, data in enumerate(train_loader):
        # get the inputs
        inputs, labels, comp_ids, target_ids = data

        # wrap them in Variable
        if use_gpu:
            inputs, labels = Variable(inputs).cuda(), Variable(labels).cuda()
        else:
            inputs, labels = Variable(inputs), Variable(labels)
        #print(inputs.shape[0], labels.shape)
        total_training_count += inputs.shape[0]
        if total_training_count >=int(n_of_training_samples*0.80):
            #print("NOT TRAINING")
            training = False
        #print(labels.shape)
        #print(labels)
        # Forward pass: Compute predicted y by passing x to the model
        y_pred = model(inputs)


        #print(y_pred)
        # Compute and print loss
        loss = criterion(y_pred.squeeze(), labels)
        if training:
            #print("T")
            total_training_loss += float(loss.data[0])
        else:
            #print("V")
            #print(y_pred.numpy())
            #validation_predictions.a
            #validation_predictions = np.concatenate((validation_predictions, list(y_pred)), axis=None)
            for item in y_pred:
                validation_predictions.append(float(item.data[0]))
            for item in labels:
                validation_labels.append(float(item.data[0]))
            total_validation_loss += float(loss.data[0])


        #print("Epoch:{}, Number:{}, Loss:{}".format(epoch, i, loss.data[0]))
        #for i in range(len(y_pred.squeeze())):
        #    print(labels[i], y_pred.squeeze()[i])
        # Zero gradients, perform a backward pass, and update the weights.
        optimizer.zero_grad()
        if training:
            loss.backward()
            optimizer.step()

    #print(len(validation_predictions))
    #print(len(validation_labels))
    print("Epoch:{}, Training Loss:{}, Validation Loss:{}".format(epoch, total_training_loss, total_validation_loss))
    print("RMSE:\t{}".format(rmse(np.asarray(validation_labels),np.asarray(validation_predictions))))#rmse, pearson, spearman, ci, ci, average_AUC
    print("pearson:\t{}".format(pearson(np.asarray(validation_labels), np.asarray(validation_predictions))))
    print("spearman:\t{}".format(spearman(np.asarray(validation_labels), np.asarray(validation_predictions))))
    print("ci:\t{}".format(ci(np.asarray(validation_labels), np.asarray(validation_predictions))))
    print("F1-Score:\t{}".format(f1(np.asarray(validation_labels), np.asarray(validation_predictions))))
    print("average_AUC:\t{}".format(average_AUC(np.asarray(validation_labels), np.asarray(validation_predictions))))

    #print("Training Loss:\t{}".format(total_training_loss))
    #print("Validation Loss:\t{}".format(total_validation_loss))

predictions =[]
for i, data in enumerate(test_loader):
    inputs, labels = data
    if use_gpu:
        inputs, labels = Variable(inputs).cuda(), Variable(labels).cuda()
    else:
        inputs, labels = Variable(inputs), Variable(labels)
    y_pred = model(inputs)
    predictions = list(y_pred)

for i in predictions:
    print(i)


print(len(predictions))
"""



"""
import torch
import torch.nn.functional as F
class FCModel1_old(torch.nn.Module):

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

        out1 = F.dropout(self.relu(self.bn1(self.l1(x))), 0.5)
        out2 = F.dropout(self.relu(self.bn2(self.l2(out1))), 0.5)

        y_pred = self.l3(out2)

        return y_pred

class FCModel1(torch.nn.Module):

    def __init__(self, number_of_features):
        # In the constructor we instantiate two nn.Linear module
        super(Model, self).__init__()

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


class FCModel2(torch.nn.Module):

    def __init__(self, number_of_features):

        # In the constructor we instantiate two nn.Linear module

        super(Model2, self).__init__()
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

        out1 = self.l1(x)
        out1 = self.bn1(out1)
        out1 = self.relu(out1)
        out1 = F.dropout(out1, 0.5)

        out2 = self.l2(out1)
        out2 = self.bn2(out2)
        out2 = self.relu(out2)
        out2 = F.dropout(out2, 0.5)

        out3 = self.l3(out2)
        out3 = self.bn3(out3)
        out3 = self.relu(out3)
        out3 = F.dropout(out3, 0.5)

        out4 = self.l4(out3)
        out4 = self.bn4(out4)
        out4 = self.relu(out4)
        out4 = F.dropout(out4, 0.5)

        y_pred = self.l5(out4)
        # print(y_pred)
        return y_pred


class PINNModel1(torch.nn.Module):

    def __init__(self, number_of_comp_features, number_of_target_features):

        # In the constructor we instantiate two nn.Linear module

        super(PINNModel, self).__init__()
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

        # In the forward function we accept a Variable of input data and we must return
        # a Variable of output data. We can use Modules defined in the constructor as
        # well as arbitrary operators on Variables.

        out1_comp = F.dropout(self.relu(self.bn1_comp(self.l1_comp(x_comp))), 0.5)
        out2_comp = F.dropout(self.relu(self.bn2_comp(self.l2_comp(out1_comp))), 0.5)
        out3_comp = F.dropout(self.relu(self.bn3_comp(self.l3_comp(out2_comp))), 0.5)

        out4_comp = F.dropout(self.relu(self.bn4_comp(self.l4_comp(out3_comp))), 0.5)
        out4_comp = F.dropout(out4_comp, 0.5)

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
"""

