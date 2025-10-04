# Data-stuctures
Dictionary
         .combination of immutable mutable data type
         .it is an collection of elements data in the format of keys and values
            *keys are immutable
            *values are mutable
         .it is an un ordered data type.but sometimes it looks like ordered data type
         .keys should be unique
          .values can be duplicated
          .it is represented with curley brackets{}
mapping data type is dictionary
opeartions of dictionary
             .creation
             .accessing
             .insertion
             .updation
             .deletion
    creation:
               =>create an empty dictionary     
# Empty Dictionary
- x = {}
-print(x)
-print(type(x))
               =>create a dictionary with a single element:
# single element              
s = {10:100}
print(s)
print(type(s))
s2 = {10:45.67}
print(s2)
print(type(s2))
               =>create a dictionary with multiple element :
# dictionary creation with multiple elements               
x = {10:100,20:45.67,30:"Hello"}
print(x)
print(type(x))
y = {"name":"Sai Vardhan","Subject":"Python Full Stack"}
print(y)
print(type(y))               


               =>create a dictionary with user inputs:
# user input               
1 2 3 4
100 200 100 300
{1:100,2:200,3:100,4:300}

#Source Code

keys = list(map(int,input().split()))
values = list(map(int,input().split()))
d = dict(zip(keys,values))
print(d)
print(type(d))      




                  accessing dictionary:
   indexing
                           



               
               
                                                        

                                                                                             


## 📌 List
- what is list: 
    - Li
- What is deep copy & shallow copy    





## ------------------------------------------------------------------------------------------------------------
## 📌 Core Concepts

What are Python’s built-in data structures?
What’s the difference between a list and a tuple?
How does a set handle duplicate values?
What is the difference between shallow copy and deep copy in Python?
Explain the difference between mutable and immutable data structures in Python.

## 📌 Lists
How are lists implemented internally in Python?
What is list comprehension, and why is it more efficient?
How do you remove duplicates from a list while preserving order?
What is the difference between append() and extend() in lists?
How would you rotate a list in Python (e.g., move last element to the front)?

## 📌 Tuples

Why are tuples faster than lists?
Can a tuple contain mutable objects?
How do you use tuples as dictionary keys?
Explain packing and unpacking of tuples with examples.

## 📌 Dictionaries

How are Python dictionaries implemented internally?
What is hashing in Python dictionaries?
What happens if two keys hash to the same value?
Difference between dict.get() and dict[] access?
How do you merge two dictionaries in Python (pre and post Python 3.9)?
How do you sort a dictionary by keys or by values?

## 📌 Sets

What is the difference between set and frozenset?
How are sets implemented internally?
How do you perform set operations like union, intersection, and difference in Python?
What happens when you try to add a mutable object (like a list) to a set?
How would you remove duplicates from a list using a set?

## 📌 Advanced & Performance

Explain the time complexity of list, dict, and set operations.
Why is in faster in a set or dict compared to a list?
What are Python’s alternatives to built-in data structures (like collections module)?
What’s the difference between OrderedDict and normal dict (before and after Python 3.7)?
Explain deque and its advantages over lists.
What is the difference between heapq and queue.PriorityQueue?
How do you implement a stack and a queue in Python?
What is the difference between arrays from the array module and Python lists?
How do you implement a linked list in Python?
How do you detect and remove cycles in a linked list?

## 📌 Coding/Scenario-based

Given a list of numbers, find the top 3 frequent elements.
Implement a min stack (stack with getMin() in O(1)).
Check if two strings are anagrams using data structures.
Implement an LRU cache in Python.
Reverse a linked list in Python.