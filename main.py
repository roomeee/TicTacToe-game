from tkinter import *
import random

PURPLE = "#8750ab"


def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")


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
    elif empty_spaces() is False:
        return "Tie"
    else:
        return False


def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")


window = Tk()
window.title("Tic-Tac-Toe")
# window.configure(bg="black")

players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 35), fg="blue")
label.pack(side="top")

reset_button = Button(text="reset", font=('consolas', 24), command=new_game,bg="black" ,fg="white", width=10, height=1)
reset_button.pack(side="top")

frame = Frame(window, bg="black")
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=4, height=1,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
