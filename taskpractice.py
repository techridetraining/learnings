# # for voting eligibility
# x=int(input("enter your age:"))
# if x>=18:    
#     print("you can vote")
# else:
#     print("you are not eligible to vote")

# # for  Number Divisible by 3 or 5
# y=int(input("enter a number:"))
# if y%3==0 and y%5==0:
#     print("divisible by both")
# elif y%3==0:
#     print("divisible by 3")
# else:
#     print("divisible by 5")

# # for vowel or consonant
# p=input("enter a name:").swapcase()
# if "name" in 'aeiou':
#     print("vowel")
# else:
#     print("consonant")

# while loop
# p=1
# while p<=10:
#     print(p)
#     p=p+1

# p=2
# while p<=20:
#     print(p)
#     p=p+2

#     # or

# p = 1
# while p <= 20:
#     if p % 2 == 0:
#         print(p)
#     p = p + 1

# r = 1
# sum = 0
# while r <= 50:
#     sum = sum + r  # Adding each number to the sum
#     r = r + 1
# print("Total Sum =", sum)

# p=10
# while p>=1:
#     print(p)
#     p=p-1

# n = int(input("Enter a number: "))
# while n != 0:
#     n = int(input("Enter a number: "))
# print("Loop stopped")

# n = int(input("Enter a number: "))
# i=1
# while i<=10:
#     print(f"{n}x{i}'={n*i}")
#     while i<=10
#     i=i+1
tables = int(input("How many tables do you want: "))
count = 1

while count <= tables:
    n = int(input(f"Enter number {count}: "))
    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n * i}")
        i = i + 1
    print()  # For Gap between tables
    count = count + 1


   