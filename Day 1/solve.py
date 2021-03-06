"""
solve.py

Problem:
You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny
Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North.
Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees,
then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination.
Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?
"""

from bunny import Bunny

ORIGIN = 0

if __name__ == "__main__":
    filename = input("filename: ")
    file = open(filename)
    bunny = Bunny(ORIGIN,ORIGIN)

    moves = file.read().strip("\n").split(", ")

    for move in moves:
        direction = move[0]
        distance = int(move[1:])

        if bunny.move(direction,distance):
            break

    print(bunny)
    print(bunny.numBlocksAway())
