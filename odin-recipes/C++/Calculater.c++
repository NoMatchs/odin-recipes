#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

int main()
{
    srand(time(0));
    int secret = rand() % 100 + 1;
    int guess, attempts = 0;
    do
    {
        cin >> guess;
        attempts++;
        if (guess > secret)
        {
            cout << "↑" << endl;
        }
        else if (guess == secret)
        {
            cout << "BinGo!" << endl;
        }
        else
        {
            cout << "⬇️" << endl;
        }
    } while (guess != secret);
    return 0;
}