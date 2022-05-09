from math import sin

def fact(n):
	value = 1
	for z in range(1,n+1):
		value *= z
		yield value

def sin_taylor(x,n):
	odd_factorials = [f for i,f in enumerate(fact(n*2)) if i%2 == 0]
	return sum( [(-1+(2*(i%2))) * x**(i*2-1)/f for i,f in zip(range(1,n+1),odd_factorials)] )

if __name__ == '__main__':
	n = 1
	while sin_taylor(2,n) != sin(2):
		n += 1
	print('La serie viene sviluppata per {0} volte.'.format(n))
	print('Example with precision 7:')
	print( '{1:12}: {0}'.format(sin_taylor(2,7),'My sin') )
	print( '{1:12}: {0}'.format(sin(2),'Python sin') )