import tkinter as tk
from tkinter import ttk
import webbrowser

class FinalPage:
    """
    Финальная страница с благодарностью и ссылкой на git
    """

    def __init__(self, root):
        """
        Cоздается корневой объект - окно
        Устанавливается заголовок окна
        Устанавливаются размеры окна
        """

        self.root = root
        self.root.title("Крестики нолики")
        self.root.geometry("600x600+350+50")

        self.setup_ui()

    def setup_ui(self):
        """
        Создается холст
        Рисуются элементы
        """

        canvas = tk.Canvas(self.root)
        canvas.pack()

        frame = tk.Frame(self.root)
        frame.place(relwidth=1, relheight=1)

        thanks_message = ttk.Label(frame, text="Спасибо за игру!", justify="center", font=("Arial", 30, "bold"))
        thanks_message.place(relx=0.5, rely=0.20, anchor="center")

        developer = ttk.Label(frame, text="Developed by Nikita", justify="center", font=("Arial", 20))
        developer.place(relx=0.5, rely=0.70, anchor="center")

        git_link = ttk.Label(frame, text="GitHub(https://github.com/Kini218)", justify="center", font=("Arial", 20), foreground="blue")
        git_link.place(relx=0.5, rely=0.80, anchor="center")
        git_link.bind("<Button-1>", self.open_github)

    def open_github(self, event):
        """
        Открывается github по клику на ссылку
        После открытия уничтожается страница
        """

        webbrowser.open_new("https://github.com/Kini218")
        self.root.destroy()