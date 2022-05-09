from functools import reduce
from itertools import permutations 

class Monoid:
	def __init__(self,set_list,operand,neutral):
		self.set_list = set_list
		self.operand = operand
		self.neutral = neutral
	def neutral_check(self): return all( [self.operand(x,self.neutral) == x for x in self.set_list] )
	def closure_check(self): return all( [self.operand(x,y) in self.set_list for x,y in permutations(self.set_list,2)] )
	def associative_check(self): return all( [self.operand(self.operand(x,y),z) == self.operand(x,self.operand(y,z)) for x,y,z in permutations(self.set_list,3)] )
	def __str__(self): return 'NC: {} - CC: {} - AC: {}'.format(self.neutral_check(),self.closure_check(),self.associative_check())

class Group(Monoid):
	def __init__(self,set_list,operand,neutral):
		super().__init__(set_list,operand,neutral)
	def invertibility_check(self): return False 
	def __str__(self): return '{} - IC: {}'.format(super().__str__(),self.invertibility_check())


if __name__ == '__main__':
	# MONOID

	''' S = {True, False}
	 	add = or
		i = False '''
	print('M1 ->', Monoid([True,False],lambda a,b : a or b,False))
	
	'''	S = Zn={0,1,...,n-1}
		add = + where a+b=(a+b)%n
		i = 0 '''
	n = 10
	print('M2 ->', Monoid(range(0,n),lambda a,b : (a + b) % n,0))