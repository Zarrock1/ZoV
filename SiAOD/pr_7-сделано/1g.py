# Ввод данных от пользователя
number = input("Введите число: ").upper()
from_base = int(input("Введите основание исходной системы: "))
to_base = int(input("Введите основание целевой системы: "))

# Проверка на отрицательное число
is_negative = number.startswith('-')
if is_negative:
    number = number[1:]  # Убираем знак минуса для обработки

# Вывод исходных данных
print(f"\nИсходное число: {'-' if is_negative else ''}{number} в системе с основанием {from_base}")

# Перевод числа в десятичную систему
decimal_number = int(number, from_base)
if is_negative:
    decimal_number = -decimal_number  # Возвращаем отрицательный знак

print(f"Число {'-' if is_negative else ''}{number} в десятичной системе: {decimal_number}")

# Перевод числа из десятичной в целевую систему
if to_base == 10:
    converted = str(decimal_number)
else:
    converted = ''
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    print(f"\nПромежуточные этапы перевода из десятичной в систему с основанием {to_base}:")

    abs_decimal_number = abs(decimal_number)
    
    while abs_decimal_number > 0:
        remainder = abs_decimal_number % to_base
        print(f"{abs_decimal_number} % {to_base} = {remainder} (осталось {abs_decimal_number // to_base})")
        converted = digits[remainder] + converted
        abs_decimal_number //= to_base

    if is_negative:
        converted = '-' + converted

if not converted:
    converted = '0'

# Форматирование вывода в компьютерном виде
if to_base == 2:
    computer_format = '0b' + converted
elif to_base == 8:
    computer_format = '0o' + converted
elif to_base == 16:
    computer_format = '0x' + converted
else:
    computer_format = converted

# Вывод результата
print(f"\n{'='*40}\nРезультаты перевода:\n{'='*40}")
print(f"Число {'-' if is_negative else ''}{number} из системы с основанием {from_base} в системе с основанием {to_base}: {converted}")
print(f"В компьютерном виде: {computer_format}")

# Перевод числа в двоичный формат для отображения в байтах
if to_base == 2:
    binary_string = converted.zfill(32)
else:
    binary_string = bin(abs(decimal_number))[2:].zfill(32)

# Разбиение на байты
byte1 = binary_string[:8]
byte2 = binary_string[8:16]
byte3 = binary_string[16:24]
byte4 = binary_string[24:]

# Конвертация байтов в десятичный формат
decimal_byte1 = int(byte1, 2)
decimal_byte2 = int(byte2, 2)
decimal_byte3 = int(byte3, 2)
decimal_byte4 = int(byte4, 2)

# Вывод числа в виде 4 байт с битами
print(f"\nЧисло {converted} в 4 байтах (32 битах):")
print(f"{'Байты':<15} {'Биты':<40}")
print(f"1-й байт: {decimal_byte1} ({byte1})")
print(f"2-й байт: {decimal_byte2} ({byte2})")
print(f"3-й байт: {decimal_byte3} ({byte3})")
print(f"4-й байт: {decimal_byte4} ({byte4})")

# Вывод байтов в строку через пробел
byte_string = f"{byte1} {byte2} {byte3} {byte4}"
print(f"Байты в битах: {byte_string}")
