import random


# Функция, генерирующая случайное число от 1 до 100
def generate_secret_number():
    return random.randint(1, 100)


# Функция, проверяющая, насколько близко введенное число к секретному
def check_guess(secret_number, guess):
    if guess < secret_number:
        return "Холодно"
    elif guess > secret_number:
        return "Горячо"
    else:
        return "Победа!"


# Функция, запускающая игру
def play_game():
    secret_number = generate_secret_number()
    guesses_taken = 0

    print("Добро пожаловать в игру 'Холодно-горячо'!")
    print("Я загадал число от 1 до 100. Попробуйте отгадать его.")

    while True:
        guess = int(input("Введите вашу догадку: "))
        guesses_taken += 1

        result = check_guess(secret_number, guess)
        print(result)

        if result == "Победа!":
            print("Вы угадали число за", guesses_taken, "попыток!")
            break


# Запуск игры
play_game()
