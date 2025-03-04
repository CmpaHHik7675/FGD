import torch
import torch.nn as nn
import torch.optim as optim

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(10, 1)  

    def forward(self, x):
        return self.fc(x)

model = Net()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

inputs = torch.randn(1, 10)
target = torch.randn(1, 1)
output = model(inputs)
loss = criterion(output, target)
print("Початкова втрата:", loss.item())

loss.backward()
optimizer.step()

output = model(inputs)
loss = criterion(output, target)
print("Втрата після однієї ітерації:", loss.item())
