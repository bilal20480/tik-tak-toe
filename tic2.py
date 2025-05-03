import tkinter as tk
from tkinter import messagebox
import random

# Globals
players = {}
symbols = {}
current_symbol = ""
current_player = ""
board = [""] * 9
buttons = []
game_count = 0
score = {1: 0, 2: 0}
golden_chance_holder = None

# Main window
root = tk.Tk()
root.title("Tic Tac Toe - Best of 3")
root.geometry("420x600")
root.resizable(False, False)
root.config(bg="#121212")

status_label = None
game_frame = None

# Utility
def reset_board():
    global board, current_symbol, current_player
    board = [""] * 9
    for b in buttons:
        b.config(text="", state="normal", bg="#1f1f1f", fg="white")
    current_symbol = symbols[1] if random.choice([True, False]) else symbols[2]
    current_player = players[1] if current_symbol == symbols[1] else players[2]
    update_status()

def update_status():
    status_label.config(text=f"{current_player}'s Turn ({current_symbol})")

def check_winner():
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for i, j, k in wins:
        if board[i] == board[j] == board[k] != "":
            for idx in [i, j, k]:
                buttons[idx].config(bg="#4caf50")  # Highlight win
            return True
    return False

def check_draw():
    return all(cell != "" for cell in board)

def on_click(index):
    global current_symbol, current_player, game_count, golden_chance_holder
    if board[index] == "":
        board[index] = current_symbol
        buttons[index].config(text=current_symbol, state="disabled", disabledforeground="white", bg="#333333")
        if check_winner():
            if current_player == players[1]:
                score[1] += 1
            else:
                score[2] += 1
            if score[1] == 1 or score[2] == 1:
                golden_chance_holder = current_player
            messagebox.showinfo("🎉 Round Over", f"{current_player} wins this round!")
            game_count += 1
            if game_count == 3:
                show_final_result()
            else:
                reset_board()
        elif check_draw():
            messagebox.showinfo("Draw", "This round is a draw!")
            game_count += 1
            if game_count == 3:
                show_final_result()
            else:
                reset_board()
        else:
            current_player = players[2] if current_player == players[1] else players[1]
            current_symbol = symbols[1] if current_player == players[1] else symbols[2]
            update_status()

def show_final_result():
    winner = None
    if score[1] > score[2]:
        winner = players[1]
    elif score[2] > score[1]:
        winner = players[2]
    else:
        winner = golden_chance_holder + " (Golden Chance)"

    final_screen = tk.Toplevel(root)
    final_screen.attributes('-fullscreen', True)
    final_screen.configure(bg="black")
    label = tk.Label(final_screen, text=f"{winner} Wins the Game!", font=("Arial", 45, "bold"), fg="gold", bg="black")
    label.pack(expand=True)
    tk.Button(final_screen, text="Exit", command=root.destroy, font=("Arial", 20), bg="red", fg="white").pack(pady=30)

# UI Screens
def start_game():
    global players, symbols, current_symbol, current_player, status_label, game_frame

    name1 = entry1.get()
    name2 = entry2.get()

    if not name1 or not name2:
        messagebox.showerror("Input Error", "Please enter both player names.")
        return

    players[1] = name1
    players[2] = name2

    # Random symbol assignment
    if random.choice([True, False]):
        symbols[1], symbols[2] = "X", "O"
    else:
        symbols[1], symbols[2] = "O", "X"

    messagebox.showinfo("Symbols Assigned",
                        f"{players[1]} is '{symbols[1]}'\n{players[2]} is '{symbols[2]}'")

    start_frame.pack_forget()

    # Game UI
    status_label = tk.Label(root, text="", font=("Arial", 18), bg="#121212", fg="#00ffc3")
    status_label.pack(pady=20)

    game_frame = tk.Frame(root, bg="#121212")
    game_frame.pack()

    for i in range(9):
        btn = tk.Button(game_frame, text="", font=("Arial", 24), width=5, height=2, bg="#1f1f1f", fg="white",
                        command=lambda i=i: on_click(i), activebackground="#444444", relief="flat")
        btn.grid(row=i//3, column=i%3, padx=5, pady=5)
        buttons.append(btn)

    reset_board()

# Name entry screen
start_frame = tk.Frame(root, bg="#121212")
start_frame.pack(pady=100)

tk.Label(start_frame, text="Player 1 Name:", font=("Arial", 16), bg="#121212", fg="white").pack(pady=5)
entry1 = tk.Entry(start_frame, font=("Arial", 16), width=20, bg="#2a2a2a", fg="white", insertbackground="white")
entry1.pack()

tk.Label(start_frame, text="Player 2 Name:", font=("Arial", 16), bg="#121212", fg="white").pack(pady=5)
entry2 = tk.Entry(start_frame, font=("Arial", 16), width=20, bg="#2a2a2a", fg="white", insertbackground="white")
entry2.pack()

start_btn = tk.Button(start_frame, text="Start Game", font=("Arial", 16), bg="#00ffc3", fg="black", padx=20, pady=5, command=start_game)
start_btn.pack(pady=20)

# Hover effect
def on_enter(e): e.widget.config(bg="#00e6b8")
def on_leave(e): e.widget.config(bg="#00ffc3")
start_btn.bind("<Enter>", on_enter)
start_btn.bind("<Leave>", on_leave)

# Start app
root.mainloop()
