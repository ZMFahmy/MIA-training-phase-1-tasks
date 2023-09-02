#include <iostream>
#include<windows.h>
using namespace std;

int main()
{
    int num;
    cin >> num;

    for(int i = num; i >= 1; i--)
    {
        cout << i << endl;
        Sleep(1000);
    }

    cout << "Blast off to the moon!";
    return 0;
}
