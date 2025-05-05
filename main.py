import tkinter as tk
from tkinter import messagebox

game_over = 0  # счетчик нажатий на кнопку мыши для вычисления окончания игры
current_player = '' # глобальная переменная чем играет игрок
player_X = 0 # счетчик побед для Х
player_O = 0 # счетчик побед для Y


def check_winer(): # был ли случай победы
    for i in range(3): # перебор строк, столбцов
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':  # перебор строк, если было сопадение текста в строках не равное пустоте
            return True  #  возвращаем выигрышь
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':  # перебор столбцов, если было сопадение текста не равное пустоте
            return True  # возвращаем выигрышь

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':  # главная диагональ, если было сопадение текста не равное пустоте
        return True  # возвращаем выигрышь
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':  # вторая диагональ, если было сопадение текста не равное пустоте
        return True  #возвращаем выигрышь

    return False  # не было совпадений, не было выигрышей

def clear(): # очищение символов с кнопок, сброс
    for row in buttons: # перебор строк в списке кнопоу
        for button in row: # тавим на всех кнопках пустоту
            button['text'] = ''
    global game_over
    game_over = 0  # сброс счетчика нажатий, окончание игры

def on_click(row, col):  # нажатие кнопки мыши
    global game_over # сброс счетчика нажатий, окончание игры
    global current_player  # выбор текущего игрока
    global player_X # счетчики количества побед игроков
    global player_O # счетчики количества побед игроков

    if current_player == '':
        messagebox.showinfo('Выберие игрока', f'Нужно вырать чем будете играть: нолик или крестик!')

    if buttons[row][col]['text'] != '':  # если на переданой кнопке пусто
        return  # обратно к вызывающему
    buttons[row][col]['text'] = current_player  # если символ на кнопке совпал с текущим игроком
    # print(f'game_over: {game_over} ')

    if check_winer():  # проверяем была ли победа, если да то:
        if current_player == 'X':  # если победил этот, начисляем ему
            player_X += 1
        elif current_player == 'O':  #  если победил этот, начисляем ему
            player_O += 1
        messagebox.showinfo('Игра ', f'Игрок {current_player} победил, счет {player_X}:{player_O}')
        clear()  # очищаем поле после окончания игры
        if player_X == 3 or player_O == 3:
            messagebox.showinfo('Игра окончена', f'Игрок {current_player} победил, со счетом {player_X}:{player_O}')
    else:  # победы не было
        game_over += 1
        if game_over == 9:  # если было 9 нажатий игра заново, - ничья
            messagebox.showinfo('Игра окончена', 'Ничья!')
            clear()
    current_player = 'O' if current_player == 'X' else 'X'  # меняются игроки


def show_choice():  # выбор радиокнопками O или X, чем будешь играть
    global current_player
    selected_O_X = choice_var.get()
    messagebox.showinfo("Понятно, погнали!", f"Вы выбрали: {selected_O_X}")
    current_player = selected_O_X
    print(f'Выбран игрок играющий: {current_player}')
    return current_player

# главное окно
window = tk.Tk()
window.title('Крестики-нолики')
window.geometry('318x600')  # размер окна приложения

# Настраиваем строки и столбцы для центрирования
window.grid_rowconfigure(0, weight=1) # Настраиваем строки
window.grid_columnconfigure(0, weight=1) # Настраиваем  столбцы

# создаем фрейм
frame = tk.Frame(window, bg='AntiqueWhite3', width=318, height=560)
frame.grid(row=0, column=0, sticky='nsew')  # Используем grid для центрирования

# Добавляем строку текста
text1 = tk.Label(frame, text='Выберите: Х или О', font=('Arial', 16), bg='AntiqueWhite3')
text1.grid(row=0, column=0, columnspan=3, pady=10)  # Размещаем метку в верхней части фрейма

# Добавляем текстовое поле ввода
task_entry = tk.Entry(frame, font=('Arial', 12))
task_entry.grid(row=1, column=0, columnspan=3, pady=5)  # Размещаем текстовое поле под меткой

# блок радиокнопок
choice_var = tk.StringVar(value=" ")
# Создаем радиокнопки для выбора
choice_label = tk.Label(frame, text="Выберите чем будете играть:")
choice_label.grid(row=11, column=0, columnspan=3, pady=5)  # Используем grid для размещения метки
choices = ["X", "O"] # небольшой список выбора
for i, choice in enumerate(choices):
    radio = tk.Radiobutton(frame, text=choice, variable=choice_var, value=choice, command=show_choice)
    radio.grid(row=12 + i, column=0, pady=5)  # Размещаем радиокнопки в разных строках


# ставим кнопку "Очистить"
clear_button = tk.Button(frame, bg='AntiqueWhite2', text='Очистить', command=clear)
clear_button.grid(row=14, column=0, columnspan=3, pady=10)  # Используем grid для кнопки "Очистить"

buttons = []  # список для кнопок Х и О

for i in range(3):  # строим поле пока пустых кнопок Х и О
    row = []  # список строк из кнопок
    for j in range(3):
        btn = tk.Button(frame, text='', font=('Arial', 20), width=6, height=3, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i + 2, column=j)  # Увеличиваем индекс строки на 2, чтобы учесть метку и текстовое поле
        row.append(btn)  # добавляем кнопку в строку кнопок

    buttons.append(row)  # добавляем строку кнопок в список кнопок

window.mainloop()