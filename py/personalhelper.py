# `import datetime` is a Python statement that imports the `datetime` module
import datetime

def main():
    
   
    #This Python program defines a main function that acts as a personal assistant, providing various
    #commands such as recommending movies, calculating expressions, displaying today's date, and printing
    #a range of numbers based on user input.
    
    # Описание возможностей программы
    print("Привет! Я твой персональный помощник.")
    print("Я могу выполнить следующие команды:")
    print("- Какой фильм посмотреть?")
    print("- Сколько будет [выражение]? (например, '2 ** 10')")
    print("- Какое сегодня число?")
    print("- Вывести список чисел от [начальное_число] до [конечное_число] (например, 'от 1 до 10')")
    print("- Какую книгу прочесть?")
    print("- Выйти из программы")

    books = ["1984", "Мастер и Маргарита", "Война и мир", "Преступление и наказание", "Гарри Поттер"]

    while True:
        command = input("Что вы хотите узнать или сделать? ").strip().lower()

        if command == "какой фильм посмотреть?":
            recommend_movies()
        elif command.startswith("сколько будет"):
            calculate_expression(command)
        elif command == "какое сегодня число?":
            print("Сегодняшняя дата:", datetime.date.today())
        elif command.startswith("вывести список чисел от"):
            print_number_range(command)
        elif command == "выйти из программы":
            print("До свидания!")
        elif command == "какую книгу прочесть":
            print("Вот несколько книг, которые стоит прочитать:")
            for book in books:
                 print("-", book)
            break
        else:
            print("Извините, я не понимаю эту команду.")

def recommend_movies():
    # Пример списка фильмов
    movies = ["Форрест Гамп", "Побег из Шоушенка", "Звёздные войны", "Интерстеллар", "Назад в будущее"]
    print("Вот несколько фильмов, которые стоит посмотреть:")
    for movie in movies:
        print("-", movie)

def calculate_expression(command):
    # Извлекаем выражение из команды
    expression = command[command.index("будет") + len("будет"):].strip()
    try:
        result = eval(expression)
        print("Результат:", result)
    except Exception as e:
        print("Ошибка:", e)

def print_number_range(command):
    # Извлекаем начальное и конечное числа из команды
    numbers = command.split()[3:]
    start = int(numbers[0])
    end = int(numbers[-1])
    if start <= end:
        print("Список чисел от", start, "до", end, ":")
        for i in range(start, end + 1):
            print(i, end=" ")
        print()
    else:
        print("Некорректный диапазон чисел.") 

if __name__ == "__main__":
    main() 