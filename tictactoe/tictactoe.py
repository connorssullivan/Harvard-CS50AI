"""
Tic Tac Toe Player
"""

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
    action_list = []
    
    #Go through the board
    for row in len(board):
        for cell in len(row):

            #If cell is empty, append the cell to action_list
            if board[row][cell] == EMPTY:
                action_list.append((row, cell))
    #Return the action_list
    return action_list




def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #Check if the action is valid
    if action[0] > 2 or action[1] > 2 or action[0] < 0 or action[1] < 0 or board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid Move")
    
    #Check if the player is X or O and make the move
    else:
        new_board = board
        player = player(board)
        new_board[action[0]][action[1]] = player
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    
        
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
