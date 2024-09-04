# x=[1,2,3]
# print(dir(x))

# #single inheritance
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def make_sound(self):
#         print("Sound made by the animal")

# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def make_sound(self):
#         print("Bark!")

# d = Dog("Dog", "Doggerman")
# d.make_sound()



# #multiples inheritance
# class Employee:
#   def __init__(self, name):
#     self.name = name
#   def show(self):
#     print(f"The name is {self.name}")

# class Dancer:
#   def __init__(self, dance):
#     self.dance = dance

#   def show(self):
#     print(f"The dance is {self.dance}")

# class DancerEmployee(Employee, Dancer):
#   def __init__(self, dance, name):
#     self.dance = dance
#     self.name = name

# o  = DancerEmployee("Kathak", "Shivani")
# print(o.name)
# print(o.dance)
# o.show() 
# print(DancerEmployee.mro())



# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def make_sound(self):
#         print("Sound made by the animal")
        
# class Mammal:
#     def __init__(self, name, fur_color):
#         self.name = name
#         self.fur_color = fur_color
        
# class Dog(Animal, Mammal):
#     def __init__(self, name, breed, fur_color):
#         Animal.__init__(self, name, species="Dog")
#         Mammal.__init__(self, name, fur_color)
#         self.breed = breed
        
#     def make_sound(self):
#         print("Bark!")
        
# d = Dog("Dog", "Doggerman","black")
# d.make_sound()



# #Multilevel inheritance
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
        
#     def show_details(self):
#         print(f"Name: {self.name}")
#         print(f"Species: {self.species}")
        
# class Dog(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name, species="Dog")
#         self.breed = breed
        
#     def show_details(self):
#         Animal.show_details(self)
#         print(f"Breed: {self.breed}")
        
# class GoldenRetriever(Dog):
#     def __init__(self, name, color):
#         Dog.__init__(self, name, breed="Golden Retriever")
#         self.color = color
        
#     def show_details(self):
#         Dog.show_details(self)
#         print(f"Color: {self.color}")

# o =GoldenRetriever("tommy", "Black")
# o.show_details()
# print(GoldenRetriever.mro())




#Hybrid inheritance
# class Human:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
    
#   def show_details(self):
#     print("Name:", self.name)
#     print("Age:", self.age)
    
# class Person(Human):
#   def __init__(self, name, age, address):
#     Human.__init__(self, name, age)
#     self.address = address
    
#   def show_details(self):
#     Human.show_details(self)
#     print("Address:", self.address)
    
# class Program:
#   def __init__(self, program_name, duration):
#     self.program_name = program_name
#     self.duration = duration
    
#   def show_details(self):
#     print("Program Name:", self.program_name)
#     print("Duration:", self.duration)
    
# class Student(Person):
#   def __init__(self, name, age, address, program):
#     Person.__init__(self, name, age, address)
#     self.program = program
    
#   def show_details(self):
#     Person.show_details(self)
#     program.show_details()
    
# program = Program("Computer Science", 4)
# student = Student("John Doe", 25, "123 Main St.", program)
# student.show_details()



#Hierarchical inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    def show_details(self):
        print("Name:", self.name)
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed
    def show_details(self):
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)
class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color
    def show_details(self):
        Animal.show_details(self)
        print("Species: Cat")
        print("Color:", self.color)
        
dog = Dog("Max", "Golden Retriever")
dog.show_details()
cat = Cat("Luna", "Black")
cat.show_details()