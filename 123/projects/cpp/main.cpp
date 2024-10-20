#include <iostream>

int main(){
    int a, b;
    do{
        a = rand();
        b = rand();
    }while(a + b != 1137);
    std::cout << "Hello, World!" << std::endl;
}