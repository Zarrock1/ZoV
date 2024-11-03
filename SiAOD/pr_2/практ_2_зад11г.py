import math

def is_point_in_region(x, y):
    # Проверка для прямоугольника с исключёнными границами
    if -1 < x < 0 and -1 < y < 1:
        return True
    # Проверка для полукруга с исключёнными границами
    elif 0 < x < 1 and x**2 + y**2 < 1:
        return True
    else:
        return False

# Ввод координат точки
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

# Проверка
if is_point_in_region(x, y):
    print("Точка находится внутри области.")
else:
    print("Точка находится вне области.")
