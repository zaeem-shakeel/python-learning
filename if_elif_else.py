num = int(input("enter a number :"))
if(num%2==0):
    print("even")
else:
    print("odd")
    
    
    a = int(input("enter  first number :"))
    b= int(input("enter second number :"))
    c = int(input("enter third number :"))
    
    if(a>=b and a>=c):
        print("greater  a number :" ,a)
    if(b>=c):
        print("greater  a number :" ,b)    
    else:
        print("greater  a number :" ,c)    