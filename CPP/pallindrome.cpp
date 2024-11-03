#include <iostream>
using namespace std;

int main()
{
    setlocale (LC_ALL, "Ru.UTF-8");

    int length;
    cin >> length;

    char word[length + 1];
    cin >> word;
    string a;
    string b;
    bool schetchik = true;


    for(int i = 0; i < length / 2; i ++){
        if(word[i] != word[length - i - 1]){
            schetchik = false;
            break;
        }
    }
    

    if(schetchik) {
        cout << "Да";
    } else {
        cout << "Нет";
    }

    return 0;
}