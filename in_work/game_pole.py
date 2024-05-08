import tkinter as tk
from tkinter import ttk

root = tk.Tk()  # Создаем корневой объект - окно
root.title("Крестики нолики")  # Устанавливаем заголовок окна
root.geometry("600x600+350+50")  # Устанавливаем размеры окна

# Создаем холст
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Горизонтальные линии
canvas.create_line(0, 200, 600, 200, fill="black", width=4)
canvas.create_line(0, 400, 600, 400, fill="black", width=4)

# Вертикальные линии
canvas.create_line(200, 0, 200, 600, fill="black", width=4)
canvas.create_line(400, 0, 400, 600, fill="black", width=4)

#Запускаем отрисовку интерфейса
root.mainloop()