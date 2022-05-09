from itertools import permutations

r1 = lambda s: s[0][0] != 'Tom'
r2 = lambda s: s[-1][0] != 'Tom'
r3 = lambda s: s[1][0] == 'Joe'
r4 = lambda s: any([w[0] == 'Bob' if w[1] == 'Plaid' else False for w in s])
r5 = lambda s: any([w[0] != 'Tom' if w[1] == 'Orange' else False for w in s])
r6 = lambda s: any([s[i+1][1] == 'Blue' if i <= 2 and w[0] == 'Fred' else False for w,i in zip(s,range(4))])
rules = [r1,r2,r3,r4,r5,r6]

def brute_force(names,colors):
	return [[(x,y,i) for x,y,i in zip(ns,cs,range(1,5))] for ns in permutations(names) for cs in permutations(colors)]

if __name__ == '__main__':
	names = ['Bob','Tom','Joe','Fred']
	colors = ['Red','Blue','Plaid','Orange']
	print(['\n'.join(['Golfer {} is in position {} and wears some {} pants'.format(x[0],x[2],x[1]) for x in s]) for s in brute_force(names,colors) if all([f(s) for f in rules])][0])