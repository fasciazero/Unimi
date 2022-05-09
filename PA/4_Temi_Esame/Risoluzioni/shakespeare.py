'''
English (as well as any other natural language) could be really complicated; for example many terms (synonyms) can refer to the same
concept but some of them can be more complicated than others and their use can render more complicate to understand the text.
This should be evident when you try to read some English literature as Shakespeare.

This exercise consists in writing a function replace_synonyms that takes a string (the text to simplify) and returns a copy
of the same text with the complicated terms substituted with their synonym more diffuse. To be more evident the new term should be capitalized in the result.
The table of the synonym can be downloaded from here (each line contains the term to be used separated by a colon : from a comma-separated list
of terms it will substitute.'''

import string

def make_dict(f):
	diz={}
	with open(f,"r") as s_list:
		for line in s_list:
			value,keys="".join(line.split()).split(':')
			keys=[word for word in keys.split(',')] 
			for x in keys:
				diz[x]=value
	s_list.close()
	return diz
			
def replace_synonyms(s):
	diz=make_dict('synonyms-list.txt')
	words="".join([ch for ch in s if ch not in string.punctuation]).split()
	res=s[:]
	for word in words:
		if word.lower() in diz:
			res=res.replace(word, diz[word.lower()].upper())
	return res

if __name__ == "__main__":
	s0 = "The deadline is approximately midnight though it could vary."
	s1 = "She is a fascinating lady; she has an astonishing smile, an alluring voice and an entertaining sense of humor."
	s2 = "The topic is appealing nevertheless the speaker was too monotonous."
	print(replace_synonyms(s0))
	print(replace_synonyms(s1))
	print(replace_synonyms(s2))
