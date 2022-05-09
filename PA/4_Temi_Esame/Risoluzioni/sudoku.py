'''
Exercise 1: Sudoku's Generator.
Sudoku is a logic-based, combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, 
each row, and each of the nine 3×3 sub-grids that compose the grid contains all of the digits from 1 to 9. The puzzle setter provides 
a partially completed grid, which typically has a unique solution. There are 6,670,903,752,021,072,936,960 possible sudokus. 
By reducing the grid size to a 4×4 and considering only figures from 1 to 4 you get a simplified version of the sudoku with only 4 
sub-grids 2×2 that admits much less solutions.

The exercise consists of writing a generator function (sudoku) that at each call returns a valid (and different) sudoku 
solutions for the simplified version of the problem. Note that not all combinations are valid solutions. 
The returned combination should be a list of lists where each entry will represent a row of the grid.

Note that the solutions which calculate the combinations via a nested loops are considered wrong.
'''

import functools
import itertools
from math import sqrt

def isvalid(s):
	n=4
	tot=functools.reduce(lambda a,b:a + b,range(1,n+1))
	rows=functools.reduce(lambda a,b:a and b,[sum(elem for elem in s[x])==tot for x in range(n)])
	columns=functools.reduce(lambda a,b:a and b,[sum(s[y][x] for y in range(n))==tot for x in range(n)])
	quad=functools.reduce(lambda a,b:a and b,\
					[sum(s[x+z][y] for y in range(int(sqrt(n))) for z in range(int(sqrt(n))))==tot for x in range(0,n,int(sqrt(n)))])
	return quad and rows and columns

def sudoku():
	n=4		
	for x in itertools.permutations([x for x in itertools.permutations([elem for elem in range (1,n+1)],n)],n):
		if isvalid(x):
			yield x

if __name__=="__main__":
	S = sudoku()
	for i in range(1,101):
		print("S[{:3}] :- {}".format(i,next(S)))
