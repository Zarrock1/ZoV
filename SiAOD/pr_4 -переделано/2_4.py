import math

x = float(input("Введите x: "))  # Считываем значение x
epsilon = float(input("Введите ε (точность): "))  # Считываем точность

sum_value = 1.0  # Инициализация суммы с первого члена (x^0 / 0!)
term = 1.0  # Первый член ряда
k = 1  # Начинаем с x^2 / 2!

# Переменная для хранения факториала
factorial = 1  # Инициализация для 0!

print(f"{'Шаг':<5} {'Текущий член':<20} {'Сумма':<20}")  # Заголовок для таблицы шагов

while True:
    factorial *= (2 * k - 1) * (2 * k)  # Вычисляем (2k)!
    term = (x ** (2 * k)) / factorial  # Вычисляем текущий член ряда

    # Если член ряда меньше заданной точности, прекращаем цикл
    if abs(term) < epsilon:
        break

    sum_value += term  # Добавляем текущий член к сумме  `sum_value += term` 
    print(f"{k:<5} {term:<20.10f} {sum_value:<20.10f}")  # Выводим текущий шаг, член и сумму
    k += 1  # Увеличиваем счетчик степеней

# Вычисляем точное значение гиперболического косинуса с помощью math.cosh
exact_value = math.cosh(x)  # Формула для cosh(x)

# Выводим результаты
print(f"\nПриближенное значение суммы ряда: {sum_value:.6f}")
print(f"Точное значение: {exact_value:.6f}")
print(f"Разница: {abs(sum_value - exact_value):.6f}")
