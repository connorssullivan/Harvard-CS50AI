"""
Tic Tac Toe Player
"""

import copy
import math

#
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    xcount =0
    
    # Go through the board
    for row in board:
        for cell in row:
            if cell == X:#If cell is X, increment xcount
                xcount += 1
            elif cell == O:#If cell is O, decrement xcount
                xcount -= 1
            else: #If cell is empty, continue
                continue
    #If xcount is greater than -1, return X Turn
    if xcount > -1:
        return X
    #If xcount is less than -1, return O Turn
    else:
        return O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_list = set()
    
    #Go through the board
    for row in range(len(board)):
        for col in range(len(board[row])):

            #If cell is empty, append the cell to action_list
            if board[row][col] == EMPTY:
                action_list.add((row, col))
    #Return the action_list
    return action_list




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #Check if the action is valid
    if action not in actions(board):
        raise Exception("Invalid Move")
    
    #Check if the player is X or O and make the move
    else:
        row, col = action
        new_board = copy.deepcopy(board)
        current_player = player(board)
        new_board[row][col] = current_player
        return new_board
    
#My Function
def checkRow(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
        
    return False

#My Function
def checkCol(board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
        
    return False

#My Function
def checkDiag(board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else: 
        return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Check for X
    if checkRow(board, X) or checkCol(board, X) or checkDiag(board, X):
        return X
    #Check for O
    elif checkRow(board, O) or checkCol(board, O) or checkDiag(board, O):
        return O
    #If no winner, return None
    else:
        return EMPTY
        
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #check for winner
    if winner(board) != EMPTY:
        return True
    #Check for empty cells
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #Check for winner
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None





