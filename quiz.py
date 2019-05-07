def tens(t):
	x=[range(0,10)]
	for numbers in t:
		for y in numbers:
			z=y*10
			x.append(z)

	return z
	
def squares(s):
	square=[]
	for sublist in s:
		for y in sublist:
			z=y*y
			square.append(z)

	return z		

def range(number):
	z=[]
	number=n
	for p in range (1,n):
		z.append(p)
		y = sum(z)
	return y

def largest(l):
	c=[]
	for x in l:
		y=max(c)

	return y
def smallest(s):
	c=[]
	for x in s:
		y=min(c)

	return y


def sorted(st):
	a=[]
	b=[]

	for p in st:
		x=a+b
		y=sort(x)
	return y


def students(balance,name):
	students=[]
	b=balance
	n=name
	for student in students:
		print("hello {},your balance is {}".format(n,b))


def my_modulus(number):
	for p in range(10,20):
		y=p%3
		z={p:y}

	return z	
