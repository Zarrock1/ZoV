def calculate_series(n):
    sum_series = 0.0
    for i in range(1, n + 1):
        sum_series += (-1)**(i + 1) / (i * (i + 1))
    return sum_series

# Ввод значения n
n = int(input("Введите n: "))

# Вычисление и вывод результата
result = calculate_series(n)
print(f"Результат: {result}")
