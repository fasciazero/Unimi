def fib():
	x,y = 1,1
	while True:
	    yield x
	    x,y = y, x+y

def even(s):
	while True:
		r = next(s)
		if r%2 == 0: yield r

def stopAt(s,n):
	r = next(s)
	while r < n:
		yield r
		r = next(s)

def buffer(s,n):
	while True:
		l = list()
		try:
			for _ in range(n):
				v = next(s)
				l.append(v)
			yield l
			l = list()
		except StopIteration:
			yield l
			break

def conditional(s,p):
	y = next(s)
	while True:
		x,y = y,next(s)
		if p(y):
			yield x


if __name__ == '__main__':
	even_fib = even(fib())
	for _ in range(10): print(next(even_fib),end=' ')
	print()
	for i in stopAt(even(fib()), 40000000): print(i, end=' ')
	print()
	buffered_limited_fib = buffer(stopAt(fib(),3000), 5)
	for i in buffered_limited_fib: print(i)
	condfib = conditional(fib(), lambda x: (x%2 == 0))
	for i in range(10): print(next(condfib), end=' ')
	print()
	condfib2 = conditional(fib(), lambda x: (x%2 != 0))
	for i in range(15): print(next(condfib2), end=' ')
	print()