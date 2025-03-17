import torch
import numpy as np

Y = torch.arange(12).reshape(3, 4)
X = torch.tensor([[1, 2, 3, 1], [4, 5, 6, 2], [7, 8, 9, 1]])
z = torch.zeros_like(Y)
print("id(z):", id(z))
z[:] = X + Y
print("id(z):", id(z))

A = X.numpy()
B = torch.tensor(A)
print(type(A), type(B))
