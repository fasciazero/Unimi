'''In this exercise you have to implement your own version of some of these functions,
of course without using such a module. In particular the only admitted operations
on strings are: '+', '[]', 'in', '==', '!=', and ':'.

The operations to implement are:
- reverse(s): 		this returns the string sreversed.
- strip(s,chars): 	this removes all the occurrences of the characters
					in charsfrom the string sand returns the resulting string.
- split(s,seps): 	this splits the string son the characters listed in seps
					(if two elements of sepsare adjacent in the string no empty token is generated).
					the tokens are returned in a list in the order they have in the original string.
- find(s,ch): 		this finds the character chin the string sand returns the position in the string of the
					first occurrence of ch(positions starts from 0) or -1when the character doesn't
					occur in the string; note that if the function is called two or more times in a
					row with the same arguments it returns the position of the next occurrence instead.'''

import re

def reverse(s):
	if s == '': return s
	return s[-1]+reverse(s[:-1])

def strip(s,chars):
	if s == '': return s
	if s[0] not in chars: return s[0]+strip(s[1:],chars)
	else: return strip(s[1:],chars)

def split(s,seps):
	def acc(i):
		if s[i:] == '': return []
		if s[i] in seps: return [s[:i]] + split(s[i+1:],seps) if s[:i] != '' else split(s[i+1:],seps)
		return acc(i+1)
	return acc(0)

def memoization(f):
	def wrapper(*args):
		if args not in cache: cache[args] = 1
		else: cache[args] += 1
		result = f(*args,cache[args])
		if result == -1 and cache[args] != 0: cache[args] = 0
		return result 
	cache = dict()	
	return wrapper

@memoization
def find(s,ch,occ=1):
	def acc(i,times):
		if s[i:] == '': return -1
		if s[i] == ch:
			if times == occ: return i
			else: times += 1
		return acc(i+1,times)
	return acc(0,1)
 
if __name__ == "__main__":
	s0 = "The deadline is approximately midnight though it could vary."
	s1 = "She is a fascinating lady; she has an astonishing smile, an alluring voice and an entertaining sense of humor."
	s2 = "The topic is appealing nevertheless the speaker was too monotonous."
	s3 = "The topic ais appealing nevertheless the speaker was too monotonous."
	print(strip(s0, 'aeiou'))
	print(reverse(s0))
	print(strip(reverse(s0), 'aeiou'))
	print(split(s1, ' ;,.'))
	print(reverse(s2))
	print("tests on find:")
	print(find(s2, 'a'))
	print(find(s2, 'a'))
	print(find(s2, 'a'))
	print(find(s3, 'a'))
	print(find(s3, 't'))
	print(find(s3, 't'))
	print(find(s3, 't'))
	print(find(s3, 't'))
	print(find(s3, 't'))
	print(find(s3, 't'))
	print(find(s3, 't'))
