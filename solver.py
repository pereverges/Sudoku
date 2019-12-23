import pygame, sys

class Sudoku:
    def __init__(self, size=9):
        self.size = size
        self.cells = []
        for i in range(size):
            for j in range(size):
                self.cells.append(Cell())

    #TODO random generation of sudoku

class Cell:
    def __init__(self):
        self.val = 0

    def assignValue(self, val):
        self.val = val

    def empty(self):
        return self.val == 0

def print_rows(self):
    for i in range(self.size):
        for j in range(self.size):
            print(self.cells[i * self.size + j].val, end=' ')
            if j%3 == 2 and j < 8:
                print('|', end=' ')
        print()
        if i%3 == 2 and i < 8:
            print('- - -   - - -   - - -')

def print_cols(self):
    for i in range(self.size):
        for j in range(self.size):
            print(self.cells[i + self.size * j].position, end=' ')
        print()

def print_blocks(self):
    for r in range(3):
        for c in range(3):
            for i in range(3):
                for j in range(3):
                    print(self.cells[27 * r + i * 9 + 3 * c + j].val, end=' ')
            print()

def used_in_row(self, row, val):
    for i in range(self.size):
        if val == self.cells[row * self.size + i].val:
            return True
    return False

def used_in_col(self, col, val):
    for i in range(self.size):
        if val == self.cells[i * 9 + col].val:
            return True
    return False

def used_in_block(self, block, val):
    c = block % 3
    if block < 3:
        r = 0
    elif block < 6:
        r = 1
    else:
        r = 2
    for i in range(3):
        for j in range(3):
            if val == self.cells[27 * r + i * 9 + 3 * c + j].val:
                return True
    return False

def from_i_j_to_block(self, i, j):
    if i < 3 and j < 3:
        return 0
    elif i < 3 and j < 6:
        return 1
    elif i < 3 and j < 9:
        return 2
    elif i < 6 and j < 3:
        return 3
    elif i < 6 and j < 6:
        return 4
    elif i < 6 and j < 9:
        return 5
    elif i < 9 and j < 3:
        return 6
    elif i < 9 and j < 6:
        return 7
    elif i < 9 and j < 9:
        return 8

def valid_assignment(self, val, i, j):
    return not used_in_row(self, i, val) and not used_in_col(self, j, val) and not used_in_block(self, from_i_j_to_block(self,i,j),val)

def sudoku_complete(self):
    for i in range(9):
        for j in range(9):
            if self.cells[i * self.size + j].empty():
                return False
    return True

def find_empty(self):
    for i in range(9):
        for j in range(9):
            if self.cells[i*self.size+j].empty():
                return i, j
    return -1, -1

def solve(self):
    i, j = find_empty(self)
    if i == -1:
        print_rows(self)
        print()
        return True
    else:
        for n in range(1, 10):
            if valid_assignment(self, n, i, j):
                self.cells[i * self.size + j].assignValue(n)
                if solve(self):
                    return True
                print("Backtrack")
                self.cells[i * self.size + j].assignValue(0)
    return False


def main():
    #A = Sudoku()
    #solve(A)
    pygame.init()

    size = 320, 320
    height = width = 35
    margin = 5
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)

    while 1:
        for i in range(9):
            for j in range(9):
                pygame.draw.rect(screen,(255,255,255),[(margin+width) * j + margin, (margin+height) * i + margin, width, height] )

        screen.fill(black)
        pygame.display.flip()

if __name__ == "__main__":
    main()
