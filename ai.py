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

    # when dealing with the flattened 2d list
    self.corners = [0, 2, 6, 8]
    self.edges = [1, 3, 5, 7]
    self.center = [4]
    self.rows = [0, 1, 2]
    self.cols = ['a', 'b', 'c']

  def determineFirstMove(self, flatBoard):
    # Check if P1 plays corner
    self.numberOfPlays += 1

    i = flatBoard.index(1)
    if i in self.corners or i in self.edges:
      return 1, 1
    else:
      return 0, 0

  def makeMove(self, board):
    # Decides what move to take
    flatBoard = self.flattenBoard(board)
    if self.numberOfPlays == 0:
      index = self.determineFirstMove(flatBoard)
    else:
      index = self.analyzeBoard(board)
      
    xindexstr = str(chr(index[0]+97))
    print('Computer playing at :', xindexstr, index[1])
    return xindexstr, index[1]
    
  def flattenBoard(self, board):
    return list(np.array(board).flatten())

  def analyzeBoard(self, board):

    crucialMove = self.canBlockOrWin(board)
    
    if crucialMove[0] == True:
      return crucialMove[1], crucialMove[2]
    elif crucialMove[3]:
      # there is a fork
      # block the fork opportunity
      keys = list(crucialMove[3].keys())
      if keys[0] in self.rows:
        return keys[1], keys[0]
      else:
        return keys[0], keys[1]
    else:
      rowNumber = 0
      for row in board:
        if 0 in row:
          return row.index(0), rowNumber
        rowNumber += 1


  def canBlockOrWin(self, board):
    # check the horizontals
    potentialForkRows = {}
    rowNumber = 0
    for row in board:
      if self.determinePotentialMove(row):
        return True, self.getZeroIndex(row), rowNumber
      elif self.determinePotenialForkRow(row):
        temp = {rowNumber: row}
        potentialForkRows.update(temp)
        del(temp)
      rowNumber += 1

    # check the verticals
    rowNumber = 0
    for col in range(0,3):
      colNumber = 0
      check = []
      for row in board:
        check.append(row[col])
        colNumber += 1
      if self.determinePotentialMove(check):
        return True, rowNumber, self.getZeroIndex(check)
      elif self.determinePotenialForkRow(check):
        temp = {str(chr(rowNumber + 97)): check}
        potentialForkRows.update(temp)
        del(temp)
      rowNumber += 1

    #check the diagonals
    # checking the main diagonal
    rowNumber = -1
    check = []
    for index in range(0,3):
      check.append(board[index][index])
      rowNumber += 1
    if self.determinePotentialMove(check):
      return True, self.getZeroIndex(check), rowNumber

    # checking the reverse diagonal
    # rowNumber = -1
    # check = []
    # for index in range(0,3):
    #   j = len(range(0,3)) - index - 1
    #   check.append(board[index][j])
    #   rowNumber += 1
    # if self.checkWinPotential(check):
    #   checkIndex = self.getZeroIndex(check)
    #   return True, checkIndex, rowNumber
    # if self.checkBlockPotential(check):
    #   checkIndex = self.getZeroIndex(check)
    #   return True, checkIndex, rowNumber
    # rowNumber += 1
    del(check)

    return False, -1, -1, potentialForkRows # if nothing is found, return false

  def getZeroIndex(self, row):
    try:
      return row.index(0)
    except ValueError:
      return

  def determinePotentialMove(self, check):
    # Determines the spot that needs to be blocked or the spot to win
    zeroCount = check.count(0)
    oneCount = check.count(1)
    twoCount = check.count(2)

    if (twoCount == 2 or oneCount == 2) and zeroCount == 1:
      return True
    else:
      return False

  def determinePotenialForkRow(self, check):
    zeroCount = check.count(0)
    oneCount = check.count(1)
    if oneCount == 1 and zeroCount == 2:
      return True
    return False

    
    

  