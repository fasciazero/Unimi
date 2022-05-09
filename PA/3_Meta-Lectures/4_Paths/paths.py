# Sia una matrice NxM, dove ogni cella è colorata di bianco o nero (0 o 1), in particolare 
# la cella (0,0) e la cella (N-1,M-1) bianche, calcolare il numero dei possibili percorsi
# dalla cella (0,0) alla (N-1,M-1), passando solo per caselle bianche e potendosi muovere
# solo in basso o a destra di una cella.

from functools import lru_cache

def read_input():
	n,m = input().split()
	return [[int(x) for x in input().split()] for _ in range(int(n))]

def percorsi(matrix):
	N,M = len(matrix),len(matrix[0])
	@lru_cache(maxsize=None)
	def wrapper(i,j):
		if i == N-1 and j == M-1: return 1
		if i == N or j == M or matrix[i][j] == 1: return 0 
		return wrapper(i+1,j) + wrapper(i,j+1)
	return wrapper(0,0)


if __name__ == '__main__':
	m = read_input()
	print('\n'.join([' '.join([str(x) for x in line]) for line in m]))
	print('Possible paths: ', percorsi(m))