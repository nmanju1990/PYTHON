print("hello")

# Simple list program in Python

# create a list
fruits = ["apple", "banana", "cherry"]

# print the list
print("1 print the full list - Fruits:", fruits)

# add an item
fruits.append("orange")
print("2 After adding:", fruits)

# remove an item
fruits.remove("banana")
print("3 After removing:", fruits)

# access an item
print("4 First fruit:", fruits[0])

# loop through list
print("All fruits:")
for fruit in fruits:
    print(fruit)
