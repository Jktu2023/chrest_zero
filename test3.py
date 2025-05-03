import tkinter as tk
from tkinter import messagebox

game_over = 0  # счетчик нажатий на кнопку мыши для вычисления окончания игры
current_player = ''

def check_winer():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True

    return False

def clear():
    for row in buttons:
        for button in row:
            button['text'] = ''
    global game_over
    game_over = 0  # сброс счетчика нажатий

def on_click(row, col):
    global game_over
    global current_player
    if current_player == '':
        messagebox.showinfo('Выбор игрока', 'Выберите, чем будете играть: нолик или крестик!')
        return
    if buttons[row][col]['text'] != '':
        return
    buttons[row][col]['text'] = current_player
    if check_winer():
        messagebox.showinfo('Игра окончена', f'Игрок {current_player} победил')
        clear()
    else:
        game_over += 1
        if game_over == 9:
            messagebox.showinfo('Игра окончена', 'Ничья!')
            clear()
    current_player = 'O' if current_player == 'X' else 'X'

def show_choice():
    global current_player
    selected_O_X = choice_var.get()
    messagebox.showinfo("Понятно, погнали!", f"Вы выбрали: {selected_O_X}")
    current_player = selected_O_X
    print(f'Выбран игрок: {current_player}')

window = tk.Tk()
window.title('Крестики-нолики')
window.geometry('318x600')

# Настраиваем строки и столбцы для центрирования
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

frame = tk.Frame(window, bg='AntiqueWhite3', width=318, height=560)
frame.grid(row=0, column=0, sticky='nsew')

# Добавляем метку
text1 = tk.Label(frame, text='Выберите: Х или О', font=('Arial', 16), bg='AntiqueWhite3')
text1.grid(row=0, column=0, columnspan=3, pady=10)

# Добавляем текстовое поле ввода
task_entry = tk.Entry(frame, font=('Arial', 12))
task_entry.grid(row=1, column=0, columnspan=3, pady=5)

# блок радиокнопок
choice_var = tk.StringVar(value=" ")
choice_label = tk.Label(frame, text="Выберите чем будете играть:")
choice_label.grid(row=11, column=0, columnspan=3, pady=5)
choices = ["X", "O"]
for i, choice in enumerate(choices):
    radio = tk.Radiobutton(frame, text=choice, variable=choice_var, value=choice, command=show_choice)
    radio.grid(row=12 + i, column=0, pady=5)

# Добавляем кнопку "Сброс"
reset_button = tk.Button(frame, text='Сброс', command=clear)
reset_button.grid(row=14, column=0, columnspan=3, pady=10)  # Размещаем кнопку ниже радиокнопок

buttons = []  # список для кнопок
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(frame, text='', font=('Arial', 20), width=6, height=3, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i + 2, column=j)
        row.append(btn)
    buttons.append(row)

window.mainloop()