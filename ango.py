figures = [
'A','B','C','D','E','F','G',
'H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U',
'V','W','X','Y','Z'
]

while True:
	mes_in = input()
	
	if mes_in != "exit":	
		mes_out = ""

		for j in range(len(mes_in)):
			for i in range(len(figures)):
				if(mes_in[j] == figures[i]):
					mes_out += figures[(i+10)%26]
					break
		
		print (mes_in + " -> " + mes_out)
	else:
		exit()