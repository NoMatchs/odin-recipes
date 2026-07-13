// #include <iostream>
// #include <vector>
// using namespace std;

// int Binary_Search(vector<int> arr,int low,int high,int target)
// {
//     if(low > high)
//     {
//         return 0;
//     }
//     int mid = (low + high) >> 1;
//     if(arr.at(mid) == target)
//     {
//         return mid + 1;
//     }
//     if(arr.at(mid) < target)
//     {
//         low = mid + 1;
//     }
//     else if(arr.at(mid) > target)
//     {
//         high = mid - 1;
//     }
//     return Binary_Search(arr,low,high,target);
// }

// int main()
// {

//     return 0;
// }
#include <iostream>
#include <vector>
#include <windows.h>
using namespace std;

// 修正后的二分查找函数
int Binary_Search(vector<int> arr, int target)
{
    int low = 0;
    int high = arr.size() - 1;

    while (low <= high)
    {
        int mid = low + (high - low) / 2;

        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

// 打印测试结果
void printResult(const vector<int> &arr, int target, int result)
{
    cout << "数组: ";
    for (int num : arr)
        cout << num << " ";

    cout << "\n查找目标: " << target;

    if (result != -1)
        cout << "\n结果: 找到，索引位置 = " << result << " (元素值 = " << arr[result] << ")\n";
    else
        cout << "\n结果: 未找到目标元素\n";
    cout << "------------------------\n";
}

int main()
{
    SetConsoleOutputCP(65001); // 控制台输出UTF8
    SetConsoleCP(65001);
    // 测试数据1：基本有序数组
    vector<int> test1 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};

    // 测试数据2：偶数长度数组
    vector<int> test2 = {2, 4, 6, 8, 10, 12, 14, 16};

    // 测试数据3：包含重复元素的数组
    vector<int> test3 = {1, 2, 3, 3, 3, 4, 5, 6};

    // 测试数据4：单个元素
    vector<int> test4 = {42};

    // 测试数据5：较大数值
    vector<int> test5 = {100, 200, 300, 400, 500, 600, 700, 800, 900, 1000};

    // 测试数据6：负数
    vector<int> test6 = {-10, -5, -3, 0, 2, 4, 7};

    cout << "========== 二分查找测试程序 ==========\n\n";

    // 测试数组1
    cout << "【测试1：基本有序数组】\n";
    printResult(test1, 7, Binary_Search(test1, 7));   // 存在 - 中间偏左
    printResult(test1, 1, Binary_Search(test1, 1));   // 存在 - 第一个元素
    printResult(test1, 19, Binary_Search(test1, 19)); // 存在 - 最后一个元素
    printResult(test1, 10, Binary_Search(test1, 10)); // 不存在
    printResult(test1, 0, Binary_Search(test1, 0));   // 不存在 - 小于最小值
    printResult(test1, 20, Binary_Search(test1, 20)); // 不存在 - 大于最大值

    // 测试数组2
    cout << "\n【测试2：偶数长度数组】\n";
    printResult(test2, 8, Binary_Search(test2, 8));   // 存在
    printResult(test2, 2, Binary_Search(test2, 2));   // 存在 - 第一个
    printResult(test2, 16, Binary_Search(test2, 16)); // 存在 - 最后一个
    printResult(test2, 9, Binary_Search(test2, 9));   // 不存在

    // 测试数组3
    cout << "\n【测试3：包含重复元素】\n";
    printResult(test3, 3, Binary_Search(test3, 3)); // 存在（返回第一个遇到的索引）

    // 测试数组4
    cout << "\n【测试4：单元素数组】\n";
    printResult(test4, 42, Binary_Search(test4, 42));   // 存在
    printResult(test4, 100, Binary_Search(test4, 100)); // 不存在

    // 测试数组5
    cout << "\n【测试5：大数值】\n";
    printResult(test5, 500, Binary_Search(test5, 500));   // 存在 - 中间
    printResult(test5, 100, Binary_Search(test5, 100));   // 存在 - 第一个
    printResult(test5, 1000, Binary_Search(test5, 1000)); // 存在 - 最后一个
    printResult(test5, 550, Binary_Search(test5, 550));   // 不存在

    // 测试数组6
    cout << "\n【测试6：包含负数】\n";
    printResult(test6, -5, Binary_Search(test6, -5)); // 存在
    printResult(test6, 0, Binary_Search(test6, 0));   // 存在
    printResult(test6, 7, Binary_Search(test6, 7));   // 存在 - 最后一个
    printResult(test6, -8, Binary_Search(test6, -8)); // 不存在

    // 测试边界情况
    cout << "\n【测试7：空数组】\n";
    vector<int> empty_arr;
    printResult(empty_arr, 5, Binary_Search(empty_arr, 5));

    cout << "\n========== 测试完成 ==========\n";

    return 0;
}
