import turtle
import random
import time

class Sudoku:

    INTERFACE=True
    CELL_SIZE=35

    def __init__(self, size=9):
        self.size = size
        self.cells = []
        for i in range(size):
            for j in range(size):
                self.cells.append(Cell())

    # GENERATOR AND SOLUTION DEMONSTRATION

    def generation_and_solution(self,diff,inter=False):
        prob = 0.4
        if diff == 1:
            prob = 0.55
        elif diff == 3:
            prob = 0.35
        self.INTERFACE = inter
        self.generate_random_sudoku()
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

    def generate_other_blocks(self):
        i, j = self.find_empty()
        if i == -1:
            #print('Generated')
            return True
        else:
            possible_nums = random.sample(range(1, 10), 9)
            for n in possible_nums:
                if self.valid_assignment(n, i, j):
                    self.cells[i * self.size + j].assignValue(n)

                    if self.generate_other_blocks():
                        return True
                    self.cells[i * self.size + j].assignValue(0)
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
        self.generate_other_blocks()
        self.generate_diagonal_blocks()
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
                    self.cells[i * self.size + j].assignValue(n)
                    if self.INTERFACE:
                        size = 35
                        self.text(self.cells[i * 9 + j].val, self.top_left_x + j * size + 12, self.top_left_y - i * size - size + 2, 18)
                        self.tt.getscreen().update()

                    if self.solver():
                        return True
                    #print("Backtrack")
                    self.cells[i * self.size + j].assignValue(0)
        return False

    # COMPARATORS #

    def valid_assignment(self, val, i, j):
        return not self.used_in_row(i, val) and not self.used_in_col(j, val) and not self.used_in_block(self.from_i_j_to_block(i, j),val)

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

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i * self.size + j].empty():
                    return i, j
        return -1, -1

    def sudoku_complete(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i * self.size + j].empty():
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

    # PRINTERS #

    def print_rows(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.cells[i * self.size + j].val, end=' ')
                if j % 3 == 2 and j < 8:
                    print('|', end=' ')
            print()
            if i % 3 == 2 and i < 8:
                print('- - -   - - -   - - -')
        print()

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
        size = 35
        for i in range(0, 10):
            if i % 3 == 0:
                self.tt.pensize(3)
            else:
                self.tt.pensize(1)
            self.tt.penup()
            self.tt.goto(self.top_left_x, self.top_left_y - i * size)
            self.tt.pendown()
            self.tt.goto(self.top_left_x + 9 * size, self.top_left_y - i * size)
        for j in range(0, 10):
            if j % 3 == 0:
                self.tt.pensize(3)
            else:
                self.tt.pensize(1)
            self.tt.penup()
            self.tt.goto(self.top_left_x + j * size, self.top_left_y)
            self.tt.pendown()
            self.tt.goto(self.top_left_x + j * size, self.top_left_y - 9 * size)
        for i in range(0, 9):
            for j in range(0, 9):
                if not self.cells[i * 9 + j].empty():
                    if self.cells[i*9+j].initial:
                        self.tt.color('#FF0000')
                        self.text(self.cells[i * 9 + j].val, self.top_left_x + j * size + 12,self.top_left_y - i * size - size + 2, 18)
                        self.tt.color('#000000')
                    else:
                        self.text(self.cells[i * 9 + j].val, self.top_left_x + j * size + 12,self.top_left_y - i * size - size + 2, 18)

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

