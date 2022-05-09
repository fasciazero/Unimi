'''
If you don't know that, a palindrome string is a string that can be read in the same way from left to right and from right to left. Of course not all the strings are palindrome but any of them can be transformed into a palindrome by adding a minimum (depending on the string) number of characters.

In this exercise, you have to write a function palin that given a string returns how many characters are necessary to render it palindrome and which are those characters. Please note that the correct answer minimizes the number of introduced characters and list them in (temporal) order of introduction (characters can be introduced everywhere).
'''
import functools

def ispalindrome(word):
	l=len(word)
	for x in range(int(l/2)):
		if word[x]!=word[l-1-x]:
			return False
	return True

def palindrome_substring(word):
	l=len(word)
	double_ch=[(x,y) for x in range(l) for y in range(l) if word[x]==word[y] and x!=y]
	palindrome_sub=[]
	for x in double_ch:
		w=word[x[0]:x[1]+1]
		if ispalindrome(w) and len(w)>1:
			palindrome_sub.append(w)
	if palindrome_sub!=[]:
		return functools.reduce(lambda a,b: a if len(a)>len(b) else b,palindrome_sub)
	else:	
		return False	

def palin(word):
	w=word[:]
	ilist=[]
	p=palindrome_substring(word)
	if p: i,j = word.find(p)-1, word.find(p)+len(p)
	else: i,j = int(len(w)/2)-1, int(len(w)/2)+1
	while not ispalindrome(w):
		if i<0:
			[ilist.append(x) for x in w[len(w)-1:j-1:-1]]
			w=w[len(w)-1:j-1:-1]+w
		elif j>=len(w):
			[ilist.append(x) for x in w[i::-1]]
			w=w+w[i::-1]
		else:	
			if w[i]!=w[j]:
				if w[j] not in w[:i+1]:
					ilist.append(w[j])
					w=w[:i+1]+w[j]+w[i+1:]
					j+=1
					i+=1
				else:
					ilist.append(w[i])
					w=w[:j]+w[i]+w[j:]	
		i-=1
		j+=1
	if ilist!=[]:
		return "The word '{}' needs {} insertions to become palindrome: {} -> {}".format(word,len(ilist),ilist,w)
	else:
		return "The word '{}' needs {} insertions to become palindrome.".format(word,len(ilist))


if __name__ == "__main__":
	print()
	print(palin("casa"))
	print(palin("otto"))
	print(palin("palindromo"))
	print(palin("posero"))
	print(palin("coccinella"))
	print(palin("oponopono"))
	print(palin("hanoi"))
	print(palin("susanna"))
	print()


