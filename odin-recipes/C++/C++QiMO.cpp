// // #include <iostream>

// // using namespace std;

// // int main()
// // {
// //     cout << "Welcome to C++!" << endl;
// //     return 0;
// // }

// #include <iostream>
// using namespace std;

// class Vehicle
// {
// public:
//     Vehicle()
//     {
//         cout << "Call Vehicle" << endl;
//     }
//     ~Vehicle()
//     {
//         cout << "Delete base class" << endl;
//     }
// };

// class Car : public Vehicle
// {
// public:
//     Car()
//     {
//         cout << "Call Car" << endl;
//     }
//     ~Car()
//     {
//         cout << "Delete Car" << endl;
//     }
// };

// int main()
// {
//     Car Lamborghini;
//     return 0;
// }

// #include <iostream>

// using namespace std;

// class Date
// {
// public:
//     Date(int, int, int);
//     friend void show(Date &);

// private:
//     int year;
//     int month;
//     int day;
// };

// Date::Date(int y, int m, int d)
// {
//     year = y;
//     month = m;
//     day = d;
// }

// void show(Date &t)
// {
//     cout << t.year << "." << t.month << "." << t.day << endl;
// }

// int main()
// {
//     Date t(2026, 6, 24);
//     show(t);
// }

// #include <iostream>

// using namespace std;

// int main()
// {
//     int num = 30;
//     int &m = num;
//     cout << "m = " << m << endl;
//     m = 40;
//     cout << "num = " << num << endl;
//     return 0;
// }

// #include <iostream>
// using namespace std;

// class Test
// {
// public:
//     void set(char ch)
//     {
//         c = ch;
//     }
//     void show()
//     {
//         cout << "char in Test is:" << c << endl;
//     }

// private:
//     char c;
// };

// int main()
// {
//     Test t1, t2;
//     t1.set('a');
//     t2.set('b');
//     t1.show();
//     t2.show();
//     return 0;
// }

#include <iostream>

using namespace std;

// template <typename T>
// void swapValues(T &a, T &b)
// {
//     T temp = a;
//     a = b;
//     b = temp;
// }

// int main()
// {
//     int x = 3, y = 5;
//     swapValues(x, y);
//     cout << "x:" << x << " y:" << y << endl;

//     double m = 1.2, n = 3.4;
//     swapValues(m, n);
//     cout << "m:" << m << " n:" << n << endl;
//     return 0;
// }

// template <class T>
// class Stack
// {

// private:
//     T data[100];
//     int top;

// public:
//     Stack() : top(0) {}
//     void push(T val) { data[top++] = val; }
//     T pop() { return data[--top]; }
// };

// int main()
// {
//     Stack<int> s1;
//     s1.push(10);

//     Stack<double> s2;
//     s2.push(3.14);
//     return 0;
// }

// class Myclass{
//     public:
//         int getValue()
//         {
//             return value;
//         }
//     protected:
//         int protectedData;
//     private:
//         int value;
// };

// int main()
// {
//     // int num = 30;
//     // int &rn = num;

//     // cout << rn << endl;
//     // rn = 40;
//     // cout << num << endl;

//     int num = 10;

//     cout << num << endl;

//     int &m = num;

//     cout << m << endl;

//     num = 20;

//     cout << m << endl;

//     m = 40;

//     cout << num << endl;

//     return 0;
// }

// void swap(int &a, int &b)
// {
//     int temp = a;
//     a = b;
//     b = temp;
// }

// int main()
// {
//     int x = 3, y = 2;
//     swap(x, y);
//     cout << x << " " << y << endl;
// }

// class Date
// {
// public:
//     Date(int y, int m, int d);
//     void show();

// private:
//     int year, month, day;
// };

// Date::Date(int y, int m, int d)
// {
//     year = y;
//     month = m;
//     day = d;
// }

// void Date::show()
// {
//     cout << year << " " << month << " " << day << endl;
// }

// void printInfo(string name, int age = 18, string city = "beijing")
// {
//     cout << name << ", " << age << ", " << city << endl;
// }

// int main()
// {
//     printInfo("lq");
//     printInfo("lq", 20);
//     printInfo("lq", 20, "hunan");
//     Date D(2006, 5, 12);
//     D.show();
//     return 0;
// }

// class Student
// {
// public:
//     Student()
//     {
//         name = "wwvi";
//         age = 0;
//     }
//     Student(string n, int a)
//     {
//         name = n;
//         age = a;
//     }
//     void show()
//     {
//         cout << "name:" << name << " age:" << age << endl;
//     }

// private:
//     string name;
//     int age;
// };

// int main()
// {
//     Student s1;
//     s1.show();
//     Student s2("lq", 10);
//     s2.show();
//     return 0;
// }

// class Student
// {

// public:
//     Student()
//     {
//         name = "wwvi";
//         age = 0;
//     }
//     Student(string n, int a)
//     {
//         name = n;
//         age = a;
//     }
//     ~Student()
//     {
//     }
//     void show()
//     {
//         cout << "Name:" << name << " Age:" << age << endl;
//     }

// private:
//     string name;
//     int age;
// };

// class Array
// {

// public:
//     Array(int size)
//     {
//         data = new int[size];
//     }
//     ~Array()

//     {
//         delete[] data;
//     }

