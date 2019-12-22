# Sudoku

Sudoku solver using Python

#### Data Structures
To solve this problem I used a simple list to store cell objects, which have a position, value and state attributes.

That is why we need a few formulas to read the cells, in a row, col and block manner.

Row: i*9+j
Col: i+9*j
Block: 27*r + 3*c + i * 9 + j