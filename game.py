# import random module for later use to decide who goes first
import random
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
  # return markerers as tuple so we can later unpack
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
  # go to specified position on board and place marker there
  board[position] = marker

# test to see if place_marker works
# place_marker(test_board, '$', 8)
# display_board(test_board)

# Function that takes in board and marker and then checks to see if that marker has won the game
# this will return True if a win condition is met , False if not
def win_check(board, marker):
  # check to see different ways to win 
  # EACH ROW, EACH COLLUMN, EACH DIAGONAL, and check to see if they all share same markerer
  # remember marker is what you passed in before
  (board[1] == board[2] == board[3] == marker) or (board[4] == board[5] == board[6] == marker) or (board[7] == board[8] == board[9] == marker) or (board[1] == board[4] == board[7] == marker) or (board[2] == board[5] == board[8] == marker) or (board[3] == board[6] == board[9] == marker) or (board[1] == board[5] == board[9] == marker) or (board[3] == board[5] == board[7] == marker)

# use random module to create function to decide who goes first
def choose_first():
  # create variable that randomly gets assigned either 0 or 1
  rand_num = random.randint(0,1)
  # if statement to return P1 if 0, P2 if 1
  if rand_num == 0:
    return 'Player 1'
  else:
    return 'Player 2'

# Function that returns a boolean indicating whether a space of the board is available (empty string) or not
def space_check(board, position):
  # get board[position] and see if it equals blank space. Since already a boolean we can just return its value
  return board[position] == " "

# test space_check. Also comment in place_test to see difference 
# print(space_check(test_board,8))

# Function that checks if the board is full and returns a boolean. True if full, False otherwise
def full_board_check(board):
  # for loop that goes from range 1-10 bc board has 9 spaces
  for i in range(1,10):
    # use space check function from above in if statement to see if all spaces are taken. i as second argument will count all spaces
    if space_check(board, i):
      # return false if space check comes back true since that means not all spaces are taken
      return False
  # Otherwise return True because board is full
  return True

# Function to ask for player's next position and then uses space_check() to see if it is a free position
# If free position, return the position for later use
def player_choice(board):
  # have position = 0 to be placeholder because we know that cannot be taken
  position = 0
  # while position is not in the list of possible playable positions or space isnt free
  while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
    # ask the user to input a position and convert to int
    position = int(input('Choose a available position: (1-9)'))
  # return the new position choice for later use 
  return position

# function to ask player if they want to play again. Returns True if they do, False if not
def replay():
  choice = input('Play Again? Enter Y/N')
  
  return choice == 'Y'

## NEED TO PUT IT ALL TOGETHER NOW.........
