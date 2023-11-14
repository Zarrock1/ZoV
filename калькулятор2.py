def weight_converter(): # Определение функцию weight_converter (сделано для удобства)
   
    print("Выберите конвертер мер и весов:")# это команда печати текста
    print("1. Килограммы в фунты")# это команда печати текста
    print("2. Фунты в килограммы")# это команда печати текста
    print("3. Километры в мили")# это команда печати текста
    print("4. Мили в километры")# это команда печати текста

    choice = input("Введите номер конвертера: ") # Обьявление переменной choise, вывод текста на экран и ожидание ввода значения от пользователя

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


def calculate_interest(principal, rate, time): # Объявление функции calculate_interest с параметрами principal, rate, time (также для удобства) 
    interest = principal * rate * time / 100 # Вычисление процентной ставки (доходности вклада) по формуле: Принципал * Ставка * Время / 100
    return interest # Возвращение рассчитанной процентной ставки


def calculator(): # Обьявление функции calculator  
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
    # Вывод доступных операций в консоль

    choice = input("Выберите операцию (введите соответствующий номер): ") # Получение выбора пользователя в переменную choice

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

    elif choice == '8':  # Конвертер мер и весов
        weight_converter()

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

    else:
        print("Ошибка! Неверный выбор операции.")


# Запуск калькулятора
calculator()
