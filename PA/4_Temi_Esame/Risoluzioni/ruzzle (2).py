import functools

def trovaParole(griglia, xPartenza, yPartenza, lettere, posVecchie):
	tupla= tuple((xPartenza,yPartenza))
	if tupla in posVecchie:
		return lettere if len(lettere)>2 else ''
	if yPartenza not in range(0,4) or xPartenza not in range(0,4):
		return lettere if len(lettere)>2 else ''
	lettere+= griglia[yPartenza][xPartenza]
	posVecchie.add(tupla)
	
	#su, giu, sinistra, destra
	return trovaParole(griglia, xPartenza, yPartenza-1, lettere[:], posVecchie.copy())+ ' ' +\
		trovaParole(griglia, xPartenza, yPartenza+1, lettere[:], posVecchie.copy())+ ' ' +\
		trovaParole(griglia, xPartenza-1, yPartenza, lettere[:], posVecchie.copy())+ ' ' +\
		trovaParole(griglia, xPartenza+1, yPartenza, lettere[:], posVecchie.copy())

def ruzzles(griglia):
	dizionario= [word.strip() for word in open("wordlist.txt")]
	lista= [[trovaParole(griglia, j,i, "", set())] for j in range(4) for i in range(4)] #bruteforce partendo da ogni casella
	listaUnica= functools.reduce(lambda l1,l2: l1+l2, lista)
	stringaUnica= functools.reduce(lambda l1,l2: l1+' '+l2, listaUnica)	
	parole= stringaUnica.split()
	insiemeParole= set(parole)
	massimo= len(max(insiemeParole, key=lambda x: len(x)))
	insiemeParole= {parola[:i] for i in range(3, massimo) for parola in insiemeParole}
	listaParole= sorted([parola for parola in insiemeParole if parola in dizionario])
		
	return listaParole
 
if __name__=="__main__":
	print(ruzzles(["walk", "moon", "hate", "rope"]))
	print(ruzzles(["abbr", "evia", "tion", "alba"]))
	print(ruzzles(["abse", "imtn", "nded", "ssen"]))
	print(ruzzles(["reca", "rwar", "aazp", "syon"]))
	print(ruzzles(["abst", "oime", "uesl", "snsp"]))
	print(ruzzles(["essx", "ndet", "sigh", "raen"]))
	print(ruzzles(["poap", "lkjh", "aswe", "jhnh"]))
