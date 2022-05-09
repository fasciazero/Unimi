# Punto 1

def fromK(x) : return x
def fromC(x) : return x - 273.15
def fromF(x) : return x * 9 / 5 - 459.67
def fromR(x) : return x * 9 / 5
def fromD(x) : return (373.15 - x) * 3 / 2
def fromN(x) : return (x - 273.15) * 33 / 100 
def fromRe(x) : return (x - 273.15) * 4 / 5
def fromRo(x) : return (x - 273.15) * 21 / 40 + 7.5

def toK(x) : return x
def toC(x) : return x + 273.15
def toF(x) : return (x + 459.67) * 5 / 9
def toR(x) : return x * 5 / 9
def toD(x) : return 373.15 - x * 2 / 3
def toN(x) : return x * 100 / 33 + 273.15 
def toRe(x) : return x * 5 / 4 + 273.15
def toRo(x) : return (x - 7.5) * 40 / 21 + 273.15

toK = {'K': toK, 'C' : toC, 'F': toF, 'R': toR, 'D': toD, 'N': toN, 'Re': toRe, 'Ro': toRo}
fromK = {'K': fromK, 'C' : fromC, 'F': fromF, 'R': fromR, 'D': fromD, 'N': fromN, 'Re': fromRe, 'Ro': fromRo}

def fromKtoAll(scale,value):
	kelvin_value = fromK[scale](value)
	return [f(kelvin_value) for f in toK.values()]

def table(value):
	values_dict = {scale : fromKtoAll(scale,value) for scale in toK.keys()}
	return values_dict

def format_table(table):
	return '  '+''.join(['{:>8}'.format(scale) for scale in sorted(toK.keys())]) \
	+ '\n' + \
	'\n'.join(['{:3}'.format(scale)+''.join(['{:8.1f}'.format(v) for v in values]) for scale,values in table.items()])

print(format_table(table(42))) 

# Punto 2
def toAll(scale,value):
	values = sorted([(value,scale) for value,scale in zip(fromKtoAll(scale,value),toK.keys())])
	sorted(values)
	return ', '.join(['{1:.1f} {0}'.format(scale,value) for value,scale in values])

print('42 K corresponds to ' + toAll('K',42))