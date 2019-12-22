class Sudoku:
    def __init__(self, size=9):
        self.size = size
        self.cells = []
        for i in range(size):
            for j in range(size):
                self.cells.append(Cell(i,j))

    def print_rows(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.cells[i*self.size+j].position, end = ' ')
            print()

    def print_cols(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.cells[i+self.size*j].position, end = ' ')
            print()

    def print_blocks(self):
        for r in range(3):
            for c in range(3):
                for i in range(3):
                    for j in range(3):
                        print(self.cells[27 * r + i * 9 + 3 * c + j].position, end = ' ')
                print()





class Cell:
    def __init__(self, x, y):
        self.position = (x,y)
        self.val = None
        self.state = None

    def assignValue(self, val):
        self.val = val

def main():
    print("Solver")
    F = Cell(0,0)
    A = Sudoku()
    print(F.val)
    print(A.cells[80].position)
    A.print_rows()
    print()
    A.print_blocks()


if __name__ == "__main__":
    main()

