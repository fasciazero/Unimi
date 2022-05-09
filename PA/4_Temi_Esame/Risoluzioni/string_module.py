'''
The python module strings provides the programmer with several functions to manipulate strings; some functions are really straightforward some others are more complicated.

In this exercise you have to implement your own version of some of these functions, of course without using such a module. In particular the only admitted operations on strings are: '+', '[]', 'in', '==', '!=', and ':'; any solution that doesn't use recursion is considered wrong (doesn't matter if shorter or more efficient).

The operations to implement are:

	- reverse(s): this returns the string s reversed (max 2 points);
	- strip(s, chars): this removes all the occurrences of the characters in chars from the string s and returns the resulting string 
	  (max 3 points);
	- split(s, seps): this splits the string s on the characters listed in seps (if two elements of seps are adjacent in the string no empty token 
      is generated); the tokens are returned in a list in the order they have in the original string (max 4 points); 
	- and find(s, ch): this finds the character ch in the string s and returns the position in the string of the first occurrence of ch (positions 
      starts from 0) or -1 when the character doesn't occur in the string; note that if the function is called two or more times in a row with the 
      same arguments it returns the position of the next occurrence instead (max 5 points).

'''
def reverse(s):
	if len(s)==1: return s
	else: return s[-1]+reverse(s[:-1])

def strip(s,ch):
	if len(s)==1: return (s[0] not in ch) and s or ""
	else: return (s[0] in ch) and s[:0]+strip(s[1:],ch) or s[:1]+strip(s[1:],ch)
		
def split(s,seps):
	if len(s)==0: return []
	else:
		i=0
		while i<len(s) and s[i] not in seps: i+=1
		aux=[s[:i]]
		i+=1
		while i<len(s) and s[i] in seps: i+=1
		return aux+split(s[i:],seps)


def ricorda_stato(f):
	var={}
	def wrapper(*args):
		if args in var and var[args]!=-1:
			res=f(args[0][(var[args]+1):],args[1])
			if res!=-1:
				res=res+var[args]+1
			var[args]=res
			return res
		else:
			res=f(*args)
			var[args]=res
			return res
	return wrapper

def inner_find(s,ch,count):
	if s[0]==ch: return count
	elif len(s)==1: return -1
	else: return inner_find(s[1:],ch,count+1)

@ricorda_stato
def find(s,ch):
	return inner_find(s,ch,0)


if __name__ == "__main__":
	s0 = "The deadline is approximately midnight though it could vary."
	s1 = "She is a fascinating lady; she has an astonishing smile, an alluring voice and an entertaining sense of humor."
	s2 = "The topic is appealing nevertheless the speaker was too monotonous."
	s3 = "The topic ais appealing nevertheless the speaker was too monotonous."
	print(strip(s0, 'aeiou'))
	print(strip(s0, '.'))
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
