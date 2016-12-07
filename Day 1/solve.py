"""
solve.py
"""
ORIGIN = (0,0)

class Bunny():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def moveX(self,amount):
        self.x += amount

    def moveY(self,amount):
        self.y += amount

def main():
    filename = input("filename: ")
    file = open(filename)
    for line in file:
        line = line.strip('\n')
        print(line.split(", "))

main()
