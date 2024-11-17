class Grid:

    def __init__(self):
        self.grid = []

    def create_grid(self):
        for i in range(8):
            self.grid.append(' '*8)

    def display_grid(self):
        for item in self.grid:
            print(" ___ ___ ___ ___ ___ ___ ___ ___")
            print(f"|{item[0]}|{item[1]}|{item[2]}|{item[3]}|{item[4]}|{item[5]}|{item[6]}|{item[7]}|")





class Game:

    def __init__(self):
        self.grid = Grid()
        self.allowedBlocks = []
        self.score = 0

    def display_score(self):
        print("\n")
        print(f"Your score is: {self.score} ")

    def turn(self):
        self.grid.display_grid()

    def setup(self):
        self.grid.create_grid()


class Blocks:

    def __init__(self):
        ...


