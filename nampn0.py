a=int(input(" enter a value:"))

def func1(a):
	print("the entered value is:")
	if a==0:
		print("value of a is zero!!")
	elif a>=0:
		print("value of a is positive!!")
	elif a<=0:
		print("value of a is negative!!")

func1(a)