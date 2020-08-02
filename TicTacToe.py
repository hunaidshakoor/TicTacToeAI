"""

Tic Tac Toe Functions
"""

import copy
from math import inf

X = 'X'
O = 'O'

def initial_state():
    #Starting State of Board
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]

def player(board):

    #Returns player who has next turn
    new_board = initial_state()
    Xs = 0
    Os = 0
    if board == new_board:
        return X
    else:
        for row in board:
            for value in row:
                if value == X:
                    Xs += 1
                elif value == O:
                    Os += 1

        if Xs > Os:
            return O
        else:
            return X

def actions(board):

    #returns set of all possible actions (i, j) available on the board
    moves = []
    for row_i, row in enumerate(board):
        for col_i, value in enumerate(row):
            if not value:
                moves.append((row_i, col_i))
    return moves


def result(board, action):
    #Returns new board based on action
    row_i = action[0]
    col_i = action[1]
    new_board = copy.deepcopy(board)
    p = player(new_board)

    if new_board[row_i][col_i] == None:
        new_board[row_i][col_i] = p
    else:
        raise Exception("Not Valid Spot")
    return new_board


def winner(board):
    #Returns winner if there is one
    win_row_X = [X, X, X]
    win_row_O = [O, O, O]
    win_p = None

    # check if winner in row
    for row in board:
        if row == win_row_X or row == win_row_O:
            win_p = row[0]

    #check for column winner
    for i in range(0,3):
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i]:
            win_p = board[0][i]

    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0]:
        win_p = board[0][0]

    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2]:
        win_p = board[0][2]

    return win_p

def terminal(board):

    #Returns true if game is over, returns false otherwise
    empty_space = any(None in row for row in board)
    win = winner(board)

    # if theres an empty space and no winner game continues
    if (empty_space is True) and (win is None):
        return False
    #if theres no winner game is over or spaces left game is over
    else:
        return True


def utility(board):
    #only called if terminal exists
    #Returns 1 if X wins, -1 if O wins
    #Returns 0 if tie
    win_p = winner(board)
    if win_p == X:
        return 1
    elif win_p == O:
        return -1
    else: # tie game
        return 0


def minimax(board):
    "returns optimal action"
    # X would be the maximizing player
    # O is the minimizing player
    # check if game is over
    if terminal(board):
        return None

    max_val = -inf
    min_val = inf
    p = player(board) # get player

    return _minimax(board, max_val, min_val, p)[1]

def _minimax(board, max_val, min_val, p):
    move = None

    if terminal(board):
        return [utility(board), None]

    if p == X:
        val = -inf
        for action in actions(board):
            test = _minimax(result(board, action), max_val, min_val, O)[0]
            max_val = max(max_val, test)
            if test > val:
                val = test
                move = action
            if min_val <= max_val:
                break
        return [val, move]
    else:
        val = inf
        for action in actions(board):
            test = _minimax(result(board, action), max_val, min_val, X)[0]
            min_val = min(min_val, test)
            if test < val:
                val = test
                move = action
            if min_val <= max_val:
                break
        return [val, move]




