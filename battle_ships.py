# Final Project for Codecademy CS101 Introduction to Programming
import re
import random

# List of letters to be used for rows
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# Define functions
def find_space(ship, board):
    """Return a list of all vacant positions that a ship can take"""
    
    potential_positions = []

    # Find horizontal space
    row_num = 0
    column_num = 0
    
    for row in board.map:
        row_current_state = ''.join(row)
        space_needed = '_' * ship.length
        columns = [pos.start() for pos in re.finditer('(?={})'.format(space_needed), row_current_state)]
        for column_num in columns:
            potential_positions.append(['H', row_num, column_num])
        row_num += 1
    
    # Find vertical space
    row_num = 0
    column_num = 0

    trans_board = [list(column) for column in zip(*board.map)]
    for column in trans_board:
        column_current_state = ''.join(column)
        space_needed = '_' * ship.length       
        rows = [pos.start() for pos in re.finditer('(?={})'.format(space_needed), column_current_state)]
        
        for row_num in rows:
            potential_positions.append(['V', row_num, column_num])
        column_num += 1
        
    return potential_positions

def get_row(question_text):
    """Take row letter as user input and return index for board map"""
    while True:
        letter = input(question_text).upper()
        if letter in letters:
            row = letters.index(letter.upper())
            break
        else:
            print("That is not a valid row. Letter must be between A and J.")
    
    return row

def get_column(question_text):
    """Take column number as user input and return index for board map"""
    while True:
        try:
            number = int(input(question_text))
            if 1 <= number <= 10:
                column = number - 1
                break
            else:
                print("That is not a valid column. Number should be between 1 and 10.")
        except ValueError:
            print("That is not a valid column. Enter a number.")
    
    return column

# Define custom exceptions
class OffBoard(Exception):
    pass

class OccupiedSpace(Exception):
    pass

#Define classes
class Ship():
    board_size = 10

    def __init__(self, length):
        self.length = length
        self.found = False
    
    def place_ship(self, board, orientation, row, column):
        if orientation.upper() == 'H':
            if column + self.length > Ship.board_size:
                raise OffBoard
            else:
                required_coords = [(row, column + i) for i in range(self.length)]

        if orientation.upper() == 'V':
            if row + self.length > Ship.board_size:
                raise OffBoard
            else:
                required_coords = [(row + i, column) for i in range(self.length)]
        
        for coord in required_coords:
            if board.map[coord[0]][coord[1]] == 'X':
                raise OccupiedSpace
        self.coords = required_coords
        for coord in self.coords:
            board.map[coord[0]][coord[1]] = 'X'

class Carrier(Ship):
    def __init__(self):
        super().__init__(5)
        self.type = 'carrier'

class Battleship(Ship):
    def __init__(self):
        super().__init__(4)
        self.type = 'battleship'

class Cruiser(Ship):
    def __init__(self):
        super().__init__(3)
        self.type = 'cruiser'

class Submarine(Ship):
    def __init__(self):
        super().__init__(3)
        self.type = 'submarine'

class Destroyer(Ship):
    def __init__(self):
        super().__init__(2)
        self.type = 'destroyer'

class Board():
    display_dict = {'_':'|__', 'X':'|X_'}
    def __init__(self):
        self.map = [['_' for j in range(10)] for i in range(10)]
    
    def __repr__(self):
        display = '   1  2  3  4  5  6  7  8  9  10\n'
        row = 0
        for i in self.map:
            row_string = letters[row] + ' ' + ''.join(Board.display_dict[j] for j in i)
            display += row_string + '\n'
            row += 1
        return display


class Player():
    def __init__(self, name, board, guesses, ships):
        self.name = name
        self.board = board
        self.guesses = guesses
        self.ships = ships
    
#########
# Setup #
#########

# Create ships and boards
p_carrier = Carrier()
p_battleship = Battleship()
p_cruiser = Cruiser()
p_submarine = Submarine()
p_destroyer = Destroyer()
c_carrier = Carrier()
c_battleship = Battleship()
c_cruiser = Cruiser()
c_submarine = Submarine()
c_destroyer = Destroyer()

p_board = Board()
p_guesses = Board()
c_board = Board()
c_guesses = Board()

# Create player objects
player_name = input('What is your name? ')
player1 = Player(player_name, p_board, p_guesses, [p_carrier, p_battleship, p_cruiser, p_submarine, p_destroyer])

computer = Player('Computer', p_board, c_guesses, [c_carrier, c_battleship, c_cruiser, c_submarine, c_destroyer])

# Take user input to place player ships on the board
print(p_board)
for ship in player1.ships:
    while True:
        while True:
            orientation = input("Would you like to place the {} horizonatally or vertically? Enter 'H' or 'V': ".format(ship.type))
            if orientation.upper() in ['H', 'V']:
                break
            else:
                print("That is not a valid orientation.")

        row = get_row("Where would you like to place the {}? Enter a row from A-J: ".format(ship.type))
        column = get_column("Where would you like to place the {}? Enter a column from 1-10:".format(ship.type))
        
        try:
            ship.place_ship(p_board, orientation, row, column)
            break
        except OffBoard:
            print("No room for that ship here, too close to edge of board, choose another location.")
        except OccupiedSpace:
            print("There is already a ship here, choose another location.")
    print(p_board)
print(p_board)

# Place computer ships on the board
for ship in computer.ships:
    empty_spaces = find_space(ship, c_board)
    chosen_space = random.choice(empty_spaces)
    print(chosen_space)
    ship.place_ship(c_board, chosen_space[0], chosen_space[1], chosen_space[2])

