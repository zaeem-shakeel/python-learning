"""
movies=[]
mov1=input("emter a 1st movies :")
mov2=input("enter a 2nd movies :")
mov3=input("enter a 3nd movies :")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

"""

"""
list1=["m","a","a","m"]
list1=[1,2,1]

list_copy=list1.copy()
list1.reverse()

if(list_copy==list1):
    print("palindrome")
else:
    print("palindrome")
    
    """
    
# grade=("C","A","B","B","A","D","A")
# print(grade.count("A"))
    
    
    
# grade=["C","A","B","B","A","D","A"]
# grade.sort()
# print(grade)
    
    
# lst=(i*i for i in range(5))
# print(lst)



#Map  methode
def cube(x):
    return x*x*x

# print(cube(2))
# l=[1,3,4,5,6]
# A=[]
# for items in l:
#     A.append(cube(items))
#     print(A)
    
    
# l=[1,3,5,9,5,4,6]

# newl=list(map( cube,l))
# print(newl)



#FILTER method
# def new(x):
#     return x>4
# t=[1,3,4,5,7,8,9]

# newe=list(filter(new,t))
# print(newe)



#REDUCE method
from functools import reduce
num=[2,3,5,6,7,8,9,1]
def sum(x,y):
    return x+y

numl= reduce(sum,num)

print(numl)