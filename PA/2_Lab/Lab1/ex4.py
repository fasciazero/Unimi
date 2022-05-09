def format_matrix(matrix):
	return '\n'.join([''.join(['{:4}'.format(v) for v in row]) for row in matrix] )+'\n------------------------------------'

# Punto 1
def identity(n):
	return [[1 if i == j else 0 for i in range(n)] for j in range(n)]

# Punto 2
def square(n):
	return [[i+j*n for i in range(1,n+1)] for j in range(n)]

# Punto 3
def transpose(matrix):
	return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

# Punto 4
def multiply(matrix1,matrix2):
	return  [[sum([x*y for x,y in zip(row1,row2)]) for row2 in transpose(matrix2)] for row1 in matrix1]

print(format_matrix(identity(5)))
print(format_matrix(square(5)))
print(format_matrix(transpose(square(5))))
print(format_matrix(multiply([[1,2,3],[4,5,6]],[[7,8],[9,10],[11,12]])))
print(format_matrix(multiply(square(2),transpose(square(2)))))