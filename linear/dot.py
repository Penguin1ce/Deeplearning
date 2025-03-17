import torch

# 向量点乘
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
dot_product = torch.dot(a, b)
print(dot_product)  # 输出：32 = 1*4 + 2*5 + 3*6

# 矩阵点乘
A = torch.tensor([[1, 2], [3, 4]])
B = torch.tensor([[5, 6], [7, 8]])
matrix_dot_product = torch.matmul(A, B)
print(matrix_dot_product)  # 输出：
# tensor([[19, 22],
#         [43, 50]])

# 也可以使用 @ 运算符
matrix_dot_product2 = A @ B
print(matrix_dot_product2)
print(matrix_dot_product2 == matrix_dot_product)
