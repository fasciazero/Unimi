from re import findall

class UpDownFile:
	def __init__(self,file):
		self.file = findall(r'[a-zA-Z0-9]+',open(file).read())
		self.len = len(self.file)
	def __iter__(self):
		self.idx = -1
		return self
	def __next__(self):
		if self.idx + 1 == self.len:
			raise StopIteration('Index out of bound')
		self.idx += 1
		return self.file[self.idx]
	def ungetw(self):
		if self.idx > 0:
			self.idx -= 1
	def __str__(self):
		return 'Testo\n'+' '.join(self.file)

if __name__ == "__main__":
  fiter = UpDownFile('text.txt')
  iter(fiter)
  print('### Let\'s go up and down for a while') 
  print(next(fiter))
  print(next(fiter))
  print(next(fiter))
  print(next(fiter))
  print(next(fiter))
  print(next(fiter))
  fiter.ungetw()
  fiter.ungetw()
  fiter.ungetw()
  print(next(fiter))
  print(next(fiter))
  fiter.ungetw()
  fiter.ungetw()
  print(next(fiter))
  fiter.ungetw()
  fiter.ungetw()
  fiter.ungetw()
  print(next(fiter))
  print(next(fiter))
  print(next(fiter))
  fiter.ungetw()
  print('### Let\'s finish the iteration') 
  try:
    while True:
      print(next(fiter))
  except StopIteration: pass
  print('### Let\'s restart the iteration') 
  iter(fiter)
  print(next(fiter))
  print(next(fiter))
  print(next(fiter))
  fiter.ungetw()
  print(next(fiter))