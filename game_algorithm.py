import random

class GameAlgorithm:
    """
    Алгоритм для игры в крестики нолики с выбором сложности
    """

    def __init__(self, board_state, difficulty_level):
        """
        Устанавливаетя состояние доски 
        И выбранная сложность
        """

        self.board_state = board_state
        self.difficulty_level = difficulty_level

    def make_move(self):
        """
        В зависимости от уровня сложности ход делают разные алгоритмы
        """

        if self.difficulty_level == 0:
            return self.random_move()
        elif self.difficulty_level == 1:
            return self.pattern_move('O', 'X')
        elif self.difficulty_level == 2:
            return self.best_move('O', 'X')
        elif self.difficulty_level == 3:
            return self.best_move_alpha_beta('O', 'X')

    def random_move(self):
        """
        Ход делается рандомно в свободное поле
        """

        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board_state[i][j] is None]
        return random.choice(empty_cells)
    
    def pattern_move(self, player, opponent):
        """
        Проверка, можно ли победить одним ходом
        Если нельзя, проверка, какой ход сделать, чтобы заблокировать оппонента
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
        Проверка всех возможных выигрышных комбинаций
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
        Поиск лучшего хода используя алгоритм minimax
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
        Алгоритм minimax
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
        Поиск лучшего хода используя алгоритм minimax с альфа-бета отсечением
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
        Minimax алгоритм с альфа-бета отсечением
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