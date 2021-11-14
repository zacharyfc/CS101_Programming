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
                raise OffBoard("Too close to edge of board")
            else:
                required_coords = [(start_row, start_column + i) for i in range(self.length)]

        if orientation.upper() == 'V':
            if start_row + self.length > Ship.board_size:
                raise OffBoard("Too close to edge of board")
            else:
                required_coords = [(start_row + i, start_column) for i in range(self.length)]
        
        for coord in required_coords:
            if board.map[coord[0]][coord[1]] == '|_*':
                raise OccupiedSpace
        self.coords = required_coords
        for coord in self.coords:
            board.map[coord[0]][coord[1]] = '|_*'

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
p_carrier = Ship(5)
p_battleship = Ship(4)
p_cruiser = Ship(3)
p_submarine = Ship(3)
p_destroyer = Ship(2)
c_carrier = Ship(5)
c_battleship = Ship(4)
c_cruiser = Ship(3)
c_submarine = Ship(3)
c_destroyer = Ship(2)

p_board = Board()
p_guesses = Board()
c_board = Board()
c_guesses = Board()

# Create player objects
player_name = input('What is your name? ')
player1 = Player(player_name, p_board, p_guesses, [p_carrier, p_battleship, p_cruiser, p_submarine, p_destroyer])

computer = Player('Computer', p_board, c_guesses, [c_carrier, c_battleship, c_cruiser, c_submarine, c_destroyer])


# Place ships on the board
ship_types = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']

print(player1.board)
p_carrier.place_ship(p_board,'H', 'G', 1)
print(player1.board)
p_battleship.place_ship(p_board,'V', 'D', 5)