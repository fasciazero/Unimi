def reverse(s):
	if len(s)==1:
		return s
	return s[-1]+reverse(s[:-1])

def strip(s, chars):
	if len(s)==1:
		return '' if s[0] in chars else s
			
	return strip(s[1:], chars) if s[0] in chars else s[0]+strip(s[1:], chars)
	
def auxSplit(s, seps, index, aux, lista):
	if index==len(s):
		return lista
		
	if s[index] in seps:
		if len(s[aux:index])>0:
			lista+= [s[aux:index]]
		aux= index+1
		
	return auxSplit(s, seps, index+1, aux, lista)
	
def split(s, seps):
	return auxSplit(s, seps, 0, 0, [])

find_state= ['','',0]

def auxFind(s, ch, index):
	if index==len(s):
		return -1
	if s[index]==ch:
		return index
		
	return auxFind(s, ch, index+1)
	
def find(s, ch):

	if find_state[0]!=s:
		find_state[0]= s[:]
		find_state[1]= ch
		find_state[2]= 0
	if find_state[1]!=ch:
		find_state[1]= ch
		find_state[2]= 0

	index= auxFind(s, ch, find_state[2]+1)
	find_state[2]= index
	return index
	
if __name__=="__main__":

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