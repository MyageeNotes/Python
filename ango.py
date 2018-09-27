import sys

figures = [
'A','B','C','D','E','F','G',
'H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U',
'V','W','X','Y','Z'
]

while True:
	key = input()

	for i in range(len(figures)):
		if(key == figures[i]):
			print(figures[(i+10)%26])
