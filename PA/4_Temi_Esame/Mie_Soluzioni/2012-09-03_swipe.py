from re import search

dictionary = open('dictionary.txt').read().split()

def get_suggestion(chars):
	possible_words = [x for x in dictionary if x[0] == chars[0] and x[-1] == chars[-1]]
	regex = ['.*'.join([c for c in word]) for word in possible_words]
	return [possible_words[i] for i,pattern in enumerate(regex) if search(pattern,chars)]

if __name__ == '__main__':
	test_cases = ['heqerqllo','qwertyuihgfcvbnjk','wertyuioiuytrtghjklkjhgfd','dfghjioijhgvcftyuioiuytr','aserfcvghjiuytedcftyuytre','asdfgrtyuijhvcvghuiklkjuytyuytre','mjuytfdsdftyuiuhgvc','vghjioiuhgvcxsasdvbhuiklkjhgfdsaserty','werfghgfrerteyuiklkmnbvcxsasdrrtyuioiuytrews']
	for test in test_cases: print(get_suggestion(test))