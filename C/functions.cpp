#include <iostream>
using namespace std;

int add(int x, int y) 
{
    return x + y;
}

int main()
{
    int a = 3, b = 5;
    int result;

    result = add(a, b);
    cout << result << endl;

    return 0;
}
//Note(Important): Declaring the function under the main method results in an error
/*int add(int x, int y) 
{
    return x + y;
}*/
