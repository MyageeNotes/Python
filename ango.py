# Words Array
figures = [
'A','B','C','D','E','F','G',
'H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U',
'V','W','X','Y','Z'
]

# Loop endless untill you input "exit"
while True:
	
	# INPUT Message
	mes_in = input()
	
	# Continue or NOT
	if mes_in != "exit":
	
		# Initialize OUTPUT Message
		mes_out = ""
		
		# Checking each figures
		for j in range(len(mes_in)):
			
			# Find out a INPUT figure from 'figures' array
			for i in range(len(figures)):
			
				# Found a figure, add to OUTPUT Message and finish searching
				if(mes_in[j] == figures[i]):
					mes_out += figures[(i+10)%26]
					break
		
		# Display Changing
		print (mes_in + " -> " + mes_out)
	
	else:
		exit()