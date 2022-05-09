import sys
import re

def replace_punctuations(text,replace):
	return re.sub(replace,' ',text)

def freqs(text,n,l):
	freq = [(w,text.lower().split().count(w)) for w in set(text.split())]
	return sorted([(w,f) for w,f in freq if f > n and len(w) > l],key=lambda x:x[1],reverse=True)

if __name__ == '__main__':

	if len(sys.argv) < 4: print('-- USAGE : python3 ex2.py <nome_file> <freq_at_least> <len_at_least>')
	else: 
		file = sys.argv[1]
		at_least = int(sys.argv[2])
		len_single = int(sys.argv[3]) 
		replace = '[.,;:!?\n\'\"<>]'

		with open(file,encoding='utf-8') as f:
			text = ' '.join(f)
			print(freqs(replace_punctuations(text,replace),at_least,len_single))
