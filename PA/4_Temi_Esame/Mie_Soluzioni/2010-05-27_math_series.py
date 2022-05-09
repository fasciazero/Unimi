from math import factorial,pi,e

def pi_gen():
	r = 0
	i = 0
	while True:
		r += ((i%2)*(-2)+1) * (4/(i*2+1)) # segno * frazione
		yield r
		i += 1

def e_gen():
	r = 0
	i = 0
	while True:
		r += 1/factorial(i)
		yield r
		i += 1

def booster(s):
	a = next(s)
	b = next(s)
	c = next(s)
	while True:
		yield c - ((c-b)**2/(a-2*b+c))
		a,b,c = b,c,next(s)

if __name__ == '__main__':

	print('Pi -			   ',pi)
	g1 = booster(pi_gen())
	for _ in range(10): next(g1)
	print("Pi - After 10, with boost: ",next(g1))
	p = pi_gen()
	for _ in range(9000): next(p)
	print("Pi - After 9000, no boost: ",next(p))

	print('e  -			   ',e)
	g2 = booster(e_gen())
	for _ in range(10): next(g2)
	print("e  - After 10, with boost: ",next(g2))
	e = e_gen()
	for _ in range(1000): next(e)
	print("e  - After 1000, no boost: ",next(e))