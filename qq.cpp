#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    string put;
    cin >> put;
    ifstream content(put, ios::ate);

    int colvo_byte = content.tellg(); 

    char aa[colvo_byte + 1] = {0};
    content.seekg(0);
    content.read(aa, colvo_byte);

    

    cout << aa;
}