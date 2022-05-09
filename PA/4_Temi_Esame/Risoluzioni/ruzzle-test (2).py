import unittest, itertools
from ruzzle import ruzzles

def trovaLettera(griglia, lettera):
	#trovo tutte le posizioni x,y della lettera
	posizioni= [(j,i) for j in range(0,4) for i in range(0,4) if griglia[i][j]==lettera]
	return posizioni

def isVicino(pos1,pos2):
	if pos2==tuple([pos1[0]+1,pos1[1]]) or pos2==tuple([pos1[0]-1,pos1[1]]) \
		or pos2==tuple([pos1[0],pos1[1]+1]) or pos2==tuple([pos1[0],pos1[1]-1]):
		return True	
	return False
	
def pairwise(iterable):
    #s -> (s0,s1), (s1,s2), (s2, s3), ...
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def trovaParola(griglia, parola):
	lettere= list(parola)
	posizioni= [trovaLettera(griglia, lettera) for lettera in lettere]	#trovo tutte le posizioni di ogni lettera
	possibiliParole= list(itertools.product(*posizioni))
	for parola in possibiliParole:
		vicinanze= list()
		for coppia in pairwise(parola):
			vicinanze.append(isVicino(*coppia))
		if all(vicinanze):
			return True

	return False

class TestRuzzle(unittest.TestCase):
	
	known_grids= [["walk", "moon", "hate", "rope"],["abbr", "evia", "tion", "alba"],["abse", "imtn", "nded", "ssen"],
				["reca", "rwar", "aazp", "syon"], ["abst", "oime", "uesl", "snsp"], ["essx", "ndet", "sigh", "raen"],
				["poap", "lkjh", "aswe", "jhnh"]]
	#known_res= ['alp', 'ash', 'ask', 'hew', 'hewn', 'lash', 'phew', 'plash']
	results= [ruzzles(grid) for grid in known_grids]
	
	def test_sort(self):
		for res in self.results:
			self.assertEqual(res, sorted(res))
	
	def test_english(self):
		dizionario= [word.strip() for word in open("wordlist.txt")]
		for res in self.results:
			for parola in res:
				self.assertIn(parola, dizionario)

	def test_len(self):
		for res in self.results:
			for parola in res:
				self.assertIn(len(parola), range(3, int(len(self.known_grids[0]))**2+1))
			
	def test_occurrence(self):
		for i in range(len(self.known_grids)):
			lettereunite= "".join(self.known_grids[i])
			for parola in self.results[i]:
				lettere= set(list(parola))
				for lettera in lettere:
					self.assertLessEqual(parola.count(lettera), lettereunite.count(lettera))
				
	def test_in_grid(self):
		for i in range(len(self.known_grids)):
			for parola in self.results[i]:
				self.assertTrue(trovaParola(self.known_grids[i], parola))
	
if __name__ == '__main__':
    unittest.main()