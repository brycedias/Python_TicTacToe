# Author: Bryce Dias
# Date: 2/13/19
# Basic CLI Tic Tac Toe

class TicTacToe:

  def __init__(self, boardSize):
    # variable to dictate size of board
    self.boardSize = boardSize
    self.boardRange = range(0, self.boardSize)
    self.totalMoves = 0
    self.totalPossibleNumOfMoves = boardSize * boardSize

    # initializes an empty game board
    # '0' represents an empty space
    # dynamically initializes square board of size boardSize
    self.board = []
    for i in self.boardRange:
      row = [0] * self.boardSize
      self.board.append(row)

  
  def printBoard(self):
    # print("   a  b  c ...")
    colIDs = '   '
    for i in self.boardRange:
      tempChar = str(chr(i+97))
      colIDs += (tempChar + '  ')

    print(colIDs)
    for count, row in enumerate(self.board):
      print(count, row)

  def IX(self, x, y):
    # x will be a character a, b, or c (column)
    # y is an integer 0, 1, or 2 (row)
    # returns the value at the specified index
    if type(x) == str:
      xindex = ord(x) - 97
    return self.board[y][xindex]

  def turn(self, x, y, player):
    # x will be a character a, b, or c (column)
    # y is an integer 0, 1, or 2 (row)
    # move is either 1 or 2 : 1 representing circle, 2 representing X
    
    xindex = ord(x) - 97
    if xindex not in self.boardRange:
      print(x, "is not a valid column.")
      print("Choose one of the labeled columns. (a, b, c ...)")
      return False
    elif y not in self.boardRange:
      print(y, "is not a valid row.")
      print("Choose one of the labeled rows. (1, 2, 3 ...)")
      return False
    elif 1 <= self.board[y][xindex] <= 2:
      print("Player ", self.board[y][xindex], "has already moved there.")
      print("Try a different spot.")
    else:
      self.updateBoard(xindex, y, player)
      return True

  def updateBoard(self, xindex, y, player):
    self.totalMoves += 1
    self.board[y][xindex] = player
    self.printBoard()

  def gameOver(self):

    if self.totalMoves == self.totalPossibleNumOfMoves:
      return True, -1
    # checking the rows
    for row in self.board:
      if self.checkWin(row):
        return True, row[0]

    # checking the columns
    for col in self.boardRange:
      check = []
      for row in self.board:
        check.append(row[col])
      if self.checkWin(check):
        return True, check[0]

    # checking the main diagonal
    check = []
    for index in self.boardRange:
      check.append(self.board[index][index])
    if self.checkWin(check):
      return True, check[0]

    # checking the reverse diagonal
    check = []
    for index in self.boardRange:
      j = len(self.boardRange) - index - 1
      check.append(self.board[index][j])
    if self.checkWin(check):
      return True, check[0]
    del(check)

  def checkWin(self, check):
    if check.count(check[0]) == len(check) and check[0] != 0:
      return True


  
