import math


def arithmaticOperations():
	print("Select Operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
	ctr=int(input("enter number for corresponding operation"))
	a=float(input("enter first number"))
	b=float(input("enter second number"))
	if ctr==1:
		print("addtion of ",a," and ",b," is:")
		print(a+b)
	elif ctr==2:
		print("difference of ",a," and ",b," is:")
		print(a-b)
	elif ctr==3:
		print("Product of ",a," and ",b," is:")
		print(a*b)
	elif ctr==4:
		print("Division of ",a," and ",b," is:")
		print(a/b)
	else:
		print("invalid input")

	return

def power():
	print("enter base and power separated by space")
	a=[int(x) for x in input().split()]
	print(a[0],"^",a[1]," is:")
	print(a[0]**a[1])
	return

while 1:
	n=int(input("Select Operation:\n1. Arithmatic\n2. Exponentiation and roots\n3. Logarithmic\n4. Natural Exponentiation\nAny other number to stop\n"))
	if n==1:
		arithmaticOperations()
	elif n==2:
		power()
	elif n==3:
		num1=input("Enter number (x)\n")
		base=input("enter base of log\n")
		print("Log(x)=", math.log(int(num1),int(base)))
	elif n==4:
		b=int(input("enter power"))
		print("e^",b," is:")
		print(2.73**b)
	else:
		break
