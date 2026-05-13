#include <iostream>
using namespace std;

const int MAXN = 100;
int n, c;              // 物品数量、背包容量
int w[MAXN], p[MAXN];  // 物品重量、价值
int maxValue = 0;      // 最大价值
int currentValue = 0;  // 当前已选物品的价值
int currentWeight = 0; // 当前已选物品的重量

// 回溯法求解 0-1 背包
void Backtrack(int t)
{
    if (t > n)
    {
        // 所有物品处理完毕，更新最大价值
        if (currentValue > maxValue)
            maxValue = currentValue;
        return;
    }

    // 剪枝：当前重量 + 第 t 个物品重量 <= 背包容量，才尝试选这个物品
    if (currentWeight + w[t] <= c)
    {
        // 选第 t 个物品
        currentWeight += w[t];
        currentValue += p[t];
        Backtrack(t + 1);

        // 回溯：恢复状态
        currentWeight -= w[t];
        currentValue -= p[t];
    }

    // 不选第 t 个物品，直接处理下一个
    Backtrack(t + 1);
}

int main()
{
    cout << "请输入物品数量 n 和背包容量 c：";
    cin >> n >> c;

    cout << "请输入每个物品的重量和价值（格式：重量 价值）：" << endl;
    for (int i = 1; i <= n; i++)
    {
        cin >> w[i] >> p[i];
    }

    maxValue = 0;
    currentValue = 0;
    currentWeight = 0;

    Backtrack(1); // 从第 1 个物品开始回溯

    cout << "背包能装的最大价值为：" << maxValue << endl;

    return 0;
}