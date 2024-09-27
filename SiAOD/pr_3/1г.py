def calculate_sum(n):
    result = 0
    for k in range(1, n + 1):
        result += (-1)**(k + 1) / (k * (k + 1))
    return result

# Ввод значения n
n = int(input("Введите натуральное число n: "))

# Вычисление суммы
sum_result = calculate_sum(n)

# Вывод результата
print(f"Результат суммы: {sum_result}")
