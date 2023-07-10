# pip install pillow rembg

import tkinter as tk
from PIL import ImageTk, Image


def like():
    global total_likes
    total_likes += 1
    update_likes()


def dislike():
    global total_dislikes
    total_dislikes += 1
    update_dislikes()


def update_likes():
    likes_label.config(text="Likes: {}".format(total_likes))


def update_dislikes():
    dislikes_label.config(text="Dislikes: {}".format(total_dislikes))


def remove_background(image):
    alpha = image.split()[3]  # Получаем альфа-канал изображения
    bg = Image.new("RGBA", image.size, root.cget("bg"))  # Создаем изображение с фоном окна
    bg.paste(image, (0, 0), mask=alpha)  # Наложение изображения на фон с использованием альфа-канала
    return bg


total_likes = 0
total_dislikes = 0

root = tk.Tk()
root.title("Лайк-дизлайк")
root.geometry("400x300")
root.configure(bg="#F5F5F5")

# Загрузка изображений для лайка и дизлайка с альфа-каналом
like_image = Image.open("like.png").convert("RGBA")
dislike_image = Image.open("dislike.png").convert("RGBA")

# Удаление фона кнопок
like_image = remove_background(like_image)
dislike_image = remove_background(dislike_image)

# Масштабирование изображений
like_image = like_image.resize((100, 100), Image.LANCZOS)
dislike_image = dislike_image.resize((100, 100), Image.LANCZOS)

like_image = ImageTk.PhotoImage(like_image)
dislike_image = ImageTk.PhotoImage(dislike_image)

# Создаем фрейм для кнопок и размещаем его
buttons_frame = tk.Frame(root, bg="#F5F5F5")
buttons_frame.pack(pady=20)

# Создаем и размещаем кнопку "Лайк"
like_button = tk.Button(buttons_frame, image=like_image, bd=0, command=like)
like_button.pack(side=tk.LEFT, padx=10)

# Создаем и размещаем кнопку "Дизлайк"
dislike_button = tk.Button(buttons_frame, image=dislike_image, bd=0, command=dislike)
dislike_button.pack(side=tk.LEFT, padx=10)

# Создаем и размещаем метку для отображения количества лайков
likes_label = tk.Label(root, text="Likes: 0", font=("Arial", 14), bg="#F5F5F5")
likes_label.pack()

# Создаем и размещаем метку для отображения количества дизлайков
dislikes_label = tk.Label(root, text="Dislikes: 0", font=("Arial", 14), bg="#F5F5F5")
dislikes_label.pack()

root.mainloop()
