import math

def matrixMultiplication():
    print("Enter the dimensions of Ist matrix:(enter them in a line with a space separation in the order of rows first and then columns)")
    str=input()
    a,b=str.split()
    a=int(a)
    b=int(b)
    Matrix1 = [[0 for i in range(b)] for j in range(a)]
    print("Enter the elements of the first matrix:(enter a row in a line with space separated integers)")
    # print(Matrix1)
    for i in range(a):
        X=input()
        str=X.split()
        for j in range(b):
            Matrix1[i][j]=int(str[j])

    print("Enter the dimensions of 2nd matrix:(enter them in a line with a space separation in the order of rows first and then columns)")
    str=input()
    x,y=str.split()
    x=int(x)
    y=int(y)
    Matrix2 = [[0 for i in range(y)] for j in range(x)]

    print("Enter the elements of the second matrix:(enter a row in a line with space separated integers)")
    for i in range(x):
        X=input()
        str=X.split()
        for j in range(y):
            Matrix2[i][j]=int(str[j])
    if b!=x:
        print("Can not be multiplied")
    else:
        sum=0
        Matrix3 = [[0 for i in range(y)] for j in range(a)]
        for c in range(a):
            for d in range(y):
                for k in range(x):
                    sum = sum + Matrix1[c][k]*Matrix2[k][d]
                Matrix3[c][d] = sum
                sum = 0;

        print("Product of the Matrices:\n")

        for i in range(a):
            for j in range(y):
                print(Matrix3[i][j],end=" ")
            print()

def rootsPowers():
    print("Select Operation:\n")
    print("1. Sq.root")
    print("2. Nth root")
    print("3. Square")
    print("4. Nth power")
    n=input()
    n=int(n)
    if n == 1:
        num1=input("Enter number x\n")
        print("square root of x=",int(num1)**(0.5))
        print()
    elif n == 2:
        num1=input("Enter number x\n")
        num2=input("Enter the value of n\n")
        print("nth root of x=", int(num1)**(float(1/int(num2))))
        print()
    elif n == 3:
        num1=input("Enter number x\n")
        print("Square of x=", int(num1)**2)
        print()
    elif n == 4:
        num1=input("Enter number x\n")
        num2=input("Enter the value of n\n")
        print("nth power of x=", int(num1)**int(num2))
        print()
    else:
        print("Invalid input")
        return 0
    return 1


def simpleCalculator():
    print("Select Operation:\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    n=input()
    n=int(n)
    if n == 1:
        num1=input("Enter number 1\n")
        num2=input("Enter number 2\n")
        print("Addition=",int(num1)+int(num2))
        print()
    elif n == 2:
        num1=input("Enter number 1\n")
        num2=input("Enter number 2\n")
        print("Subtraction=", int(num1)-int(num2))
        print()
    elif n == 3:
        num1=input("Enter number 1\n")
        num2=input("Enter number 2\n")
        print("Multiplication=", int(num1)*int(num2))
        print()
    elif n == 4:
        num1=input("Enter number 1\n")
        num2=input("Enter number 2\n")
        print("Division=", int(num1)/int(num2))
        print()
    else:
        print("Invalid input")
        return 0
    return 1



while 1:
    print("Please select operation-\n")
    print("1. Arithmetic Operations")
    print("2. Log")
    print("3. Exponent")
    print("4. Roots and Powers")
    print("5. Matrix Multiplication\n")
    n = input("Select operations form 1, 2, 3, 4, 5 :(enter any other number to break)\n")
    n=int(n)
    if n == 1:
        x=simpleCalculator()
        if x==0:
            break
    elif n == 2:
        num1=input("Enter number (x)\n")
        base=input("enter base of log\n")
        print("Log(x)=", math.log(int(num1),int(base)))
        print()
    elif n == 3:
        num1=input("Enter number x\n")
        print("e^x=", math.exp(int(num1)))
        print()
    elif n == 4:
        y=rootsPowers()
        if y==0:
            break
    elif n==5:
        matrixMultiplication()
    else:
        print("Invalid input")
        break
