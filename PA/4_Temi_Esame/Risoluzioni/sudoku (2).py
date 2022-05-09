import random

def random_permutation(iterable, r=None):
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))

def newrow():
	return random_permutation(range(1,5), 4)
	
def checkcols(matrice):
	m= [[matrice[j][i] for j in range(len(matrice))] for i in range(4)]
	for l in m:
		if len(set(l)) != len(l):
			return False
	return True
	
def getsquares(matrice, offset, x,y):
	if offset==2:
		return [[[matrice[y+i][x+j] for j in range(2)] for i in range(2)]]
	
	offset= int(offset/2)
	return getsquares(matrice, offset,x,y)+getsquares(matrice, offset,x+offset,y)+ \
			getsquares(matrice, offset,x,y+offset)+getsquares(matrice, offset, x+offset,y+offset)

def checksquares(matrice):
	m= getsquares(matrice, 4, 0,0)
	for s in m:
		if len(set(s[0]).union(set(s[1])))!=4:
			return False
	return True
	
def genmat(mat):
	if len(mat)==4:
		return mat
		
	newl= newrow()
	mat.append(newl)
	while not checkcols(mat):
		mat.pop()
		newl= newrow()
		mat.append(newl)
	
	return genmat(mat)

def sudoku():
	s= set()
	while True:
		m= tuple(genmat(list()))
		while not checksquares(m) or m in s:
			m= tuple(genmat(list()))
		s.add(m)
		yield m

if __name__=="__main__":

	S = sudoku()
	for i in range(1,101):
		print("S[{:3}] :- {}".format(i,next(S)))