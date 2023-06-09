#                                               ⊞||===--- TIC TAC TOE ---===||⊞                                                              #


# Importing ⇓

from tkinter import *
import random

# Window []


win = Tk()
win.title("Tic Tac Toe")

# Main Game Schmeat

# Defining {/}


def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+"'s turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+"'s turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie!"))


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="#95E8A3")
            buttons[row][1].config(bg="#95E8A3")
            buttons[row][2].config(bg="#95E8A3")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="#95E8A3")
            buttons[1][column].config(bg="#95E8A3")
            buttons[2][column].config(bg="#95E8A3")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="#95E8A3")
        buttons[1][1].config(bg="#95E8A3")
        buttons[2][2].config(bg="#95E8A3")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="#95E8A3")
        buttons[1][1].config(bg="#95E8A3")
        buttons[2][0].config(bg="#95E8A3")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#FDFD96")
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
    label.config(text=(player+"'s turn"))
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")


players = ["X", "O"]
player = random.choice(players)

buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

label = Label(text=player + "'s turn", font=('comic sans', 40))
label.pack(side="top")

reset_button = Button(text="↻", font=("comic sans", 15), command=new_game)
reset_button.pack(side="top")

frame = Frame(win)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=(
            'comic sans', 40), width=5, height=2, command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# Main Game Loop ↻

win.mainloop()
