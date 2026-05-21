#include <iostream>
using namespace std;

class Figure
{
protected:
    double height;
    double width;

public:
    Figure(double h, double w) : height(h), width(w) {}
    virtual double area() const = 0;
};

class Rectangle : public Figure
{
public:
    Rectangle(double h, double w) : Figure(h, w) {}
    double area() const override
    {
        return height * width;
    }
};

class Triangle : public Figure
{
public:
    Triangle(double h, double w) : Figure(h, w) {}
    double area() const override
    {
        return 0.5 * height * width;
    }
};

int main()
{
    Rectangle rect(10, 5);
    Triangle tri(10, 5);

    cout << "矩形面积: " << rect.area() << endl;
    cout << "三角形面积: " << tri.area() << endl;
    return 0;
}