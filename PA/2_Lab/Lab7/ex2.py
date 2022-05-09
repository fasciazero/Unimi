def primes(n):
	i = 1
	while i < n:
		if len([x for x in range(2,i) if i%x == 0]) == 0:
			yield i
		i += 1

def goldbach(n):
	return [(x,y) for x in primes(n) for y in primes(n) if x+y == n]

def goldbach_list(n,m):
	return {x:goldbach(x) for x in range(n,m+1,2)}

if __name__ == '__main__':
	print( goldbach_list(2,30) )