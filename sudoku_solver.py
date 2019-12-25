import turtle
import random
import time

class Cell:
    def __init__(self):
        self.val = 0
        self.initial = False

    def assignValue(self, val):
        self.val = val

    def empty(self):
        return self.val == 0

    def setInitial(self):
        self.initial = True

class Sudoku:

    INTERFACE=True
    CELL_SIZE=35
    LAST_FIND_I = 0
    LAST_FIND_J = 0

    def __init__(self):
        self.cells = []
        for i in range(9):
            for j in range(9):
                self.cells.append(Cell())

    # GENERATOR AND SOLUTION DEMONSTRATION

    def generation_and_solution(self,diff,inter=False):
        prob = 0.4
        if diff == 1:
            prob = 0.55
        elif diff == 3:
            prob = 0.35
        elif diff == 4:
            prob = 0.25
        self.INTERFACE = inter
        self.generate_random_sudoku()
        self.LAST_FIND_I = 0
        self.LAST_FIND_J = 0
        print('Solution')
        self.print_rows()
        self.remove_numbers(prob)
        print('Initial Sudoku')
        self.print_rows()
        if self.INTERFACE:
            self.turtle_init()
            self.draw_grid_tt()
            time.sleep(2.5)
        self.solver()
        self.print_rows()
        if self.sudoku_check():
            print("Correct")
        else:
            print("Error")
        if self.INTERFACE:
            turtle.mainloop()

    # TURTLE INIT #

    def turtle_init(self):
        self.tt = turtle.Turtle()
        self.top_left_x = -150
        self.top_left_y = 150
        self.tt.speed(3)
        self.tt.color('#000000')
        self.tt.hideturtle()
        self.tt._tracer(0)

    # GENERATOR #

    def generate_diagonal_blocks(self):
        for k in range(3):
            possible_nums = random.sample(range(1, 10), 9)
            for i in range(3):
                for j in range(3):
                    for n in possible_nums:
                        if not self.used_in_block(self.from_i_j_to_block(i + (k * 3), j + (k * 3)), n):
                            self.cells[(i + (k * 3)) * 9 + j + k * 3].assignValue(n)
                            possible_nums.remove(n)
                            break
        return self

    # Not working (should do backtrack instead)
    def generate_not_diagonals(self):
        for k in [1,2,3,5,6,7]:
            possible_nums = random.sample(range(1, 10), 9)
            for i in range(3):
                for j in range(3):
                    for n in possible_nums:
                        print(possible_nums)
                        if self.valid_assignment(n, (int(k/3)*3)+i, ((k%3)*3)+j):
                            self.cells[((int(k/3)*3)+i)*9+(((k%3)*3)+j)].assignValue(n)
                            print((int(k/3)*3)+i, ((k%3)*3)+j)
                            possible_nums.remove(n)
                        else:
                            print('nope ' + str(n))
                            possible_nums.append(n)
                            possible_nums.remove(n)

    def generate_other_blocks(self):
        i, j = self.find_empty()
        if i == -1:
            return True
        else:
            possible_nums = random.sample(range(1, 10), 9)
            for n in possible_nums:
                if self.valid_assignment(n, i, j):
                    self.cells[i*9+j].assignValue(n)
                    if self.generate_other_blocks():
                        return True
                    self.LAST_FIND_I = i
                    self.LAST_FIND_J = j
                    self.cells[i*9+j].assignValue(0)
        return False

    def remove_numbers(self, prob):
        for i in range(9):
            for j in range(9):
                if prob < random.uniform(0, 1):
                    self.cells[i * 9 + j].assignValue(0)
                else:
                    self.cells[i*9+j].setInitial()
        return self

    def generate_random_sudoku(self):
        self.generate_diagonal_blocks()
        self.generate_other_blocks()
        return self

    # SOLVER #

    def solver(self):
        i, j = self.find_empty()
        if i == -1:
            print('Solved')
            return True
        else:
            for n in range(1, 10):
                if self.valid_assignment(n, i, j):
                    self.cells[i*9+j].assignValue(n)
                    if self.INTERFACE:
                        self.text(self.cells[i*9+j].val, self.top_left_x + j * self.CELL_SIZE + 12, self.top_left_y - i * self.CELL_SIZE - self.CELL_SIZE + 2, 18)
                        self.tt.getscreen().update()
                    if self.solver():
                        return True
                    self.LAST_FIND_I = i
                    self.LAST_FIND_J = j
                    #print("Backtrack")
                    self.cells[i*9+j].assignValue(0)
        return False

    # COMPARATORS #

    def valid_assignment(self, val, i, j):
        return not self.used_in_row(i, val) and not self.used_in_col(j, val) and not self.used_in_block(self.from_i_j_to_block(i, j),val)

    def used_in_row(self, row, val):
        for i in range(9):
            if val == self.cells[row*9+i].val:
                return True
        return False

    def used_in_col(self, col, val):
        for i in range(9):
            if val == self.cells[i*9+col].val:
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

    #Depracated
    def find_empty_initial(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i*9+j].empty():
                    return i, j
        return -1, -1

    def find_empty(self):
        for i in range(self.LAST_FIND_I,9):
            for j in range(self.LAST_FIND_J,9):
                if self.cells[i*9+j].empty():
                    self.LAST_FIND_I = i
                    self.LAST_FIND_J = j
                    return i, j
            self.LAST_FIND_J = 0
        return -1, -1

    def sudoku_complete(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i*9+j].empty():
                    return False
        return True

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

    def sudoku_check(self):
        for i in range(9):
            for j in range(9):
                if not self.check_cell(i,j,self.cells[i*9+j].val):
                    print(i,j)
                    return False
        return True

    def check_cell(self,i,j,val):
        return self.check_row(val,i,j) and self.check_col(val,j,i) and self.check_block(self.from_i_j_to_block(i,j),val,i*9+j)

    def check_row(self,val,row,j):
        for i in range(9):
            if val == self.cells[row*9+i].val and i!=j:
                return False
        return True

    def check_col(self,val,col,j):
        for i in range(9):
            if val == self.cells[i*9+col].val and i!=j:
                return False
        return True

    def check_block(self,block,val,pos):
        c = block % 3
        if block < 3:
            r = 0
        elif block < 6:
            r = 1
        else:
            r = 2
        for i in range(3):
            for j in range(3):
                if val == self.cells[27*r+i*9+3*c+j].val and pos!=(27*r+i*9+3*c+j):
                    print(str(27*r+i*9+3*c+j), pos)
                    return False
        return True

    # PRINTERS #

    def print_rows(self):
        for i in range(9):
            for j in range(9):
                print(self.cells[i*9+j].val, end=' ')
                if j % 3 == 2 and j < 8:
                    print('|', end=' ')
            print()
            if i % 3 == 2 and i < 8:
                print('- - -   - - -   - - -')
        print()

    def print_cols(self):
        for i in range(9):
            for j in range(9):
                print(self.cells[i+9*j].position, end=' ')
            print()

    def print_blocks(self):
        for r in range(3):
            for c in range(3):
                for i in range(3):
                    for j in range(3):
                        print(self.cells[27 * r + i * 9 + 3 * c + j].val, end=' ')
                print()

    # DRAWERS #

    def remove_text(self, x, y, size):
        size = size+5
        turtle.ht()
        turtle.setpos(x, y+5)
        turtle.color(turtle.bgcolor())
        turtle.begin_fill()
        turtle.fd(size-5)
        turtle.setheading(90)
        turtle.fd(size)
        turtle.setheading(180)
        turtle.fd(size)
        turtle.setheading(270)
        turtle.fd(size)
        turtle.setheading(0)
        turtle.fd(size)
        turtle.end_fill()
        turtle.ht()

    def text(self, msg, x, y, size):
        FONT = ('Arial', size, 'normal')
        turtle.penup()
        self.remove_text(x,y,size)

        self.tt.penup()
        self.tt.goto(x, y)
        self.tt.pendown()
        self.tt.write(msg, align="left", font=FONT)

    def draw_grid_tt(self):
        for i in range(0, 10):
            if i % 3 == 0:
                self.tt.pensize(3)
            else:
                self.tt.pensize(1)
            self.tt.penup()
            self.tt.goto(self.top_left_x, self.top_left_y - i * self.CELL_SIZE)
            self.tt.pendown()
            self.tt.goto(self.top_left_x + 9 * self.CELL_SIZE, self.top_left_y - i * self.CELL_SIZE)
        for j in range(0, 10):
            if j % 3 == 0:
                self.tt.pensize(3)
            else:
                self.tt.pensize(1)
            self.tt.penup()
            self.tt.goto(self.top_left_x + j * self.CELL_SIZE, self.top_left_y)
            self.tt.pendown()
            self.tt.goto(self.top_left_x + j * self.CELL_SIZE, self.top_left_y - 9 * self.CELL_SIZE)
        for i in range(0, 9):
            for j in range(0, 9):
                if not self.cells[i * 9 + j].empty():
                    if self.cells[i*9+j].initial:
                        self.tt.color('#FF0000')
                        self.text(self.cells[i * 9 + j].val, self.top_left_x + j * self.CELL_SIZE + 12,self.top_left_y - i * self.CELL_SIZE - self.CELL_SIZE + 2, 18)
                        self.tt.color('#000000')
                    else:
                        self.text(self.cells[i * 9 + j].val, self.top_left_x + j * self.CELL_SIZE + 12,self.top_left_y - i * self.CELL_SIZE - self.CELL_SIZE + 2, 18)

