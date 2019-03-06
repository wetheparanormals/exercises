print('welcome to scientific calculator.')
print('available operations: 1.addition 2.subtraction 3.multiplication 4.divison 5.nth power 6.nth root 7.log(x) 8.e^x')
print('enter number of operands: 1 or 2')
h=int(input());
if(h==1):
    print('enter operand')
    b=int(input())
elif h==2:
    x,y=input('enter two numbers ').split()
    x=int(x)
    y=int(y)
else:
    print("invalid input")
if h==1 or h==2:
    c=int(input('enter operation '))
    if(c==1):
        print(x+y)
    elif(c==2):
        print(x-y)
    elif(c==3):
        print(x*y)
    elif(c==4):
        print(x/y)
    elif(c==5):
        print(x**y)
    elif(c==6):
        print(x**(1/y))
    elif(c==7):
        import math
        print(math.log(b))
    elif(c==8):
        import math
        print(math.exp(b))
    else:
        print('enter valid operation')
        
    
        

    
      
