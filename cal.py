import math
print("\t-----Calculator-----")
def sum(a,b):
    a += b
    return a

def sub(a,b):
    if a>b:
        a -= b
        return a
    else:
        b -= a
        return b
def mul(a,b):
    a *= b
    return a

def div(a,b):
    q = a/b
    r = a%b
    print("\n Quotient is : %s"%q)
    print("\n Remainder is : %s"%r)
    
def sqr(a):
    x = math.sqrt(a)
    return x

while(True):
    print("\n\nChoose the operation you want to perform")
    print("\n\t1.ADDITION")
    print("\n\t2.SUBTRACTION")
    print("\n\t3.DIVISION")
    print("\n\t4.SQUARE ROOT")
    print("\n\t5.EXIT")
    
    choice = int(input())
    
    if choice == 1:
        n1 = int(input())
        n2 = int(input())
        a = sum(n1,n2)
        print("The sum is: %s"%a)
        
    if choice == 2:
        n1 = int(input())
        n2 = int(input())
        s = sub(n1,n2)
        print("The diffrence is: %s"%s)
        
    if choice == 3:
        n1 = int(input())
        n2 = int(input())
        m = mul(n1,n2)
        print("\nThe product is: %s"%m)
        
    if choice == 4:
        n1 = int(input())
        n2 = int(input())
        div(n1,n2)
        
    if choice == 5:
        n1 = int(input())
        r = sqr(n1)
        print("\nThe square root is: %s"%r)
        
    else:
        print("You chose to exit.Bye!!!!!!")
        break
