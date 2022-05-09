import functools, re

linee= [linea.replace(",", '').split() for linea in open("synonyms-list.txt")]
dizionari= [{parola:linea[0] for parola in linea[2:]} for linea in linee]
def uniscidiz(d1,d2):
	d1.update(d2)
	return d1
dizionario= functools.reduce(uniscidiz, dizionari)

def myreplace(string):
	lowerS= string.lower()
	if lowerS in dizionario.keys():
		return dizionario[lowerS].upper()

	return string

def replace_synonyms(string):
	splitstring= re.split('(\W+)', string)
	splitstring= [myreplace(s) for s in splitstring]
	return functools.reduce(lambda s1,s2: s1+s2, splitstring)

if __name__=="__main__":

	s0 = "The deadline is approximately midnight though it could vary."
	s1 = "She is a fascinating lady; she has an astonishing smile, an alluring voice and an entertaining sense of humor."
	s2 = "The topic is appealing nevertheless the speaker was too monotonous."
	print(replace_synonyms(s0))
	print(replace_synonyms(s1))
	print(replace_synonyms(s2))