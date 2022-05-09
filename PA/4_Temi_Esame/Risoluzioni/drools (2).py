import itertools

class Golfer:
	def __init__(self, name, color, position):
		self.color= color
		self.position= position
		self.name= name
	def __str__(self):
		return "Golfer {} is in position {} and wears {} pants".format(self.name, self.position, self.color)

def haValoriDiversi(combinazione):
	zippato= list(zip(*combinazione))
	sonodiversi= [len(set(gruppo))==len(gruppo) for gruppo in zippato]
	return all(sonodiversi)	
		
class Drools:
	def __init__(self, rules,*args):
		self.classe= Golfer
		self.rules= rules
		self.quanti= len(args[0])
		self.args= args
	def eval(self):
		abbinamentivalori= list(itertools.product(*self.args))
		gruppi= [list(g) for n,g in itertools.groupby(abbinamentivalori, key= lambda a: a[0])]
		combinazioni= list(itertools.product(*gruppi))
		combinazionivalide= [c for c in combinazioni if haValoriDiversi(c)]
		combinazioniOggetti= [[self.classe(*valori) for valori in c] for c in combinazionivalide]
		for c in combinazioniOggetti:
			matches= [r(c) for r in self.rules]
			if all(matches):
				for golfista in c:
					print(golfista)
				print()

if __name__=="__main__":
	
	def rule1(golfers):
		colori= [g.color for g in golfers]
		return True if colori.count('red')==1 else False
	def rule2(golfers):
		fredlist= list(filter(lambda g: g.name=='fred', golfers))
		if len(fredlist)==0:
			return False
		fred= fredlist[0]
		destrafred= list(filter(lambda g: g.position==fred.position+1, golfers))
		return False if (len(destrafred)!=1 or destrafred[0].color != 'blue') else True
	def rule3(golfers):
		for g in golfers:
			if g.name=='joe':
				return True if g.position==2 else False
	def rule4(golfers):
		for g in golfers:
			if g.name=='bob':
				return True if g.color=='plaid' else False
	def rule5(golfers):
		for g in golfers:
			if g.name=='tom':
				return True if ((g.position in range(2,4)) and g.color!='orange') else False
	
	rules= list()
	rules.append(rule1)
	rules.append(rule2)
	rules.append(rule3)
	rules.append(rule4)
	rules.append(rule5)

	d = Drools(rules, ['bob', 'joe', 'fred', 'tom'], ['red', 'orange', 'blue', 'plaid'],list(range(1,5)))
	#d = Drools(rules, ['bob', 'joe'], ['red', 'orange'],list(range(1,3)))
	d.eval()