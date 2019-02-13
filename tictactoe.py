# Bryce Dias
# Basic CLI Tic Tac Toe

class tictactoe:
  def __init__(self):
    self.board = [
      [0, 0, 0],
      [0, 0, 0],
      [0, 5, 0]
    ]
  
  def IX(self, board, x, y):
    return board[y][x]

  def printBoard(self, board):
    for row in board:
      print(row)

game = tictactoe()
game.printBoard(game.board)