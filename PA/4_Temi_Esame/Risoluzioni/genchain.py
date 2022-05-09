'''Vi passo una soluzione di genchain alternativa a quella del prof (che sinceramente non ho
    capito) :)

Nicolò'''

def genchain(animal, *args):
    f = max
    if len(args)>0:
        f = args[0] #la funzione Ã¨ un argomento opzionale
    animals = open('animals.txt').read().split('\n')

    #generatore che costruisce il percorso
    def build_path(an, visited):
        last_char = an[len(an)-1]#ultimo carattere

        #animali che iniziano per l'ultimo carattere
        last_char_beginning = [a for a in animals if a.startswith(last_char) and a not in visited]

        if last_char_beginning == []:
            yield [an]
        else:
            for a in last_char_beginning:
                paths = build_path(a, visited+[a])
                for path in paths:
                    yield [an]+path

    paths = list(build_path(animal, [animal]))
    #calcolo il piÃ¹ corto o il piÃ¹ lungo tra i percorsi
    min_or_max = f(paths, key = len)

    #controllo se c'Ã¨ qualche percorso della stessa lunghezza
    same_lenght = [path for path in paths if len(path)==len(min_or_max)]

    #nel caso vi siano percorsi con la stessa lunghezza, cerco quello che alfabeticamente viene prima degli altri
    if len(same_lenght)>1:
        path = min([path for path in same_lenght])
    else:
        path = min_or_max

    return path

if __name__ == '__main__':
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
