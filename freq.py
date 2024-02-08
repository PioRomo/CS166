import sys 

ETAOIN = 'etaoinshrdlcumwfgypbvkjxqz' 
LETTERS = 'abcdefghijklmnopqrstuvwxyz'

with open(sys.argv[1], 'r') as file:

	letterCount = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

	for line in file: 
		for letter in line: 
			if letter in LETTERS: 
				letterCount[letter] +=1

	myList = sorted(letterCount.items(), key=lambda x:x[1], reverse=True)
	print myList 
	
