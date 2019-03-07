import os, sys
import re
import string
import pathlib
import random
from collections import Counter, OrderedDict
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import spacy
from tqdm import tqdm, tqdm_notebook, tnrange
tqdm.pandas(desc='Progress')

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
from torch.autograd import Variable

from sklearn.model_selection import StratifiedShuffleSplit, train_test_split
from sklearn.metrics import accuracy_score

import warnings
warnings.filterwarnings('ignore')

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity='all'


print('Python version:',sys.version)
print('Pandas version:',pd.__version__)
print('Pytorch version:', torch.__version__)
print('Spacy version:', spacy.__version__)

data_root = pathlib.Path('./data')

df = pd.read_csv(data_root/'Sentiment Analysis Dataset.csv', error_bad_lines=False)[:20000]
print(df.shape)
print(df.head())
# show label distribution
print(df.Sentiment.value_counts())
fig = plt.figure(figsize=(8,5))
ax = sns.barplot(x=df.Sentiment.unique(),y=df.Sentiment.value_counts());
ax.set(xlabel='Labels');
# load spacy tokenizer
nlp = spacy.load('en',disable=['parser', 'tagger', 'ner'])

nlp(df.SentimentText.values[0])
# remove leading and trailing spaces
df['SentimentText'] = df.SentimentText.progress_apply(lambda x: x.strip())

# Use Counter to calculate the frequency of the unique words¶
words = Counter()
for sent in tqdm_notebook(df.SentimentText.values):
    words.update(w.text.lower() for w in nlp(sent))

print(len(words))
print(words.most_common(20))

words = sorted(words, key=words.get, reverse=True)
print(words[:20])
words = ['_PAD','_UNK'] + words
print(words[:10])


word2idx = {o:i for i,o in enumerate(words)}
idx2word = {i:o for i,o in enumerate(words)}

def indexer(s): return [word2idx[w.text.lower()] for w in nlp(s)]

df['sentimentidx'] = df.SentimentText.apply(indexer)
print(df.head())

df['lengths'] = df.sentimentidx.apply(len)
print(df.head())
# Plot the frequency distribution of the lengths of the tokenized tweets
fig = plt.figure(figsize=(8,5))
ax = sns.distplot(df.lengths.values,kde=False);
ax.set(xlabel='Tweet Length', ylabel='Frequency');

"""
class VectorizeData(Dataset):
    def __init__(self, df_path):
        self.df = pd.read_csv(df_path, error_bad_lines=False)[:20000]
        self.df['SentimentText'] = self.df.SentimentText.apply(lambda x: x.strip())
        self.df['sentimentidx'] = self.df.SentimentText.apply(indexer)

    def __len__(self):
        return self.df.shape[0]

    def __getitem__(self, idx):
        X = self.df.sentimentidx[idx]
        y = self.df.Sentiment[idx]
        return X, y

ds = VectorizeData(data_root/'Sentiment Analysis Dataset.csv')
print(len(ds))
print(ds[:4])

dl = DataLoader(dataset=ds, batch_size=3)
print('Total batches', len(dl))


it = iter(dl)
xs,ys = next(it)
xs,ys = next(it)
print('Samples in batch', len(xs))
print(type(xs))
print(xs)
print(ys)
"""


class VectorizeData(Dataset):
    def __init__(self, df_path, maxlen=10):
        self.maxlen = maxlen
        self.df = pd.read_csv(df_path, error_bad_lines=False)[:20000]
        self.df['SentimentText'] = self.df.SentimentText.apply(lambda x: x.strip())
        print('Indexing...')
        self.df['sentimentidx'] = self.df.SentimentText.progress_apply(indexer)
        print('Calculating lengths')
        self.df['lengths'] = self.df.sentimentidx.progress_apply(
            lambda x: self.maxlen if len(x) > self.maxlen else len(x))
        print('Padding')
        self.df['sentimentpadded'] = self.df.sentimentidx.progress_apply(self.pad_data)
        print(df)
    def __len__(self):
        return self.df.shape[0]

    def __getitem__(self, idx):
        X = self.df.sentimentpadded[idx]
        lens = self.df.lengths[idx]
        y = self.df.Sentiment[idx]
        return X, y, lens

    def pad_data(self, s):
        padded = np.zeros((self.maxlen,), dtype=np.int64)
        if len(s) > self.maxlen:
            padded[:] = s[:self.maxlen]
        else:
            padded[:len(s)] = s
        return padded
ds = VectorizeData(data_root/'Sentiment Analysis Dataset.csv')
print("ds",ds)
dl = DataLoader(ds, batch_size=3)
print('Total batches', len(dl))

it = iter(dl)
xs,ys,lens =  next(it)


print(type(xs))
print(xs)

print('Labels:',ys)
print('Lengths:',lens)

vocab_size = len(words)
embedding_dim = 4
n_hidden = 5
n_out = 2


