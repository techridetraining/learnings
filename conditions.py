# Even or odd numberchecker
x=int(input("enter a number"))
y=x%3
if y==0:
    print('even')
else:
    print('odd')

# check if it is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# age group classification
age = int(input("Enter your age: "))
if age < 13:
    print("child")
elif 13 <= age <= 17:
    print(" teenager")
elif 18 <= age <= 64:
    print("adult")
else:
    print("senior citizen")

# grade evaluation
grade = int(input("Enter your grade (0-100): "))
if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B.")
elif grade >= 70:
    print("You got a C.")
elif grade >= 60:
    print("You got a D.")
else:
    print("You got an F.")

# number comparision
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num2} is greater than {num1}.")
else:
    print("Both numbers are equal.")

# for multplication table
    num = int(input("Enter a number: "))
if num <= 0:
    print("Please enter a positive number.")
else:
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
