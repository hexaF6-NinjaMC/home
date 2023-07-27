"""
Assignment: A Tic-Tac-Toe Game
By: Aaron Bechtel
Based on Tic-Tac-Toe: A Solution, by Bro. Manley
"""

"""
This may only work in Windows OS because of the clear() lambda function. If you use Linux or macOS, delete all mentions of "clear"!
There are two sections to delete.
"""

# I used the solution provided, after thinking how each function worked, to get an idea of how to start. I also added 
# a few other functions, like game_winner(), and a lambda (clear()), to display end-game messages,
# clear the terminal screen for easier readability (only works in Windows OS, I believe), and comments throughout to demonstrate my understanding
# of the solution. I tried to do this from memory,on my own, and with my understanding, rather than copying code-for-code the solution.

import os                               # Delete all of this
clear = lambda:os.system("cls")         # if using
clear()                                 # non-Windows OS.

def main():
    board = create_the_board()
    show_the_board(board)
    players = ["X", "O"]
    player = ""     # Default of neither X nor O. X always goes first.
    while not (game_has_winner(board) or game_is_draw(board, player)):      # game has neither been won nor ended in a draw
        player = assign_player(player, players)     # Starts with X, then proceeds to alternate players, unless game has ended.
        player_makes_move(board, player)
        clear()                                                                             # Delete if using non-Windows OS.
        show_the_board(board)
    if game_is_draw(board, player) == (True, None):
        player = None                               # enables to show the draw message.
    
    game_winner(player, players)    # show the end-game message (O/X has won, or draw)

def create_the_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board

def show_the_board(board):
    # print a new line before and after the board for decent whitespace
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def assign_player(current_player, players):
    if current_player == "" or current_player == players[1]:
        return players[0]
    elif current_player == players[0]:
        return players[1]

def game_has_winner(board):
    # return all possible solutions for a win.
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or     # Horizontal solutions
            
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or     # Vertical solutions
            
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])       # Diagonal solutions

def game_winner(current_player, players):
    if current_player == players[0]:
        print(f"\nPlayer {current_player} has won the game! Congratulations!")  # X has won!
    elif current_player == players[1]:
        print(f"\nPlayer {current_player} has won the game! Congratulations!")  # O has won!
    else:
        print("Game has ended in a draw. Tough game, you two!")             # Draw message. current_player = None

def game_is_draw(board, current_player):

    # If not all spaces are filled, game is NOT a draw (it could still have ended with a win)...
    for space in range(9):
        if board[space] != "X" and board[space] != "O":
            return False
    
    # ...otherwise, game is a draw.
    current_player = None
    return True, current_player

def player_makes_move(board, current_player):
    space = int(input(f"Player {current_player}'s turn.\nWhat space will you take (1-9, as available)?    "))
    board[space - 1] = current_player       # replaces integer value in board list with player value (X or O)
    return board

if __name__ == "__main__":
    main()