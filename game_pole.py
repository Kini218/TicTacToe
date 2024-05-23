import tkinter as tk
from tkinter.messagebox import askyesno
from game_algorithm import MinimaxAlgorithm

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

        # Создание холста
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()

        self.setup_board()

        self.game_mode = game_mode
        self.difficulty_level = difficulty_level

        self.current_player = "X"
        self.winner = False
        self.board_state = [[None for _ in range(3)] for _ in range(3)]

        # Привязка события клика мыши к холсту
        self.canvas.bind("<Button-1>", self.click_on_board)

    def setup_board(self):
        """
        Создание игровового поля
        """

        # Горизонтальные линии
        self.canvas.create_line(0, 200, 600, 200, fill="black", width=4)
        self.canvas.create_line(0, 400, 600, 400, fill="black", width=4)

        # Вертикальные линии
        self.canvas.create_line(200, 0, 200, 600, fill="black", width=4)
        self.canvas.create_line(400, 0, 400, 600, fill="black", width=4)

    def check_win(self):
        """
        Проверка на победу или ничью
        """

        # Проверка, есть ли победа
        wins = self.check_win_combinations()
        if wins:
            self.canvas.bind("<Button-1>", self.disable_click)
            self.draw_win_line(wins)
            # Запуск функции через 2 секунды, чтобы было время увидеть линию
            self.root.after(2000, self.trigger_win_alert)
            self.winner = True
        
        # Проверка на ничью
        elif all(all(cell is not None for cell in row) for row in self.board_state):
            self.root.after(2000, self.trigger_no_win)
            self.winner = True

    def check_win_combinations(self):
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

    def clear_canvas(self):
        """
        Очистить экран
        """
        self.canvas.delete("all")

    def click_on_board(self, event):
        """
        Действия происходящие по клику на доску
        """

        # Получение координат клика
        x, y = event.x, event.y
        
        # Определение, в какой квадрат был сделан клик
        row, col = y // 200, x // 200

        # Проверка, что квадрат пустой
        if self.board_state[row][col] == None and self.winner == False:
            self.board_state[row][col] = self.current_player

            # Отрисовка крестик или нолик
            self.draw_symbol(row, col, self.current_player)

            # Смена текущего игрока
            self.current_player = 'O' if self.current_player == 'X' else 'X'

            self.check_win()

        if self.game_mode == "С компьютером":
            self.computer_move()

    def computer_move(self):
        """
        Компьютер делает ход
        """

        minimax = MinimaxAlgorithm(self.board_state, self.difficulty_level)

        row, col = minimax.make_move()
        # Проверка, что квадрат пустой
        if self.board_state[row][col] == None and self.winner == False:
            self.board_state[row][col] = self.current_player

            # Отрисовка крестик или нолик
            self.draw_symbol(row, col, self.current_player)

            # Смена текущего игрока
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.check_win()

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
            # Нахождение минимального и максимального значений по x и y для линии
            min_x = min(point[1] for point in line)
            max_x = max(point[1] for point in line)
            min_y = min(point[0] for point in line)
            max_y = max(point[0] for point in line)

            # Выбор начальной и конечной точки линии в зависимости от направления
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

        self.clear_canvas()
        self.setup_board()
        self.current_player = "X"
        self.board_state = [[None for _ in range(3)] for _ in range(3)]
        self.winner = False
        # Привязка события клика мыши к холсту
        self.canvas.bind("<Button-1>", self.click_on_board)
        
    def trigger_no_win(self):
        """
        alert с сообщением о ничьей
        """

        result = askyesno(title="Ничья", message="Ничья, сыграем еще?")
        if result: 
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
            self.play_again()
        else:
            self.destroy_window()