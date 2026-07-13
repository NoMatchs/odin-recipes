"""
Titanic 数据分析 + 机器学习完整流程（修复版）
使用模拟数据，无需联网
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("=" * 60)
print("第1步：生成模拟数据")
print("=" * 60)

# ---------- 1. 生成模拟数据 ----------
np.random.seed(42)
n = 891  # Titanic 原始数据有 891 条

# 修复：确保所有概率加起来 = 1
data = {
    'survived': np.random.choice([0, 1], n, p=[0.62, 0.38]),
    'pclass': np.random.choice([1, 2, 3], n, p=[0.24, 0.21, 0.55]),
    'sex': np.random.choice(['male', 'female'], n, p=[0.65, 0.35]),
    'age': np.random.normal(30, 14, n).astype(int),
    'sibsp': np.random.choice([0, 1, 2, 3, 4, 5], n, p=[0.60, 0.20, 0.10, 0.05, 0.03, 0.02]),  # 修复：概率和=1
    'parch': np.random.choice([0, 1, 2, 3, 4, 5], n, p=[0.70, 0.15, 0.08, 0.04, 0.02, 0.01]),  # 修复：概率和=1
    'fare': np.random.exponential(32, n),
    'embarked': np.random.choice(['C', 'Q', 'S'], n, p=[0.19, 0.09, 0.72])
}

df = pd.DataFrame(data)

# 制造一些缺失值
df.loc[np.random.choice(n, 150, replace=False), 'age'] = np.nan
df.loc[np.random.choice(n, 50, replace=False), 'embarked'] = np.nan

print(f"✅ 数据集已生成，形状: {df.shape}")
print(f"列名: {df.columns.tolist()}")
print("\n前5行数据预览:")
print(df.head())

# ---------- 2. 数据探索 ----------
print("\n" + "=" * 60)
print("第2步：数据探索（EDA）")
print("=" * 60)

print("\n2.1 数据基本信息:")
print(df.info())

print("\n2.2 描述性统计:")
print(df.describe())

print("\n2.3 缺失值统计:")
missing = df.isnull().sum()
print(missing[missing > 0])

# 可视化缺失值
plt.figure(figsize=(10, 4))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
plt.title('缺失值热力图')
plt.tight_layout()
plt.savefig('01_missing_values.png', dpi=150)
print("✅ 缺失值热力图已保存: 01_missing_values.png")

# ---------- 3. 数据可视化 ----------
print("\n" + "=" * 60)
print("第3步：数据可视化")
print("=" * 60)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
sns.countplot(x='sex', hue='survived', data=df)
plt.title('性别与存活率')
plt.xlabel('性别')
plt.ylabel('人数')
plt.legend(['遇难', '幸存'])

plt.subplot(1, 3, 2)
sns.countplot(x='pclass', hue='survived', data=df)
plt.title('舱位与存活率')
plt.xlabel('舱位等级')
plt.ylabel('人数')
plt.legend(['遇难', '幸存'])

plt.subplot(1, 3, 3)
df['age'].hist(bins=30, edgecolor='black')
plt.title('年龄分布')
plt.xlabel('年龄')
plt.ylabel('人数')

plt.tight_layout()
plt.savefig('02_visualization.png', dpi=150)
print("✅ 可视化图表已保存: 02_visualization.png")

# ---------- 4. 数据清洗 ----------
print("\n" + "=" * 60)
print("第4步：数据清洗")
print("=" * 60)

df_clean = df.copy()

# 4.1 处理缺失值
print("4.1 处理缺失值...")
df_clean['age'].fillna(df_clean['age'].median(), inplace=True)
df_clean['embarked'].fillna(df_clean['embarked'].mode()[0], inplace=True)
print(f"   - age 缺失值已用中位数 {df_clean['age'].median()} 填充")
print(f"   - embarked 缺失值已用众数 '{df_clean['embarked'].mode()[0]}' 填充")

# ---------- 5. 特征工程 ----------
print("\n" + "=" * 60)
print("第5步：特征工程")
print("=" * 60)

# 5.1 编码分类变量
le_sex = LabelEncoder()
df_clean['sex_encoded'] = le_sex.fit_transform(df_clean['sex'])

# 5.2 创建新特征
df_clean['family_size'] = df_clean['sibsp'] + df_clean['parch'] + 1
df_clean['is_alone'] = (df_clean['family_size'] == 1).astype(int)

print(f"✅ 新增特征: sex_encoded, family_size, is_alone")
print(f"\n清洗后数据前5行:")
print(df_clean[['sex', 'sex_encoded', 'sibsp', 'parch', 'family_size', 'is_alone']].head())

# ---------- 6. 准备训练数据 ----------
print("\n" + "=" * 60)
print("第6步：准备训练数据")
print("=" * 60)

feature_cols = ['pclass', 'age', 'fare', 'sex_encoded', 'family_size', 'is_alone']
X = df_clean[feature_cols]
y = df_clean['survived']

print(f"特征矩阵 X 形状: {X.shape}")
print(f"目标向量 y 形状: {y.shape}")
print(f"\n特征列: {feature_cols}")

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\n训练集: {X_train.shape[0]} 条")
print(f"测试集: {X_test.shape[0]} 条")

# ---------- 7. 训练模型 ----------
print("\n" + "=" * 60)
print("第7步：训练随机森林模型")
print("=" * 60)

model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train, y_train)

print("✅ 模型训练完成")

# ---------- 8. 模型评估 ----------
print("\n" + "=" * 60)
print("第8步：模型评估")
print("=" * 60)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"✅ 模型准确率: {accuracy:.4f}")

print("\n分类报告:")
print(classification_report(y_test, y_pred))

# ---------- 9. 特征重要性 ----------
print("\n" + "=" * 60)
print("第9步：特征重要性分析")
print("=" * 60)

importance = pd.DataFrame({
    '特征': feature_cols,
    '重要性': model.feature_importances_
}).sort_values('重要性', ascending=False)

print(importance)

# 可视化特征重要性
plt.figure(figsize=(8, 5))
sns.barplot(x='重要性', y='特征', data=importance)
plt.title('特征重要性')
plt.tight_layout()
plt.savefig('03_feature_importance.png', dpi=150)
print("✅ 特征重要性图已保存: 03_feature_importance.png")

# ---------- 10. 混淆矩阵 ----------
print("\n" + "=" * 60)
print("第10步：混淆矩阵")
print("=" * 60)

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('混淆矩阵')
plt.xlabel('预测值')
plt.ylabel('真实值')
plt.tight_layout()
plt.savefig('04_confusion_matrix.png', dpi=150)
print("✅ 混淆矩阵已保存: 04_confusion_matrix.png")

print("\n" + "=" * 60)
print("🎉 项目运行完成！")
print("=" * 60)
print("\n生成的文件:")
print("  1. 01_missing_values.png - 缺失值热力图")
print("  2. 02_visualization.png - 数据可视化图表")
print("  3. 03_feature_importance.png - 特征重要性")
print("  4. 04_confusion_matrix.png - 混淆矩阵")