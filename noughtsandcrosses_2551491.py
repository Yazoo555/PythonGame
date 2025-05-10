"""Noughts and Crosses game module"""

import random
import os.path
import json

random.seed()


def draw_board(board):
    """Draws the current state of the board"""
    print()
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print()


def welcome(board):
    """Displays welcome message and the board"""
    print("Welcome to Noughts and Crosses!")
    print("You are X, the computer is O. First to get three in a row wins.")
    draw_board(board)


def initialise_board(board):
    """Initializes the board with empty spaces"""
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board


def get_player_move(board):
    """Prompts the player for a move and returns (row, col)"""
    while True:
        move = input("Enter a number between 1 and 9: ")
        if move.isdigit() and 1 <= int(move) <= 9:
            index = int(move) - 1
            row, col = divmod(index, 3)
            if board[row][col] == ' ':
                board[row][col] = 'X'
                return row, col
            print("That cell is already taken.")
        else:
            print("Invalid input. Please enter a valid number.")


def choose_computer_move(board):
    """Computes the computer's move and returns (row, col)"""
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                if check_for_win(board, 'O'):
                    return i, j
                board[i][j] = ' '

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                if check_for_win(board, 'X'):
                    board[i][j] = 'O'
                    return i, j
                board[i][j] = ' '

    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    row, col = random.choice(empty)
    board[row][col] = 'O'
    return row, col


def check_for_win(board, mark):
    """Checks if the given mark has won"""
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)):
            return True
        if all(board[j][i] == mark for j in range(3)):
            return True
    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False


def check_for_draw(board):
    """Checks if the board is full and no winner"""
    for row in board:
        if ' ' in row:
            return False
    return True


def play_game(board):
    """Main loop to play the game and return score"""
    initialise_board(board)
    draw_board(board)
    while True:
        get_player_move(board)
        draw_board(board)
        if check_for_win(board, 'X'):
            print("You win!")
            return 1
        if check_for_draw(board):
            print("It's a draw.")
            return 0
        print("Computer's move:")
        choose_computer_move(board)
        draw_board(board)
        if check_for_win(board, 'O'):
            print("Computer wins!")
            return -1
        if check_for_draw(board):
            print("It's a draw.")
            return 0


def menu():
    """Displays menu and returns valid user choice"""
    print("\nMenu:")
    print("1 - Play the game")
    print("2 - Save score")
    print("3 - Load and display leaderboard")
    print("q - Quit")
    choice = input("Enter your choice: ").strip().lower()
    while choice not in ['1', '2', '3', 'q']:
        choice = input("Invalid choice. Enter 1, 2, 3 or q: ").strip().lower()
    return choice


def load_scores():
    """Loads leaderboard scores from file and returns as a dictionary"""
    leaders = {}
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r", encoding="utf-8") as file:
            leaders = json.load(file)
    return leaders


def save_score(score):
    """Saves the score to leaderboard file after prompting for name"""
    name = input("Enter your name: ").strip()
    leaders = load_scores()
    if name in leaders:
        leaders[name] += score
    else:
        leaders[name] = score
    with open("leaderboard.txt", "w", encoding="utf-8") as file:
        json.dump(leaders, file)


def display_leaderboard(leaders):
    """Displays the leaderboard"""
    if not leaders:
        print("No scores found.")
        return
    print("\nLeaderboard:")
    for name, score in sorted(leaders.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {score}")
