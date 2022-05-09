'''
Esercizio 2 esame del 30/01/2014
Versione ricorsiva
Claudio
'''


animals = {line[:-1].lower() for line in open('animals.txt')}

def choose(paths, minmax):
    n = minmax([len(path) for path in paths])
    return sorted([path for path in paths if len(path) == n])[0]

def genchain(path, minmax = max):
    if not type(path) is list: path = [path]
    newpath = [path + [animal] for animal in animals - set(path) if path[-1][-1] == animal[0]]
    if len(newpath) == 0: return path   
    elif len(newpath) == 1: return genchain(newpath[0], minmax)
    else: return choose([genchain(p, minmax) for p in newpath],minmax)
        

if __name__ == "__main__":
    print("longest {0} :- {1}".format('turtle', genchain('turtle')))
    print("shortest {0} :- {1}".format('turtle', genchain('turtle',min)))
    print("longest {0} :- {1}".format('aardvark', genchain('aardvark')))
    print("shortest {0} :- {1}".format('aardvark', genchain('aardvark',min)))
    print("longest {0} :- {1}".format('tiger', genchain('tiger')))
    print("shortest {0} :- {1}".format('tiger', genchain('tiger',min)))
    print("longest {0} :- {1}".format('alligator', genchain('alligator')))
    print("shortest {0} :- {1}".format('alligator', genchain('alligator',min)))
    print("longest {0} :- {1}".format('fish', genchain('fish')))
    print("shortest {0} :- {1}".format('fish', genchain('fish',min)))
    print("longest {0} :- {1}".format('scorpion', genchain('scorpion')))
    print("shortest {0} :- {1}".format('scorpion', genchain('scorpion',min)))
    print("longest {0} :- {1}".format('crocodile', genchain('crocodile')))
    print("shortest {0} :- {1}".format('crocodile', genchain('crocodile',min)))
