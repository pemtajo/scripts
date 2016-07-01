
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
	print os.system(out)
	end=time.time()
	end_hour= time.strftime("%H:%M:%S")#the final hour
	arquive = open('./TCC.log', "a")

	
	msg=out+CHAR+ str(end-start)
	arquive.write(start_hour + CHAR + msg + CHAR + end_hour)#concatenate the string, with the CHAR
	arquive.close()
