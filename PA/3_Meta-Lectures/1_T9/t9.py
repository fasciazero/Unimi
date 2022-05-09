from functools import reduce
from re import sub

t9 = {'a':'2','b':'2','c':'2','d':'3','e':'3','f':'3','g':'4','h':'4','i':'4','j':'5','k':'5','l':'5','m':'6','n':'6','o':'6','p':'7','q':'7','r':'7','s':'7','t':'8','u':'8','v':'8','w':'9','x':'9','y':'9','z':'9'}
wordToNum = lambda w: reduce(lambda a,b:a+b,[t9[x] for x in w])

def create_dictionary(dictionary,freqs=False):
	coded_dict = dict()
	with open(dictionary,'r') as f:
		for row in f:
			word = row[:-1]
			if freqs: word,freq = word.split()
			coded_word = wordToNum(word)
			if freqs:
				if coded_word not in coded_dict or freq > coded_dict[coded_word][1]: coded_dict[coded_word] = (word,freq)
			else:
				if coded_word not in coded_dict: coded_dict[coded_word] = [word]
				else: coded_dict[coded_word].append(word)
	return coded_dict

def possible_words(phrase,coded_dictionary): return [coded_dictionary[word] for word in phrase.split()]

def possible_phrase(listed_words,freqs=False):
	if freqs: return ' '.join([x[0] for x in listed_words])
	else: return reduce(lambda a,b: [x+' '+y for x in a for y in b],listed_words)

if __name__ == '__main__':
	# Exercise 1
	coded_dictionary = create_dictionary('dictionary.txt')
	with open('t9_texts.txt','r') as f:
		for phrase in f:
			parsed_phrase = sub('!([0-9\s])','',phrase)
			listed_text = possible_words(parsed_phrase,coded_dictionary)
			all_phrases = possible_phrase(listed_text)
			print( '\n'.join(all_phrases) )
	# Exercise 2
	coded_dictionary = create_dictionary('dictionary_frequency.txt',True)
	with open('t9_texts.txt','r') as f:
		for phrase in f:
			parsed_phrase = sub('!([0-9\s])','',phrase)
			listed_text = possible_words(parsed_phrase,coded_dictionary)
			all_phrases = possible_phrase(listed_text,True)
			print( all_phrases )