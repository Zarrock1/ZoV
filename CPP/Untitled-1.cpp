#include <iostream>
#include <string>
using namespace std;

int main()
{
    setlocale (LC_ALL, "Ru.UTF-8");

    string fnd;
    string vst;

    getline(cin, fnd);
    getline(cin, vst);

    int pos = fnd.find("<-here->");

    fnd.erase(pos, 8);
    fnd.replace(pos, vst.length(), vst);
    
    cout << fnd;

}