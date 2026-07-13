// #include <iostream>
// #include <windows.h>
// using namespace std;

// class Number
// {
// private:
//     int value;

// public:
//     Number(int v = 0) : value(v) {}

//     Number &operator=(const Number &other)
//     {
//         if (this != &other)
//         {
//             value = other.value;
//         }
//         return *this;
//     }

//     Number operator+(const Number &other) const
//     {
//         return Number(value + other.value);
//     }
//     Number operator-(const Number &other) const
//     {
//         return Number(value - other.value);
//     }
//     Number operator*(const Number &other) const
//     {
//         return Number(value * other.value);
//     }
//     Number operator/(const Number &other) const
//     {
//         if (other.value == 0)
//         {
//             cerr << "错误：除以零！" << endl;
//             exit(1);
//         }
//         return Number(value / other.value);
//     }

//     Number &operator++()
//     {
//         value++;
//         return *this;
//     }
//     Number &operator--()
//     {
//         value--;
//         return *this;
//     }

//     Number operator++(int)
//     {
//         Number temp = *this;
//         value++;
//         return temp;
//     }
//     Number operator--(int)
//     {
//         Number temp = *this;
//         value--;
//         return temp;
//     }

//     friend bool operator>(const Number &a, const Number &b);
//     friend bool operator<(const Number &a, const Number &b);
//     friend bool operator==(const Number &a, const Number &b);
//     friend bool operator!=(const Number &a, const Number &b);

//     friend ostream &operator<<(ostream &os, const Number &n);
//     friend istream &operator>>(istream &is, Number &n);

//     int getValue() const { return value; }
// };

// bool operator>(const Number &a, const Number &b)
// {
//     return a.value > b.value;
// }
// bool operator<(const Number &a, const Number &b)
// {
//     return a.value < b.value;
// }
// bool operator==(const Number &a, const Number &b)
// {
//     return a.value == b.value;
// }
// bool operator!=(const Number &a, const Number &b)
// {
//     return a.value != b.value;
// }

// ostream &operator<<(ostream &os, const Number &n)
// {
//     os << n.value;
//     return os;
// }
// istream &operator>>(istream &is, Number &n)
// {
//     is >> n.value;
//     return is;
// }

// int main()
// {
//     SetConsoleOutputCP(65001);
//     SetConsoleCP(65001);
//     Number a(10), b(3);

//     Number c;
//     c = a;
//     cout << "赋值运算符测试：c = " << c << endl;

//     cout << "a + b = " << a + b << endl;
//     cout << "a - b = " << a - b << endl;
//     cout << "a * b = " << a * b << endl;
//     cout << "a / b = " << a / b << endl;

//     cout << "前置++a：" << ++a << "  a的值：" << a << endl;
//     cout << "后置a++：" << a++ << "  a的值：" << a << endl;
//     cout << "前置--b：" << --b << "  b的值：" << b << endl;
//     cout << "后置b--：" << b-- << "  b的值：" << b << endl;

//     cout << "a > b? " << (a > b ? "是" : "否") << endl;
//     cout << "a < b? " << (a < b ? "是" : "否") << endl;
//     cout << "a == b? " << (a == b ? "是" : "否") << endl;
//     cout << "a != b? " << (a != b ? "是" : "否") << endl;

//     Number d;
//     cout << "请输入一个整数给d：";
//     cin >> d;
//     cout << "你输入的d的值是：" << d << endl;

//     return 0;
// }
