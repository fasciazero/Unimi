from functools import lru_cache

def ruzzle_(grid):
	result = set()
	@lru_cache()
	def wrapper(i,j,k,word):
		if k == len(word): return result.add(word)
		elif i >= 0 and i <= 3 and j >= 0 and j <= 3 and word[k] == grid[i][j]:
			wrapper(i+1,j,k+1,word)
			wrapper(i-1,j,k+1,word)
			wrapper(i,j+1,k+1,word)
			wrapper(i,j-1,k+1,word)
	for word in english_dict:
		for i in range(4):
			for j in range(4): wrapper(i,j,0,word)
	return sorted(list(result)),wrapper.cache_info()

if __name__ == '__main__':
	english_dict = open('dictionary.txt').read().split()
	r0 = ['walk','moon','hate','rope']
	print(ruzzle_(r0))