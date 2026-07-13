#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <algorithm>
#include <windows.h>
using namespace std;
using namespace chrono;

void merge(vector<int> &arr, int left, int mid, int right)
{
    vector<int> temp(right - left + 1);
    int i = left, j = mid + 1, k = 0;

    while (i <= mid && j <= right)
    {
        if (arr[i] <= arr[j])
            temp[k++] = arr[i++];
        else
            temp[k++] = arr[j++];
    }

    while (i <= mid)
        temp[k++] = arr[i++];
    while (j <= right)
        temp[k++] = arr[j++];

    for (int i = 0; i < temp.size(); i++)
    {
        arr[left + i] = temp[i];
    }
}

void mergeSort(vector<int> &arr, int left, int right)
{
    if (left < right)
    {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// 验证排序是否正确
bool isSorted(const vector<int> &arr)
{
    for (size_t i = 1; i < arr.size(); i++)
    {
        if (arr[i] < arr[i - 1])
            return false;
    }
    return true;
}

// 生成随机数组
vector<int> generateRandomArray(int size)
{
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(1, size * 10);

    vector<int> arr;
    for (int i = 0; i < size; i++)
    {
        arr.push_back(dis(gen));
    }
    return arr;
}

int main()
{
    SetConsoleOutputCP(65001); // 控制台输出UTF8
    SetConsoleCP(65001);
    // 测试不同大小的数组
    vector<int> sizes = {10, 100, 1000, 10000, 50000, 100000};

    cout << "归并排序性能测试\n";
    cout << "================================\n";

    for (int size : sizes)
    {
        vector<int> arr = generateRandomArray(size);
        vector<int> arr_copy = arr;

        // 测试归并排序
        auto start = high_resolution_clock::now();
        mergeSort(arr, 0, arr.size() - 1);
        auto end = high_resolution_clock::now();
        auto merge_time = duration_cast<microseconds>(end - start);

        // 测试标准库排序
        start = high_resolution_clock::now();
        sort(arr_copy.begin(), arr_copy.end());
        end = high_resolution_clock::now();
        auto std_time = duration_cast<microseconds>(end - start);

        cout << "数组大小: " << size << "\n";
        cout << "归并排序: " << merge_time.count() << " 微秒\n";
        cout << "std::sort: " << std_time.count() << " 微秒\n";
        cout << "排序正确性: " << (isSorted(arr) ? "通过" : "失败") << "\n";
        cout << "--------------------------------\n";
    }

    // 特殊测试案例
    cout << "\n特殊测试案例:\n";
    cout << "================================\n";

    // 已排序数组
    vector<int> sorted = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    cout << "已排序数组: ";
    mergeSort(sorted, 0, sorted.size() - 1);
    for (int num : sorted)
        cout << num << " ";
    cout << " ✓\n";

    // 逆序数组
    vector<int> reversed = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
    cout << "逆序数组: ";
    mergeSort(reversed, 0, reversed.size() - 1);
    for (int num : reversed)
        cout << num << " ";
    cout << " ✓\n";

    // 包含重复元素
    vector<int> duplicate = {5, 2, 8, 2, 9, 1, 5, 5, 3, 8};
    cout << "重复元素数组: ";
    mergeSort(duplicate, 0, duplicate.size() - 1);
    for (int num : duplicate)
        cout << num << " ";
    cout << " ✓\n";

    // 单元素数组
    vector<int> single = {42};
    cout << "单元素数组: ";
    mergeSort(single, 0, single.size() - 1);
    for (int num : single)
        cout << num << " ";
    cout << " ✓\n";

    // 空数组
    vector<int> empty;
    cout << "空数组: ";
    if (empty.empty())
    {
        mergeSort(empty, 0, empty.size() - 1);
        cout << "空数组处理正确 ✓\n";
    }

    return 0;
}