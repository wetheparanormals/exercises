import math
print("Choose the required operation: ")
print("1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division ")
print("5. Nth root of a number ")
print("6. Nth power of a number ")
print("7. Logarithm ")
print("8. Expoential (e^x) ")
print("9. Matrix Multiplication: ")
r=int(input())
if r==1:
    print("Enter the numbers to be added: ")
    x,y=input().split()
    X=int(x)
    Y=int(y)
    print("The sum of {} and {} is {}".format(X,Y,X+Y))
elif r==2:
    print("Enter the numbers to be subtracted: ")
    x,y=input().split()
    X=int(x)
    Y=int(y)
    print("The difference of {} and {} is {}".format(X,Y,X-Y))
elif r==3:
    print("Enter the numbers for multiplication: ")
    x,y=input().split()
    X=int(x)
    Y=int(y)
    print("The multiplication of {} and {} is {}".format(X,Y,X*Y))
elif r==4:
    print("Enter the numbers for division: ")
    x,y=input().split()
    X=int(x)
    Y=int(y)
    print("The division of {} and {} is {}".format(X,Y,X/Y))
elif r==5:
    print("Enter number for base: ")
    x=int(input())
    print("Enter number for root: ")
    y=int(input())
    z=1/y
    if y==1:
        print("{}st root of {} is {}".format(y,x,x**z))
    elif y==2:
        print("{}nd root of {} is {}".format(y,x,x**z))
    elif y==3:
        print("{}rd root of {} is {}".format(y,x,x**z))
    else:
        print("{}th root of {} is {}".format(y,x,x**z))
elif r==6:
    print("Enter number for base: ")
    x=int(input())
    print("Enter number for power")
    y=int(input())
    z=y
    if y==1:
        print("{}st power of {} is {}".format(y,x,x**z))
    elif y==2:
        print("{}nd power of {} is {}".format(y,x,x**z))
    elif y==3:
        print("{}rd power of {} is {}".format(y,x,x**z))
    else:
        print("{}th power of {} is {}".format(y,x,x**z))
elif r==7:
    print("Enter the base of log: ")
    X=(input())
    print("Enter the number: ")
    y=int(input())
    if not X=='e':
        x=int(X)
        print("The log of {} to the base {} is {}".format(y,x,math.log(y,x)))
    else:
        print("The natural log of {} is {}".format(y,math.log(y)))
elif r==8:
    print("Enter the power of exponential: ")
    x=int(input())
    print("e to the power of {} is {}".format(x,math.exp(x)))
elif r==9:
    print("Enter the no. of rows and columns for First Matrix: ")
    r1,c1=input().split()
    r1=int(r1)
    c1=int(c1)
    M1 = [[0 for x in range(c1)] for y in range(r1)]
    for i in range (0,r1):
        print("Enter the elements of row no. {}".format(i+1))
        M1[i]=input().split()
    print("Enter the no. of rows and columns for Second Matrix: ")
    r2,c2=input().split()
    r2=int(r2)
    c2=int(c2)
    M2 = [[0 for x in range(c2)] for y in range(r2)]
    for k in range (0,r2):
        print("Enter the elements of row no. {}".format(k+1))
        M2[k]=input().split()
    M3=[[0 for j in range(c2)]for h in range (r1)]
    for t in range (r1):
        for u in range (c2):
            for g in range (c1):
                M3[t][u]+=int(M1[t][g])*int(M2[g][u])
    print("The resultant Matrix is: ")
    print(M3)
else:
    print("Please restart the program and enter a valid input ")



    
















        
    
