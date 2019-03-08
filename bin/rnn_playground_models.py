import torch.nn as nn
import torch
import torch.nn.functional as F
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
from operator import itemgetter
use_gpu = torch.cuda.is_available()
import numpy as np
device = "cpu"
if use_gpu:
    device = "cuda"

class CompFCNNTarRNN(nn.Module):

    # The RNN model that will be used to perform Sentiment analysis.

    def __init__(self, number_of_comp_features, comp_l1, comp_l2, vocab_size, output_size, embedding_dim, hidden_dim, n_layers, fc_l1, fc_l2, drop_prob=0.5):

        # Initialize the model by setting up the layers.

        super(CompFCNNTarRNN, self).__init__()

        self.layer_2_comp = FC_2_Layer(number_of_comp_features, comp_l1, comp_l2, drop_prob)


        self.output_size = output_size
        self.n_layers = n_layers
        self.hidden_dim = hidden_dim
        #print(vocab_size, embedding_dim)
        # embedding and LSTM layers
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, n_layers,
                            dropout=drop_prob, batch_first=True)#, bidirectional=True)

        # dropout layer
        self.dropout = nn.Dropout(0.3)

        # linear and sigmoid layers
        self.fc = nn.Linear(hidden_dim, output_size)
        # print(self.fc)
        self.layer_2_combined = FC_2_Layer(comp_l2 + output_size, fc_l1, fc_l2, drop_prob)

        self.output = None

        #if regression_classifier == "r":

        #else:
        #    self.output = torch.nn.Linear(fc_l2, 2)

        self.output = torch.nn.Linear(fc_l2, 1)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()
        self.softmax = torch.nn.Softmax()
        # self.drop_rate = drop_rate
        self.r_c = "r"


    def forward(self, x_comp, x_tar, hidden):

        # Perform a forward pass of our model on some input and hidden state.

        out2_comp = self.layer_2_comp.forward(x_comp)

        batch_size = x_tar.size(0)
        # print(batch_size)
        # embeddings and lstm_out
        x_tar = x_tar.long()
        print("Target shape:", x_tar.shape)
        embeds = self.embedding(x_tar)
        #print("embeddings:", embeds)
        # print("embedding shape", embeds.shape)
        lstm_out_tar, hidden = self.lstm(embeds, hidden)
        # print("lstm_out no reshape", lstm_out.shape)
        # print("hidden", hidden[0][-1].shape)
        # print("compound output shape:", out2_comp.shape)

        # stack up lstm outputs
        #lstm_out_tar = lstm_out.contiguous().view(-1, self.hidden_dim)
        # print("lstm_out", lstm_out.shape)

        # dropout and fully-connected layer
        #out = self.dropout(lstm_out_tar)

        # Experiment 1
        # out_tar = self.fc(hidden[0][-1])

        # Experiment 2
        lstm_out_tar = self.dropout(lstm_out_tar)
        lstm_out_tar = lstm_out_tar[:, -1, :]
        out_tar = self.fc(lstm_out_tar)
        combined_layer = torch.cat((out2_comp, out_tar), 1)
        # print(combined_layer.shape)
        out_combined = self.layer_2_combined.forward(combined_layer)
        y_pred = None

        if self.r_c == "r":
            y_pred = self.output(out_combined)
        else:
            y_pred = self.softmax(self.output(out_combined))

        return y_pred, hidden
        #print(out.shape)
        #out = out.view(batch_size, -1)
        #print(out.shape)
        #out = out[:, -1]
        #print(out.shape)
        #out_tar = self.fc(out_tar)
        #out_tar = out_tar.view(batch_size, -1)
        #out_tar = out_tar[:, -1]
        # print("TARGET_OUTPUT:", out_tar.shape)
        """
        #print(out2_comp.shape)
        #combined_layer = torch.cat((out2_comp, out_tar), 1)
        #out_combined = self.layer_2_combined.forward(combined_layer)
        y_pred = None

        if self.r_c == "r":
            y_pred = self.output(out_combined)
        else:
            y_pred = self.softmax(self.output(out_combined))

        return y_pred, hidden
        """
        #return sig_out, hidden
    def init_hidden(self, batch_size):
        ''' Initializes hidden state '''
        # Create two new tensors with sizes n_layers x batch_size x hidden_dim,
        # initialized to zero, for hidden state and cell state of LSTM
        weight = next(self.parameters()).data

        """
        if (train_on_gpu):
            hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().cuda(),
                      weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().cuda())
        else:
            hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_(),
                      weight.new(self.n_layers, batch_size, self.hidden_dim).zero_())
        """
        hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().to(device),
                  weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().to(device))
        # hidden = (weight.new(self.n_layers*2, batch_size, self.hidden_dim).zero_().to(device),
        #          weight.new(self.n_layers*2, batch_size, self.hidden_dim).zero_().to(device))
        return hidden



