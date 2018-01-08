# Globals for the bearings
# Change the values as you see fit
WEST = 1
NORTH = 2
EAST = 3
SOUTH = 4


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.bearing = bearing

    def turn_right(self):
        self.bearing += 1
        if self.bearing == 5:
            self.bearing = 1

    def turn_left(self):
        self.bearing -= 1
        if self.bearing == 0:
            self.bearing = 4

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
        self.coordinates = list(self.coordinates)
        if self.bearing == NORTH:
            self.coordinates[1] += 1
        elif self.bearing == SOUTH:
            self.coordinates[1] -= 1
        elif self.bearing == WEST:
            self.coordinates[0] -= 1
        elif self.bearing == EAST:
            self.coordinates[0] += 1
        self.coordinates = tuple(self.coordinates)
