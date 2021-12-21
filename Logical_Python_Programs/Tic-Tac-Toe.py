"""
   * Author - Nitin Babar
   * Date -  20-DEC-2021
   * Time -  8:00 AM
   * Title - Tic-Tac-Toe
"""

import random
print("Tic Tac Toe Game")

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


game_still_going = True
current_player = "X"


def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])
    print()


def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_gameover()
        flip_player()


def handle_turn(player):
    global current_player
    position = 0
    valid = False
    while not valid:
        if current_player == "O":
            position = random.randint(0, 8)
        else:
            position = int(input("Enter your position from 1-9: ")) - 1
        while position not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            if current_player == "O":
                position = random.randint(0, 8)
            else:
                position = int(input("Enter your position from 1-9: ")) - 1
        if board[position] == "-":
            valid = True
        else:
            if current_player == "X":
                print("Choose differnt position")
    board[position] = player
    display_board()



def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def check_if_gameover():
    check_winner()
    check_tie()


def check_winner():
    global game_still_going
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[2] == board[4] == board[6] != "-"

    if row1 or row2 or row3:
        game_still_going = False
        print(current_player, "won")
    elif col1 or col2 or col3:
        game_still_going = False
        print(current_player, "won")
    elif dia1 or dia2:
        game_still_going = False
        print(current_player, "won")


def check_tie():
    global game_still_going
    if ("-" not in board) and game_still_going:
        game_still_going = False
        print("It's a Tie")


play_game()



