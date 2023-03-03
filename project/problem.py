from random import randint
from typing import List

Board = List[List[int]]
Answer = List[int]

# Sudoku matrix
first_example = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

"""
Solution
[
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
"""


def cnt_mistakes(board: Board) -> int:
    mstks = 0

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                # Check rows
                if board[i].count(board[i][j]) > 1:
                    mstks += 1
                # Check columns
                column = [board[x][j] for x in range(9)]
                if column.count(board[i][j]) > 1:
                    mstks += 1
                # Check quadrant
                quadrant = []
                x = (i // 3) * 3
                y = (j // 3) * 3
                for a in range(x, x + 3):
                    for b in range(y, y + 3):
                        quadrant.append(board[a][b])
                if quadrant.count(board[i][j]) > 1:
                    mstks += 1
    return mstks


def fill_board(answers: Answer, board: Board) -> Board:
    new_board = [row.copy() for row in board]
    new_answers = answers.copy()
    for i in range(9):
        for j in range(9):
            if new_board[i][j] == 0:
                new_board[i][j] = new_answers.pop(0)
    return new_board


def fitness(answers: Answer, board: Board) -> int:
    return cnt_mistakes(fill_board(answers, board))


def print_board(board: Board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                if board[i][j] == 0:
                    print("*")
                else:
                    print(board[i][j])
            else:
                if board[i][j] == 0:
                    print("* ", end="")
                else:
                    print(str(board[i][j]) + " ", end="")
    print()


def board_spaces(board: Board) -> int:
    spaces = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                spaces += 1
    return spaces


def add_spaces(board: Board, spaces: int) -> Board:
    new_board = [row.copy() for row in board]
    i = 0
    while i < spaces:
        x = randint(0, 8)
        y = randint(0, 8)
        if new_board[x][y] != 0:
            new_board[x][y] = 0
            i = i + 1
    return new_board
