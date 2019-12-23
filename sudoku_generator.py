import random

class Sudoku:
    def __init__(self, size=9):
        self.size = size
        self.cells = []
        for i in range(size):
            for j in range(size):
                self.cells.append(Cell())

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

def solve_diagonal_blocks(self):
    for k in range(3):
        nums = range(1,10)
        for i in range(3):
            for j in range(3):
                aux = []
                length = nums.len
                found = False
                for n in range(1,length) and not found:
                    index = random.randint(1,nums.len)
                    if not used_in_block(self, from_i_j_to_block(i+k*i, j+k*j), nums[index]):
                        self.cells[(i+i*k)*9 + j + k*j].assaign_value(nums[index])
                        nums.remove(nums[index])
                        nums = nums+aux
                        found = True
                    else:
                        aux.append(nums[index])
                        nums.remove(nums[index])
    return self

def generate_other_blocks(self):
    i, j = find_empty(self)
    if i == -1:
        print('Generated')
        print_rows(self)
        print()
        return True
    else:
        for n in range(1, 10):
            if valid_assignment(self, n, i, j):
                self.cells[i * self.size + j].assignValue(n)
                tt.clear()
                self.draw_grid_tt()
                tt.getscreen().update()
                if solve(self):
                    return True
                print("Backtrack")
                self.cells[i * self.size + j].assignValue(0)
    return False

def generate_random_sudoku(self):
    new_self = solve_diagonal_blocks(self)
