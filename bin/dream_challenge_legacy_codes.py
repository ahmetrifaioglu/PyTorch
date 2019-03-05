
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

class TrainRNNDream(Trainable):
    def _setup(self, config):
        args = config.pop("args")
        vars(args).update(config)
        args.cuda = not args.no_cuda and torch.cuda.is_available()
        print(args.cuda)

        torch.manual_seed(1)
        use_gpu = torch.cuda.is_available()

        self.device = "cpu"

        if use_gpu:
            print("GPU is available on this device!")
            self.device = "cuda"
        else:
            print("CPU is available on this device!")

        kwargs = {'num_workers': 1, 'pin_memory': True} if args.cuda else {}

        loader_fold_dict, number_of_comp_features, number_of_target_features = get_nfold_data_loader_dict(num_of_folds,
                                                                                                          args.batch_size,
                                                                                                          ["ecfp4"],
                                                                                                          ["trigramencodings1000"],
                                                                                                          "idg_comp_targ_uniq_inter_filtered.csv",
                                                                                                          "r")

        original_number_of_comp_features = int(number_of_comp_features)
        original_number_of_target_features = int(number_of_target_features)

        print(original_number_of_comp_features, original_number_of_target_features)

        self.train_loader = loader_fold_dict[0][0]
        self.valid_loader = loader_fold_dict[0][1]

        self.model = CompFCNNTarRNN(number_of_comp_features, args.first_comp_layer, args.second_comp_layer, args.vocab_size, args.output_size, args.embedding_dim, args.hidden_dim, args.n_rnn_layers, args.first_comb_layer, args.second_comb_layer, "r").to(self.device)
        # model = CompFCNNTarRNN(int(number_of_comp_features), int(comp_hidden_lst[0]), int(comp_hidden_lst[1]), vocab_size, output_size, embedding_dim, hidden_dim, n_rnn_layers, fc1, fc2).to(device)
        if args.cuda:
            self.model.cuda()

        self.optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)
        self.criterion = torch.nn.MSELoss()
        self.args = args

    def _train_iteration(self):


        total_training_loss = 0.0
        total_training_count = 0

        batch_number = 0
        h = self.model.init_hidden(batch_size)

        self.model.train()
        for i, data in enumerate(train_loader):
            batch_number += 1
            h = tuple([each.data for each in h])
            # clear gradient DO NOT forget you fool!
            self.optimizer.zero_grad()

            # get the inputs
            comp_feature_vectors, target_feature_vectors, labels, compound_ids, target_ids, number_of_comp_features, number_of_target_features = data
            # wrap them in Variable
            comp_feature_vectors, target_feature_vectors, labels = Variable(comp_feature_vectors).to(device), Variable(
                target_feature_vectors).to(self.device), Variable(labels).to(self.device)
            if comp_feature_vectors.shape[0] == batch_size:
                inputs = None
                y_pred = None

                total_training_count += comp_feature_vectors.shape[0]

                y_pred, h = self.model(comp_feature_vectors, target_feature_vectors, h)

                loss = self.criterion(y_pred.squeeze(), labels)

                total_training_loss += float(loss.item())
                loss.backward()
                self.optimizer.step()

        print("Epoch {} training loss:".format(epoch), total_training_loss)
        return {"neg_mean_loss": -1 * total_training_loss}

    def _test(self):
        self.model.eval()
        regression_classifier = "r"
        total_validation_loss = 0.0
        total_validation_count = 0
        validation_predictions = []
        validation_labels = []

        h = model.init_hidden(batch_size)
        with torch.no_grad():  # torch.set_grad_enabled(False):
            for i, data in enumerate(self.valid_loader):

                val_comp_feature_vectors, val_target_feature_vectors, val_labels, val_compound_ids, val_target_ids, val_number_of_comp_features, val_number_of_target_features = data
                val_comp_feature_vectors, val_target_feature_vectors, val_labels = Variable(
                    val_comp_feature_vectors).to(
                    self.device), Variable(val_target_feature_vectors).to(self.device), Variable(val_labels).to(self.device)
                total_validation_count += val_comp_feature_vectors.shape[0]

                if val_comp_feature_vectors.shape[0] == batch_size:
                    val_inputs = None
                    val_y_pred = None

                    val_y_pred, h = self.model(val_comp_feature_vectors, val_target_feature_vectors, h)
                    loss_val = self.criterion(val_y_pred.squeeze(), val_labels)
                    total_validation_loss += float(loss_val.item())
                    for item in val_labels:
                        validation_labels.append(float(item.item()))

                    for item in val_y_pred:
                        validation_predictions.append(float(item.item()))

        # if regression_classifier == "r":
        rmse_score = rmse(np.asarray(validation_labels), np.asarray(
            validation_predictions))
        pearson_score = pearson(np.asarray(validation_labels), np.asarray(validation_predictions))
        spearman_score = spearman(np.asarray(validation_labels), np.asarray(validation_predictions))
        ci_score = ci(np.asarray(validation_labels), np.asarray(validation_predictions))
        f1_score = f1(np.asarray(validation_labels), np.asarray(validation_predictions))
        ave_auc_score = average_AUC(np.asarray(validation_labels), np.asarray(validation_predictions))
        print("================================================================================")
        print("Fold:{}\tEpoch:{}\tTest RMSE:{}\tTraining Loss:{}\tValidation Loss:{}".format(fold + 1, epoch,
                                                                                             rmse_score,
                                                                                             total_training_loss,
                                                                                             total_validation_loss))
        print("RMSE:\t{}".format(rmse_score))  # rmse, pearson, spearman, ci, ci, average_AUC
        print("Pearson:\t{}".format(pearson_score))
        print("Spearman:\t{}".format(spearman_score))
        print("Ci:\t{}".format(ci_score))
        print("F1-Score:\t{}".format(f1_score))
        print("Average_AUC:\t{}".format(ave_auc_score))
        print("IDG File:\t{}".format(comp_tar_pair_dataset))
        print("Number of training samples:\t{}".format(total_training_count))
        print("Number of validation samples:\t{}".format(total_validation_count))
        return {"RMSE": rmse_score, "F1-Score": f1_score, "neg_mean_loss": -1*total_validation_loss}

    def _train(self):
        self._train_iteration()
        return self._test()

    def _save(self, checkpoint_dir):
        checkpoint_path = os.path.join(checkpoint_dir, "model.pth")
        torch.save(self.model.state_dict(), checkpoint_path)
        return checkpoint_path

    def _restore(self, checkpoint_path):
        self.model.load_state_dict(checkpoint_path)

'''
name_of_the_experiment = "last_rnn_out_experiment_1"
comp_feature_list = ["ecfp4"]
tar_feature_list = ["trigramencodings1000"]  # , "DDE", "pfam"]
batch_size = [32, 64, 128]
lst_learning_rate = [0.0001, 0.005, 0.001]
vocab_size = [8000]
n_of_neuron_list_h = [1024, 512, 256]
n_of_neuron_list_fc = [1024, 512, 256]
rnn_output_size = [128, 256, 512]
embedding_dim = [100, 200, 400]
hidden_dim = [128, 256, 512, 1024]
rnn_layers = [2, 3]
n_of_h_layers = 2
'''


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
                    "training_iteration": 10 if args.smoke_test else 10,
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
