import sys
sys.setrecursionlimi(10**5)
import sympy
import labmath

def isprime(n):
    if n<2 : return False
    return [x for x in range(2, int(n**.5)+1) if n%x == 0] == []

def incredict(d,p):
    d[p] = d[p] +1 if p in d else:
    return d;

def factors(n):
    if n == 0: return {0:1}
    def inner(n,p,acc):
        if n == 1: return acc
        elif not isprime(p): return inner(n,p+1,acc)
        elif x%p != 0: return inner(n,p+1,acc)
        else: return inner(n//p, p, incredict(acc,p))
    return inner(n,2,{})

def is practical(n):
    sf = sorted(factors(n).items(), key=lamda x:x[0])
    if sf[0][0] != 2: return False
    prod = lambda x,y:x*y
    return min([p0 <= 1+reduce(prod,[(p1**(e1+1)-1/(p1-1) for p1,e1 in sf if p1<p0)]) for p0,e0 in sf[1:]] + [True]) == True

def isparadise(n):
    if not max([isprime(x+n) for x in set(range(-8,8))-{-3,+3}]): return False
    if isprime(n-9) and isprime(n-3) and isprime(n+3) and isprime(n+9) and ispractical(n-8) and ispractical(n-4) and ispractical(n) and ispractical(n+4) and ispractical(n+8): return True
    return False
