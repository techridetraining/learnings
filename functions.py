# logic for create function to parameter

# def add(a,b):
#    print(a+b)

# add(20,37)

# def multi(a,b):
#     print(a*b)

# multi(15,15)

# def sub(a,b):
#     print(a-b)

# sub(775,341)

# logic for function parameter to return (value that gives to argument or parameter)

# def hello():
#     return("hello world!")
# z=hello() 
# print(z)

# def greet(name):
#     print("Hi",{name})

# # def sayhi(name):
# #     print("Hi",name)

# def greet(name = 'user!'):
#     return "Hello"+ name

# a=greet("bob")
# print(a)

# def animal(name='pet'):
#     return "the animal is "+name

# x=animal("dog")
# print(x)

# positional arguements:gives the exact positon of variable or assigning value
# def pet(animal,name):
#     return (f"this is a {animal} and the name is {name}")

# x=pet("dog","brownie")
# print(x)

# def student(name, age, phno):
#     print(f"name is {name},age is{age}, ph.no is{phno}")

# x=student("sam",20,987654321)
# print(x)

# def student(age,name, phno):
#     return(f"name is {name},age is{age}, ph.no is{phno}")

# x=student("sam",20,987654321)
# print(x)
# Global variable
x = 10

# def my_function():
#     # Local variable
#     y = 5
#     print("Inside the function:")
#     print("Global variable x:", x)  # Accessing global variable
#     print("Local variable y:", y)   # Accessing local variable

# # Calling the function
# my_function()

# print("Outside the function:")
# print("Global variable x:", x)  # Can access global variable
# # print("Local variable y:", y)  # This will raise an error, as 'y' is local to the function



# def func(a):
#     a=a+10

# c=func(5)
# print(c)
# print(f'global:{a}')
    
# class Example:
#     def __init__(self, name):
#         self.name = name 

#     def display(self):
#         print("Name:", self.name)  

# obj = Example("Rahul")
# print(obj.name)  
# obj.display() 

# class Parent:
#     def __init__(self):
#         self._protected_var = "I am protected" 

# class Child(Parent):
#     def show(self):
#         print(self._protected_var)  
# obj = Child()
# obj.show() 
# print(obj._protected_var) 
