import math

def calculate_series(x, m):
    sum_series = 0.0
    for i in range(1, m + 1):
        term = ((-1) ** (i - 1)) * (x ** (2 * i - 1)) / math.factorial(2 * i - 1)
        sum_series += term
    return sum_series

# Ввод значений t (количество членов ряда) и x (действительное число)
m = int(input("Введите m: "))
x = float(input("Введите x: "))

# Вычисление и вывод результата
result = calculate_series(x, m)
print(f"Результат: {result}")
