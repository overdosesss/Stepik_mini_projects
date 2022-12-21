from random import randint


# Функция для осуществления и проверки ввода пользователя
def user_input():
    try:
        num = int(input("Введите число:\n"))

        if 1 <= num <= 100:
            return num
        
        raise Exception
    except ValueError:
        print("Вы ошиблись при вводе, попробуйте ещё раз...")
        return main()
    except Exception:
        print("Не попали в диапазон [1; 100], попробуйте ещё раз...")
        return main()


def main():
    num_for_guess = randint(1, 100)

    while True:
        user_data = user_input()

        # Сравниваем с загаданным числом и выводим результат
        if user_data > num_for_guess:
            print("Промах — перебор.\n")
        elif user_data < num_for_guess:
            print("Промах — недобор.\n")
        else:
            print("Вы угадали!\n")
            break


if __name__ == "__main__":
    print("Игра 'Угадай число от 1 до 100'.\nСейчас мы загадаем число, а ваша задача — отгадать его.\n")
    main()