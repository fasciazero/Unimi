def even(gen):
	while True:
		val= next(gen)
		if val%2==0:			
			yield val

def stopAt(gen, num):
	while True:
		val= next(gen)
		if val>num:
			raise StopIteration
		yield val

def buffer(gen, num):
	lista= []
	while True:
		try:
			val= next(gen)
		except:
			yield lista
			raise StopIteration
		lista.append(val)
		if len(lista)==num:
			yield lista
			lista= []

def conditional(gen, predicato):
	val1= next(gen)
	while True:
		val2= next(gen)
		if predicato(val2):
			yield val1
		val1= val2
	
def fib():
	x,y = 1,1
	while True:
		yield x
		x,y = y, x+y

if __name__=="__main__":

	even_fib = even(fib())
	for i in range(10):	print(next(even_fib), end=' ')
	print()
	
	for i in stopAt(even(fib()), 40000000): print(i, end=' ')
	print()
	
	buffered_limited_fib = buffer(stopAt(fib(),3000), 5)
	for i in buffered_limited_fib: print(i)

	condfib = conditional(fib(),lambda x: (x%2 == 0))
	for i in range(10): print(next(condfib), end=' ')
	print()
	
	condfib2 = conditional(fib(), lambda x: (x%2 != 0))
	for i in range(15): print(next(condfib2), end=' ')
	print()