from functools import reduce
from math import gcd,log10,floor

# Support Function
def digits(x): return (x < 2 and 1) or floor(log10(x)) + 1

# Punto 1
# Sum all the natural numbers below one thousand that are multiples of 3 or 5.
def naturalsSum(x): return reduce(lambda x,y : x+y, filter(lambda x : x%3 == 0 or x%5 == 0, range(x)))
print('Esercizio 1 :', naturalsSum(1000))

# Punto 2
# Calculate the smallest number divisible by each of the numbers 1 to 20.
def samllestNumber(a,b): return reduce(lambda x,y: (x*y)//gcd(x,y), range(a,b))
print('Esercizio 2 :', samllestNumber(1,20) )

# Punto 3
# Calculate the sum of the figures of 2^1000
def digitsSum(x) : return reduce(lambda x,y : int(x)+int(y), str(x))
print('Esercizio 3 :', digitsSum(2**1000) )

# Punto 4
# Calculate the first term in the Fibonacci sequence to contain 1000 digits.
def fib(n):
	def generator():
		a,b = 0,1
		a_th = 0
		while digits(a) < n:
			a_th += 1
			a,b = b,a+b
			yield (a_th,a)
	return list(generator())[-1]
print('Esercizio 4 :',  fib(1000))