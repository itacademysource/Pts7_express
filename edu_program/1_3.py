import os
import tkinter as tk

from PIL import ImageTk, Image


def like():
    global total_likes, current_image_index
    total_likes += 1
    current_image_index = (current_image_index + 1) % len(image_filenames)
    update_likes()
    update_image()


def dislike():
    global total_dislikes, current_image_index
    total_dislikes += 1
    current_image_index = (current_image_index + 1) % len(image_filenames)
    update_dislikes()
    update_image()


def update_likes():
    likes_label.config(text="Likes: {}".format(total_likes))


def update_dislikes():
    dislikes_label.config(text="Dislikes: {}".format(total_dislikes))


def remove_background(image):
    alpha = image.split()[3]  # Получаем альфа-канал изображения
    bg = Image.new("RGBA", image.size, root.cget("bg"))  # Создаем изображение с фоном окна
    bg.paste(image, (0, 0), mask=alpha)  # Наложение изображения на фон с использованием альфа-канала
    return bg


def update_image():
    image_path = os.path.join(image_directory, image_filenames[current_image_index])
    image = Image.open(image_path)
    image = image.resize((300, 200), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    image_label.configure(image=photo)
    image_label.image = photo


total_likes = 0
total_dislikes = 0
current_image_index = 0

image_directory = "images"
image_filenames = sorted(os.listdir(image_directory))

root = tk.Tk()
root.title("Лайк-дизлайк")
root.geometry("400x450")
root.configure(bg="#F5F5F5")

image_path = os.path.join(image_directory, image_filenames[current_image_index])
image = Image.open(image_path)
image = image.resize((300, 200), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(root, image=photo)
image_label.pack(pady=10)

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
