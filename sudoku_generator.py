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

def generate_diagonal_blocks(self):
    for k in range(3):
        possible_nums = random.sample(range(1, 10), 9)
        for i in range(3):
            for j in range(3):
                for n in possible_nums:
                    if not used_in_block(self, from_i_j_to_block(self,i+(k*3),j+(k*3)), n):
                        self.cells[(i+(k*3))*9 + j + k*3].assignValue(n)
                        possible_nums.remove(n)
                        break
    return self

def generate_other_blocks(self):
    i, j = find_empty(self)
    if i == -1:
        print('Generated')
        print_rows(self)
        print()
        return True, self
    else:
        possible_nums = random.sample(range(1,10),9)
        for n in possible_nums:
            if valid_assignment(self, n, i, j):
                self.cells[i * self.size + j].assignValue(n)
                b, B = generate_other_blocks(self)
                if b:
                    return True, self
                print("Backtrack")
                self.cells[i * self.size + j].assignValue(0)
    return False, self

def remove_numbers(self,prob):
    for i in range(9):
        for j in range(9):
            if prob > random.uniform(0,1):
                self.cells[i*9+j].assignValue(0)
    return self

def generate_random_sudoku(self):
    new_self = generate_diagonal_blocks(self)
    print_rows(new_self)
    print()
    b, B = generate_other_blocks(new_self)
    print_rows(B)
    print()
    return B




def main():
    A = Sudoku()
    B = generate_random_sudoku(A)
    print_rows(remove_numbers(B,0.7))

if __name__ == "__main__":
    main()
