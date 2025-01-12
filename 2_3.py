# Функция для вычисления факториала через цикл
def factorial(n):
    result = 1
    for i in range(2, n + 1):  # Перебираем числа от 2 до n
        result *= i  # Умножаем на текущее число
    return result

# Ввод значений x и epsilon с клавиатуры
x = float(input("Введите значение x: "))  # Ввод значения x
epsilon = float(input("Введите значение точности epsilon: "))  # Ввод точности epsilon

n = 1  # Индекс для ряда, начиная с 1
total_sum = 0  # Итоговая сумма ряда

while True:
    term = x**(2 * n + 1) / factorial(2 * n - 1)  # Вычисляем текущий член ряда
    if abs(term) <= epsilon:  # Проверяем, если член меньше или равен точности
        break  # Прерываем цикл
    total_sum += term  # Добавляем текущий член к сумме
    n += 1  # Увеличиваем индекс

# Вывод результата
print(f"Сумма ряда при x = {x}, epsilon = {epsilon}: {total_sum}")
