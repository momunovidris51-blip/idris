import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("X-O Оюну")
        
        # Оюндун абалы
        self.player = "X"
        self.board = [""] * 9
        self.buttons = []
        
        # Интерфейсти түзүү
        self.create_board()
        
        # Маалымат жазуучу текст
        self.label = tk.Label(self.root, text="Кезек: X", font=("Arial", 14))
        self.label.pack(pady=10)
        
        # Рестарт топчусу (оюн бүткөндө чыгат)
        self.restart_button = tk.Button(self.root, text="Кайра баштоо", font=("Arial", 12), 
                                       bg="green", fg="white", command=self.restart_game)

    def create_board(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        for i in range(9):
            btn = tk.Button(self.frame, text="", font=("Arial", 20, "bold"), 
                           width=5, height=2, command=lambda x=i: self.click(x))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def click(self, i):
        if self.board[i] == "" and self.label["text"].startswith("Кезек"):
            self.board[i] = self.player
            color = "red" if self.player == "X" else "blue"
            self.buttons[i].config(text=self.player, fg=color)
            
            if self.check_win():
                self.label.config(text=f"Жеңүүчү: {self.player}!", fg="green")
                self.restart_button.pack(pady=10)
            elif "" not in self.board:
                self.label.config(text="Тең чыгуу!", fg="orange")
                self.restart_button.pack(pady=10)
            else:
                self.player = "O" if self.player == "X" else "X"
                self.label.config(text=f"Кезек: {self.player}")

    def check_win(self):
        wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def restart_game(self):
        self.player = "X"
        self.board = [""] * 9
        self.label.config(text="Кезек: X", fg="black")
        for btn in self.buttons:
            btn.config(text="", fg="black")
        self.restart_button.pack_forget()

# Программаны жүргүзүү
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
