import random

class GameAlgorithm:
    """
    Алгоритм для игры в крестики нолики с выбором сложности
    """

    def __init__(self, board_state, difficulty_level, player_starts):
        """
        Инициализируется игра с заданным состоянием доски, уровнем сложности и начальным игроком.
        
        Args:
            board_state (list of list of str): Текущее состояние доски.
            difficulty_level (int): Уровень сложности игры (от 0 до 3).
            player_starts (bool): True, если игрок начинает, False, если начинает противник.
        """

        self.board_state = board_state
        self.difficulty_level = difficulty_level
        self.player_starts = player_starts

    def make_move(self):
        """
        Делается ход в зависимости от выбранного уровня сложности.

        Returns:
            tuple: Координаты хода.
        """

        if self.player_starts:
            player_opponent = ['O', 'X']
        else:
            player_opponent = ['X', 'O']
            
        if self.difficulty_level == 0:
            return self.random_move()
        elif self.difficulty_level == 1:
            return self.pattern_move(*player_opponent)
        elif self.difficulty_level == 2:
            return self.best_move(*player_opponent)
        elif self.difficulty_level == 3:
            return self.best_move_alpha_beta(*player_opponent)

    def random_move(self):
        """
        Делает случайный ход в пустую ячейку.

        Returns:
            tuple: Координаты хода.
        """

        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board_state[i][j] is None]
        return random.choice(empty_cells)
    
    def pattern_move(self, player, opponent):
        """
        Проверяет возможность выиграть одним ходом.
        Если выиграть нельзя, проверяет, можно ли заблокировать ход противника.

        Args:
            player (str): Символ игрока ('X' или 'O').
            opponent (str): Символ противника ('X' или 'O').

        Returns:
            tuple: Координаты хода.
        """

        # Проверка на победный ход
        for i in range(3):
            for j in range(3):
                if self.board_state[i][j] is None:
                    self.board_state[i][j] = player
                    if self.check_win(player):
                        self.board_state[i][j] = None
                        return (i, j)
                    self.board_state[i][j] = None
        
        # Проверка, для того, чтобы блокировать ход игрока
        for i in range(3):
            for j in range(3):
                if self.board_state[i][j] is None:
                    self.board_state[i][j] = opponent
                    if self.check_win(opponent):
                        self.board_state[i][j] = None
                        return (i, j)
                    self.board_state[i][j] = None
        
        return self.random_move()

    def check_win(self, player):
        """
        Проверяет все возможные выигрышные комбинации.

        Args:
            player (str): Символ игрока ('X' или 'O').

        Returns:
            bool: True, если игрок выиграл, иначе False.
        """

        win_states = [
            [self.board_state[0][0], self.board_state[0][1], self.board_state[0][2]],
            [self.board_state[1][0], self.board_state[1][1], self.board_state[1][2]],
            [self.board_state[2][0], self.board_state[2][1], self.board_state[2][2]],
            [self.board_state[0][0], self.board_state[1][0], self.board_state[2][0]],
            [self.board_state[0][1], self.board_state[1][1], self.board_state[2][1]],
            [self.board_state[0][2], self.board_state[1][2], self.board_state[2][2]],
            [self.board_state[0][0], self.board_state[1][1], self.board_state[2][2]],
            [self.board_state[2][0], self.board_state[1][1], self.board_state[0][2]],
        ]
        return [player, player, player] in win_states

    def best_move(self, player, opponent):
        """
        Находит лучший ход, используя алгоритм minimax.

        Args:
            player (str): Символ игрока ('X' или 'O').
            opponent (str): Символ противника ('X' или 'O').

        Returns:
            tuple: Координаты хода.
        """

        best_score = -float('inf')
        move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if self.board_state[i][j] is None:
                    self.board_state[i][j] = player
                    score = self.minimax(0, False, player, opponent)
                    self.board_state[i][j] = None
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def minimax(self, depth, is_maximizing, player, opponent):
        """
        Алгоритм minimax для поиска оптимального хода.

        Args:
            depth (int): Глубина рекурсии.
            is_maximizing (bool): Флаг, указывающий, оптимизирует ли текущий игрок.
            player (str): Символ игрока ('X' или 'O').
            opponent (str): Символ противника ('X' или 'O').

        Returns:
            int: Оценка текущего состояния доски.
        """

        if self.check_win(player):
            return 10 - depth
        elif self.check_win(opponent):
            return depth - 10
        elif all(self.board_state[i][j] is not None for i in range(3) for j in range(3)):
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board_state[i][j] is None:
                        self.board_state[i][j] = player
                        score = self.minimax(depth + 1, False, player, opponent)
                        self.board_state[i][j] = None
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board_state[i][j] is None:
                        self.board_state[i][j] = opponent
                        score = self.minimax(depth + 1, True, player, opponent)
                        self.board_state[i][j] = None
                        best_score = min(best_score, score)
            return best_score

    def best_move_alpha_beta(self, player, opponent):
        """
        Находит лучший ход, используя алгоритм minimax с альфа-бета отсечением.

        Args:
            player (str): Символ игрока ('X' или 'O').
            opponent (str): Символ противника ('X' или 'O').

        Returns:
            tuple: Координаты хода.
        """

        best_score = -float('inf')
        move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if self.board_state[i][j] is None:
                    self.board_state[i][j] = player
                    score = self.minimax_alpha_beta(0, -float('inf'), float('inf'), False, player, opponent)
                    self.board_state[i][j] = None
                    if score > best_score:
                        best_score = score
                        move = (i, j)
        return move

    def minimax_alpha_beta(self, depth, alpha, beta, is_maximizing, player, opponent):
        """
        Алгоритм minimax с альфа-бета отсечением.

        Args:
            depth (int): Глубина рекурсии.
            alpha (float): Текущее значение альфа.
            beta (float): Текущее значение бета.
            is_maximizing (bool): Флаг, указывающий, оптимизирует ли текущий игрок.
            player (str): Символ игрока ('X' или 'O').
            opponent (str): Символ противника ('X' или 'O').

        Returns:
            int: Оценка текущего состояния доски.
        """

        if self.check_win(player):
            return 10 - depth
        elif self.check_win(opponent):
            return depth - 10
        elif all(self.board_state[i][j] is not None for i in range(3) for j in range(3)):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board_state[i][j] is None:
                        self.board_state[i][j] = player
                        score = self.minimax_alpha_beta(depth + 1, alpha, beta, False, player, opponent)
                        self.board_state[i][j] = None
                        best_score = max(best_score, score)
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board_state[i][j] is None:
                        self.board_state[i][j] = opponent
                        score = self.minimax_alpha_beta(depth + 1, alpha, beta, True, player, opponent)
                        self.board_state[i][j] = None
                        best_score = min(best_score, score)
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
            return best_score