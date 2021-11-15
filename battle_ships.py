# Final Project for Codecademy CS101 Introduction to Programming
# Define custom exceptions
class OffBoard(Exception):
    pass

class OccupiedSpace(Exception):
    pass

class Ship():
    board_size = 10

    def __init__(self, length):
        self.length = length
        self.found = False
    
    def place_ship(self, board, orientation, letter, number):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        start_row = letters.index(letter.upper())
        start_column = number - 1
        if orientation.upper() == 'H':
            if start_column + self.length > Ship.board_size:
                raise OffBoard
            else:
                required_coords = [(start_row, start_column + i) for i in range(self.length)]

        if orientation.upper() == 'V':
            if start_row + self.length > Ship.board_size:
                raise OffBoard
            else:
                required_coords = [(start_row + i, start_column) for i in range(self.length)]
        
        for coord in required_coords:
            if board.map[coord[0]][coord[1]] == '|_*':
                raise OccupiedSpace
        self.coords = required_coords
        for coord in self.coords:
            board.map[coord[0]][coord[1]] = '|_*'

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
    def __init__(self):
        self.map = [['|__' for j in range(10)] for i in range(10)]
    
    def __repr__(self):
        display = '   1  2  3  4  5  6  7  8  9  10\n'
        row = 0
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        for i in self.map:
            row_string = letters[row] + ' ' + ''.join(i)
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


# Place ships on the board
print(p_board)
for ship in player1.ships:
    while True:
        while True:
            orientation = input("Would you like to place the {} horizonatally or vertically? Enter 'H' or 'V': ".format(ship.type))
            if orientation.upper() in ['H', 'V']:
                break
            else:
                print("That is not a valid orientation.")
        
        while True:
            letter = input("Where would you like to place the {}? Enter a row from A-J: ".format(ship.type)).upper()
            if letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
                break
            else:
                print("That is not a valid row. Letter must be between A and J.")

        while True:
            try:
                number = int(input("Where would you like to place the {}? Enter a column from 1-10:".format(ship.type)))
                if 1 <= number <= 10:
                    break
                else:
                    print("That is not a valid column. Number should be between 1 and 10.")
            except ValueError:
                print("That is not a valid column. Enter a number.")

        try:
            ship.place_ship(p_board, orientation, letter, number)
            break
        except OffBoard:
            print("No room for that ship here, too close to edge of board, choose another location.")
        except OccupiedSpace:
            print("There is already a ship here, choose another location.")
    print(p_board)
print(p_board)
 

