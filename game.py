from tictactoe import TicTacToe

def main():
  game = TicTacToe()

  game.printBoard()
  player = 1

  while not game.gameOver():
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

main()