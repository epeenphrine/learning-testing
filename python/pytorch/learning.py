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
    ## setup of nn
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28*28, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 64)
        self.fc4 = nn.Linear(64, 10)

    ## move data to each  nn 
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
## pre procesing. Flatten image, make it smaller,
import os
import cv2
import numpy as np
from tqdm import tqdm

import torch
import torch.nn as nn
import torch.nn.functional as F


REBUILD_DATA = True
class Net(nn.Module):
    def __init__(self):
        super().__init__() # just run the init of parent class (nn.Module)
        self.conv1 = nn.Conv2d(1, 32, 5) # input is 1 image, 32 output channels/convolution, 5x5 kernel / window
        self.conv2 = nn.Conv2d(32, 64, 5) # input is 32, bc the first layer output 32. Then we say the output will be 64 channels, 5x5 kernel / window
        self.conv3 = nn.Conv2d(64, 128, 5) # input is output from previous layers. 

        x = torch.randn(50,50).view(-1,1,50,50)
        self._to_linear = None
        self.convs(x)

        self.fc1 = nn.Linear(self._to_linear, 512) #flattening.
        self.fc2 = nn.Linear(512, 2) # 512 in, 2 out bc we're doing 2 classes (dog vs cat).

    def convs(self, x):
        # max pooling over 2x2
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv3(x)), (2, 2))

        if self._to_linear is None:
            self._to_linear = x[0].shape[0]*x[0].shape[1]*x[0].shape[2]
        return x

    def forward(self, x):
        x = self.convs(x)
        x = x.view(-1, self._to_linear)  # .view is reshape ... this flattens X before 
        x = F.relu(self.fc1(x))
        x = self.fc2(x) # bc this is our output layer. No activation here.
        return F.softmax(x, dim=1)


net = Net()

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
        np.save("training_data.npy", self.training_data)

if REBUILD_DATA:
    dogsvscats = DogVsCats()
    dogsvscats.make_training_data()
    print("CATS:", dogsvscats.catcount)
    print("DOGS: ", dogsvscats.dogcount)

# split into x and y and convert to tensor
import torch 

training_data = np.load("training_data.npy",allow_pickle=True)
print(training_data)
print(training_data.dtype)


import torch.optim as optim
optimizer = optim.Adam(net.parameters(), lr=0.001)
loss_function = nn.MSELoss()

X = torch.Tensor([i[0] for i in training_data]).view(-1,50,50)
X = X/255.0
y = torch.Tensor([i[1] for i in training_data])

# reverse 10 % of data for validation
VAL_PCT = 0.1 
val_size = int(len(X)*VAL_PCT)
print(val_size)


train_X = X[:-val_size]
train_y = y[:-val_size]

test_X = X[-val_size:]
test_y = y[-val_size:]

print(len (train_X), len(test_X))

## iterate over data to fit and test

BATCH_SIZE = 100
EPOCHS = 20

for epoch in range(EPOCHS):
    for i in tqdm(range(0, len(train_X), BATCH_SIZE)): # from 0, to the len of x, stepping BATCH_SIZE at a time. [:50] ..for now just to dev
        
        ##print(f"{i}:{i+BATCH_SIZE}")

        batch_X = train_X[i:i+BATCH_SIZE].view(-1,1,  50, 50)
        batch_y = train_y[i:i+BATCH_SIZE]

        net.zero_grad()
        outputs = net(batch_X)

        loss = loss_function(outputs, batch_y)
        loss.backward()
        optimizer.step()    # Does the update

    print(f"Epoch: {epoch}. Loss: {loss}")

# validation

correct = 0 
total = 0 

with torch.no_grad():
    for i in tqdm(range(len(test_X))):
        real_class = torch.argmax(test_y[i])
        net_out = net(test_X[i].view(-1, 1, 50, 50))[0] #return a list
        predicted_class = torch.argmax(net_out)

        if predicted_class == real_class:
            correct +=1
        total += 1

print(f"Accuracy: {round(correct/total, 3)}")
