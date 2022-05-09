'''
Ruzzle is a grid (4×4) based game where each element of the grid is a letter and the aim of the game consists in determining all the possible English words out of all possible paths in the grid (where a path is a sequence of adjacent grid elements).

The exercise consists of writing a function ruzzles that calculates all the English words hidden in a given grid with the following simplifications/constraints:

- the minimum length for a word is 3 characters;
- an entry is considered adjacent to another if it is immediately at left, at right, above or below it (no diagonals are considered); note that a word can also be hidden in the grid in its reversed form (i.e., it can be read from right to left);
- no entry can be considered twice in the same word;
- the words should be checked against this dictionary;
- the list of resulting words must be alphabetically sorted;
- The input is a list of 4-character strings where each string represents a row in the grid and their position in the list mimic the position in the grid.
'''
import copy

def find_word(i1,i2,word,scheme):
	scheme[i1][i2]='*'
	if len(word)==1:
		return True
	else:
		for x in [elem for elem in [(0,-1),(0,1),(-1,0),(1,0)] if -1<i1+elem[0]<4 and -1<i2+elem[1]<4]:
			if word[1]==scheme[i1+x[0]][i2+x[1]] and find_word(i1+x[0],i2+x[1],word[1:],scheme):
				return True
	return False		

def thereis(word,schema):
	chars=[elem[x] for elem in schema for x in range(4)]
	sch=[[elem for elem in x] for x in schema]
	if not 2<len(word)<17 or [ch for ch in word if (ch in chars)and(chars.remove(ch)==None)]!=list(word):
		return False
	index=[(x,y) for x in range(4) for y in range(4) if sch[x][y]==word[0]]
	for x in index:
		#print("tentativo con indice {}".format(x))
		if find_word(x[0],x[1],word,copy.deepcopy(sch)):
			return True
	return False

def ruzzles(schema):
    first_chars={elem[x] for elem in schema for x in range(4)}
    res=[]
    with open('wordlist.txt','r') as diz:
        for line in diz:
            if line[0] in first_chars and thereis(line[:-1],schema):
                res.append(line[:-1])
    return sorted(res)


if __name__ == "__main__":
	print(ruzzles(["walk", "moon","hate","rope"]))
	print(ruzzles(["abbr", "evia","tion","alba"]))
	print(ruzzles(["abse", "imtn","nded","ssen"]))
	print(ruzzles(["reca", "rwar","aazp","syon"]))
	print(ruzzles(["abst", "oime","uesl","snsp"]))
	print(ruzzles(["essx", "ndet","sigh","raen"]))
	print(ruzzles(["poap", "lkjh","aswe","jhnh"]))

	

