class Grid:

    def __init__(self):
        self.grid = []

    def create_grid(self):
        for i in range(8):
            self.grid.append(' '*8)

    def display_grid(self):
        count = 1
        print("    1   2   3   4   5   6   7   8 ")
        for item in self.grid:
            print("   ___ ___ ___ ___ ___ ___ ___ ___")
            print(f"{count} |{item[0]}|{item[1]}|{item[2]}|{item[3]}|{item[4]}|{item[5]}|{item[6]}|{item[7]}| {count}")
        print("    1   2   3   4   5   6   7   8 ")




class Game:

    def __init__(self):
        self.grid = Grid()
        self.allowedBlocks = {}
        self.score = 0
        self.possibleMoves = True

    def display_score(self):
        print("\n")
        print(f"Your score is: {self.score} ")
        print("\n")

    def turn(self):
        self.display_score()
        self.grid.display_grid()



    def game(self):
        self.grid.create_grid()
        while self.possibleMoves:





class Blocks:

    def __init__(self):
        ...


