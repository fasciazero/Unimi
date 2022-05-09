'''
The python's generators provide a easy way to lazy set constructions but the interaction with them can be improved by composing them with other generators.

In this exercise you have to implement the following generators to wrap other generators.

- even(s): this returns the even elements of the generator s at each iteration (max 2 points);
- stopAt(s, n): this generator stops to iterate when the next element of s is greater than n; it only works for sorted generators (max 2 points);
- buffer(s, n): this generator at each iteration returns a chunk of n consecutive elements of the generator s; note that last chunk can be shorter (max 5 points); and
- conditional(s, p): this generator returns those elements of the generator s whose successive element respects the predicate p (max 5 points).
'''

def even(s):
	while True:
		x=next(s)
		if x%2==0:
			yield x

def stopAt(s,n):
	x=next(s)
	while x<n:
		yield x
		x=next(s)
	raise StopIteration


class LookaheadIterator:
	def __init__(self, iterable):
		self.iterator = iter(iterable)
		self.buffer = []
	def __iter__(self):
		return self
	def __next__(self):
		if self.buffer: return self.buffer.pop()
		else: return next(self.iterator)
	def has_next(self):
		if self.buffer: return True
		try:
			self.buffer = [next(self.iterator)]
		except StopIteration: return False
		else: return True

def buffer(s,n):
	while True:
		aux=LookaheadIterator(s)
		chunk=[]
		i=1
		while True:
			if aux.has_next():
				chunk.append(next(aux))
				if i%n==0:
					yield chunk
					chunk=[]
				i+=1
			else:
				yield chunk
				raise StopIteration

def conditional(s,p):
	while True:
		aux=LookaheadIterator(s)
		a=next(aux)
		i=1
		while True:
			if aux.has_next():
				b=next(aux)
				if p(b):
					yield a
				a=b
			else:
				raise StopIteration


def fib():
	x,y = 1,1
	while True:
		yield x
		x,y = y, x+y

if __name__ == "__main__":
	even_fib = even(fib())
	for i in range(10): print(next(even_fib), end=' ')
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
