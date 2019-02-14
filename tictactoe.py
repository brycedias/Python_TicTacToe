# Author: Bryce Dias
# Basic CLI Tic Tac Toe

class tictactoe:

  boardRange = range(0, 3)

  def __init__(self):
    # initializes an empty game board
    # '0' represents an empty space
    self.board = [
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]
    ]
  
  def printBoard(self):
    print("   a  b  c")
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
      print("Choose a, b, or c.")
      return False
    elif y not in self.boardRange:
      print(y, "is not a valid row.")
      print("Choose 0, 1, or 2.")
      return False
    elif 1 <= self.board[y][xindex] <= 2:
      print("Player ", self.board[y][xindex], "has already moved there.")
      print("Try a different spot.")
    else:
      self.updateBoard(xindex, y, player)
      return True

  def updateBoard(self, xindex, y, player):
    self.board[y][xindex] = player
    self.printBoard()

  def gameOver(self):
    #checking the rows
    for row in self.board:
      if self.checkWin(row):
        return True, row[0]

    #checking the columns
    for col in self.boardRange:
      check = []
      for row in self.board:
        check.append(row[col])
      if self.checkWin(check):
        return True, check[0]

    #checking the main diagonal
    check = []
    for index in self.boardRange:
      check.append(self.board[index][index])
    if self.checkWin(check):
      return True, check[0]

    #checking the reverse diagonal
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


  
