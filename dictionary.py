# # Creating a dictionary
# student = {
#     "name": "Alice",
#     "age": 20,
#     "course": "Computer Science",
#     "grades": [90, 85, 88]
# }

# # Accessing values
# print("Name:", student["name"])  
# print("Age:", student["age"])    
# print("Course:", student["course"])  
# print("Grades:", student["grades"])  

# # Adding a new key-value pair
# student["city"] = "New York"

# # Updating a value
# student["age"] = 21

# # Removing a key-value pair
# del student["grades"]

# # Looping through dictionary
# print("\nStudent Details:")
# for key, value in student.items():
#     print(key, ":", value)

num1, num2, num3 = 10 , 350 , 550
max = 0
if num1 >= num2:
    if num1 >= num3:
        print(num1)
elif num2 >= num1:
    if num2 >= num3:
        print(num2)
    else :
        print(num3)