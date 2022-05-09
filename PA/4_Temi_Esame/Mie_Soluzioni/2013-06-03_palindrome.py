from functools import lru_cache

@lru_cache()
def palin(s):
	if len(s) <= 1: return []
	if s[0] == s[-1]: return palin(s[1:-1])
	return min([s[-1]]+palin(s[:-1]),[s[0]]+palin(s[1:]),key=lambda x:len(x))

if __name__ == "__main__":
	print(palin("casa"))
	print(palin("otto"))
	print(palin("palindromo"))
	print(palin("posero"))
	print(palin("coccinella"))