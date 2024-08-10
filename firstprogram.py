"""
name="zaeem"
age=22
price=55
print(name,age)

name=input("enter a name")
print("welcome", name)"""

"""
a = int(input("firstnumber :"))
b = int(input("secondnumber :"))
sum = a+b
print(sum)"""

"""
str1= "apnacollage"
ch=str1[2]
len1=len(str1)
print(len1)
print(ch)

#slicing
#positive
str2="zaeem shakeel"
print(str2[0:8])"""


"""
#slicing
#negative 
str4="zaeem shakeel"
print(str4[-8:-1])"""


""""
name=input("enter a name :")
print("length of you name is :", len(name))"""


"""
str=" hi $I am the $ symbol $999.0"
print(str.count("$"))
"""



#conditional statement
light="pink"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("wait")
else:
    print("light is broken")
    
    
    
    mark=75
    if(mark>=90):
        grade="A"
    elif(mark>=80 and mark<90):
        grade="B"
    elif(mark>=70 and mark<80):
        grade="C"
    else:
        grade="D"
    print("grade of this student->" ,grade)
    
    
    #nested
    
    age=95
    
    if(age>=18):
        if(age>=80):
            print("cannot drive")
        else:
            print("can drive")
            
            

            