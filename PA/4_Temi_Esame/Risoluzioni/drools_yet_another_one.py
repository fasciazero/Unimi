#By Fra#
'''Drools is a production rule system whose main goal is to solve constrained systems describing
problems like this.
A foursome of golfers is standing at a tee, in line from left to right; each golfers wears different
colored pants
one golfer is wearing red pants;
the golfer to Fred's right is wearing blue pants;
Joe is second in line;
Bob is wearing plaid pants; and
Tom isn't in position one or four and he isn't wearing orange pants;
In what order will the four golfers tee off and what color are each golfer's pants?
The aim of this exercise is to write a class Drools (general) that fed with the rules and elements of
the problem can (via a brute force approach) find a solution to the problem. This class, among the
others, will have a method eval that validates all the possible solutions against the constraint the
problem imposes.
Hints Currying, itertools, recursion lambdas and closures will be your best friends.'''

from itertools import *

rules = [
    lambda tee: any([x[0] == "red" for x in tee]), #one golfer is wearing red pants
    lambda tee : any([x[1] == tee[1][1] +1 and x[0] =="blue" for x in tee]), #the golfer to fred's right has blue pants
    lambda tee : tee[2][1]==2, #joe is second in line
    lambda tee : tee[0][0] == "plaid", #bob is wearing plaid pants
    lambda tee: tee[3][1] != 1 and tee[3][1] != 4 and tee[3][0] != "orange" #Tom isn't in position one or four and he isn't wearing orange pants;
        ]

class Drools:
    def __init__(self,rules,namelist,colors,positions):
        self.rules = rules
        self.namelist = sorted(namelist)
        self.colors = colors
        self.positions = positions
        
    def eval(self):
        self.color_perm = permutations(self.colors) 
        self.pos_perm = permutations(self.positions)
        all_poss = (list(zip(i[0],i[1])) for i in product(self.color_perm,self.pos_perm))
        for tee in all_poss:
            if all([rule(tee) for rule in rules]):
                for i in range(len(self.namelist)):
                    print("Golfer {} is in position {} and wears some {} pants".format(self.namelist[i],tee[i][1],tee[i][0]))
                
                
if __name__ == "__main__":
    d = Drools(rules,["bob", "joe", "fred", "tom"],["red", "orange", "blue", "plaid"],list(range(1,5)))
    d.eval()
