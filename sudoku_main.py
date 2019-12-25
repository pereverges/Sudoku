import importlib
from Sudoku.sudoku_solver import Sudoku

importlib.import_module('sudoku_solver')

# Chose between difficulty between 1(easy), 2(normal) or 3(hard)
Sudoku().generation_and_solution(2,True)
