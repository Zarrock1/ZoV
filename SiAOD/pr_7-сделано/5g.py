import struct # Модуль преобразования типов данных,требует импорта

# ANSI-коды для цветов
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
ENDC = '\033[0m'  # Сброс цвета

# Ввод двоичного представления числа с клавиатуры
binary_str = input("Введите 32-битное двоичное число: ")

# Промежуточный шаг: двоичное представление числа
print(f"\n{YELLOW}[Промежуточный шаг]{ENDC} Двоичное представление числа: {binary_str}")

# Целое число со знаком
signed_int = int(binary_str, 2)
print(f"{YELLOW}[Промежуточный шаг]{ENDC} Перевод двоичного числа в десятичное (как целое число): {signed_int}")

if signed_int & (1 << 31):  # Проверка старшего бита (если это отрицательное число)
    print(f"{YELLOW}[Промежуточный шаг]{ENDC} Старший бит равен 1, число отрицательное.")
    signed_int -= (1 << 32)  # Применение дополнения до двух
else:
    print(f"{YELLOW}[Промежуточный шаг]{ENDC} Старший бит равен 0, число положительное.")
    
print(f"{GREEN}Целое число со знаком: {signed_int}{ENDC}\n")

# Промежуточный шаг: вывод целого числа без изменений
unsigned_int = int(binary_str, 2)
print(f"{YELLOW}[Промежуточный шаг]{ENDC} Целое число без знака (интерпретируем как положительное): {unsigned_int}\n")

# Вещественное число с плавающей точкой (IEEE 754)
binary_int = int(binary_str, 2)
float_value = struct.unpack('f', struct.pack('I', binary_int))[0]

# Промежуточные шаги для вещественного числа
print(f"{YELLOW}[Промежуточный шаг]{ENDC} 32-битное целое представление числа (интерпретируем как плавающее): {binary_int}")

# Промежуточный шаг: экспонента
exp_bits = binary_str[1:9]
exp_value = int(exp_bits, 2)
actual_exponent = exp_value - 127
print(f"{YELLOW}[Промежуточный шаг]{ENDC} Экспонента (в двоичном виде): {exp_bits} -> {exp_value}, реальный порядок: {actual_exponent}")

# Промежуточный шаг: мантисса
mantissa_bits = '1' + binary_str[9:]  # Добавляем скрытый бит (1)
mantissa_value = 1.0
for i, bit in enumerate(mantissa_bits[1:]):
    mantissa_value += int(bit) * 2**-(i+1)
print(f"{YELLOW}[Промежуточный шаг]{ENDC} Мантисса: {mantissa_bits} -> {mantissa_value}")

# Финальный результат: ручное вычисление вещественного числа
final_float = mantissa_value * (2 ** actual_exponent)
print(f"\n{BLUE}Ручное вычисление вещественного числа: {final_float}{ENDC}")

# Финальный результат: использование struct
print(f"{BLUE}Вещественное число с плавающей точкой (через struct): {float_value}{ENDC}")


#"01000101000000011000000110011000"
