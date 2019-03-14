l=[2,4,6,8,10]

def func1(l):
	a=1
	for i in l:
		a=i*a
	return a
b=func1(l)
print("the multiplication of the list is:",b)
