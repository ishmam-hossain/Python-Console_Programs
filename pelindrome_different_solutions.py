import time

def isPelindrome(s):
	length = len(s)
	for i in range(length//2):
		if s[i] != s[length - 1 - i]:
			return "Not a pelindrome!"
	
	return "Pelindrome"

def pelindrome_reverse(word):
	rev = word[::-1]
	if word != rev:
		return "Not a Peindrome!"
	else:
		return "Peindrome!"	

def pelindrome_shortcut(word):
	return word == word[::-1]

print(isPelindrome('abcb'))
