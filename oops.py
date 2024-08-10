# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     def get__avg (self):
#         sum=0
#         for val in self.marks:
#           sum+=val
#         print('Hi',self.name , "studednt at avg score",sum/3 )     
        
# s1=student("zaeem",[98,97,90])
# s1.get__avg()





# class Account:
#     def __init__(self,baln,acc):
#         self.balance=baln 
#         self.account=acc
        
#     def debit(self,amount):
#          self.balance-=amount
#          print("Rs", amount ,"was debited")
#          print("Totals balance =", self.get_balance())
         
#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs",amount,"was credits")
#         print("Totals balance =", self.get_balance())
        
#     def get_balance(self):
#         return self.balance  
    
    
# s1=Account(10000,223344)    
# s1.debit(1000)
# s1.credit(400)    
# s1.credit(5000)



#polymorphism

# class complex:
#     def __init__(self,real,imag):
#         self.real=real
#         self.imag=imag
        
#     def showNumber(self):
#         print(self.real,"i","+",self.imag,"j")
        
#     def add(self,num2):
#         Newreal=self.real+num2.real
#         Newimag=self.imag+num2.imag
#         return complex(Newreal,Newimag)
        
# num1=complex(1,3)
# num1.showNumber()
   
# num2=complex(5,7)
# num2.showNumber()

# num3=num1.add(num2)
# num3.showNumber()
    
    
    
    
    
# class circle:
#     def __init__(self,radius):
#         self.radius=radius
        
#     def area(self):
#         return int((22/7)*self.radius**2)  
    
#     def parimter(self):
#         return int(2*(22/7)*self.radius)
 
# c1=circle(6)
# print(c1.area())
# print(c1.parimter())
    
      
      
      
      
      
# class Empolyee:
#     def __init__(self,role,dept,salary) :
#         self.role=role
#         self.dept=dept
#         self.salary=salary
        
#     def showdetails(self):
#             print("role=",self.role)
#             print("dept=",self.dept)
#             print("salary=",self.salary)
            
# class Engineer(Empolyee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Engineer", "softer engineer","10,00000")            
    
    
# c1=Engineer("Zaeem shakeel","22")
# c1.showdetails()   






# class order:
#     def __init__(self,items,price):
#         self.items=items
#         self.price=price
            
#     def __get__ (self,odr2):
#         return self.price > odr2.price
    
    
# odr1=("cake",50)
# odr2=("tea",10)



# print(odr1>odr2) #true

