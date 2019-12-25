# Sudoku

Sudoku generator and solver using Python

#### Data Structures
To solve this problem I used a simple list to store cell objects, which have a value, and inital (if its the a cell of initial problem (already solved)) attributes.

That is why we need a few formulas to read the cells, in a row, col and block manner.
```python
Row: i*9+j
Col: i+9*j
Block: 27*r+3*c+i*9+j
```
Where **i** and **j** are the rows and cols of the whole sudoku, and **r** and **c** are the row and col of each block (from 1 to 3)

#### Generator


