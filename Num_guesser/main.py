from random import randint


# Функция для проверки ввода пользователя
def user_input():
    try:
        num = int(input("Введите число:\n"))

        if 1 <= num <= 100:
            return num
        
        raise Exception
    except ValueError:
        print("Вы ошиблись при вводе, попробуйте ещё раз...")
        main()
    except Exception:
        print("Не попали в диапазон [1; 100], попробуйте ещё раз...")
        main()
    


# Приветствие
print("Игра 'Угадай число от 1 до 100'.\nСейчас мы загадаем число, а ваша задача — отгадать его.\n")


def main():
    # Сгенерируем случайное число из диапазона [1; 100]
    num_for_guess = randint(1, 100)

    # Бесконечный цикл, где будет ввод данных от пользователя и проверка угадал ли он
    while True:
        # Получаем вариант пользователя
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
    main()