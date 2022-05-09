from re import sub
from itertools import permutations

class MyString:
	def __init__(self,s):
		self.s = s
	def palindrome(self):
		s = sub('[^a-z]','',self.s.lower())
		return s == s[::-1]
	def subtract(self,replace):
		return sub('['+replace+']','',self.s)
	def anagram(self,d):
		s = sub('[^a-z]','',self.s.lower())
		print(s)
		return [''.join(x) for x in set(permutations(s)) if ''.join(x) in d]

if __name__ == '__main__':
	d = []
	with open(r'C:/Users/Oscar/Desktop/PA/2_Lab/Lab4/dictionary.txt','r') as f:
		for r in f.readlines():
			d += [r[:-1]]
	s = MyString('Addres')
	print( s.palindrome() )
	print( s.subtract('dr') )
	print( s.anagram(d) )