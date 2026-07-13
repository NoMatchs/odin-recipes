"""
深度学习入门：MNIST 手写数字识别
使用 PyTorch 构建神经网络，在 GPU 上训练
"""
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
from torch.utils.data import DataLoader

# 设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"✅ 使用设备: {device}")

# ============================================
# 第1步：加载数据
# ============================================
print("\n" + "="*60)
print("第1步：加载 MNIST 数据集")
print("="*60)

# 数据预处理：转为张量 + 归一化
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # 归一化到 [-1, 1]
])

# 下载训练集和测试集
train_dataset = torchvision.datasets.MNIST(
    root='./data', train=True, download=True, transform=transform
)
test_dataset = torchvision.datasets.MNIST(
    root='./data', train=False, download=True, transform=transform
)

# 创建数据加载器（批量读取）
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

print(f"✅ 训练集大小: {len(train_dataset)} 张图片")
print(f"✅ 测试集大小: {len(test_dataset)} 张图片")
print(f"✅ 图片尺寸: {train_dataset[0][0].shape}")

# 查看几张样本图片
fig, axes = plt.subplots(1, 6, figsize=(12, 3))
for i in range(6):
    img, label = train_dataset[i]
    axes[i].imshow(img.squeeze(), cmap='gray')
    axes[i].set_title(f'数字: {label}')
    axes[i].axis('off')
plt.savefig('01_mnist_samples.png', dpi=150)
print("✅ 样本图片已保存: 01_mnist_samples.png")

# ============================================
# 第2步：定义神经网络模型
# ============================================
print("\n" + "="*60)
print("第2步：定义神经网络模型")
print("="*60)

class SimpleNN(nn.Module):
    """一个简单的全连接神经网络"""
    def __init__(self):
        super(SimpleNN, self).__init__()
        # 输入: 28x28 = 784 个像素
        self.fc1 = nn.Linear(28 * 28, 128)   # 第一层: 784 -> 128
        self.fc2 = nn.Linear(128, 64)        # 第二层: 128 -> 64
        self.fc3 = nn.Linear(64, 10)         # 输出层: 64 -> 10 (10个数字)
        self.relu = nn.ReLU()                # 激活函数
        self.dropout = nn.Dropout(0.2)       # 防止过拟合

    def forward(self, x):
        # 将图片展平为一维向量
        x = x.view(-1, 28 * 28)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)  # 输出层不需要激活，CrossEntropyLoss 自带 softmax
        return x

model = SimpleNN().to(device)
print(f"✅ 模型结构:")
print(model)

# 统计模型参数数量
total_params = sum(p.numel() for p in model.parameters())
print(f"✅ 模型总参数: {total_params:,} 个")

# ============================================
# 第3步：定义损失函数和优化器
# ============================================
print("\n" + "="*60)
print("第3步：训练准备")
print("="*60)

criterion = nn.CrossEntropyLoss()  # 多分类损失函数
optimizer = optim.Adam(model.parameters(), lr=0.001)  # 优化器

print(f"✅ 损失函数: CrossEntropyLoss")
print(f"✅ 优化器: Adam (学习率: 0.001)")

# ============================================
# 第4步：训练模型
# ============================================
print("\n" + "="*60)
print("第4步：开始训练")
print("="*60)

num_epochs = 5  # 训练轮数
train_losses = []

for epoch in range(num_epochs):
    model.train()  # 切换到训练模式
    running_loss = 0.0
    
    for batch_idx, (images, labels) in enumerate(train_loader):
        # 把数据放到 GPU
        images, labels = images.to(device), labels.to(device)
        
        # 前向传播
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # 反向传播
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
    
    avg_loss = running_loss / len(train_loader)
    train_losses.append(avg_loss)
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {avg_loss:.4f}")

print("✅ 训练完成！")

# 绘制训练损失曲线
plt.figure(figsize=(8, 5))
plt.plot(range(1, num_epochs+1), train_losses, 'b-o')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('训练损失曲线')
plt.grid(True)
plt.savefig('02_training_loss.png', dpi=150)
print("✅ 训练损失曲线已保存: 02_training_loss.png")

# ============================================
# 第5步：评估模型
# ============================================
print("\n" + "="*60)
print("第5步：评估模型")
print("="*60)

model.eval()  # 切换到评估模式
correct = 0
total = 0
all_preds = []
all_labels = []

with torch.no_grad():  # 不计算梯度，节省内存
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        
        all_preds.extend(predicted.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())

accuracy = 100 * correct / total
print(f"✅ 测试集准确率: {accuracy:.2f}%")

# ============================================
# 第6步：可视化预测结果
# ============================================
print("\n" + "="*60)
print("第6步：可视化预测结果")
print("="*60)

# 显示一些预测结果
fig, axes = plt.subplots(2, 5, figsize=(12, 6))
axes = axes.flatten()

for i in range(10):
    img, label = test_dataset[i]
    img_tensor = img.unsqueeze(0).to(device)
    
    with torch.no_grad():
        output = model(img_tensor)
        _, predicted = torch.max(output, 1)
    
    axes[i].imshow(img.squeeze(), cmap='gray')
    axes[i].set_title(f'真实: {label} | 预测: {predicted.item()}')
    axes[i].axis('off')

plt.tight_layout()
plt.savefig('03_predictions.png', dpi=150)
print("✅ 预测结果图已保存: 03_predictions.png")

# ============================================
# 第7步：保存模型
# ============================================
print("\n" + "="*60)
print("第7步：保存模型")
print("="*60)

torch.save(model.state_dict(), 'mnist_model.pth')
print("✅ 模型已保存: mnist_model.pth")

print("\n" + "="*60)
print("🎉 深度学习项目完成！")
print("="*60)
print("\n生成的文件:")
print("  1. 01_mnist_samples.png - 样本图片")
print("  2. 02_training_loss.png - 训练损失曲线")
print("  3. 03_predictions.png - 预测结果")
print("  4. mnist_model.pth - 训练好的模型权重")