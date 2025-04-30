import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Крестики-нолики')
window.geometry('318x400')   # размер окна приложения

# Настраиваем строки и столбцы для центрирования
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

frame = tk.Frame(window, bg='AntiqueWhite3', width=318, height=400)  # создаем фрэйм
frame.grid(row=0, column=0, sticky='nsew')  # Используем grid для центрирования

current_player = 'X'  # устанавливаем текущего игрока
buttons = []  # список для кнопок

def check_winer():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':  # перебор строк
            return True  # если совпала возвращаем выиигрышь
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '': # перебор столбцов
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '': # главная диагональ
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '': # вторая диагональ
        return True
    return False

def clear():
    for row in buttons:
        for button in row:
            button['text'] = ''

clear_button = tk.Button(frame, bg='AntiqueWhite2', text='Очистить', command=clear)
clear_button.grid(row=3, column=0, columnspan=3, pady=5)  # Используем grid для кнопки "Очистить"

def on_click(row, col):
    global current_player
    if buttons[row][col]['text'] != '':
        return
    buttons[row][col]['text'] = current_player
    if check_winer():
        messagebox.showinfo('Игра окончена', f'Игрок {current_player} победил')
    current_player = 'O' if current_player == 'X' else 'X'

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(frame, text='', font=('Arial', 20), width=6, height=3, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

window.mainloop()