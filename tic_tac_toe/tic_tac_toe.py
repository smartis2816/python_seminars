from cProfile import label
from cgitb import text
import random
from tkinter import *

def game(push):
    global condition
    global matrix
    condition[push] = 'X'
    buttons[push].config(text='X', bg='white', state='disabled')
    matrix.remove(push)
    bot_move = random.choice(matrix)
    condition[bot_move] = '0'
    buttons[bot_move].config(text='0', bg='white', state='disabled')
    if check_winner('X'):
        label['text'] = 'Ты победил!'
    elif check_winner('0'):
        label['text'] = 'Бот победил!'

def check_winner(item):
    global condition
    if condition[0] == item and condition[1] == item and condition[2] == item:
        return True
    elif condition[3] == item and condition[4] == item and condition[5] == item:
        return True
    elif condition[6] == item and condition[7] == item and condition[8] == item:
        return True
    elif condition[0] == item and condition[3] == item and condition[6] == item:
        return True
    elif condition[1] == item and condition[4] == item and condition[7] == item:
        return True
    elif condition[2] == item and condition[5] == item and condition[8] == item:
        return True
    elif condition[0] == item and condition[4] == item and condition[8] == item:
        return True
    elif condition[2] == item and condition[4] == item and condition[6] == item:
        return True

root = Tk()
root.title('Игра "Крестики - нолики"')
condition = [None, None, None, None, None, None, None, None, None]
matrix = [0, 1, 2, 3, 4, 5, 6, 7, 8]

label = Label(width=20, text='Крестики-нолики')
label.grid(row=0, column=0, columnspan=3)
buttons = [Button(width=6, height=3, font=('Arial', 28, 'bold'), bg='#FDD9B5', command=lambda x=item: game(x)) for item in range(9)]
row, col = 1, 0
for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        col = 0
        row +=1

root.mainloop()