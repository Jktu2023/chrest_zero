import tkinter as tk
from tkinter import messagebox

def show_color_choice():
    selected_color = color_var.get()
    messagebox.showinfo("Выбранный цвет", f"Вы выбрали цвет: {selected_color}")

# Создаем основное окно
root = tk.Tk()
root.title("Пример радиокнопок")

# Переменная для выбора цвета
color_var = tk.StringVar(value="Красный")

# Создаем радиокнопки для выбора цвета
color_label = tk.Label(root, text="Выберите цвет:")
color_label.pack()

colors = ["Красный", "Зеленый", "Синий"]
for color in colors:
    radio = tk.Radiobutton(root, text=color, variable=color_var, value=color, command=show_color_choice)
    radio.pack(anchor=tk.W)
#

# Запускаем главный цикл приложения
root.mainloop()