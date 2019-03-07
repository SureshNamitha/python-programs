import random
while True:
	r = input("press 'r' to roll and press 'q' to quit the game:")
	if r =="r":
		print(random.randint(1,6))
	if r =="q":
		print("bye!")
		exit(0)