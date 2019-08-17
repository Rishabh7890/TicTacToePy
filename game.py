# function to display the board
def display_board(board):
  # statement to clear output everytime display_board is called
  print('\n' * 100)
  #print statements to display each position on board
  print(board[7] + '|' + board[8] + '|' + board[9])
  print(board[4] + '|' + board[5] + '|' + board[6])
  print(board[1] + '|' + board[2] + '|' + board[3])

test_board = [' ']*10
# test board
display_board(test_board)

# function that will take in player input and assign marker as 'X' or 'O'
def assign_marker():
  # create empty variable for player 1's marker
  marker = ''
  # Keep asking player to choose X or O until correct answer
  while marker != 'X' and marker != 'O':
    marker = input('Player 1 please choose X or O: ')
  # Assign player 2 the opposite marker
  player1 = marker
  # if statement for player 2's marker
  if marker == 'X':
    player2 = 'O'
  else:
    player2 = 'X'
  # return player 1 and player 2 as tuple so we can unpack later
  print(f'Player 1: {player1} Player 2: {player2}')
  return (player1, player2)

# test assign_marker function
assign_marker()