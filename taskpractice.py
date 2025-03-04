# for voting eligibility
x=int(input("enter your age:"))
if x>=18:    
    print("you can vote")
else:
    print("you are not eligible to vote")

# for  Number Divisible by 3 or 5
y=int(input("enter a number:"))
if y%3==0 and y%5==0:
    print("divisible by both")
elif y%3==0:
    print("divisible by 3")
else:
    print("divisible by 5")

# for vowel or consonant
p=input("enter a name:").swapcase()
if "name" in 'aeiou':
    print("vowel")
else:
    print("consonant")

