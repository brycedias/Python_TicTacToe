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

import numpy as np

class AI: 

  def __init__(self):
    self.numberOfPlays = 0
    self.corners = [0, 2, 6, 8]
    self.edges = [1, 3, 5, 7]
    self.center = [4]

  def determineFirstMove(self, flatBoard):
    # Check if P1 plays corner
    self.numberOfPlays += 1
    for num in self.corners:
      if flatBoard[num] == 1:
        return 1, 1

    for num in self.edges:
      if flatBoard[num] == 1:
        return 1, 1
    
    if flatBoard[self.center[0]] == 1:
      return 0, 0

  def makeMove(self, board):
    # Decides what move to take
    flatBoard = self.flattenBoard(board)
    # xindex = -1
    # yindex = -1
    if self.numberOfPlays == 0:
      index = self.determineFirstMove(flatBoard)
      xindex = index[0]
      yindex = index[1]
    else:
      index = self.analyzeBoard(board)
      xindex = index[0]
      yindex = index[1]
      
    xindexstr = str(chr(xindex+97))
    return xindexstr, yindex
    
  def flattenBoard(self, board):
    # Takes the 2d board and returns a 1d board
    tempBoard = np.array(board)
    flat = list(tempBoard.flatten())
    return flat

  def analyzeBoard(self, board):

    crucialMove = self.canBlockOrWin(board)
    
    if crucialMove[0] == True:
      count = 0
      for element in crucialMove[1]:
        if element == 0:
          break
        if count < 2:
          count += 1
      return count, crucialMove[2]

  def canBlockOrWin(self, board):

    # check the horizontals
    rowNumber = 0
    for row in board:
      # want to check if we can win before we check if we can block
      if self.checkWinPotential(row):
        return True, row, rowNumber
      if self.checkBlockPotential(row):
        return True, row, rowNumber
      rowNumber += 1
    return False, -1, -1

    # check the verticals


    #check the diagonals
  
  def playAtIndex(self, row, rowNumber):
    # If P2 can block, it needs to block
    for element in row:
      if element == 0:
        return element, rowNumber
        # xindex, yindex

  def checkBlockPotential(self, check):
    oneCount = 0
    zeroCount = 0
    for element in check:
      if element == 1:
        oneCount += 1
      elif element == 0:
        zeroCount += 1
    if oneCount != 2:
      return False
    elif zeroCount != 1:
      return False
    return True

  def checkWinPotential(self, check):
    twoCount = 0
    zeroCount = 0
    for element in check:
      if element == 2:
        twoCount += 1
      elif element == 0:
        zeroCount += 1
    if twoCount != 2:
      return False
    elif zeroCount != 1:
      return False
    return True
    
    

  