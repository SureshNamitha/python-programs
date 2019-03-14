a=input("enter a value for a :")
b=input("enter a value for b:")
c=input("enter a value for c:")

def func1(a,b,c):
	print(" the values of a,b and c are:",a,b,c)
func1(a,b,c)

def func2():
	if a>b and a>c:
		print("a is larger than b and c!",a) 
	if b>a and b>c:
		print("b is larger than a and c!",b)
	if c>a and c>b:
		print("c is larger than b and a!",c)   # or use "return"                         
func2()