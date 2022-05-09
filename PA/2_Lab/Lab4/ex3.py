'''
Pascal's triangle is a geometric arrangement of the binomial coefficients in a triangle.

The rows of Pascal's triangle are conventionally enumerated starting with row 0,
and the numbers in each row are usually staggered relative to the numbers in the adjacent rows.
A simple construction of the triangle proceeds in the following manner.

On row 0, write only the number 1.
Then, to construct the elements of following rows,
add the number directly above and to the left with the number directly above and to the right to find the new value.
If either the number to the right or left is not present, substitute a zero in its place.

Implement an iterator for the Pascal's triangle that:
	1. at each step will return another iterator containing all the elements in the corresponding stage sorted as in the triangle
	2. the iterator can go forward and backward
	3. (advanced) it is possible to define the working algebra for the triangle, e.g., it could be on Z7 or on the alphabet
'''

from functools import reduce
from itertools import tee,accumulate
from math import factorial

class Pascal:
	def __init__(self,row_start,up_to):
		self.up = up_to > 0
		self.up_to = abs(up_to)
		self.row_start = row_start
	def __iter__(self):
		self.row = [0]+self.row_start+[0]
		self.nrow = 1
		return self
	def __next__(self):
		curr_row = self.row
		if self.nrow > self.up_to:
			raise StopIteration
		self.row = sum_pairwise(list(self.row)) if self.up else sub_pairwise(self.row)
		self.nrow += 1
		return iter(curr_row[1:-1])

def sum_pairwise(iterable):
	'''s -> (0+s0),(s0+s1),(s1+s2),...,(sn,0)'''
	a, b = tee([0]+iterable+[0])
	next(b, None)
	return [x+y for x,y in zip(a, b)]

def sub_pairwise(iterable):
	'''s -> (t0,t1,...,tn) with t0 = s0 , t1 = s1-t0, ... , tn = sn-tn-1''' 
	return list(accumulate(iterable,lambda x,y:y-x))[:-1]

def pascal_formula(n):
	'''(x + y) ^ n'''
	return [factorial(n)//(factorial(i)*factorial(n-i)) for i in range(n+1)]

if __name__ == '__main__':
	print('Pascal\'s triangle')
	for p in Pascal([1],10): print(list(p))
	print('\nInverse Pascal\'s triangle')
	for p in Pascal([1],20): pascal20 = list(p) 
	for p in Pascal(pascal20,-7): print(list(p))
	print('\nPascal triangle formula [coefficients of (x + y) ^ n]')
	print( pascal_formula(7) )