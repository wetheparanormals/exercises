import math
def add():
    num1=float(input("enter first number"))
    num2=float(input("enter second number"))
    ans=num1+num2
    print(ans)

def sub():
    num1=float(input("enter first number"))
    num2=float(input("enter second number"))
    ans=num1-num2
    print(ans)

def mul():
    num1=float(input("enter first number"))
    num2=float(input("enter second number"))
    ans=num1*num2
    print(ans)

def div():
    num1=float(input("enter first number"))
    num2=float(input("enter second number"))
    ans=num1/num2
    print(ans)

def nthroot():
    num1= float(input("enter the number"))
    nr=int(input("enter n"))
    print(math.pow(num1,(1/nr)))

def nthpow():
    num1=float(input("enter number"))
    np=int(input("enter n"))
    print(math.pow(num1,np))

def expo():
    x=int(input("enter power of e"))
    for i in range(1,x+1):
        e=1*e
    print(e)

def logf():
    num1=int(input("enter number"))
    base=int(input("enter base"))
    print(math.log(num1,base))
    
def main():
    n= int(input("press 1. for addition \n 2. subtraction \n 3.multiplication \n 4. division\n 5. nth root\n 6. nth power\n 7.e raised to power x \n 8. logarithmic value"))
    if(n==1):
        add()
    if(n==2):
        sub()
    if(n==3):
        mul()
    if(n==4):
        div()

    if(n==5):
        nthroot()
    if(n==6):
        nthpow()
    if(n==7):
        expo()
    if(n==8):
        logf()
    
    
    
if __name__=="__main__":
    main()
