import torch
X = torch.normal(0, 1, (5, 1))
print(X)
y = torch.tensor([1.2, 2.3, 3.4, 4.5, 5.6])
print(y)
print(y.shape)
y = y.reshape((-1, 1))
print(y)
print(y.shape)
for i in range(5):
    print(i)