class CompFCNNTarRNNPadding(nn.Module):

    # The RNN model that will be used to perform Sentiment analysis.

    def __init__(self, number_of_comp_features, comp_l1, comp_l2, vocab_size, output_size, embedding_dim, hidden_dim, n_layers, fc_l1, fc_l2, drop_prob=0.5):

        # Initialize the model by setting up the layers.

        super(CompFCNNTarRNNPadding, self).__init__()

        self.layer_2_comp = FC_2_Layer(number_of_comp_features, comp_l1, comp_l2, drop_prob)


        self.output_size = output_size
        self.n_layers = n_layers
        self.hidden_dim = hidden_dim
        #print(vocab_size, embedding_dim)
        # embedding and LSTM layers
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, n_layers,
                            dropout=drop_prob, batch_first=True)#, bidirectional=True)

        # dropout layer
        self.dropout = nn.Dropout(0.3)

        # linear and sigmoid layers
        self.fc = nn.Linear(hidden_dim, output_size)
        # print(self.fc)
        self.layer_2_combined = FC_2_Layer(comp_l2 + output_size, fc_l1, fc_l2, drop_prob)

        self.output = None

        #if regression_classifier == "r":

        #else:
        #    self.output = torch.nn.Linear(fc_l2, 2)

        self.output = torch.nn.Linear(fc_l2, 1)
        self.relu = torch.nn.ReLU()
        self.sigmoid = torch.nn.Sigmoid()
        self.softmax = torch.nn.Softmax()
        # self.drop_rate = drop_rate
        self.r_c = "r"


    def forward(self, x_comp, x_tar, hidden):

        # Perform a forward pass of our model on some input and hidden state.

        out2_comp = self.layer_2_comp.forward(x_comp)
        # print(type(x_tar))
        batch_size = x_tar.size(0)
        # print(batch_size)
        # embeddings and lstm_out
        print("girdi")
        x_tar_with_lenghts = []
        for row_ind in range(batch_size):
            #n_of_nonzero = len(list(x_tar[row_ind])) - list(x_tar[row_ind]).count(0)
            # This is faster than above
            n_of_nonzero = len(x_tar[row_ind].nonzero())
            # print(n_of_nonzero, )
            x_tar_with_lenghts.append([list(x_tar[row_ind]), n_of_nonzero])
        print("cikti 1")
        x_tar_with_lenghts = sorted(x_tar_with_lenghts, key=itemgetter(1), reverse=True)
        print("cikti 2")
        x_tar = torch.LongTensor([item[0] for item in x_tar_with_lenghts]).to(device)
        print("cikti 3")
        x_tar = x_tar.long()

        real_lengths = [item[1] for item in x_tar_with_lenghts]
        print("cikti")
        #x_tar = x_tar.long()
        embeds = self.embedding(x_tar)
        embeds = pack_padded_sequence(embeds, real_lengths, batch_first=True)

        lstm_out_tar, hidden = self.lstm(embeds, hidden)
        lstm_out_tar, lengths = pad_packed_sequence(lstm_out_tar, batch_first=True)

        # Experiment 1
        # out_tar = self.fc(hidden[0][-1])

        # Experiment 2
        lstm_out_tar = self.dropout(lstm_out_tar)
        lstm_out_tar = lstm_out_tar[:, -1, :]
        out_tar = self.fc(lstm_out_tar)
        combined_layer = torch.cat((out2_comp, out_tar), 1)
        # print(combined_layer.shape)
        out_combined = self.layer_2_combined.forward(combined_layer)
        y_pred = None

        if self.r_c == "r":
            y_pred = self.output(out_combined)
        else:
            y_pred = self.softmax(self.output(out_combined))

        return y_pred, hidden

    def init_hidden(self, batch_size):
        ''' Initializes hidden state '''
        # Create two new tensors with sizes n_layers x batch_size x hidden_dim,
        # initialized to zero, for hidden state and cell state of LSTM
        weight = next(self.parameters()).data

        """
        if (train_on_gpu):
            hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().cuda(),
                      weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().cuda())
        else:
            hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_(),
                      weight.new(self.n_layers, batch_size, self.hidden_dim).zero_())
        """
        hidden = (weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().to(device),
                  weight.new(self.n_layers, batch_size, self.hidden_dim).zero_().to(device))
        # hidden = (weight.new(self.n_layers*2, batch_size, self.hidden_dim).zero_().to(device),
        #          weight.new(self.n_layers*2, batch_size, self.hidden_dim).zero_().to(device))
        return hidden






class FC_PINNModel_2_2_2_Modules(torch.nn.Module):

    def __init__(self, number_of_comp_features, comp_l1, comp_l2, number_of_target_features, tar_l1, tar_l2, fc_l1, fc_l2, regression_classifier):
        # In the constructor we instantiate two nn.Linear module

        super(FC_PINNModel_2_2_2_Modules, self).__init__()
        # print(type(number_of_comp_features), type(number_of_target_features))
        # print(comp_l1, comp_l2, tar_l1, tar_l2, fc_l1, fc_l2,)
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

class FC_2_Layer(torch.nn.Module):

    def __init__(self, number_of_inputs, neuron_l1, neuron_l2, drop_rate):
        # In the constructor we instantiate two nn.Linear module
        super(FC_2_Layer, self).__init__()
        # print(number_of_inputs, neuron_l1, neuron_l2)
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
        # print(out1.shape)
        out2 = F.dropout(self.relu(self.bn2(self.l2(out1))), self.drop_rate)
        # print(out2.shape)
        # print("BURAYA ")
        return out2
