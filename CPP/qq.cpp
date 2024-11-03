#include <iostream>
using namespace std;

// ↓ Определи здесь функцию get_max ↓

int get_max(int arr[], int size){

    int max = arr[0];

    for (int i = 0; i < size; ++i)
    {
        if (arr[i] > max){max = arr[i];}

    }

    return max;
}

int main()
{
    int size;
    cin >> size;
    int arr[size];

    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }

    // Вызов функции (не изменяй это)
    cout << get_max(arr, size);
}