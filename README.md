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

In order to generate a sudoku problem, you can not place random numbers in the grid just by looking that the numbers placed do not break the rules. What you have to do is generate a solution of a random sudoku and then delete some of the cells.

This is the way I designed my generator. To do it a bit more efficent first I assign values to the diagonal blocks and then I fill the rest.

![Sudoku Unsolved](https://github.com/pereverges/Sudoku/blob/master/SudokuUnsolved.png)


#### Solver

Basically to create a generator first you have to create the solver. My solver uses a basic backtrack algorithm that looks for all the possible solutions and when it found one stops and outputs the solution.

![Sudoku Solved](https://github.com/pereverges/Sudoku/blob/master/SudokuSolved.png)


#### Functions

We have the creator of a Sudoku **Sudoku()**, and the main function that is **generation_and_solution(diff,inter)** where **diff** has value between (1-4), specifying the difficulty of the sudoku, and the attribute **inter** that if set to True will show the resolution using an interface, otherwise will be only output in the console.

```python
#Create an empty sudoku
S = Sudoku()
#Generate a random sudoku and solve it
S.generation_and_solution(diff,inter):
```
