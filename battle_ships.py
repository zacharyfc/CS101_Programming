# Final Project for Codecademy CS101 Introduction to Programming
class Ship():
    board_size = 10

    def __init__(self, length):
        self.length = length
        self.found = False
    
    def place_ship(self, orientation, letter, number):
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        start_row = letters.index(letter.upper())
        start_column = number - 1
        if orientation.upper() == 'H':
            if start_column + self.length > Ship.board_size:
                print("No room for the ship here, try a position further away from the edge")
            else:
                self.coords = [(start_row, start_column + i) for i in range(self.length)]
        if orientation.upper() == 'V':
            if start_row + self.length > Ship.board_size:
                print("No room for the ship here, try a position further away from the edge")
            else:
                self.coords = [(start_row + i, start_column) for i in range(self.length)]


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
    def __init__(self, name, board, ships):
        self.name = name
        self.board = board
        self.ships = ships
    

# Setup
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
c_board = Board()

player_name = input('What is your name?')
player1 = Player(player_name, p_board, [p_carrier, p_battleship, p_cruiser, p_submarine, p_destroyer])
computer = Player('Computer', p_board, [c_carrier, c_battleship, c_cruiser, c_submarine, c_destroyer])

print(player1.board)