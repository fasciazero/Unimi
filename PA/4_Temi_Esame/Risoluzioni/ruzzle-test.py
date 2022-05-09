'''
Given the specification of Exercise 1 in this exercise you have to test the correctness of your
solution (i.e.., the result of the ruzzles function).

Hint, some of the properties that can be tested are:
- the resulting list of words is alphabetically sorted;
- the words in the result are really English words, i.e., they are in the given dictionary;
- no word in the result are shorter than 3 characters and longer than the maximum number of characters available
- each word in the result is really hidden in the grid (use a different algorithm than the one used in exercise 1, otherwise I will consider the exercise as wrong)
- no grid element is used twice (or as an approximation: there should be as many occurrence of an element in the word as in the grid or less.
- Please submit a complete program including the main to execute the tests.
'''

import unittest
import functools

from ruzzle import ruzzles

def TestGoodInputs(known_values,attended_result):
	class test_GoodInputs(unittest.TestCase):
		def test_goodinput(self):
			print('\n#### TEST good input ####')
			self.assertEqual(attended_result,ruzzles(known_values))
		def test_alphabeticalorder(self):
			print('\n#### TEST alphabetical order ####')
			self.assertEqual(sorted(ruzzles(known_values)),ruzzles(known_values))
	return test_GoodInputs

known1=(["walk", "moon","hate","rope"],['alone', 'ate', 'atone', 'eta', 'hat', 'hate', 'knee', 'knot', 'law',\
	'lone', 'loom', 'lot', 'moat', 'moo', 'moon', 'moot', 'nee', 'net', 'not','note', 'oat', 'oaten', 'one',\
	 'opt', 'pee', 'peen', 'rope', 'tee', 'ten','ton', 'tone', 'too', 'walk'])

known2=(["essx", "ndet","sigh","raen"],['aegis', 'aid', 'aide', 'dig', 'dis', 'ear', 'end', 'gear', 'get', 'ides',\
	'near', 'nearsighted', 'nearsightedness', 'raid', 'send', 'set', 'side','sigh', 'sight', 'sighted'])

def TestDictionary(known_values,diz):
	class test_Dictionary(unittest.TestCase):
		def test_dict(self):
			print('\n#### TEST dictionary ####')
			with open(diz,'r') as dizionario:
				for elem in ruzzles(known_values):
					self.assertEqual(True,elem+"\n" in dizionario)
	return test_Dictionary

def TestLen(i):
	class test_WordLength(unittest.TestCase):
		def test_len(self):
			print("\n#### TEST word length ####")
			for elem in ruzzles(i):
				self.assertEqual(True,3<=len(elem)<=16)
	return test_WordLength

def TestTwice(i):
	class test_Twice(unittest.TestCase):
		def test_t(self):
			print("\n#### TEST no elements in the grid are used twice ####")
			r=ruzzles(i)
			s=list(functools.reduce(lambda a,b:a+b , i))
			length=len(s)
			for word in r:
				s2=s[:]
				for elem in word:
					if elem in s2:
						s2.remove(elem)
				self.assertEqual(length-len(s2),len(word))
	return test_Twice


test1=TestGoodInputs(known1[0],known1[1])
test2=TestGoodInputs(known2[0],known2[1])
test3=TestDictionary(known1[0],"wordlist.txt")
test4=TestDictionary(known2[0],"wordlist.txt")
test5=TestLen(known1[0])
test6=TestLen(known2[0])
test7=TestTwice(known1[0])
test8=TestTwice(known2[0])

if __name__=="__main__":
	unittest.main()
	


