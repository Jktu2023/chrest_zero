import tkinter as tk
from tkinter import messagebox


game_over = 0 # счетчик нажатий на кнопку мыши  для вычисления окончания игры
def check_winer():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':  # перебор строк
            return True  # если совпала возвращаем выигрышь
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '': # перебор столбцов
            return True # если совпала возвращаем выигрышь
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '': # главная диагональ
        return True # если совпала возвращаем выигрышь
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '': # вторая диагональ
        return True # если совпала возвращаем выигрышь
    return False  # не было выигрышей

def clear():
    for row in buttons:
        for button in row:
            button['text'] = ''



def on_click(row, col):  #  нажатие кнопки мыши
    global game_over
    global current_player
    if buttons[row][col]['text'] != '':  # если на кнопке пусто
        return  # обратно к вызывающему
    buttons[row][col]['text'] = current_player  # если символ на кнопке совпал с текущим игроком
    if check_winer():  # проверяем была ли победа,  если да то:
        messagebox.showinfo('Игра окончена', f'Игрок {current_player} победил')
    else: # победы не было
        game_over += 1
        if game_over == 9:  # если было 9 нажатий игра заново, - ничья
            clear()
    current_player = 'O' if current_player == 'X' else 'X' # меняются игроки

def show_choice():
    selected_O_X = choice_var.get()
    messagebox.showinfo("Выбранный цвет", f"Вы выбрали: {selected_O_X}")


window = tk.Tk()
window.title('Крестики-нолики')
window.geometry('318x550')   # размер окна приложения

# Настраиваем строки и столбцы для центрирования
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

frame = tk.Frame(window, bg='AntiqueWhite3', width=318, height=500)  # создаем фрэйм
frame.grid(row=0, column=0, sticky='nsew')  # Используем grid для центрирования

# Добавляем метку
text1 = tk.Label(frame, text='Выбирите: Х или О', font=('Arial', 16), bg='AntiqueWhite3')
text1.grid(row=0, column=0, columnspan=3, pady=10)  # Размещаем метку в верхней части фрейма

# Добавляем текстовое поле ввода
task_entry = tk.Entry(frame, font=('Arial', 12))
task_entry.grid(row=1, column=0, columnspan=3, pady=5)  # Размещаем текстовое поле под меткой


choice_var = tk.StringVar(value="X")
# Создаем радиокнопки для выбора цвета
choice_label = tk.Label(frame, text="Выберите чем будете играть:")
choice_label.grid(row=11, column=0, columnspan=3, pady=5)  # Используем grid для размещения метки

choices = ["X", "O"]
for choice in choices:
    radio = tk.Radiobutton(frame, text=choice, variable=choice_var, value=choice, command=show_choice)
    #radio.pack(anchor=tk.W)
    radio.grid(row=12, column=0, columnspan=3, pady=5)  #


# task_entry1 = tk.Radiobutton(frame, font=('Arial', 12))
# task_entry1.grid(row=12, column=0, columnspan=3, pady=5)  # Размещаем текстовое поле под меткой

current_player = 'X'  # устанавливаем текущего игрока
buttons = []  # список для кнопок

clear_button = tk.Button(frame, bg='AntiqueWhite2', text='Очистить', command=clear) # ставим кнопку "Очистить"
clear_button.grid(row=3, column=0, columnspan=3, pady=55)  # Используем grid для кнопки "Очистить"

for i in range(3):  # строим поле пустых кнопок
    row = [] # список строк из кнопок
    for j in range(3):
        btn = tk.Button(frame, text='', font=('Arial', 20), width=6, height=3, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i + 2, column=j)  # Увеличиваем индекс строки на 2, чтобы учесть метку и текстовое поле
        row.append(btn) # добавляем кнопку в строку кнопок

    buttons.append(row) # добавляем строку кнопок в список кнопок

window.mainloop()