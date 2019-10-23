# Ryan Bierman
# 10-21-19
# Period 6

myWord = "ryan"
myList = list(myWord)

secret = []

# Hangman Picture
print("0=-- Welcome to Hangman --=0")
for s in myList:
		secret.append("_")

	

	print(secret)
	count = 0
	choice = input("what word am I thinking of? ")
	if chioce == "ryan":
		print("Nice Guess, you are correct")
	else:
		print("Not the word that I'm thinking of")
while True:	
		
	for x in myList:
		if x == choice:
			secret[count] = choice
			print(secret)

		count = count + 1



	