class Game:
    def __init__(self):
        self.grid = [['_' for _ in range(5)] for _ in range(5)]
        self.goats_in_hand = 20
        self.goats_killed = 0
        self.current_turn = "Goat"
        self.winner = None

    def board_init(self):
        # Place 4 tigers at corners
        self.grid[0][0] = 'T'
        self.grid[0][4] = 'T'
        self.grid[4][0] = 'T'
        self.grid[4][4] = 'T'

    def reload_config(self):
        self.goats_in_hand = 20
        self.goats_killed = 0
        self.current_turn = "Goat"
        self.winner = None

    def is_game_over(self):
        if self.goats_killed >= 5:
            self.winner = "Tiger"
            return True
        elif self.goats_in_hand == 0 and not self.any_goat_can_move():
            self.winner = "Tiger"
            return True
        elif not self.any_tiger_can_move():
            self.winner = "Goat"
            return True
        return False

    def any_goat_can_move(self):
        # Very basic logic: if there's any goat and at least one empty spot
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] == 'G':
                    for ni, nj in self.get_valid_moves(i, j):
                        return True
        return False

    def any_tiger_can_move(self):
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] == 'T':
                    if self.get_valid_moves(i, j) or self.get_eat_moves(i, j):
                        return True
        return False

    def get_valid_moves(self, i, j):
        # Return adjacent empty cells (up/down/left/right)
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < 5 and 0 <= nj < 5 and self.grid[ni][nj] == '_':
                moves.append((ni, nj))
        return moves

    def get_eat_moves(self, i, j):
        # Check for goat in adjacent cell and empty cell after that (basic rule)
        moves = []
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            mi, mj = i + dx // 2, j + dy // 2
            if (
                0 <= ni < 5 and 0 <= nj < 5 and
                0 <= mi < 5 and 0 <= mj < 5 and
                self.grid[mi][mj] == 'G' and
                self.grid[ni][nj] == '_'
            ):
                moves.append((ni, nj, mi, mj))
        return moves

    def apply_action(self, action, player):
        kind = action[0]

        if kind == "place":
            _, _, (x, y) = action
            self.grid[x][y] = 'G'
            self.goats_in_hand -= 1

        elif kind == "move":
            _, (x1, y1), (x2, y2) = action
            piece = self.grid[x1][y1]
            self.grid[x1][y1] = '_'
            self.grid[x2][y2] = piece

        elif kind == "eat":
            _, (x1, y1), (x2, y2), (gx, gy) = action
            self.grid[x1][y1] = '_'
            self.grid[gx][gy] = '_'
            self.grid[x2][y2] = 'T'
            self.goats_killed += 1

        # Switch turn
        self.current_turn = "Tiger" if player == "Goat" else "Goat"
