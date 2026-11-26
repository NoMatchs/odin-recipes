#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> v = {5, 1, 9, 3, 7, 2, 8};

    nth_element(v.begin(), v.begin() + v.size() - 1, v.end());

    cout << v[v.size() - 1] << endl;

    nth_element(v.begin(), v.begin() + v.size() / 2, v.end());
    int median = v[v.size() / 2];

    cout << "median:" << median << endl;

    return 0;
}