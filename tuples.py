# Creating a tuple
person = ("Alice", 25, "New York")

# Accessing elements by index
print("Name:", person[0])  
print("Age:", person[1])    
print("City:", person[2])  

# Looping through a tuple
print("\nTuple elements:")
for item in person:
    print(item)

# Tuple unpacking
name, age, city = person
print("\nUnpacked values:")
print("Name:", name)
print("Age:", age)
print("City:", city)

# Trying to modify a tuple (This will cause an error)
# person[1] = 26  # TypeError: 'tuple' object does not support item assignment

# Creating a tuple with one element (must include a comma)
single_element_tuple = ("Hello",)  
print("\nSingle element tuple:", single_element_tuple)

# tuple with hash value

# Creating tuples
t1 = (1, 2, 3)
t2 = ("apple", "banana", "cherry")

# Using tuples as dictionary keys
tuple_dict = {
    (1, 2): "Point A",
    (3, 4): "Point B"
}

print("Value for key (1,2):", tuple_dict[(1, 2)])

# Using tuples in a set
tuple_set = {(10, 20), (30, 40), (10, 20)}  # Duplicate tuples will be removed

print("\nUnique tuples in the set:", tuple_set)

# Checking hash value of a tuple
print("\nHash of t1:", hash(t1))
print("Hash of t2:", hash(t2))

# Tuples with mutable elements (unhashable)
# t3 = ([1, 2], 3)  # This will raise an error: TypeError: unhashable type: 'list'
