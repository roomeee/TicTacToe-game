from tkinter import *
from tkinter import messagebox
import random

PURPLE = "#8750ab"


def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        buttons[row][column]['text'] = player

        if check_winner() is False:
            player = players[1] if player == players[0] else players[0]
            label.config(text=(player + " turn"))
            highlight_player(player)

            if ai_mode and player == players[1]:  
                ai_move()
        else:
            end_game()


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg=PURPLE)
            buttons[row][1].config(bg=PURPLE)
            buttons[row][2].config(bg=PURPLE)
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg=PURPLE)
            buttons[1][column].config(bg=PURPLE)
            buttons[2][column].config(bg=PURPLE)
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg=PURPLE)
        buttons[1][1].config(bg=PURPLE)
        buttons[2][2].config(bg=PURPLE)
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg=PURPLE)
        buttons[1][1].config(bg=PURPLE)
        buttons[2][0].config(bg=PURPLE)
        return True
    elif not empty_spaces():
        return "Tie"
    else:
        return False


def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False


def highlight_player(current_player):
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(disabledforeground="black" if buttons[row][column]['text'] == current_player else "grey")


def end_game():
    global player, player_wins, ai_mode

    # for row in range(3):
    #     for column in range(3):
    #         buttons[row][column].config(state=DISABLED)

    if check_winner() == "Tie":
        messagebox.showinfo("Game Over", "It's a Tie!")
    else:
        player_wins[player] += 1
        messagebox.showinfo("Game Over", f"{player} wins!")

    score_label.config(text=f"Score: X {player_wins['X']} - {player_wins['O']} O")

    if not ai_mode:
        play_again_button.pack()
    else:
        new_game()


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    highlight_player(player)

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0", state=NORMAL)

    if ai_mode and player == players[1]:
        ai_move()


def ai_move():
    empty_cells = [(row, col) for row in range(3) for col in range(3) if buttons[row][col]['text'] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        # Choose the first available empty cell
        buttons[row][col].invoke()


def toggle_ai_mode():
    global ai_mode, players
    ai_mode = not ai_mode
    if ai_mode:
        players = ["X", "AI"]
        score_label.config(text=f"Score: X {player_wins['X']} - AI {player_wins['AI']}")
    else:
        players = ["X", "O"]
        score_label.config(text=f"Score: X {player_wins['X']} - {player_wins['O']} O")

    new_game()


window = Tk()
window.title("Tic-Tac-Toe")

players = ["X", "O"]
player = random.choice(players)
player_wins = {"X": 0, "O": 0, "AI": 0}
ai_mode = False

buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 35), fg="blue")
label.pack(side="top")

score_label = Label(text=f"Score: X {player_wins['X']} - {player_wins['O']} O", font=('consolas', 20), fg="black")
score_label.pack(side="top")

button_frame = Frame(window, bg="black")
button_frame.pack(side="top")

reset_button = Button(button_frame, text="Reset", font=('consolas', 10), command=new_game, bg="black", fg="white", width=10, height=1)
reset_button.pack(side="left", padx=5, pady=5)

ai_mode_button = Button(button_frame, text="Auto Turn", font=('consolas', 10), command=toggle_ai_mode, bg="black", fg="white")
ai_mode_button.pack(side="left", padx=5, pady=5)

play_again_button = Button(text="Play Again", font=('consolas', 16), command=new_game, bg="black", fg="white")

frame = Frame(window, bg="black")
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=4, height=1,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

highlight_player(player)

window.mainloop()
