def tuples(n): 
  if n == 1: 
    yield [0] 
    yield [1] 
  else: 
    for i in {0,1}: 
      for tmp in tuples(n-1): 
        yield [i]+tmp

#versione alternativa a quella del prof
def tuples2(n):
    for i in range(2**n):
        stringa = str(bin(i))[2:]
        lista = [int(c) for c in stringa]
        zeri = [0 for c in range(n-len(lista))]
        zeri.extend(lista)
        yield zeri
   
def pretty(f, n):
    print("\ntuples")
    for row in tuples(n): 
        print("{0} :- {1}".format(row, f(*row)))
    print("tuples2")
    for row in tuples2(n): 
        print("{0} :- {1}".format(row, f(*row)))
      
if __name__ == "__main__": 
  f0 = lambda x: 1-x 
  f1 = lambda x,y: x&y 
  f2 = lambda x,y: x|y 
  f3 = lambda x,y,z: (x&y)|(x&z) 
  f4 = lambda x1,x2,x3,x4,x5,x6,x7: f1(f0(x1),x2)|(f2(x3,f0(x4))&x5)|f3(x5,x6,x7) 
  pretty(f0, 1) 
  pretty(f1, 2) 
  pretty(f2, 2) 
  pretty(f3, 3) 
  pretty(f4, 7)
