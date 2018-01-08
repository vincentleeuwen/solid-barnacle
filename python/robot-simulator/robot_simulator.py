import operator

# Globals for the bearings
# Change the values as you see fit
WEST = 3
NORTH = 0
EAST = 1
SOUTH = 2


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.bearing = bearing

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def simulate(self, commands):
        for command in commands:
            if command == 'R':
                self.turn_right()
            elif command == 'A':
                self.advance()
            elif command == 'L':
                self.turn_left()
            else:
                raise ValueError('Unknown command')

    def advance(self):
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.coordinates = tuple(
            map(operator.add, list(move[self.bearing]), list(self.coordinates)))
