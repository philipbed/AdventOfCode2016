"""
solve.py
"""
ORIGIN = 0

class Bunny:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.facing = "N"

    def __str__(self):
        return "("+str(self.x)+", " +str(self.y)+")"

    def setFacing(self,direction):
        if self.facing == "N":
            if direction == "L":
                self.facing = "W"
            else:
                self.facing = "E"

        elif self.facing == "W":
            if direction == "L":
                self.facing = "S"
            else:
                self.facing = "N"

        elif self.facing == "S":
            if direction == "L":
                self.facing = "E"
            else:
                self.facing = "W"

        elif self.facing == "E":
            if direction == "L":
                self.facing = "N"
            else:
                self.facing = "S"

    def setPos(self,dist):
        if self.facing == "N":
            self.y += dist
        elif self.facing == "S":
            self.y -= dist
        elif self.facing == "E":
            self.x += dist
        elif self.facing == "W":
            self.x -= dist

    def move(self,direction,distance):
        self.setFacing(direction)
        self.setPos(distance)

    def blocksAway(self):
        return abs(self.x) + abs(self.y)

def main():
    filename = input("filename: ")
    file = open(filename)
    bunny = Bunny(ORIGIN,ORIGIN)
    for line in file:

        line = line.strip('\n')
        moves = line.split(", ")
        print(moves)
    for move in moves:
        direction = move[0]
        distance = int(move[1:])

        bunny.move(direction,distance)

    print(bunny)
    print(bunny.blocksAway())


main()
