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

# test_board = [' ']*10
# test board
# display_board(test_board)

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

# use tuple unpacking so we can print each choice indv later on if we need to
# player1_marker, player2_marker = assign_marker()
# test player 1 marker which should be unpacked due to above statement
# print(player1_marker)

# function which takes in board as object, mark, and desired position on board and assigns it to the board
def place_marker(board, mark, position):
  # go to specified position on board and place mark there
  board[position] = mark

# test to see if place_marker works
# place_marker(test_board, '$', 8)
# display_board(test_board)

# Function that takes in board and mark and then checks to see if that mark has won the game
# this will return True if a win condition is met , False if not
def win_check(board, mark):
  # check to see different ways to win 
  # EACH ROW, EACH COLLUMN, EACH DIAGONAL, and check to see if they all share same mark
  # remember mark is what you passed in before
  return (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark)

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
    position = int(input('Choose an available position: (1-9)'))
  # return the new position choice for later use 
  return position

# function to ask player if they want to play again. Returns True if they do, False if not
def replay():
  choice = input('Play Again? Enter Y/N')
  
  return choice == 'Y'

# NEED TO PUT IT ALL TOGETHER NOW...
print("Welcome to Tic-Tac-Toe in Python!")
# While loop to keep running the game
while True:
  # Play the game
  
  ## Set everything up (board, whose first, choose markers)
  game_board = [' ']*10
  # using tuple unpacking assignt p1 and p2 respective markers using assign_marker()
  player1_marker,player2_marker = assign_marker()
  # using choose_first() set turn
  turn = choose_first()
  # since choose_first returns either player 1 or 2, we can print out to show user
  print(turn + ' will go first.')
  # now that game is set up as user if they are ready to play
  play_game = input('Ready to play? Y/N')

  if play_game == 'Y':
    game_on = True
  else:
    game_on = False
  ### Gameplay
  # run game while game_on is True
  while game_on:
    if turn == 'Player 1': 
      ### Player 1 turn
      # first thing to do is display board
      display_board(game_board)
      # choose a position
      position = player_choice(game_board)
      # place marker on position
      place_marker(game_board, player1_marker, position)
      # check if they won
      if win_check(game_board, player1_marker):
        display_board(game_board)
        print('Player 1 has won!!')
        game_on = False
      # check if there is a tie
      else:
        if full_board_check(game_board):
          display_board(game_board)
          print('TIE game!')
          game_on = False
      # no tie and no win? Then next players turn
        else:
          turn = 'Player 2'
    else:
      ### Player 2 turn. Same logic as player 1
      display_board(game_board)
      # choose a position
      position = player_choice(game_board)
      # place marker on position
      place_marker(game_board, player2_marker, position)
      # check if they won
      if win_check(game_board, player2_marker):
        display_board(game_board)
        print('Player 2 has won!!')
        game_on = False
      # check if there is a tie
      else:
        if full_board_check(game_board):
          display_board(game_board)
          print('TIE game!')
          game_on = False
      # no tie and no win? Then next players turn
        else:
          turn = 'Player 1'

  ### break out of while True loop 
  if not replay():
    break
  # Break out of while loop on replay()
