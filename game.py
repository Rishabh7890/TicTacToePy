# function to display the board
def display_board(board):
  # statement to clear output everytime display_board is called so we dont see history of boards
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
  
  '''
  OUTPUT = (Player 1 marker, Player 2 marker)

  '''

  # create empty variable for player 1's marker
  marker = ''
  # Keep asking player 1 to choose X or O until correct answer
  while marker != 'X' and marker != 'O':
    marker = input('Player 1 please choose X or O: ')
  # if statement for player 2's marker
  # return markers as tuple so we can later unpack
  if marker == 'X':
    print(('X', 'O'))
    return ('X', 'O')
  else:
    print(('O', 'X'))
    return ('O', 'X')

# test assign_marker function
# use tuple unpacking so we can print each choice indv later on if we need to
player1_marker, player2_marker = assign_marker()
# test player 1 marker which should be unpacked due to above statement
# print(player1_marker)

# function which takes in board as object, marker, and desired position on board and assigns it to the board
def place_marker(board, marker, position):

  board[position] = marker

# test to see if place_marker works
# place_marker(test_board, '$', 8)
# display_board(test_board)

# Function that takes in board and mark and then checks to see if that mark has won the game
# this will return True if a win condition is met , False if not
def win_check(board, mark):
  # check to see different ways to win 

  # EACH ROW, EACH COLLUMN, EACH DIAGONAL, and check to see if they all share same marker
  # remember mark is what you passed in before
  (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark)

