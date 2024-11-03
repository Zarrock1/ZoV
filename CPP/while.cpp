#include <iostream>
using namespace std;

int main()
{
    setlocale(LC_ALL, "Ru.UTF-8");

    int pp[13] = {33, 39, 33, 47, 43, 52, 46, 43, 47, 41, 43, 37, 33};
    int dubl = 0;

    // Пробегаем по всем элементам массива
    for (int j = 0; j < 13; j++) {
        // Проверяем, является ли текущее число дубликатом
        for (int k = 0; k < j; k++) {
            if (pp[j] == pp[k]) {
                dubl++;
                break; // Если найден дубликат, выходим из внутреннего цикла
            }
        }
    }

    cout << "Дубликатов найдено " << dubl << endl;
    return 0;
}
