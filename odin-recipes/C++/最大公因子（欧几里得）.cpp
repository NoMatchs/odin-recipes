#include <iostream>
#include <vector>
#include <windows.h>
using namespace std;

int GCD(int m, int n)
{
    int Max = max(m, n);
    int Min = min(m, n);
    int r = Max % Min;
    while (r != 0)
    {
        Max = Min;
        Min = r;
        r = Max % Min;
    }
    return Min;
}

int main()
{

    SetConsoleOutputCP(65001); // 控制台输出UTF8
    SetConsoleCP(65001);

    cout << GCD(2166, 6099) << endl;

    return 0;
}