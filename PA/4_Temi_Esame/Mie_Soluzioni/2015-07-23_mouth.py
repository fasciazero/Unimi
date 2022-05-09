dictionary = open('dictionary-7.txt').read().split()

def chain(origin,target):
	def rec(new,acc):
		if new == target: return acc
		distance_one = [word for word in dictionary if sum([0 if c == new[i] else 1 for i,c in enumerate(word)]) == 1]
		return '\n'.join([r for r in [str(rec(w,acc+[w])) for w in distance_one if w not in acc] if r])
	return rec(origin,[origin])

if __name__ == '__main__':
  print("### witness → fatness")
  print(chain("witness", "fatness"))
  print()
  print("### warning → earring")
  print(chain("warning", "earring"))
  print()
  print("### sailing → writing")
  print(chain("sailing", "writing"))