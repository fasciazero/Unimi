from functools import lru_cache

def read_input():
	n = input()
	return tuple(sorted([[int(x) for x in input().split()] for _ in range(int(n))]))

def next_bigger(k,start,dishes): 
	try: return dishes.index(next(x for x in dishes[start:] if x[0] >= k))
	except: return len(dishes)

def find_best_food(dishes):
	@lru_cache(maxsize=None)
	def wrapper_rec(start):
		if(len(dishes) > start + 1):
			cho = dishes[start][1] + wrapper_rec(next_bigger(dishes[start][0]+dishes[start][2],start,dishes))
			nocho = wrapper_rec(start+1)
			return max(cho,nocho)
		else: return 0
	return wrapper_rec(0)

if __name__ == '__main__':
	dishes = read_input()
	print( find_best_food(dishes))