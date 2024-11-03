def weight_converter():
    print("Выберите конвертер мер и весов:")
    print("1. Килограммы в фунты")
    print("2. Фунты в килограммы")
    print("3. Километры в мили")
    print("4. Мили в километры")

    choice = input("Введите номер конвертера: ")

    if choice in ['1', '2', '3', '4']:
        value = float(input("Введите значение: "))

        if choice == '1':
            result = value * 2.20462
            print(f"{value} кг = {result} фунтов")

        elif choice == '2':
            result = value / 2.20462
            print(f"{value} фунтов = {result} кг")

        elif choice == '3':
            result = value * 0.621371
            print(f"{value} км = {result} миль")

        elif choice == '4':
            result = value / 0.621371
            print(f"{value} миль = {result} км")

    else:
        print("Ошибка! Неверный выбор конвертера мер и весов.")

# Обновленная функция калькулятора
def calculator():
    print("Добро пожаловать в Калькулятор!")
    print("Я могу выполнять следующие операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Целочисленное деление")
    print("6. Возведение в степень")
    print("7. Остаток от деления")
    print("8. Конвертер мер и весов")
    print("9. Рассчет доходности вклада")
    print("10. Перевод из различных систем счисления в десятичную")

    choice = input("Выберите операцию (введите соответствующий номер): ")

    if choice in ['1', '2', '3', '4', '5', '7']:
        num_1 = float(input('Введите первое число: '))
        num_2 = float(input('Введите второе число: '))

    elif choice == '6':
        num_1 = float(input('Введите число: '))
        num_2 = float(input('Введите степень: '))

    if choice == '1':
        result = num_1 + num_2
        print("Результат сложения:", result)

    elif choice == '2':
        result = num_1 - num_2
        print("Результат вычитания:", result)

    elif choice == '3':
        result = num_1 * num_2
        print("Результат умножения:", result)

    elif choice == '4':
        if num_2 != 0:
            result = num_1 / num_2
            print("Результат деления:", result)
        else:
            print("Ошибка! Деление на ноль.")

    elif choice == '5':
        if num_2 != 0:
            result = num_1 // num_2
            print("Результат целочисленного деления:", result)
        else:
            print("Ошибка! Деление на ноль.")

    elif choice == '6':
        result = num_1 ** num_2
        print("Результат возведения в степень:", result)

    elif choice == '7':
        if num_2 != 0:
            result = num_1 % num_2
            print("Остаток от деления:", result)
        else:
            print("Ошибка! Деление на ноль.")

    elif choice == '8':
        # Call the weight converter function
        weight_converter()

    elif choice == '9':
        # Рассчет доходности вклада
        principal = float(input("Введите сумму вклада: "))
        rate = float(input("Введите годовую процентную ставку: "))
        time = float(input("Введите срок вклада в годах: "))
        interest = calculate_interest(principal, rate, time)
        print(f"Доходность вклада: {interest} руб.")

    elif choice == '10':
        # Перевод из различных систем счисления в десятичную
        decimal_converter()

    else:
        print("Ошибка! Вы что-то неправильно ввели.")

# Запуск калькулятора
calculator()