class SimpleGRU(nn.Module):
    def __init__(self, vocab_size, embedding_dim, n_hidden, n_out):
        super().__init__()
        self.vocab_size, self.embedding_dim, self.n_hidden, self.n_out = vocab_size, embedding_dim, n_hidden, n_out
        self.emb = nn.Embedding(self.vocab_size, self.embedding_dim)
        self.gru = nn.GRU(self.embedding_dim, self.n_hidden)
        self.out = nn.Linear(self.n_hidden, self.n_out)

    def forward(self, seq, lengths, gpu=True):
        # print('Sequence shape', seq.shape)
        if int(seq[:,0][-1])==0:
            print(seq[:,0], int(seq[:,0][-1]), lengths[0])
        #print('Lengths', lengths)
        bs = seq.size(1)  # batch size
        #print('batch size', bs)
        self.h = self.init_hidden(bs, gpu)  # initialize hidden state of GRU
        #print('Inititial hidden state shape', self.h.shape)
        # print(seq[-1], lengths[-1])
        embs = self.emb(seq)


        embs = pack_padded_sequence(embs, lengths)  # unpad
        print(embs)
        gru_out, self.h = self.gru(embs,
                                   self.h)  # gru returns hidden state of all timesteps as well as hidden state at last timestep
        gru_out, lengths = pad_packed_sequence(gru_out)  # pad the sequence to the max length in the batch
        #print('GRU output(all timesteps)', gru_out.shape)
        #print(gru_out)
        #print('GRU last timestep output')
        #print(gru_out[-1])
        #print('Last hidden state', self.h)
        # since it is as classification problem, we will grab the last hidden state
        outp = self.out(self.h[-1])  # self.h[-1] contains hidden state of last timestep
        return F.log_softmax(outp, dim=-1)

    def init_hidden(self, batch_size, gpu):
        if gpu:
            return Variable(torch.zeros((1, batch_size, self.n_hidden)))
        else:
            return Variable(torch.zeros((1, batch_size, self.n_hidden)))

m = SimpleGRU(vocab_size, embedding_dim, n_hidden, n_out)

print(m)

def sort_batch(X, y, lengths):
    lengths, indx = lengths.sort(dim=0, descending=True)
    X = X[indx]
    y = y[indx]
    return X.transpose(0,1), y, lengths # transpose (batch x seq) to (seq x batch)


dl = DataLoader(ds, batch_size=3)
it = iter(dl)
xs,ys,lens =  next(it)

xs,ys,lens = sort_batch(xs,ys,lens)
outp = m(xs,lens.cpu().numpy(), gpu=False) # last non zero values from gru is same as hidden output by gru

print(outp)

torch.max(outp, dim=1)

print(ys.shape)


print(F.nll_loss(outp, Variable(ys)))


def fit(model, train_dl, val_dl, loss_fn, opt, epochs=3):
    num_batch = len(train_dl)
    for epoch in tnrange(epochs):
        y_true_train = list()
        y_pred_train = list()
        total_loss_train = 0

        if val_dl:
            y_true_val = list()
            y_pred_val = list()
            total_loss_val = 0

        t = tqdm_notebook(iter(train_dl), leave=False, total=num_batch)
        for X, y, lengths in t:
            t.set_description(f'Epoch {epoch}')
            X, y, lengths = sort_batch(X, y, lengths)
            X = Variable(X)
            y = Variable(y)
            lengths = lengths.numpy()

            opt.zero_grad()
            pred = model(X, lengths, gpu=True)
            loss = loss_fn(pred, y)
            loss.backward()
            opt.step()

            t.set_postfix(loss=loss.data[0])
            pred_idx = torch.max(pred, dim=1)[1]

            y_true_train += list(y.cpu().data.numpy())
            y_pred_train += list(pred_idx.cpu().data.numpy())
            total_loss_train += loss.data[0]

        train_acc = accuracy_score(y_true_train, y_pred_train)
        train_loss = total_loss_train / len(train_dl)
        print(f' Epoch {epoch}: Train loss: {train_loss} acc: {train_acc}')

        if val_dl:
            for X, y, lengths in tqdm_notebook(valdl, leave=False):
                X, y, lengths = sort_batch(X, y, lengths)
                X = Variable(X)
                y = Variable(y)
                pred = model(X, lengths.numpy())
                loss = loss_fn(pred, y)
                pred_idx = torch.max(pred, 1)[1]
                y_true_val += list(y.cpu().data.numpy())
                y_pred_val += list(pred_idx.cpu().data.numpy())
                total_loss_val += loss.data[0]
            valacc = accuracy_score(y_true_val, y_pred_val)
            valloss = total_loss_val / len(valdl)
            print(f'Val loss: {valloss} acc: {valacc}')

train_dl = DataLoader(ds, batch_size=512)
print(train_dl)
m = SimpleGRU(vocab_size, embedding_dim, n_hidden, n_out)
opt = optim.Adam(m.parameters(), 1e-2)
fit(model=m, train_dl=train_dl, val_dl=None, loss_fn=F.nll_loss, opt=opt, epochs=4)
