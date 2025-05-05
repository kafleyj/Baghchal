def is_inside_board(x, y):
    """Check if the coordinates are inside the 5x5 board."""
    return 0 <= x < 5 and 0 <= y < 5


def is_reachable(x1, y1, x2, y2):
    """Check if a piece can move from (x1, y1) to (x2, y2)."""
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return (dx == 1 and dy == 0) or (dx == 0 and dy == 1) or (dx == 1 and dy == 1 and (x1 % 2 == 0 and y1 % 2 == 0))


def is_reachable_to_eat(board, x1, y1, x2, y2):
    """Check if a tiger can jump over a goat to (x2, y2)."""
    dx = x2 - x1
    dy = y2 - y1

    # Must be 2-step move
    if abs(dx) == 2 or abs(dy) == 2:
        mid_x = x1 + dx // 2
        mid_y = y1 + dy // 2

        if is_inside_board(mid_x, mid_y) and is_inside_board(x2, y2):
            if board[mid_x][mid_y] == "G" and board[x2][y2] == "_":
                # Diagonal moves only allowed from even-even cells
                if abs(dx) == abs(dy) == 2:
                    return x1 % 2 == 0 and y1 % 2 == 0
                return True
    return False


def locate_goat_to_be_eaten(board, x1, y1, x2, y2):
    """Get the coordinates of the goat between a tiger's jump move."""
    mid_x = (x1 + x2) // 2
    mid_y = (y1 + y2) // 2
    if board[mid_x][mid_y] == "G":
        return (mid_x, mid_y)
    return None


def graphics_coordinates_to_index(graphic_board, x, y):
    """Map canvas (pixel) coordinates to board index (row, col)."""
    for i in range(5):
        for j in range(5):
            gx, gy = graphic_board[i][j]
            if abs(gx - x) <= 40 and abs(gy - y) <= 40:
                return i, j
    return 0, 0  # fallback
