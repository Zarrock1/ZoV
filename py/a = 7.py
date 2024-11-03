def transform_string(s, n):
    for _ in range(n):
        s = s.replace('011', '10220').replace('022', '201102')
    return s

# Ввод данных
s = '201122'  # исходная строка
n = 10  # количество повторений

# Преобразование строки
result = transform_string(s, n)

# Вывод результата
print(len(result))  # Выводит 24064