def gray_rec(n):
	if n == 1: return ['0','1']
	else:
		rec_step = gray_rec(n-1)
		return ['0'+x for x in rec_step] + ['1'+y for y in rec_step[::-1]]

def gray(n):
	for x in gray_rec(n): yield x

def memoization(f):
	def wrapper(*args):
		if not args in cache: cache[args] = f(*args)
		else: print('\nUsing cache value for {} -> {}'.format(args,cache[args]))
		return cache[args]
	cache = dict()
	return wrapper

def mgray(n):
	global gray_rec
	gray_rec = memoization(gray_rec)
	return gray(n)

if __name__ == "__main__":
	print( "GC(1) :-", end=' ')
	for gc in gray(1): print(gc, end=' ')
	print( "\nGC(2) :-", end=' ')
	for gc in gray(2): print(gc, end=' ')
	print( "\nGC(3) :-", end=' ')
	for gc in gray(3): print(gc, end=' ')
	print( "\nGC(4) :-", end=' ')
	for gc in gray(4): print(gc, end=' ')
	print()
	print( "GCm(1) :-", end=' ')
	for gc in mgray(1): print(gc, end=' ')
	print( "\nGCm(2) :-", end=' ')
	for gc in mgray(2): print(gc, end=' ')
	print( "\nGCm(3) :-", end=' ')
	for gc in mgray(3): print(gc, end=' ')
	print( "\nGCm(4) :-", end=' ')
	for gc in mgray(4): print(gc, end=' ')
	print()