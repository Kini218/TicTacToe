import tkinter as tk
from tkinter import ttk

class StartPage:
    """
    Стартовая страница с приветствием и настройками
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
        
        self.mode_var = tk.StringVar()
        self.scale_value = tk.IntVar()

        self.selected_game_mode = None
        self.selected_difficulty_level = None
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

        hello_message = ttk.Label(frame, text="Привет!", justify="center", font=("Arial", 30, "bold"))
        hello_message.place(relx=0.5, rely=0.20, anchor="center")

        game_title = ttk.Label(frame, text="Это игра крестики-нолики", justify="center", font=("Arial", 20))
        game_title.place(relx=0.5, rely=0.30, anchor="center")

        mode_select = ttk.Label(frame, text="Как будешь играть?", justify="center", font=("Arial", 20))
        mode_select.place(relx=0.5, rely=0.40, anchor="center")

        btn1 = ttk.Button(frame, text="Вдвоем", command=lambda: self.mode_var.set("Вдвоем"))
        btn1.place(relx=0.15, rely=0.5, anchor="center")

        btn2 = ttk.Button(frame, text="С компьютером", command=lambda: self.mode_var.set("С компьютером"))
        btn2.place(relx=0.8, rely=0.5, anchor="center")

        game_difficult = ttk.Label(frame, text="Выберите уровень сложности для игры с компьютером", justify="center", font=("Arial", 20))
        game_difficult.place(relx=0.5, rely=0.60, anchor="center")

        self.scale = ttk.Scale(frame, orient="horizontal", from_=0, to=3)
        self.scale.place(relx=0.5, rely=0.70, anchor="center")

        start_game_btn = ttk.Button(frame, text="Начать игру!", command=self.setup_settings)
        start_game_btn.place(relx=0.5, rely=0.8, anchor="center")

    def setup_settings(self):
        """
        Сохраняется режим игры и уровень сложности
        Закрывается окно
        """

        selected_mode = self.mode_var.get()

        self.selected_game_mode = selected_mode
        self.scale_value.set(int(self.scale.get()))
        self.selected_game_mode = selected_mode
        self.selected_difficulty_level = self.scale_value.get()
        
        if selected_mode =="":
            self.selected_game_mode = "С компьютером"
        self.root.destroy()