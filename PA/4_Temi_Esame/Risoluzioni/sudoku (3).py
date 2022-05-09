'''
The exercise consists of writing a generator function (sudoku) that at each call returns a valid
(and different) sudoku solutions for the simplified version of the problem.
Note that not all combinations are valid solutions.
The returned combination should be a list of lists where each entry will represent a row of the
grid.

Note that the solutions which calculate the combinations via a nested loops are considered wrong.

for comb in itertools.permutations(numeri, len(caratteri)):
        if zero not in comb[:num]:
            equazione=stringa.translate(dict(zip(caratteri, comb)))
            if eval(equazione): print(equazione)
'''
import itertools

        
class sudoku():
    def __init__(self):
        self.risultato=[]
        self.contatore=-1        

    def __iter__(self):
        return self
        

    def __next__(self):
        contatore=self.contatore
        self.contatore+= 1
        valori=self.risultato
        val_base=[]        
        
        if valori!=[]:
            return valori[contatore]

        else:

            val_base=list((itertools.permutations(range(1,5),4)))
            grigle_possibili=(list(itertools.permutations(val_base, 4)))

            def check(matrix):
                matriceT=[[matrix[x][n] for x in range(0,4)] for n in range(0,4)] #genero matrice che abbia su ogni riga valori di ogni colonna
                matriceQ=[[matrix[x+y][a+b] for y in [0,1] for b in [0,1]]  for a in [0, 2] for x in [0, 2]] #genero matrice che abbia su ogni riga i valori di un quadrato
                    
                
                matrice_corretta=list([matriceT[n] for n in range(0,4) if tuple(matriceT[n]) in val_base]) #controllo regola colonne matrice
                matrice_corretta2=list([matriceQ[n] for n in range(0,4) if tuple(matriceQ[n]) in val_base]) #controllo regola quadrati matrice
                if (len(matrice_corretta) ==4) and (len(matrice_corretta2) ==4):
                    return True
            
            
            self.risultato=[x for x in grigle_possibili if check(x)]

            return self.risultato[contatore]

    


if __name__ == "__main__":
    


    S = sudoku()
    for i in range(1,100):
        print("S[{:3}] :- {}".format(i,next(S)))
    
    
