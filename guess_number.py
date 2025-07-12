import random
num_guess=0
rng=random.randint(1,100) # εάν το rng ήταν ενταχμένο στην επανλάψη τότε θα είχαμε για κάθε προσπάθεια  έναν νέο αριθμό πχ. αν ειχαμε το 1 μετά από λάθος μαντεψιά θα είχαμε το 100 πχ
while True:
	a=int(input("Hello,usr please select a number 1 to 100: "))
	if a>rng:
		print("Too large guess!")
	else:
		print("Too small guess!")
	if a==rng:
		print("Congrats!, you guess was correct!")
		print("The number was",rng,)
		break
	else:
	    num_guess+=1
	    print("Wrong Guess! Try again!")
	    print("Guesses",num_guess,)	
