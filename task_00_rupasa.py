import math
import numpy as np
def arithmetic():
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    sum=float(num1)+float(num2)
    print('sum is : {0}'.format(sum))
    diff=float(num1)-float(num2)
    print('difference is : {0}'.format(diff))
    mul=float(num1)*float(num2)
    print('product is : {0}'.format(mul))
    div=float(num1)/float(num2)
    print('sum is : {0}'.format(div))

def square_root():
    num1 = input('Enter number: ')
    print('Square root is: ')
    print(math.sqrt(float(num1)))

def nth_root():
    num1 = float(input('Enter number: '))
    num2 = float(input('Enter n: '))
    print('nth root is: ')
    print(num1**(1/num2))

def square():
    num1 = float(input('Enter number: '))
    print('Sqaure is: ')
    print(num1*num1)

def cube():
    num1 = float(input('Enter number: '))
    print('Cube is: ')
    print(num1*num1*num1)

def nth_power():
    num1 = float(input('Enter number: '))
    num2 = float(input('Enter n: '))
    print('nth power is: ')
    print(num1**(num2))

def exponential():
    num1 = float(input('Enter number: '))
    print('exponential is: ')
    print(math.exp(num1))

def logarithm():
    num1 = float(input('Enter number: '))
    print('logarithm is: ')
    print(math.log(num1))

def matmul():
    m1=int(input("Enter number of rows: "))
    n1=int(input("Enter number of columns: "))
    mat1=[]
    for i in range(0,n1):
        mat1.append([])
    for i in range (0,m1):
        for j in range(0,n1):
            mat1[i].append(j)
            mat1[i][j]=0
    for i in range (0,m1):
        for j in range(0,n1):
            print('entry in row: ',i+1,' column: ',j+1)
            mat1[i][j]=int(input())
    print(mat1)
    m2=int(input("Enter number of rows: "))
    n2=int(input("Enter number of columns: "))
    mat2=[]
    for i in range(0,n2):
        mat2.append([])
    for i in range (0,m2):
        for j in range(0,n2):
            mat2[i].append(j)
            mat2[i][j]=0
    for i in range (0,m2):
        for j in range(0,n2):
            print('entry in row: ',i+1,' column: ',j+1)
            mat2[i][j]=int(input())
    print(mat2)
    result=np.dot(mat1,mat2)
    print(result)
    
def calc(choice):
    while choice!=0:
        if choice == 1:
            arithmetic()
        elif choice==2:
            square_root()
        elif choice ==3:
            nth_root()
        elif choice==4:
            square()
        elif choice==5:
            cube()
        elif choice==6:
            nth_power()
        elif choice==7:
            exponential()
        elif choice==8:
            logarithm()
        elif choice==9:
            matmul()
        elif choice==0:
            print('operation ended')
            break
        choice=int(input('Enter your choice :'))
    
print('1. Arithmetic operations \n 2. Square root \n 3. nth root \n 4. square \n 5.cube \n 6.nth power \n 7. exp \n 8.logarithm\n 9.matrix multiplication\n')

choice=int(input('Enter your choice :'))
calc(choice)
