board = [["-", "-", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"]]

# skriv ut spelbrädet
def print_board():
  print(board[0][0] + "  " + board[0][1] + "  " + board[0][2])
  print(board[1][0] + "  " + board[1][1] + "  " + board[1][2])
  print(board[2][0] + "  " + board[2][1] + "  " + board[2][2])

# kolla om någon har vunnit
# TODO: returnera True om någon vunnit, annars False
def has_winner():
  return False

# kolla om det är oavgjort
# TODO: returnera True om oavgjort, annars False
def is_tie():
  return False

# kicka igång spel
def play(player_turn):

  print_board()
  
  while True:
    print("Spelare " + player_turn + ", din tur.")

    rad = input("Välj rad: ")
    kolumn = input("Välj kolumn: ")

    # TODO: kolla att rad och kolumn är 1,2 eller 3
    # TODO: kolla att vald plats ej är upptagen
    rad = int(rad) - 1
    kolumn = int(kolumn) - 1

    board[rad][kolumn] = player_turn

    print_board()

    # kolla om någon har vunnit eller blivit oavgjort
    if has_winner():
      print("Spelare " + player_turn + " vann!")
      break
    elif is_tie():
      print("Spelet blev oavgjort.")
      break

    # byt spelare
    if player_turn == "X":
      player_turn = "0"
    else:
      player_turn = "X"

play("X")

print("#################")
print("### TRE I RAD ###")
print("#################")

board = [["-", "-", "-"],
          ["-", "-", "-"],
          ["-", "-", "-"]]

# skriv ut spelbrädet
def print_board():
  print(board[0][0] + "  " + board[0][1] + "  " + board[0][2])
  print(board[1][0] + "  " + board[1][1] + "  " + board[1][2])
  print(board[2][0] + "  " + board[2][1] + "  " + board[2][2])

# kolla om någon har vunnit
def has_winner():
  # kolla rader
  if board[0][0] == board[0][1] == board[0][2] != "-":
    return True
  elif board[1][0] == board[1][1] == board[1][2] != "-":
    return True
  elif board[2][0] == board[2][1] == board[2][2] != "-":
    return True
  # kolla kolumner
  elif board[0][0] == board[1][0] == board[2][0] != "-":
    return True
  elif board[0][1] == board[1][1] == board[2][1] != "-":
    return True
  elif board[0][2] == board[1][2] == board[2][2] != "-":
    return True
  # kolla diagonaler
  elif board[0][0] == board[1][1] == board[2][2] != "-":
    return True
  elif board[0][2] == board[1][1] == board[2][0] != "-":
    return True
  else:
    return False

# kolla om det är oavgjort
def is_tie():
  for rad in board:
    for element in rad:
      if element == "-":
        return False
  return True

# kicka igång spel
def play(player_turn):

  print_board()
  
  while True:
    print("Spelare " + player_turn + ", din tur.")

    input_ok = False
    rad = ""
    kolumn = ""
    while not input_ok:
      rad = input("Välj rad: ")
      kolumn = input("Välj kolumn: ")
      if rad in ["1", "2", "3"] and kolumn in ["1", "2", "3"]:
        rad = int(rad) - 1
        kolumn = int(kolumn) - 1
        if board[rad][kolumn] == "-":
          input_ok = True
        else:
          print("Upptagen plats. Försök igen.")
      else:
        print("Försök igen.")
 

    board[rad][kolumn] = player_turn

    print_board()

    # kolla om någon har vunnit eller blivit oavgjort
    if has_winner():
      print("Spelare " + player_turn + " vann!")
      break
    elif is_tie():
      print("Spelet blev oavgjort.")
      break

    # byt spelare
    if player_turn == "X":
      player_turn = "0"
    else:
      player_turn = "X"

play("X")