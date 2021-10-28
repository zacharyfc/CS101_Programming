# Final Project for Codecademy CS101 Introduction to Programming
class Ship():
    def __init__(self, length):
        self.length = length
    
    def place_ship(orientation, row, column):
        self.orientation = orientation
        self.row = row
        self.column = column


class Board():
    def __init__(self):
        self.map = [['|__' for j in range(10)] for i in range(10)]
    
    def __repr__(self):
        display = '    A  B  C  D  E  F  G  H  I  J \n'
        row = 1
        for i in self.map:
            row_string = str(row).rjust(2) + ' ' + ''.join(i)
            display += row_string + '\n'
            row += 1
        return display


class Player():
    def __init__(self, name, board, ships):
        self.name = name
        self.board = board
        self.ships = ships
    

