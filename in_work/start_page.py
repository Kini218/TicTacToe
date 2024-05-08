import tkinter as tk
from tkinter import ttk

root = tk.Tk()  # Cоздаем корневой объект - окно
root.title("Крестики нолики")  # Устанавливаем заголовок окна
root.geometry("600x600+350+50")  # Устанавливаем размеры окна

# Создаем холст
canvas = tk.Canvas(root)
canvas.pack()

# Cоздаем фрейм, в котором будем располагать все элементы
frame = tk.Frame(root)
frame.place(relwidth=1, relheight=1)

hello_message = ttk.Label(frame, text = "Привет!", justify="center", font=("Arial", 30, "bold"))
hello_message.place(relx= 0.5, rely=0.20, anchor="center")

game_title = ttk.Label(frame, text = "Это игра крестики-нолики", justify="center", font=("Arial", 20))
game_title.place(relx= 0.5, rely=0.30, anchor="center")

mode_select = ttk.Label(frame, text = "Как будешь играть?", justify="center", font=("Arial", 20))
mode_select.place(relx= 0.5, rely=0.40, anchor="center")

btn1 = ttk.Button(frame, text = 'Вдвоем')
btn1.place(relx= 0.15, rely=0.5, anchor="center")

btn2 = ttk.Button(frame, text = 'С компьютером')
btn2.place(relx= 0.8, rely=0.5, anchor="center")

game_difficult = ttk.Label(frame, text = "Выберите уровень сложности для игры с компьютером", justify="center", font=("Arial", 20))
game_difficult.place(relx= 0.5, rely=0.60, anchor="center")

scale = ttk.Scale(frame, orient="horizontal", from_=0, to=3)
scale.place(relx= 0.5, rely=0.70, anchor="center")

start_game_btn = ttk.Button(frame, text = 'Начать игру!')
start_game_btn.place(relx= 0.5, rely=0.8, anchor="center")

#Запускаем отрисовку интерфейса
root.mainloop()