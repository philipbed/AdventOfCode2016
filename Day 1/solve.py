"""
solve.py
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
