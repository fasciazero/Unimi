'''
Drools is a production rule system whose main goal is to solve constrained systems describing problems like this.

A foursome of golfers is standing at a tee, in line from left to right; each golfers wears different colored pants

- one golfer is wearing red pants;
- the golfer to Fred's right is wearing blue pants;
- Joe is second in line;
- Bob is wearing plaid pants; and
- Tom isn't in position one or four and he isn't wearing orange pants;

In what order will the four golfers tee off and what color are each golfer's pants?

The aim of this exercise is to write a class Drools (general) that fed with the rules and elements of the problem can (via a brute force approach) find a solution to the problem. This class, among the others, will have a method eval that validates all the possible solutions against the constraint the problem imposes.

Hints Currying, itertools, recursion lambdas and closures will be your best friends.
'''

from itertools import permutations
from itertools import tee
import functools

r1= lambda a,b: True if a.pants=="red" else False
r2= lambda a,b: True if a.name=="fred" and b.pants=="blue" and a.position==b.position-1 else False 
r3= lambda a,b: True if a.position==2 and a.name=='joe' else False
r4= lambda a,b: True if a.pants=="plaid" and a.name=="bob" else False
r5= lambda a,b: True if a.name=="tom" and 1<a.position<4 and a.pants!="orange" else False
rules=[r1,r2,r3,r4,r5]

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

class Golfer:
	def __init__(self,name,pants,position):
		self.name=name
		self.pants=pants
		self.position=position
	def __str__(self):
		return "Golfer {} is in position {} and wears some {} pants".format(self.name,self.position,self.pants)

class Drools:
	def __init__(self,rules,golfers,colors,pos):
		self.rules=rules
		self.golfers=golfers
		self.colors=colors
		self.pos=pos
		self.n=len(pos)	
	def eval(self):
		d_colors=[x for x in permutations(self.colors) for y in permutations(self.pos)] 
		d_positions=[y for x in permutations(self.colors) for y in permutations(self.pos)] 
		d_names=[x for x in permutations(self.golfers) for y in zip(d_positions,d_colors)]
		comb=[[Golfer(x[0][j],x[1][j],x[2][j]) for j in range(self.n)] for x in zip(d_names,d_colors,d_positions)]
		for x in comb:
			if satisfy_rules(rules,x):
				print("\n{0}\n{1}\n{2}\n{3}\n".format(x[0],x[1],x[2],x[3]))
		return 

def satisfy_rules(flist,glist):
	glist.append(glist[0])
	partial=[functools.reduce(lambda a,b:a or b,[f(g[0],g[1]) or f(g[1],g[0]) for g in pairwise(glist)]) for f in flist]
	return functools.reduce(lambda a,b:a and b,partial)

if __name__ == "__main__":
	d=Drools(rules,['bob', 'joe', 'fred', 'tom'],['red', 'orange', 'blue', 'plaid'],list(range(1,5)))
	d.eval()
