l=[1,2,3,4,5]

def func1(l):
	k=0

	for s in l:
		k=s+k
	return k

p=func1(l)
print("the sum of the list is:",p)