// private:
//     int *data;
// };

// void print(int a);
// void print(double a);
// void print(int a, int b);
// void print(double a, int b);

// class Date
// {

// private:
//     int year, month, day;

// public:
//     Date(int y, int m, int d) : year(y), month(m), day(d) {}
//     friend void show(Date &d);
// };

// void show(Date &d)
// {
//     cout << d.year << "." << d.month << "." << d.day << endl;
// }

// class Complex
// {

// private:
//     double real, imag;

// public:
//     Complex(double r = 0, double i = 0) : real(r), imag(i) {}

//     Complex operator+(const Complex &other)
//     {
//         return Complex(real + other.real, imag + other.imag);
//     }
//     void show()
//     {
//         cout << "real:" << real << " imag:" << imag << endl;
//     }
// };

// class Shape
// {

// public:
//     virtual double area() = 0;
// };

// class Circle : public Shape
// {

// public:
//     Circle(double r) : radius(r) {}
//     double area() override { return 3.14 * radius * radius; }

// private:
//     double radius;
// };

// class Base
// {

// public:
//     void show() { cout << "Base::show" << endl; }
// };

// class Derived : public Base
// {
// public:
//     void show()
//     {
//         cout << "Derived::show" << endl;
//     }
// };

// Base* p = new Derived();
// // p->show();

// class Base
// {

// public:
//     virtual void show()
//     {
//         cout << "Base::show" << endl;
//     }
// };

// class Derived : public Base
// {
// public:
//     void show() override
//     {
//         cout << "Derived::show" << endl;
//     }
// };

// int main()
// {
//     Base *p = new Derived();
//     p->show();
//     // Complex c1(1, 2), c2(3, 4);
//     // Complex c3 = c1 + c2;
//     // c3.show();
//     // // Student s1;
//     // // Student s2("sda", 20);
//     // // s1.show();
//     // // s2.show();
//     // // return 0;
//     // Date d(16, 12, 4);
//     // show(d);
//     Circle c(5.0);
//     cout << c.area();
//     return 0;
// }

// #include <iostream>
// using namespace std;

// class Vehicle
// {

// public:
//     Vehicle()
//     {
//         cout << "Call Vehicle" << endl;
//     }
//     ~Vehicle()
//     {
//         cout << "Delete base class" << endl;
//     }
// };

// class Car : public Vehicle
// {

// public:
//     Car()
//     {
//         cout << "Call Car" << endl;
//     }
//     ~Car()
//     {
//         cout << "Detele Car class" << endl;
//     }
// };

// class Date
// {

// public:
//     Date(int, int, int);
//     friend void show(Date &);

// private:
//     int year;
//     int month;
//     int day;
// };

// Date::Date(int y, int m, int d)
// {
//     year = y;
//     month = m;
//     day = d;
// }

// void show(Date &t)
// {
//     cout << t.year << "." << t.month << "." << t.day << endl;
// }

// void Swap(int &a, int &b)
// {
//     int temp = a;
//     a = b;
//     b = temp;
// }

// int main()
// {
//     int a = 10, b = 20;
//     cout << "Start-> a:" << a << "and b:" << b << endl;
//     Swap(a, b);
//     cout << "a:" << a << "b:" << b << endl;
//     Date t(2026, 6, 24);
//     return 0;
// }

// #include <iostream>
// using namespace std;

// class Test
// {

// private:
//     char c;

// public:
//     void set(char ch)
//     {
//         c = ch;
//     }
//     void show()
//     {
//         cout << "char in Test is:" << c << endl; // C++
//     }
// };

// int main()
// {
//     Test t1, t2;
//     t1.set('a');
//     t2.set('b');
//     t1.show();
//     t2.show();
//     return 0;
// }

// #include <iostream>
// using namespace std;

// template <class T>

// T Min(T a, T b)
// {
//     return a < b ? a : b;
// }

// int main()
// {
//     cout << Min(1.2, 0.4) << endl;
//     cout << Min(1000, 10) << endl;
//     return 0;
// }

// #include <iostream>
// using namespace std;

// class Shape
// {

// public:
//     Shape()
//     {
//         cout << "Shape构造" << endl;
//     }
//     virtual double area() = 0;
//     virtual ~Shape()
//     {
//         cout << "Shape析构" << endl;
//     }
// };

// class Circle : public Shape
// {

// private:
//     double radius;

// public:
//     Circle(double r) : radius(r)
//     {
//         cout << "Circle构造" << endl;
//     }
//     double area() override
//     {
//         return 3.14 * radius * radius;
//     }
//     ~Circle()
//     {
//         cout << "Circle析构" << endl;
//     }
// };

// int main()
// {
//     Shape *p = new Circle(5.0);
//     cout << "面积：" << p->area() << endl;
//     delete p;
//     return 0;
// }

#include <iostream>
using namespace std;

class Point
{

private:
    int x, y;

public:
    Point(int a = 0, int b = 0) : x(a), y(b) {}
    void show()
    {
        cout << "(" << x << "," << y << ")" << endl;
    }
    Point operator+(const Point &p1)
    {
        return Point(x + p1.x, y + p1.y);
    }
};

int main()
{
    Point p1(1, 2), p2(3, 4);
    Point p3 = p1 + p2;
    p3.show(); // 输出 (4,6)
    return 0;
}