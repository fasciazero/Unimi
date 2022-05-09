import re
from functools import reduce

class IncrementalDict:
    def __init__(self):
        self.d = dict()
    def __call__(self, selff, word):
        self.d[word] = self.d[word]+1 if word in self.d else 1
        return self

def freqs(filename, maxfreq):
    return list(map(lambda x:x[0], sorted(filter(lambda x:x[1]>=maxfreq, reduce(IncrementalDict(), list(map(lambda x:x.lower(), filter(lambda x:x!="", re.sub(r"[\W]", " ", open(filename).read()).split(" "))))).d.items()), key=lambda x:x[1], reverse=True)))

print(freqs(r"C:\Users\Oscar\Desktop\PA\Exercises\Lab 2\freq.txt", 10))
