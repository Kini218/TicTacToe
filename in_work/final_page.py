import tkinter as tk
from tkinter import ttk
import webbrowser

def open_github(event):
    webbrowser.open_new("https://github.com/Kini218")

root = tk.Tk()  # Создаем корневой объект - окно
root.title("Крестики нолики")  # Устанавливаем заголовок окна
root.geometry("600x600+350+50")  # Устанавливаем размеры окна

# Создаем холст
canvas = tk.Canvas(root)
canvas.pack()

# Cоздаем фрейм, в котором будем располагать все элементы
frame = tk.Frame(root)
frame.place(relwidth=1, relheight=1)

thanks_message = ttk.Label(frame, text="Спасибо за игру!", justify="center", font=("Arial", 30, "bold"))
thanks_message.place(relx=0.5, rely=0.20, anchor="center")

developer = ttk.Label(frame, text="Developed by Nikita", justify="center", font=("Arial", 20))
developer.place(relx=0.5, rely=0.70, anchor="center")

git_link = ttk.Label(frame, text="GitHub(https://github.com/Kini218)", justify="center", font=("Arial", 20), foreground="blue")
git_link.place(relx=0.5, rely=0.80, anchor="center")
git_link.bind("<Button-1>", open_github)

#Запускаем отрисовку интерфейса
root.mainloop()
