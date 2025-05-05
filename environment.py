from copy import deepcopy

class BaagchalEnv:
    def __init__(self, game):
        self.game = game

    def get_state(self):
        return ''.join([''.join(row) for row in self.game.grid])

    def get_legal_actions(self, player):
        actions = []

        if player == "Goat":
            if self.game.goats_in_hand > 0:
                for i in range(5):
                    for j in range(5):
                        if self.game.grid[i][j] == '_':
                            actions.append(("place", None, (i, j)))
            else:
                for i in range(5):
                    for j in range(5):
                        if self.game.grid[i][j] == 'G':
                            for ni, nj in self.game.get_valid_moves(i, j):
                                actions.append(("move", (i, j), (ni, nj)))

        elif player == "Tiger":
            for i in range(5):
                for j in range(5):
                    if self.game.grid[i][j] == 'T':
                        for ni, nj in self.game.get_valid_moves(i, j):
                            actions.append(("move", (i, j), (ni, nj)))
                        for ni, nj, gi, gj in self.game.get_eat_moves(i, j):
                            actions.append(("eat", (i, j), (ni, nj), (gi, gj)))
        return actions

    def apply_action(self, action, player):
        self.game = deepcopy(self.game)
        self.game.apply_action(action, player)
        return self.game
