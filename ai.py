# Author: Bryce Dias
# Date: 2/14/19
# Implements a stragety for the user to play against the computer
# Source: https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy

# MUST USE A BOARD SIZE OF 3x3

'''
There are only 3 possible first moves: corner, edge, center.
Player 1 can win or force a draw from any starting position.

For the first iteration, I am going to assume computer is P2
X = P1, O = P2

  If X plays corner opening move, O should take center, 
    and then an edge, forcing X to block in the next move. 
    This will stop any forks from happening. 
    When both X and O are perfect players and X chooses to start 
    by marking a corner, O takes the center, 
    and X takes the corner opposite the original. 
    In that case, O is free to choose any edge as its second move. 
    However, if X is not a perfect player and has played a corner and 
    then an edge, O should not play the opposite edge as its second move, 
    because then X is not forced to block in the next move and can fork.
  If X plays edge opening move, O should take center or one of the corners 
    adjacent to X, and then follow the above list of priorities, 
    mainly paying attention to block forks.
  If X plays center opening move, O should take corner, 
    and then follow the above list of priorities, 
    mainly paying attention to block forks.

Summarized:
  If P1 plays corner, then P2 should take center.
    after P1 plays again, P2 should take an edge.
    UNLESS P1 makes an oopsie and plays an edge or a different corner
      Then, block

    1)  1 0 2    2)  1 2 1    3) 1 1 2    4) 1 0 0    
        0 2 0        0 2 0       0 2 0       0 2 2
        0 0 1        0 0 0       0 0 0       0 1 0

  If P1 plays edge, P2 takes center or adjacent corner

    1)  0 1 0    2)  2 1 0
        0 2 0        0 0 0
        0 0 0        0 0 0

  If P1 plays center, P2 takes corner

    1)  2 0 0
        0 1 0
        0 0 0

'''

class AI: 

  numberOfPlays = 0

  def __init__(self):
    

  def makeMove(self, board):
    # Decides what move to take
    

  def analyzeBoard(self, board):
    # Determines where P1 has moved
    

  def canBlock(self, board):
    # If P2 can block, but not win, it needs to block
    

  def canWin(self, board):
    # If P2 can win, it needs to win
    

  