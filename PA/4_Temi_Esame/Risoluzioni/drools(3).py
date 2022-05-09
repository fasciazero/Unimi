'''Drools is a production rule system whose main goal is to solve constrained systems describing problems like this.

A foursome of golfers is standing at a tee, in line from left to right; each golfers wears different colored pants

one golfer is wearing red pants;
the golfer to Fred's right is wearing blue pants;
Joe is second in line;
Bob is wearing plaid pants; and
Tom isn't in position one or four and he isn't wearing orange pants;
In what order will the four golfers tee off and what color are each golfer's pants?

The aim of this exercise is to write a class Drools (general) that fed with the rules and elements of the problem can (via a brute force approach) find a solution to the problem. 
This class, among the others, will have a method eval that validates all the possible solutions against the constraint the problem imposes.

Hints Currying, itertools, recursion lambdas and closures will be your best friends.'''


#Soluzione di Francesco, non è assolutamente come vuole lui (non ho usato nè currying nè ricorsione nè closures...probabilmente non sarebbe valutata sufficiente?)
#Domani riprovo a farlo più come vorrebbe lui MAI FATTO però in yet_another_one ho fatto una versione meno arzigogolosa

from itertools import *

class Drools():
    def __init__(self,rules,names,pants,pos):
        self.rules = rules
        self.names_permut = permutations(names,len(pos))
        self.pants_permut = permutations(pants,len(pos))
        

    def eval(self):
        allofthem = [[(i[0][j],i[1][j]) for j in range(len(i[0]))] for i in product(self.names_permut,self.pants_permut)]
        filtered = [line for line in allofthem if all(rule(line) for rule in self.rules)]
        for line in filtered:
            print("Found {0} solutions:".format(len(filtered)))
            for elem in sorted(line):
                print("Golfer {0} is in position {1} and wears some {2} pants".format(elem[0],line.index(elem)+1,elem[1]))


        
if __name__ == "__main__":
    r1 = lambda line: "red" in [elem[1] for elem in line]
    r2 = lambda line: any([elem[1] =="blue" and line.index(elem) == [elem[0] for elem in line].index("fred") +1 for elem in line])
    r3 = lambda line: line [1][0] == "joe"
    r4 = lambda line: any([elem[0]=="bob" and elem[1] =="plaid" for elem in line])
    r5 = lambda line: line[0][0] !="tom" and line[3][0]!="tom" and any([elem[0]=="tom" and elem[1]!="orange" for elem in line])
    rules = [r1,r2,r3,r4,r5]
    
    
    d = Drools(rules, ["bob", "joe", "fred", "tom"], ["red", "orange", "blue", "plaid"],list(range(1,5)))
    d.eval()
        
    

