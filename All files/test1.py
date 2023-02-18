import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import numpy as np

# Load the MNIST dataset
mnist_train = data.DataLoader(
    data.MNIST(root='.', train=True, download=True, transform=transforms.Compose([
        transforms.ToTensor(), # Convert images to tensors
        transforms.Normalize((0.1307,), (0.3081,)) # Normalize images
    ])), batch_size=batch_size, shuffle=True)

mnist_test = data.DataLoader(
    data.MNIST(root='.', train=False, download=True, transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])), batch_size=batch_size, shuffle=True)

# Define the model
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

model = Net()

# Define the loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)

# Train the model
def train(epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(mnist_train):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(mnist_train.dataset),
                100. * batch_idx / len(mnist_train), loss.item()))

# Evaluate the model
def test():
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in mnist_test:
            output = model(data)
            test_loss += criterion(output, target).item()
            pred = output.max(1, keepdim=True)[1]
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(mnist_test.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(mnist_test.dataset),
        100. * correct / len(mnist_test.dataset)))

for epoch in range(1, epochs + 1):
    train(epoch)
    test()

# Fine-tune the model
for epoch in range(1, epochs + 1):
    train(epoch)
    test()
