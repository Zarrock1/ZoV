import random
import string

# Функция для генерации пароля с буквами разного регистра и цифрам


def generate_mixed_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Функция для генерации пароля только с буквами разного регистра


def generate_letters_only_password(length):
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))

# Функция для генерации пароля с буквами, цифрами и спецсимволами


def generate_complex_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Функция для генерации пароля с буквами нижнего регистра и цифрами


def generate_lowercase_password(length):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Функция для генерации пароля с буквами верхнего регистра и цифрами


def generate_uppercase_password(length):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Функция для генерации пароля только с цифрами


def generate_digits_password(length):
    characters = string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def main():
    """
    The main function displays a menu for selecting different types of passwords to generate.
    """
    print("Добро пожаловать в Генератор сложных паролей!")
    print("Выберите тип пароля:")
    print("1. Пароль с буквами разного регистра и цифрами")
    print("2. Пароль только с буквами разного регистра")
    print("3. Пароль с буквами, цифрами и спецсимволами")
    print("4. Пароль только с буквами нижнего регистра и цифрами")
    print("5. Пароль только с буквами верхнего регистра и цифрами")
    print("6. Пароль только с цифрами")

# This part of the code is responsible for taking user input to select the type of password to
# generate and then calling the corresponding password generation function based on the user's choice.
    choice = input("Введите номер выбранного типа пароля: ")

    if choice == '1':
        length = int(input("Введите длину пароля: "))
        print("Сгенерированный пароль:", generate_mixed_password(length))
    elif choice == '2':
        length = int(input("Введите длину пароля: "))
        print("Сгенерированный пароль:", generate_letters_only_password(length))
    elif choice == '3':
        length = int(input("Введите длину пароля: "))
        print("Сгенерированный пароль:", generate_complex_password(length))
    elif choice == '4':
        length = int(input("Введите длину пароля: "))
        print("Сгенерированный пароль:", generate_lowercase_password(length))
    elif choice == '5':
        length = int(input("Введите длину пароля: "))
        print("Сгенерированный пароль:", generate_uppercase_password(length))
    elif choice == '6':
        length = int(input("Введите длину пароля: "))
        print("Сгенерированный пароль:", generate_digits_password(length))
    else:
        print("Ошибка: Неверный ввод.")


if __name__ == "__main__":
    main()
