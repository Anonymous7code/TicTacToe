# ----- Global Variables -----

# Game Board
board = [
         '-','-','-',
         '-','-','-',
         '-','-','-',
]

# Game is on !!
game_is_on = True

# Who is winner?
winner = None

# Whose turn?
current_player = 'X'

r = False
c = False
d = False

# To play game
def play_game():
  # Display the board initially on screen
  display_board()
  
  # Loop for running the game until ended
  while game_is_on :
    # Handling the turn of player.
    handle_turn(current_player)

    #Check if game is Ended
    check_if_game_over()
    
    #Flip to other player
    flip_player()

    #Check if the game is ended
    if winner == 'X' or winner == 'O':
      print(winner + ' Won.')

    elif winner == None:
      print('The Game is a Tie.')
      

# Function called under ' play_game() ' - Display the board initially on screen
def display_board():
  print(board[0]+'|'+board[1]+'|'+board[2])
  print(board[3]+'|'+board[4]+'|'+board[5])
  print(board[6]+'|'+board[7]+'|'+board[8])


# Function called under 'game_is_on' loop inside 'play_game()'
# Initially handles the position for input
def handle_turn(player):
  global current_player
  print(current_player + "'s Turn.")
  
  position = input('Chose a position form 1 - 9 --> \t')
  valid = False
  while not valid:  
    while position not in ['1','2','3','4','5','6','7','8','9',]:
      print('Not a Valid position.')
      position = input('Enter a valid input.')
      position = int(position) - 1
      if board[position] == '-':
        valid = True
      else:
        print('You can\'t go there.Go again')


  board[position] = current_player 
  display_board()
  
  
  # Function called under 'game_is_on' loop inside 'play_game()'
# Verify the continuation of Game
def check_if_game_over():
  check_if_win()
  check_if_tie()
  game_is_on = False
  
 
# Function called under 'check_if_game_over()' -- For checking winner  
def check_if_win():
  global winner

  # Check Rows
  def check_rows():
    global game_is_on
    global r
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    if row_1 or row_2 or row_3:
      game_is_on = False

    if row_1:
      return board[0]
    elif row_2:
      return board[3]
    elif row_3:
      return board[6]
    r = True
    
    return

  # Check Cloumns 
  def check_col():
    global game_is_on
    global c
    col_1 = board[0] == board[3] == board[6] != '-'
    col_2 = board[1] == board[4] == board[7] != '-'
    col_3 = board[2] == board[5] == board[8] != '-'
    if col_1 or col_2 or col_3:
      game_is_on = False

    if col_1:
      return board[0]
    elif col_2:
      return board[1]
    elif col_3:
      return board[2]
    c = True

    return

  # Check Diagonal
  def check_diagonal():
    global game_is_on
    global d
    dia_1 = board[0] == board[4] == board[8] != '-'
    dia_2 = board[2] == board[4] == board[6] != '-'
    if dia_1 or dia_2:
      game_is_on = False

    if dia_1:
      return board[0]
    elif dia_2:
      return board[2]
  
    d = True 
    return

  

  row_winner = check_rows()
  col_winner = check_col()
  dia_winner = check_diagonal()
  # Assigning vallue to the variable winner
  if r :
    winner = row_winner
  elif c : 
    winner = col_winner
  elif d : 
    winner = dia_winner
  else:
    winner = None

    
  return

# Function called under 'check_if_game_over()' -- For checking tie 
def check_if_tie():
  global game_is_on
  if '-' not in board:
    game_is_on = False
  return
  
  
  # Function called under 'game_is_on' loop inside 'play_game()'
# Handles the change of turns
def flip_player():
  global current_player
  if current_player == 'X':
    current_player = 'O'
  elif current_player == 'O':
    current_player = 'X'
  return
