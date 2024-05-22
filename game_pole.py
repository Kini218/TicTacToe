import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno

class GamePole:
    """
    Страница с игровым полем
    """

    def __init__(self, root, game_mode, difficulty_level):
        """
        Устанавливается заголовок окна
        Устанавливаются размеры окна
        Устанавливается режим игры и сложность
        """

        self.root = root
        self.root.title("Крестики нолики")
        self.root.geometry("600x600+350+50")

        self.setup_board()

        self.game_mode = game_mode
        self.difficulty_level = difficulty_level

        self.current_player = "X"
        self.board_state = [[None for _ in range(3)] for _ in range(3)]

        # Привязываем событие клика мыши к холсту
        self.canvas.bind("<Button-1>", self.click_on_board)

    def setup_board(self):
        """
        Создание игровового поля
        """

        # Создаем холст
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()

        # Горизонтальные линии
        self.canvas.create_line(0, 200, 600, 200, fill="black", width=4)
        self.canvas.create_line(0, 400, 600, 400, fill="black", width=4)

        # Вертикальные линии
        self.canvas.create_line(200, 0, 200, 600, fill="black", width=4)
        self.canvas.create_line(400, 0, 400, 600, fill="black", width=4)

    def check_win(self):
        """
        Проверка выйгрышных комбинаций
        """

        wins = []

        # Проверка строк
        for i, row in enumerate(self.board_state):
            if row[0] == row[1] == row[2] and row[0] is not None:
                wins.append([(i, 0), (i, 1), (i, 2)])
                
        # Проверка столбцов
        for col in range(3):
            if self.board_state[0][col] == self.board_state[1][col] == self.board_state[2][col] and self.board_state[0][col] is not None:
                wins.append([(0, col), (1, col), (2, col)])
            
        # Проверка диагоналей
        if self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2] and self.board_state[0][0] is not None:
            wins.append([(0, 0), (1, 1), (2, 2)])
        if self.board_state[0][2] == self.board_state[1][1] == self.board_state[2][0] and self.board_state[0][2] is not None:
            wins.append([(0, 2), (1, 1), (2, 0)])

        return wins

    def click_on_board(self, event):
        """
        Действия происходящие по клику на доску
        """

        # Получаем координаты клика
        x, y = event.x, event.y
        
        # Определяем, в какой квадрат был сделан клик
        row, col = y // 200, x // 200

        # Проверяем, что квадрат пустой
        if self.board_state[row][col] == None:
            self.board_state[row][col] = self.current_player

            # Рисуем крестик или нолик
            self.draw_symbol(row, col, self.current_player)

            # Меняем текущего игрока
            self.current_player = 'O' if self.current_player == 'X' else 'X'
    
        # проверяем, есть ли победа
        wins = self.check_win()
        if wins:
            self.canvas.bind("<Button-1>", self.disable_click)
            self.draw_win_line(wins)
            # Запуск функции через 2 секунды, чтобы было время увидеть линию
            self.root.after(2000, self.trigger_win_alert)
        
        # проверка на ничью
        if all(all(cell is not None for cell in row) for row in self.board_state):
            self.root.after(2000, self.trigger_no_win)

    def destroy_window(self):
        """
        Закрытие окна
        """

        self.root.destroy()


    def disable_click(self, event):
        """
        Отключение возможности ставить символ
        """

        return "break"

    def draw_symbol(self, row, col, player):
        """
        Простановка символа в определенной клетке
        """

        x_start, y_start = col * 200, row * 200
        x_end, y_end = x_start + 200, y_start + 200
        
        if player == 'X':
            self.canvas.create_line(x_start, y_start, x_end, y_end, fill="blue", width=4)
            self.canvas.create_line(x_start, y_end, x_end, y_start, fill="blue", width=4)
        elif player == 'O':
            self.canvas.create_oval(x_start, y_start, x_end, y_end, outline="green", width=4)

    def draw_win_line(self, wins):
        """
        Рисуется линия, показывающая выйгрышную комбинацию
        """

        for line in wins:
            # Находим минимальное и максимальное значение по x и y для линии
            min_x = min(point[1] for point in line)
            max_x = max(point[1] for point in line)
            min_y = min(point[0] for point in line)
            max_y = max(point[0] for point in line)

            # Выбираем начальную и конечную точку линии в зависимости от направления
            # Если линия горизонтальная
            if min_y == max_y:
                x_start, y_start = min_x * 200, min_y * 200 + 100
                x_end, y_end = max_x * 200 + 200, max_y * 200 + 100
            # Если линия вертикальная
            elif min_x == max_x:
                x_start, y_start = min_x * 200 + 100, min_y * 200
                x_end, y_end = max_x * 200 + 100, max_y * 200 + 200
            # Если главная диагональ
            elif line == [(0, 0), (1, 1), (2, 2)]:
                x_start, y_start = line[0][1] * 200, line[0][0] * 200
                x_end, y_end = line[2][1] * 200 + 200, line[2][0] * 200 + 200
            # Если диагональ побочная
            elif line == [(0, 2), (1, 1), (2, 0)]:
                x_start, y_start = line[0][1] * 200 + 200, line[0][0] * 200
                x_end, y_end = line[2][1] * 200, line[2][0] * 200 + 200

            self.canvas.create_line(x_start, y_start, x_end, y_end, fill="red", width=4)
    
    def play_again(self):
        """
        Запустить игру снова
        """

        pass
        
    def trigger_no_win(self):
        """
        alert с сообщением о ничьей
        """

        result = askyesno(title="Ничья", message="Ничья, сыграем еще?")
        if result: 
            showinfo("Еще раз", "Отлично!")
            self.play_again()
        else:
            self.destroy_window()

    def trigger_win_alert(self):
        """
        alert с сообщением о выйгрыше и с предложением сыграть еще раз
        """

        if self.current_player == "O":
            result = askyesno(title="Победа", message="Крестики победили, сыграем еще?")
        else:
            result = askyesno(title="Победа", message="Нолики победили, сыграем еще?")
        
        if result: 
            showinfo("Еще раз", "Отлично!")
            self.play_again()
        else:
            self.destroy_window()