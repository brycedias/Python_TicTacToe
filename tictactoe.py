# Bryce Dias
# Basic CLI Tic Tac Toe

class tictactoe:

  boardRange = (0, 3)

  def __init__(self):
    self.board = [
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]
    ]
  
  def IX(self, x, y):
    # x will be a character a, b, or c
    # y is an integer 0, 1, or 2
    # returns the value at the specified index
    if type(x) == str:
      xindex = ord(x) - 97
    return self.board[y][xindex]

  def turn(self, x, y, move):
    # x will be a character a, b, or c
    # y is an integer 0, 1, or 2
    # move is either 1 or 2 : 1 representing circle, 2 representing X
    
    xindex = ord(x) - 97
    
    self.board[y][xindex] = move


  def printBoard(self):
    print("   a  b  c")
    for count, row in enumerate(self.board):
      print(count, row)

game = tictactoe()
game.printBoard()
game.turn('a', 0, 1)
game.printBoard()
game.turn('b', 2, 2)
game.printBoard()

  
