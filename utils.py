def encode_board(board):
    return ''.join([''.join(row) for row in board])

def decode_board(state_str):
    board = []
    for i in range(0, 25, 5):
        board.append(list(state_str[i:i+5]))
    return board

def get_reward(game, player):
    if game.is_game_over():
        return 1 if game.winner == player else -1
    return 0
