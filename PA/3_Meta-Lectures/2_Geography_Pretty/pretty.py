f0 = lambda x : 1 - x
f1 = lambda x,y : x & y
f2 = lambda x,y : x | y
f3 = lambda x,y,z : (x&y) | (x&z)

def permutations(n):
	def permutation_rec(step,n):
		return permutation_rec( [x+[y] if type(x) is list else [x,y] for x in step for y in [0,1]], n-1 ) if n > 1 else step
	return permutation_rec([[0], [1]],n)

def pretty(f,n):
	return '\n'.join(['{} -> {}'.format(par,f(*par)) for par in permutations(n)])


if __name__ == '__main__':
	print( pretty(f0,1) )
	print( pretty(f1,2) )
	print( pretty(f2,2) )
	print( pretty(f3,3) )