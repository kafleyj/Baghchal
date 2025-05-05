import tkinter as tk

# Define constants
BOARD_SIZE = 5
TIGER = "🐅"
GOAT = "🐐"
EMPTY = "⬜"

class BaagchalEmojiUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Baagchal 🐅🐐 Emoji UI")

        self.turn = "Goat"  # Goat starts
        self.board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.buttons = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

        self.status_label = tk.Label(root, text="Turn: 🐐 Goat", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.board_frame = tk.Frame(root)
        self.board_frame.pack()

        self.create_board()

        reset_btn = tk.Button(root, text="Reset", command=self.reset_board)
        reset_btn.pack(pady=10)

    def create_board(self):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                btn = tk.Button(
                    self.board_frame,
                    text=self.board[i][j],
                    font=("Arial", 24),
                    width=2,
                    height=1,
                    command=lambda x=i, y=j: self.place_piece(x, y)
                )
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn

    def place_piece(self, row, col):
        if self.board[row][col] != EMPTY:
            return  # Don't allow overwriting

        if self.turn == "Goat":
            self.board[row][col] = GOAT
            self.turn = "Tiger"
        else:
            self.board[row][col] = TIGER
            self.turn = "Goat"

        self.update_ui()

    def update_ui(self):
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                self.buttons[i][j].configure(text=self.board[i][j])

        self.status_label.configure(text=f"Turn: {'🐐 Goat' if self.turn == 'Goat' else '🐅 Tiger'}")

    def reset_board(self):
        self.board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.turn = "Goat"
        self.update_ui()

if __name__ == "__main__":
    root = tk.Tk()
    app = BaagchalEmojiUI(root)
    root.mainloop()
