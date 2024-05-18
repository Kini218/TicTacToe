import tkinter as tk
from tkinter import ttk

class GamePole:
    """
    Страница с игровым полем
    """
    def __init__(self, root, game_mode, difficulty_level):
        """
        Устанавливаем заголовок окна
        Устанавливаем размеры окна
        Устанавливаем режим игры и сложность
        """
        self.root = root
        self.root.title("Крестики нолики")
        self.root.geometry("600x600+350+50")
        
        self.setup_board()

        self.game_mode = game_mode
        self.difficulty_level = difficulty_level

    def setup_board(self):
        """
        Создаем игрововое поле
        """
        # Создаем холст
        canvas = tk.Canvas(self.root, width=600, height=600)
        canvas.pack()

        # Горизонтальные линии
        canvas.create_line(0, 200, 600, 200, fill="black", width=4)
        canvas.create_line(0, 400, 600, 400, fill="black", width=4)

        # Вертикальные линии
        canvas.create_line(200, 0, 200, 600, fill="black", width=4)
        canvas.create_line(400, 0, 400, 600, fill="black", width=4)