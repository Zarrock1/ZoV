#include <iostream>
using namespace std;

int main()
{
    char op;
    float a, b;

    cin >> a; 
    cin >> op; 
    cin >> b; 
if (b !=0){
    switch (op)
    {
   case '+':
        cout << a + b;
        break;
   case '-':
      cout << a - b;
      break;
    case '*':
      cout << a * b;
      break;
    case '/':
      cout << a / b;
      break;
    
    }
}
else{
  cout << "На ноль делить нельзя";
}
}