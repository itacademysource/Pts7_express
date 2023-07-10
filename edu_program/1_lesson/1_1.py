import tkinter as tk


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


total_likes = 0
total_dislikes = 0

root = tk.Tk()
root.title("Лайк-дизлайк")

# Создаем и размещаем кнопку "Лайк"
like_button = tk.Button(root, text="Лайк", width=10, command=like)
like_button.pack(pady=10)

# Создаем и размещаем кнопку "Дизлайк"
dislike_button = tk.Button(root, text="Дизлайк", width=10, command=dislike)
dislike_button.pack(pady=10)

# Создаем и размещаем метку для отображения количества лайков
likes_label = tk.Label(root, text="Likes: 0")
likes_label.pack()

# Создаем и размещаем метку для отображения количества дизлайков
dislikes_label = tk.Label(root, text="Dislikes: 0")
dislikes_label.pack()

root.mainloop()
