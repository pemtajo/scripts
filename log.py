
#this is my log, for the commanders then I use for my TCC

import sys
import os
import time

CHAR='#'#character for scape, for when read, split that caracter
if __name__ == "__main__":
	out=''
	for i in range(1, len(sys.argv)):#create a string without the first parameter (log.py)
		out+=sys.argv[i]+' '

	start=time.time() #for calculate the time
	start_hour=time.strftime("%H:%M:%S") #the hour, minute and second that I start the command
	os.system(out)
	end=time.time()
	end_hour= time.strftime("%H:%M:%S")#the final hour
	
	msg=out+CHAR+ str(end-start)
	valid=False
	while True: 
		s=raw_input('Was a valid command?(N/y)\n')
		if s=='' or s=='n' or s=='N':
			break
		elif s=='y'or s=='Y':
			valid=True
			break
	if valid:
		test=True
		while True:
			s=raw_input('The result was positive? (Y/n)\n')
			if s=='n' or s=='N':
				test=False
				break
			elif s=='' or s=='y' or s=='Y':
				break
			
		s=raw_input('Observation:\n')

		arquive = open('./TCC.log', "a")

		arquive.write(start_hour + CHAR + msg + CHAR + end_hour +CHAR+ str(test)+ CHAR + s+'\r\n')#concatenate the string, with the CHAR
		arquive.close()
