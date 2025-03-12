# Creating a set
fruits = {"apple", "banana", "cherry"}

# Adding an element to the set
fruits.add("orange")

# Removing an element from the set
fruits.remove("banana")

# Checking if an element exists in the set
if "apple" in fruits:
    print("Apple is in the set")

# Looping through the set
print("\nFruits in the set:")
for fruit in fruits:
    print(fruit)

# Performing set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\nUnion:", set1 | set2)        # Union of sets
print("Intersection:", set1 & set2)  # Intersection of sets
print("Difference:", set1 - set2)    # Difference of sets
