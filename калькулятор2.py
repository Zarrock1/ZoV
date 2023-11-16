import math


def weight_converter():  # Определение функцию weight_converter (сделано для удобства)

    print("Выберите конвертер мер и весов:")  # это команда печати текста
    print("1. Килограммы в фунты")  # это команда печати текста
    print("2. Фунты в килограммы")  # это команда печати текста
    print("3. Километры в мили")  # это команда печати текста
    print("4. Мили в километры")  # это команда печати текста

    # Обьявление переменной choise, вывод текста на экран и ожидание ввода значения от пользователя
    choice = input("Введите номер конвертера: ")

    # This code block checks if the user's choice is one of the options '1', '2', '3', or '4'. If it
    # is, it prompts the user to enter a value and converts it to a float data type. This value will
    # be used in the subsequent calculations based on the user's choice.
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


# Объявление функции calculate_interest с параметрами principal, rate, time (также для удобства)
def calculate_interest(principal, rate, time):
    # Вычисление процентной ставки (доходности вклада) по формуле: Принципал * Ставка * Время / 100
    interest = principal * rate * time / 100
    return interest  # Возвращение рассчитанной процентной ставки


def calculator():  # Обьявление функции calculator
    # Вывод приветствия в консоль
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
    print("11. Синус угла")
    print("12. Косинус угла")
    print("13. Тангенс угла")
    print("14. Арксинус угла")
    print("15. Арккосинус угла")
    print("16. Арктангенс угла")
    print("17. Корень числа")
    # Вывод доступных операций в консоль

    # Получение выбора пользователя в переменную choice
    choice = input("Выберите операцию (введите соответствующий номер): ")

    if choice in ['1', '2', '3', '4', '5', '7']:
        num_1 = float(input('Введите первое число: '))
        num_2 = float(input('Введите второе число: '))
        # Если выбраны операции, требующие ввода двух чисел, считываем их с клавиатуры и преобразуем в тип float

    elif choice in ['6']:
        num_1 = float(input('Введите число: '))
        num_2 = float(input('Введите степень: '))
        # Если выбрана операция возведения в степень, считываем число и степень с клавиатуры

    if choice == '1':
        result = num_1 + num_2
        print("Результат сложения:", result)
        # Если выбрана операция сложения, выполняем сложение и выводим результат

    elif choice == '2':
        result = num_1 - num_2
        print("Результат вычитания:", result)
        # Если выбрана операция вычитания, выполняем вычитание и выводим результат

    elif choice == '3':
        result = num_1 * num_2
        print("Результат умножения:", result)
        # Если выбрана операция умножения, выполняем умножение и выводим результат

    elif choice == '4':
        if num_2 != 0:
            result = num_1 / num_2
            print("Результат деления:", result)
        else:
            print("Ошибка! Деление на ноль.")
    # Если выбрана операция деления, проверяем, что делитель не равен нулю, и выводим результат или сообщение об ошибке

    elif choice == '5':
        if num_2 != 0:
            result = num_1 // num_2
            print("Результат целочисленного деления:", result)
        else:
            print("Ошибка! Деление на ноль.")
    # Если выбрана операция целочисленного деления, проверяем, что делитель не равен нулю,

    elif choice == '6':
        result = num_1 ** num_2
        print("Результат возведения в степень:", result)
    # Если выбрана операция возведения в степень, выполняем операцию и выводим результат

    elif choice == '7':
        if num_2 != 0:
            result = num_1 % num_2
            print("Остаток от деления:", result)
        else:
            print("Ошибка! Деление на ноль.")
    # Если выбрана операция получения остатка от деления, проверяем, что делитель не равен нулю, и выводим результат или сообщение об ошибке

    elif choice == '8':  # Если пользователь выбрал операцию конвертера мер и весов
        weight_converter()  # Вызываем функцию конвертера мер и весов

    elif choice == '9':  # Конвертер для рассчета доходности вклада
        principal = float(input("Введите сумму вклада в рублях: "))
        rate = float(input("Введите годовую процентную ставку в рублях: "))
        time = float(input("Введите срок вклада в годах: "))
        interest = calculate_interest(principal, rate, time)
        print(f"Доходность вклада: {interest} рублей")
        pass

    elif choice == '10':  # Перевод из различных систем счисления в десятичную
        number = input("Введите число: ")
        base = int(input("Введите основание системы счисления: "))
        decimal_number = int(number, base)
        print(f"{number} в десятичной системе: {decimal_number}")

    elif choice == '11': # Вычисление синуса угла 
        x = float(input("Введите угол: "))
        print(math.sin(x))

    elif choice == '12': # Вычисление косинуса угла
        x = float(input("Введите угол: "))
        print(math.cos(x))

    elif choice == '13': # Вычисление тангенса угла
        x = float(input("Введите угол: "))
        print(math.tan(x))

    elif choice == '14': # Вычисление арксинуса угла
        x = float(input("Введите угол: "))
        x_rad = x*math.pi/180
        print(math.asin(x_rad))

    elif choice == '15': # Вычисление арккосинуса угла
        x = float(input("Введите угол: "))
        x_rad = x*math.pi/180
        print(math.acos(x_rad))

    elif choice == '16':# Вычисление арктангенса угла
        x = float(input("Введите значение тангенса угла: "))
        print(math.atan(x))

    elif choice == '17': # Вычисление корня числа
        x = float(input("Введите число: "))
        print(math.sqrt(x))

    else:
        print("Ошибка! Неверный выбор операции.")


# Запуск калькулятора
calculator()

# сделать с 11 функции до конца сделать красивый вывод и заккоментировать!!!!!!!!!!!!!!!!!