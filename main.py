import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Крестики-нолики')
window.geometry('318x400')

frame = tk.Frame(window, bg='AntiqueWhite3', width=318, height= 400)
frame.pack(ipadx=5, ipady=5, pady=0)

current_player = 'X'
buttons = [] #

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
    pass

clear_botton = tk.Button(frame, bg='AntiqueWhite2', text='Очистить', command=clear()) #manager.new_task
clear_botton.pack(pady=5)
def on_click(row, col):
    global current_player
    if buttons[row][col]['text'] != '':
        return
    buttons[row][col]['text'] = current_player
    if check_winer():
        messagebox.showinfo('Игра окончена', f'Игрок {current_player} победил')
    current_player = 'O' if current_player == 'X' else 'X'

for i in range(3):
    row = [] #
    for j in range(3):
        btn = tk.Button(frame, text='', font=('Arial', 20), width=6, height=3, command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)



window.mainloop()