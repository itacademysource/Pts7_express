import tkinter as tk
from tkinter import messagebox
import random
from PIL import ImageTk, Image


def generate_secret_number():
    """Функция, генерирующая случайное число от 1 до 100

    :return:
    """
    return random.randint(1, 100)


def check_guess(secret_number, guess):
    """Функция, проверяющая, насколько близко введенное число к секретному

    :param secret_number: загаданное число
    :param guess: введенный пользователем ответ
    :return: результат
    """
    global guesses_taken
    if guess < secret_number:
        guesses_taken += 1
        return "Холодно"
    elif guess > secret_number:
        guesses_taken += 1
        return "Горячо"
    else:
        return "Победа!"


def check_button_clicked():
    """Функция для обработки события кнопки "Проверить"

    :return:
    """
    guess = int(entry.get())
    result = check_guess(secret_number, guess)
    result_label.configure(text=result)

    if result == "Победа!":
        message = "Вы угадали число за {} попыток!".format(guesses_taken)
        messagebox.showinfo("Победа!", message)
        root.destroy()


# Загрузка изображения фона и получение размеров окна
background_image = Image.open("background_image.jpg")
window_width, window_height = 800, 600  # Установка размеров окна в пикселях

# Создание главного окна
root = tk.Tk()
root.title("Игра 'Холодно-горячо'")
root.geometry(f"{window_width}x{window_height}")
root.resizable(False, False)

# Масштабирование изображения фона под размер окна
background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Создание виджетов
instruction_label = tk.Label(root, text="Я загадал число от 1 до 100. Попробуйте отгадать его.", font=("Arial", 18),
                             bg="white")
instruction_label.place(relx=0.5, rely=0.4, anchor="center")

entry = tk.Entry(root, font=("Arial", 15))
entry.place(relx=0.5, rely=0.5, anchor="center")

check_button = tk.Button(root, text="Проверить", font=("Arial", 15), bg="#4CAF50", fg="white",
                         activebackground="#45A049", activeforeground="white", command=check_button_clicked)
check_button.place(relx=0.5, rely=0.6, anchor="center")

result_label = tk.Label(root, text="", font=("Arial", 15), fg="black", bg="white")
result_label.place(relx=0.5, rely=0.7, anchor="center")

# Инициализация переменных
secret_number = generate_secret_number()
guesses_taken = 0

# Запуск главного цикла
root.mainloop()
