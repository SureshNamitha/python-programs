import random

m=input(" enter a value:")
if m=='q':
	print("game over")
	exit()


c=random.choice("rps")

di={'r':"rock",'p':"paper",'s':"scissors"}
us=0
cs=0
for x in di:
	if x==m:
		print("user choice is",di[x])
for x in di:
	if x== c:
		print("comp choice is",di[x])

if m==c:
	print("tie between user and comp!!")

if m=='r' and c=='p':
	print("comp u won!!")
	cs=cs+1
elif m=='r' and c=='s':
	print("user u won!!")
	us=us+1
elif m=='p' and c=='s':
	print("comp u won!!")
	cs=cs+1
elif m=='p' and c=='r':
	print("user u won!!")
	us=us+1
elif m=='s' and c=='r':
	print("comp u won!!")
	cs=cs+1
elif m=='s' and c=='p':
	print(" user u won!!")
	us=us+1
	
    print("score:")
	print("computer:",cs,"user:",us)
if us==3:
	print(" user u have won the GAME!!")
	exit()
if cs==3:
	print("comp has won the GAME!!")
	exit()