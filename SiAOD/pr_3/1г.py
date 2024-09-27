def calculate_series(n):
    sum_series = 0.0
    for i in range(1, n + 1):
        sum_series += (-1)**(i + 1) / (i * (i + 1))
    return sum_series

n = int(input("Введите n: "))
result = calculate_series(n)

# Округляем результат до 9 знаков после запятой
print(f"Результат: {result:.9f}")
