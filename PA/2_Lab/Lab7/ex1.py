from functools import reduce
from time import sleep

GREEN = '\033[92m'
END = '\033[0m'

titles = []
with open('C:/Users/Oscar/Desktop/PA/2_Lab/Lab7/titles.txt') as f:
	for i,row in enumerate(f):
		titles.append((i,row.split()))

all_titles = reduce(lambda x,y: x+y,[[(i,title[:n],title[n:n+1],title[n+1:]) for n in range(len(title))] for i,title in titles])
allowed_titles = [x for x in all_titles if x[2][0].lower() != 'and' and x[2][0].lower() != 'the' and len(x[2][0]) > 2]
sorted_titles = sorted(allowed_titles,key=lambda x : (x[2],x[3]))
KWIC = '\n'.join(['{:5} {:>60} {} {}'.format(i,' '.join(left),GREEN+word[0]+END,' '.join(right)) for i,left,word,right in sorted_titles])

print(KWIC)