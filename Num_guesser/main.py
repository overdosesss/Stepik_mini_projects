from random import randint


# Сгенерируем случайное число из диапазона [1; 100]
num_for_guess = randint(1, 100)

# Бесконечный цикл, где будет ввод данных от пользователя и проверка угадал ли он
while True:
    user_input = int(input("Введите число:\n"))

    if user_input > num_for_guess:
        print("Промах — перебор.")
    elif user_input < num_for_guess:
        print("Промах — недобор.")
    else:
        print("Вы угадали!")
        break