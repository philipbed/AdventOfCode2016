class Bunny:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.facing = "N"
        home = (self.x,self.y)
        self.locations = [home]

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
        visited = False

        if self.facing == "N":
            for _ in range(0,dist):
                self.y+=1
                visited,pos = self.containsPosition(dist)
                if visited:
                    return visited
                self.locations.append(pos)

        elif self.facing == "S":
            for _ in range(0,dist):
                self.y-=1
                visited,pos = self.containsPosition(dist)
                if visited:
                    return visited
                self.locations.append(pos)

        elif self.facing == "E":
            for _ in range(0,dist):
                self.x+=1
                visited,pos = self.containsPosition(dist)
                if visited:
                    return visited
                self.locations.append(pos)

        elif self.facing == "W":
            for _ in range(0,dist):
                self.x-=1
                visited,pos = self.containsPosition(dist)
                if visited:
                    return visited
                self.locations.append(pos)
        return visited

    def move(self,direction,distance):
        self.setFacing(direction)
        return self.setPos(distance)

    def numBlocksAway(self):
        return abs(self.x) + abs(self.y)

    def containsPosition( self, dist ):
        pos = (self.x,self.y)
        if pos in self.locations:
            return True,pos
        else:
            return False,pos
