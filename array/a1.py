import torch
import numpy as np

n = torch.tensor([1, 2, 3])
print(n)
x = torch.arange(12).reshape(3, 4)
print(x[-1])
print(x[:, 1])
print(n.dot(x[:, 1]))  # 1*1 + 2*5 + 3*9 = 38
