import os
import torch
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, datasets
import torchvision
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import torch.nn as nn
import torch.nn.functional as F
from math import log
import sys

model = sys.argv[1]
epochs = int(sys.argv[2])

def train_model(model, dataloaders, dataset_sizes, criterion, optimizer, scheduler, use_gpu, num_epochs=25, mixup = False, alpha = 0.1):
    #print("MIXUP".format(mixup))
    from torch.autograd import Variable

    import numpy as np
    import time
    import os
    from tqdm import tqdm
    from sklearn.metrics import accuracy_score
    import pandas as pd

    since = time.time()

    best_model_wts = model.state_dict()
    best_acc = 0.0

    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-' * 10)

        # Each epoch has a training and validation phase
        for phase in ['train', 'val']:
            if phase == 'train':
                scheduler.step()
                model.train(True)  # Set model to training mode
            else:
                model.train(False)  # Set model to evaluate mode

            running_loss = 0.0
            running_corrects = 0

            # Iterate over data.
            for data in tqdm(dataloaders[phase]):
                # get the inputs
                inputs, labels = data
                #print(inputs.shape)
                #print(labels.shape)

                #augementation using mixup
                #if phase == 'train' and mixup:
                #    inputs = mixup_batch(inputs, alpha)
                # wrap them in Variable
                if use_gpu:
                    inputs = Variable(inputs.cuda())
                    labels = Variable(labels.cuda())
                else:
                    inputs, labels = Variable(inputs), Variable(labels)
			
                # zero the parameter gradients
                optimizer.zero_grad()

                # forward
                outputs = model(inputs)
                if type(outputs) == tuple:
                    outputs, _ = outputs
                _, preds = torch.max(outputs.data, 1)
                loss = criterion(outputs, labels)
                #print(outputs)
                # backward + optimize only if in training phase
                if phase == 'train':
                    loss.backward()
                    optimizer.step()

                # statistics
                running_loss += loss.data[0]
                running_corrects += torch.sum(preds == labels.data)
            print(running_corrects.item())
            print(dataset_sizes[phase])
            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = float(running_corrects.item()) / dataset_sizes[phase]
            print(epoch_acc)
            print('{} Loss: {:.4f} Acc: {:.4f}'.format(
                phase, epoch_loss, epoch_acc))

            # deep copy the model
            if phase == 'val' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = model.state_dict()


        print()

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(
        time_elapsed // 60, time_elapsed % 60))
    print('Best val Acc: {:4f}'.format(best_acc))

    # load best model weights
    model.load_state_dict(best_model_wts)
    return model



data_dir = "/Users/trman/OneDrive/Projects/DEEPScreen/tempImage/FamilySpecificFigures/nuclearreceptor_test"
input_shape = 200
batch_size = 32
mean = [0.5, 0.5, 0.5]
std = [0.5, 0.5, 0.5]
use_gpu = torch.cuda.is_available()
if use_gpu:
	print("CUDA is available on this device!")


resize_param = 0

if model=="inception":
    resize_param = 299
elif model=="resnet" or model=="densenet":
    resize_param = 224


data_transforms = {
        'train': transforms.Compose([
        transforms.Resize(resize_param),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)]),
        'val': transforms.Compose([
        transforms.Resize(resize_param),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)]),}

image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                                      data_transforms[x]) for x in ['train', 'val']}

dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=batch_size,
                                         shuffle=True) for x in ['train', 'val']}

dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}
class_names = image_datasets['train'].classes
n_class = len(class_names)
#print(image_datasets["train"])
#print(dataset_sizes)

print("Number of classes:\t{}".format(n_class))
print(class_names)

weights = []
for cls in class_names:
    weights.append(len(os.listdir(os.path.join(data_dir,"train",cls))))
#print(weights)
weights = [log(c) for c in weights]

#print(weights)
smallest_class = min(weights)
weights = torch.Tensor([smallest_class/c for c in weights])
#print(weights)
if use_gpu:
    weights = weights.cuda()
print(weights)

model_conv = None

if model=="inception":
    model_conv = torchvision.models.inception_v3()
    num_ftrs = model_conv.fc.in_features
    # print(num_ftrs, n_class)
    model_conv.fc = nn.Linear(num_ftrs, n_class)
    if use_gpu:
        model_conv.fc = nn.Linear(num_ftrs, n_class).cuda()

elif model=="resnet":
    model_conv = torchvision.models.resnet50()
    num_ftrs = model_conv.fc.in_features
    #print(num_ftrs, n_class)
    model_conv.fc = nn.Linear(num_ftrs, n_class)
    if use_gpu:
        model_conv.fc = nn.Linear(num_ftrs, n_class).cuda()
elif model=="densenet":
    model_conv = torchvision.models.densenet121()
    num_ftrs = model_conv.classifier.in_features
    model_conv.classifier = nn.Linear(num_ftrs, n_class)
    if use_gpu:
        model_conv.classifier = nn.Linear(num_ftrs, n_class).cuda()


if use_gpu:
	model_conv = model_conv.cuda()


#print("[Using CrossEntropyLoss...]")
criterion = nn.CrossEntropyLoss(weight=weights)

#print("[Using small learning rate with momentum...]")
optimizer_conv = optim.SGD(list(filter(lambda p: p.requires_grad, model_conv.parameters())), lr=0.001, momentum=0.9)

#print("[Creating Learning rate scheduler...]")
exp_lr_scheduler = lr_scheduler.StepLR(optimizer_conv, step_size=7, gamma=0.1)

#print("[Training the model begun ....]")
# train_model function is here: https://github.com/Prakashvanapalli/pytorch_classifiers/blob/master/tars/tars_training.py
model_ft = train_model(model_conv, dataloaders, dataset_sizes, criterion, optimizer_conv, exp_lr_scheduler, use_gpu,
                     num_epochs=epochs)

"""
class Net(nn.Module):


    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 47 * 47, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 27)

    def forward(self, x):
        #print("shape of you ",x.shape)
        x = self.pool(F.relu(self.conv1(x)))
        #print("shape of you 2", x.shape)
        x = self.pool(F.relu(self.conv2(x)))
        #print("shape of you 3", x.shape)
        x = x.view(-1, 16 * 47 * 47)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


net = Net()

import torch.optim as optim

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

print('Finished Training')

for epoch in range(10):
    phase = "train"
    running_loss = 0.0
    for data in dataloaders[phase]:
        # get the inputs
        inputs, labels = data
        #print(inputs.shape)
        #print(labels.shape)

        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
    print("Epoch {} Loss:\t{}".format(epoch, running_loss))

    phase = "val"
    correct = 0
    total = 0
    for data in dataloaders[phase]:
        # get the inputs

        inputs, labels = data
        # print(inputs.shape)
        # print(labels.shape)
        outputs = net(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        print(correct, total)
    print('Validation accuracy of the network: %d %%' % (100 * correct / total))

    phase = "train"
    correct = 0
    total = 0
    for data in dataloaders[phase]:
        # get the inputs

        inputs, labels = data
        # print(inputs.shape)
        # print(labels.shape)
        outputs = net(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        print(correct, total)
    print('Training accuracy of the network: %d %%' % (100 * correct / total))
"""
