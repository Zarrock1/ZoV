def calculate_y(x):
    if x <= 0:
        return 0
    elif 0 < x <= 1:
        return x
    else:
        return x**4

# Ввод значения x
x = float(input("Введите значение x: "))

# Вычисление y
y = calculate_y(x)

# Вывод результата
print(f"Значение y при x = {x} равно: {y}")
