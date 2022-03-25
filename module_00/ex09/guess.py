import random


random_nb = random.randint(1, 99)


	
	
def treat_value(value, nb_try):
	if value is 42:
		print("The answer to the ultimate question of life, the universe and everything is 42.")
	if value < random_nb:
		print("Too low !\n")
		return nb_try + 1
	elif value > random_nb:
		print("Too high !\n")
		return nb_try + 1
	elif value is random_nb:
		if nb_try is 0:
			print("Congratulations ! You got it on your first try !")
		else:
			print("Congratulations, you've got it !")
			print("You won in {attempts} attempts !".format(attempts=nb_try))
		quit(0)
	
	
def error_checking(value):
	if value.isdigit() is False:
		print("That's not a number\n")
		return False
	elif len(value) < 1 or int(value) < 0 or int(value) > 99:
		print("Invalid value\n")
		return False
	else:
		return True
	
	
def main():
	print("This is an interactive guessing game!\n"
		"You have to enter a number between 1 and 99 to find out the secret number.\n"
		"Type 'exit' to end the game.\n"
		"Good luck!")
 
	nb_try = 0
	while 1:
		value = input("What's your guess between 1 and 99?\n>> ")
		if value == "exit":
			print("Goodbye !")
			quit(0)
		if error_checking(value) is True:
			value = int(value)
			nb_try = treat_value(value, nb_try)
		
		
if __name__ == '__main__':
	main()