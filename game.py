from tictactoe import TicTacToe
from ai import AI

def checkInt(str):
  try:
    int(str)
    return True
  except ValueError:
    return False

def changePlayer(player):
  if player == 1:
    player = 2
  else:
    player = 1
  return player

def playerVsPlayer():
  size = input("What size board do you want? Enter a whole number between 3 and 7")

  while not checkInt(size):
    size = input("Please enter a whole number between 3 and 7. ")

  size = int(size)

  while (size < 3 or size > 7):
    size = input("Please enter a whole number between 3 and 7. ")
    while not checkInt(size):
      size = input("Please enter a whole number between 3 and 7. ")
    size = int(size)

  game = TicTacToe(size)

  game.printBoard()
  player = 1

  while not game.gameOver() and game.totalMoves < game.totalPossibleNumOfMoves:
    print('Player ' + str(player) + '\'s turn!')
    y = input("What row do you want to play? ")
    while not checkInt(y):
      y = input("Please enter a whole number value. ")
    y = int(y)
    x = input("What column? ")
    success = game.turn(x, y, player)
    if(success):
      player = changePlayer(player)
    
  result = game.gameOver()
  winner = result[1]
  print("Player", winner, "has won!")

def playerVsComputer():
  game = TicTacToe(3)

  charles = AI()

  game.printBoard()
  player = 1

  while not game.gameOver() and game.totalMoves < game.totalPossibleNumOfMoves:
    if player == 1:
      print('Player ' + str(player) + '\'s turn!')
      y = input("What row do you want to play? ")
      while not checkInt(y):
        y = input("Please enter a whole number value. ")
      y = int(y)
      x = input("What column? ")
      success = game.turn(x, y, player)
      if(success):
        player = changePlayer(player)
    
    if player == 2:
      aiMove = charles.makeMove(game.board)
      game.turn(aiMove[0], aiMove[1], player)
      player = changePlayer(player)
    
  result = game.gameOver()
  if result[1] == -1:
    print("It's a draw!")
  else:
    winner = result[1]
    print("Player", winner, "has won!")

def main():

  gameMode = input("Enter 1 to play against another player, 2 to play against the computer. ")

  while not checkInt(gameMode):
    gameMode = input("Please enter 1 or 2. ")

  gameMode = int(gameMode)

  while (gameMode != 1 and gameMode != 2):
    gameMode = input("Please enter 1 or 2. ")
    while not checkInt(gameMode):
      gameMode = input("Please enter 1 or 2. ")
    gameMode = int(gameMode)

  if gameMode == 1:
    playerVsPlayer()
  else:
    playerVsComputer()

main()