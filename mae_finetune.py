import torch
import torch.nn as nn
import torch.nn.functional as F

class VideoFinetune(nn.Module):
  def __init__(self, num_layers):
    super(VideoFinetune, self).__init__()
    assert num_layers > 3
    self.layers = []

    size = 1024

    self.fc = nn.Linear(1408, size)
    self.layers.append(self.fc)
    for i in range(num_layers-4):
      self.layers.append(nn.Linear(1024,1024))

    self.layers.append(nn.Linear(1024, 512))
    self.layers.append(nn.Linear(512, 512))
    self.layers.append(nn.Linear(512,1))
  def forward(self, x):
    x = self.layers[0](x)
    for i in range(1, len(self.layers)):
      x = F.relu(x)
      x = self.layers[i](x)
    output = F.sigmoid(x)
    return output

class VideoAudioFinetune(nn.Module):
  def __init__(self, num_layers):
    super(VideoAudioFinetune, self).__init__()
    assert num_layers > 3
    self.layers = []

    size = 1024

    self.fc = nn.Linear(2176, size)
    self.layers.append(self.fc)
    for i in range(num_layers-4):
      self.layers.append(nn.Linear(1024,1024))

    self.layers.append(nn.Linear(1024, 512))
    self.layers.append(nn.Linear(512, 512))
    self.layers.append(nn.Linear(512,1))
  def forward(self, x):
    x = self.layers[0](x)
    for i in range(1, len(self.layers)):
      x = F.relu(x)
      x = self.layers[i](x)
    output = F.sigmoid(x)
    return output


