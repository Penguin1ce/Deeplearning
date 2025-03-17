import torch
import matplotlib.pyplot as plt

# 创建输入张量并启用梯度跟踪
x = torch.linspace(-5, 5, 100, requires_grad=True)
# 定义函数 y = x³ + 2x + 1
x1 = torch.tensor([0.0])
print(torch.sin(x1))
y = x**3 + 2 * x + 1
y1 = torch.sin(x)
# 计算梯度（自动求导）
print(torch.ones_like(x))
# y1.backward(torch.ones_like(x))  # 传入全1张量以计算各点梯度
y1.sum().backward()

# 转换为numpy数组用于绘图
x_np = x.detach().numpy()
y_np = y1.detach().numpy()
dy_np = x.grad.detach().numpy()

# 绘制函数和导函数图像
plt.figure(figsize=(10, 6))
plt.plot(x_np, y_np, label="function:$y = sin x$", color="blue")
plt.plot(
    x_np,
    dy_np,
    label="derivative:$\\frac{dy}{dx} = cos x$",
    color="orange",
    linestyle="--",
)

# 添加图表元素
plt.xlabel("x")
plt.ylabel("y")
plt.title("function and derivative")
plt.legend()
plt.grid(True)
plt.show()
