#include <iostream>
using namespace std;

int main()
{
    int a = 0; 
    int b = 1;
    int c = 0;  

    cout << a << " " << b << "|";  
  
    for (int i = 0; i < 30; ++i)
    {
      
      
      cout << a + b << " ";
      c = a + b;
      a = b;
      b = c;
    }
}