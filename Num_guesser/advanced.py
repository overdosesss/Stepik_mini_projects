from random import randint


# Осуществление и проверка попытки пользователя угадать число
def user_guess(left, right):
    try:
        num = int(input("Введите число:\n"))

        if left <= num <= right:
            return num
        raise Exception(f"Не попали в диапазон [{left}; {right}], попробуйте ещё раз...")
    except ValueError:
        print("Вы ошиблись при вводе, попробуйте ещё раз...")
        return user_guess(left, right)
    except Exception as error:
        print(error)
        return user_guess(left, right)


# Настраиваемые границы
def optional_borders():
    try:
        # Узнаем хочет ли пользователь установить свои границы для случайного числа
        user_input = input("Хотите установить обе границы случайного числа? (да/нет)\n").lower()

        if user_input not in ("да", "нет"):
            raise Exception("Ответом должно быть \"да\" или \"нет\"")

        is_optional_borders = True if user_input == "да" else False

        if not is_optional_borders:
            return 1, 100
        print("Отлично, теперь введите левую и правую границу через пробел:")

        left, right = map(int, input().split())

        if left < right:
            return left, right
        raise Exception("Левая граница должна быть меньше правой, попробуйте ещё раз...")
    except ValueError:
        print("Ввели не число, попробуйте ещё раз...")
        return optional_borders()
    except Exception as error:
        print(error)
        return optional_borders()


# Основная программа
def num_guesser():
    # Получим пользовательские границы
    left, right = optional_borders()

    # Сгенерируем случайное число из диапазона [1; 100]
    num_for_guess = randint(left, right)

    # Счётчик попыток пользователя
    counter = 0

    # Бесконечный цикл, где будет ввод данных от пользователя и проверка угадал ли он
    while True:
        # Получаем вариант пользователя
        user_data = user_guess(left, right)

        # Считаем попытки
        counter += 1

        # Сравниваем с загаданным числом и выводим результат
        if user_data > num_for_guess:
            print("Промах — перебор.\n")
        elif user_data < num_for_guess:
            print("Промах — недобор.\n")
        else:
            print("Вы угадали!\n")
            break

    print(f"Попыток сделано: {counter}")

    # Узнаем хочет ли пользователь сыграть ещё раз
    user_input = input("Хотите начать новую игру? (да/нет)\n").lower()

    if user_input == "да":
        num_guesser()


if __name__ == "__main__":
    # Приветствие
    print("Игра 'Угадай число'.")

    num_guesser()