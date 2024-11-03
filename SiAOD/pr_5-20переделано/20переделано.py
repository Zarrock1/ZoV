# Функция для шейкер-сортировки по неубыванию (возрастанию)
def shaker_sort_ascending(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        # Проход слева направо
        swapped = False  # Флаг, чтобы отслеживать, произошли ли изменения
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if swapped:  # Выводим массив только если произошли изменения
            print(f"Проход слева направо: {arr}")
        right -= 1

        # Проход справа налево
        swapped = False  # Сбрасываем флаг для обратного прохода
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        if swapped:  # Выводим массив только если произошли изменения
            print(f"Проход справа налево: {arr}")
        left += 1

# Функция для шейкер-сортировки по невозрастанию (убыванию)
def shaker_sort_descending(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        # Проход слева направо
        swapped = False  # Флаг, чтобы отслеживать, произошли ли изменения
        for i in range(left, right):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if swapped:  # Выводим массив только если произошли изменения
            print(f"Проход слева направо: {arr}")
        right -= 1

        # Проход справа налево
        swapped = False  # Сбрасываем флаг для обратного прохода
        for i in range(right, left, -1):
            if arr[i] > arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        if swapped:  # Выводим массив только если произошли изменения
            print(f"Проход справа налево: {arr}")
        left += 1

# Ввод массива
n = int(input("Введите количество элементов в массиве: "))
array = []

# Заполнение массива
for i in range(n):
    элемент = int(input(f"Введите элемент {i+1}: "))
    array.append(элемент)

# Ввод направления сортировки
order = input("Введите направление сортировки ('возрастание' или 'убывание'): ").strip().lower()

# Выбор метода сортировки
if order == 'возрастание':
    shaker_sort_ascending(array)
elif order == 'убывание':
    shaker_sort_descending(array)
else:
    print("Некорректное направление сортировки")

# Вывод отсортированного массива
print("Отсортированный массив:", array)
