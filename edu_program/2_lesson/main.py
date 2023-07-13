import tkinter as tk
from PIL import ImageTk, Image


def calculate_weight():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = weight / (height ** 2)
        text = f"Индекс массы тела: {bmi:.2f}"
    except ValueError:
        text = f"Данные должны иметь числовой тип"
    result_label.config(text=text)


root = tk.Tk()
root.title("Калькулятор веса")

# Загрузка изображения фона и получение размеров окна
background_image = Image.open("background_image.jpg")
window_width, window_height = 800, 600  # Установка размеров окна в пикселях

# Масштабирование изображения фона под размер окна
background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Размещение метки и поля для ввода роста
height_label = tk.Label(root, text="Рост (м):", font=("Arial", 14), fg="black")
height_label.place(relx=0.5, rely=0.3, anchor="center")
height_entry = tk.Entry(root, font=("Arial", 14))
height_entry.place(relx=0.5, rely=0.35, anchor="center")

# Размещение метки и поля для ввода веса
weight_label = tk.Label(root, text="Вес (кг):", font=("Arial", 14), fg="black", bg="white")
weight_label.place(relx=0.5, rely=0.4, anchor="center")
weight_entry = tk.Entry(root, font=("Arial", 14))
weight_entry.place(relx=0.5, rely=0.45, anchor="center")

# Кнопка для расчета веса
calculate_button = tk.Button(root, text="Рассчитать", font=("Arial", 14), command=calculate_weight,
                             bg="#4CAF50", fg="white", activebackground="#45A049", activeforeground="white")
calculate_button.place(relx=0.5, rely=0.51, anchor="center")

# Метка для отображения результата
result_label = tk.Label(root, font=("Arial", 14), bg='white', fg='black')
result_label.place(relx=0.5, rely=0.6, anchor="center")

# Установка размеров окна
root.geometry(f"{window_width}x{window_height}")

root.mainloop()
