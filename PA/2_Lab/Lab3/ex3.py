'''
Polish Calculator (no spaces)
34+				-> 3+4 -> 7
315-+			-> 3+(1-5) -> 3 + -4 -> -1
34+23-*			-> (3+4)*(2-3) -> 7 * -1 -> -7
734+23+++		-> 7+((3+4)+(2+3)) -> 7 + (7 + 5) -> 7 + 12 -> 19
34*34-+635-/* 	-> (((3*4)+(3-4))*(6/(3-5))) -> (12 + -1) * (6 / -2) -> 11 * -3 -> -33
'''

from re import findall,sub,escape

class PolishCalculator:
	def __init__(self):
		self.operands = {'+' : lambda a,b : int(a) + int(b),
						 '-' : lambda a,b : int(a) - int(b),
						 '*' : lambda a,b : int(a) * int(b),
						 '/' : lambda a,b : int(a) // int(b),
						 '^' : lambda a,b : int(a) ** int(b),
						 '&' : lambda a,b : int(bool(int(a)) and bool(int(b))),
						 '|' : lambda a,b : int(bool(int(a)) or bool(int(b)))}
		self.regex = r'(?:[0-9]{1}|\([-0-9]+\)){2}['+escape(''.join(self.operands.keys()))+']{1}'

	def eval(self,operation):
		while len(findall(self.regex,operation)) != 0:
			operation = sub(self.regex,self.leaf_eval,operation)
		return sub(r'[\(\)]','',operation)

	def leaf_eval(self,match):
		leaf = match.group(0)
		v1,v2 = [sub(r'[\(\)]','',v) for v in findall(r'([0-9]{1}|\([-0-9]+\){1})',leaf)]
		return '({})'.format(self.operands[leaf[-1]](v1,v2))

if __name__ == '__main__':
	pc = PolishCalculator()
	op = ['34+','315-+','34+23-*','734+23+++','34*34-+635-/*','81-45*+93/52/*/','12/14/+232/-*','253-63/*+','23^4/25*1/2/+','01&1|11|1&&']
	for o in op:
		print('- Resolving:',o)
		print('-- Result:',pc.eval(o))
