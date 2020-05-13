# %% basics
import matplotlib.pyplot as plt
from torchvision import transforms, datasets
import torchvision
import torch

# inputs also known as features or x
# hidden layers. No control, machine sets this value hence hidden

x = torch.zeros([2, 5])
print(x)
print(x.shape)
# %%

y = torch.rand([2, 5])
print(y)

y = y.view([1, 10])
y
# %% neural network input. example with some datasets


# pre processing data for the machine to digest
train = datasets.MNIST('', train=True, download=True, transform=transforms.Compose([
    transforms.ToTensor()
]))

test = datasets.MNIST('', train=False, download=True, transform=transforms.Compose([
    transforms.ToTensor()
]))

# iteration of the data
trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
testset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=False)


for data in trainset:
    print(data)
    x, y = data[0][0], data[1][0]
    print(data[1])

    # look at data
    plt.imshow(data[0][0].view(28, 28))
    plt.show()

    break

# iterate and count the data. To check for imabalance

total = 0
counter_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for data in trainset:
    xs,ys= data 
    for y in ys:
        counter_dict[int(y)] +=1
        total += 1
        
print(counter_dict)

for i in counter_dict:
    print(f"{i}: {counter_dict[i]/total*100.0}%")
#%% creating neural network
import torch 
import torchvision 
from torchvision import transforms, datasets
## pre processing
train = datasets.MNIST('', train=True, download=True, transform=transforms.Compose([
    transforms.ToTensor()
]))

test= datasets.MNIST('', train=False, download=True, transform=transforms.Compose([
    transforms.ToTensor()
]))
## iteration
trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
testset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=False)

import torch.nn as nn
import torch.nn.functional as F

##inheritance and run the init method with super().__init__()

class Net(nn.Module):
    def __init__(self):

        super().__init__()
        self.fc1 = nn.Linear(28*28, 64) #input 28x28 image with 64 connection  
        self.fc2 = nn.Linear(64,64)
        self.fc3 = nn.Linear(64,64)
        self.fc4 = nn.Linear(64,10) # output 10 for numbers 1-10

    # how data passes through  
    # relu activation func keeps data scaled btween 0 - 1
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x

net = Net()
print(net)

X = torch.randn((28,28))
X = X.view(-1,28*28)

output= net(X)

print(output)
# %% training neurai networks 
import torch
import torchvision
from torchvision import transforms, datasets
import torch.nn as nn
import torch.nn.functional as F

train = datasets.MNIST('', train=True, download=True,
                       transform=transforms.Compose([
                           transforms.ToTensor()
                       ]))

test = datasets.MNIST('', train=False, download=True,
                       transform=transforms.Compose([
                           transforms.ToTensor()
                       ]))


trainset = torch.utils.data.DataLoader(train, batch_size=10, shuffle=True)
testset = torch.utils.data.DataLoader(test, batch_size=10, shuffle=False)
REBUILD_DATA = True

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28*28, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 64)
        self.fc4 = nn.Linear(64, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return F.log_softmax(x, dim=1)

net = Net()
print(net)

import torch.optim as optim

loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(net.parameters(), lr=0.001)


for epoch in range(3): # 3 full passes over the data
    for data in trainset:  # `data` is a batch of data
        X, y = data  # X is the batch of features, y is the batch of targets.
        net.zero_grad()  # sets gradients to 0 before loss calc. You will do this likely every step.
        output = net(X.view(-1,784))  # pass in the reshaped batch (recall they are 28x28 atm)
        loss = F.nll_loss(output, y)  # calc and grab the loss value
        loss.backward()  # apply this loss backwards thru the network's parameters
        optimizer.step()  # attempt to optimize weights to account for loss/gradients
    print(loss)  # print loss. We hope

correct = 0
total = 0

with torch.no_grad():
    for data in testset:
        X, y = data
        output = net(X.view(-1,784))
        #print(output)
        for idx, i in enumerate(output):
            #print(torch.argmax(i), y[idx])
            if torch.argmax(i) == y[idx]:
                correct += 1
            total += 1

print("Accuracy: ", round(correct/total, 3))

#%% convol nn

import os
import cv2
import numpy as np
from tqdm import tqdm

REBUILD_DATA = True

class DogVsCats():
    IMG_SIZE = 50
    CATS =  "PetImages/Cat"
    DOGS = "PetImages/Dog"
    Testing = "PetImages/training"
    LABELS = {CATS: 0, DOGS: 1}
    training_data = [] 

    catcount = 0
    dogcount = 0 

    def make_training_data(self):
        for label in self.LABELS:
            for f in tqdm(os.listdir(label)):
                try:
                    if "jpg" in f:
                        path = os.path.join(label,f)
                        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                        img = cv2.resize(img, (self.IMG_SIZE, self.IMG_SIZE))
                        self.training_data.append([np.array(img), np.eye(2)[self.LABELS[label]]])
                        if label == self.CATS:
                            self.catcount += 1
                        elif label == self.DOGS:
                            self.dogcount += 1
                except Exception as e:
                    pass
        np.random.shuffle(self.training_data)
        np.save("training_Data.npy", self.training_data)

if REBUILD_DATA:
    dogsvscats = DogVsCats()
    dogsvscats.make_training_data()
    print("CATS:", dogsvscats.catcount)
    print("DOGS: ", dogsvscats.dogcount)
