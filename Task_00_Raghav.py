##paranormals---task0-author Raghav Madaan
from math import pi, e, sin, cos, tan, log, log10, exp, sqrt

print(" You can perform following operation:- a+b,a-b,a*b,a/b,a^b,sin(a),cos(a),tan(a),log(a),log10(a),exp(a),sqrt(a)")

op=int(input(" press 1 for uninary operation and 2 for binary operation"))
print("enter first operator")
a=int(input())
if(op==2):
    print("enter second operator")
    b=int(input())
print("which operation would you like to perform:-")
operation=input()
if(operation == '+'):
    print("Answer= ",end=" "); print(str(a+b)) ;  
elif(operation == '-'):
    print("Answer= ",end=" "); print(str(a-b))   
elif(operation == '*'):
    print("Answer= ",end=" "); print(str(a*b))   
elif(operation == '/'):
    print("Answer= ",end=" "); print(str(a/b))   
elif(operation == '^'):
    print("Answer= ",end=" "); print(str(a**b))
elif(operation == 'sin'):
    print("Answer= ",end=" "); print(str(sin(a)))
elif(operation == 'cos'):
    print("Answer= ",end=" "); print(str(cos(a)))
elif(operation == 'tan'):
    print("Answer= ",end=" "); print(str(tan(a)))
elif(operation == 'log'):
    print("Answer= ",end=" "); print(str(log(a)))
elif(operation == 'log10'):
    print("Answer= ",end=" "); print(str(log10(a)))
elif(operation == 'exp'):
    print("Answer= ",end=" "); print(str(exp(a)))
elif(operation == 'sqrt'):
    print("Answer= ",end=" "); print(str(sqrt(a)))
else:
    print("enter valid input")

