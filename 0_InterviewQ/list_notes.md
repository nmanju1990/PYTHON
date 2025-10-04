# Python List Notes

Comprehensive **Python List** reference — ideal for interview preparation and GitHub markdown storage.

---

## 1. What is a List?

A **list** in Python is an **ordered**, **mutable**, and **heterogeneous** collection that stores elements in sequence.

```python
fruits = ["apple", "banana", "cherry"]
```

* **Ordered**: preserves insertion order.
* **Mutable**: elements can be changed.
* **Heterogeneous**: can store mixed data types.

---

## 2. Creating Lists

```python
# Literal syntax
nums = [1, 2, 3]

# Using list() constructor
letters = list(('a', 'b', 'c'))

# Empty list
empty = []

# List from range
nums = list(range(5))  # [0, 1, 2, 3, 4]
```

---

## 3. Accessing Elements

```python
items = ['a', 'b', 'c', 'd']
print(items[0])   # a
print(items[-1])  # d (last element)
```

* Indexing starts at **0**.
* Negative indices access elements from the **end**.

---

## 4. Slicing

```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])   # [1, 2, 3]
print(nums[:3])    # [0, 1, 2]
print(nums[::2])   # [0, 2, 4]
print(nums[::-1])  # reverse list
```

---

## 5. Adding and Removing Elements

```python
nums = [1, 2, 3]

# Add
nums.append(4)       # [1, 2, 3, 4]
nums.insert(1, 5)    # [1, 5, 2, 3, 4]
nums.extend([6, 7])  # [1, 5, 2, 3, 4, 6, 7]

# Remove
nums.remove(5)       # remove first occurrence of value
nums.pop()           # removes and returns last element
nums.pop(2)          # removes at index 2
del nums[0]          # delete specific index
nums.clear()         # remove all elements
```

---

## 6. Searching and Counting

```python
nums = [1, 2, 3, 2, 4]
print(nums.index(2))  # 1 (first occurrence)
print(nums.count(2))  # 2 (occurrences)
```

---

## 7. Sorting and Reversing

```python
nums = [4, 1, 3, 2]
nums.sort()                 # [1, 2, 3, 4]
nums.sort(reverse=True)     # [4, 3, 2, 1]

# Custom sort
words = ["apple", "banana", "cherry"]
words.sort(key=len)         # by length

# Sorted without modifying original
sorted_nums = sorted(nums)

# Reverse order
nums.reverse()              # modifies in place
```

---

## 8. Copying Lists

```python
list1 = [1, 2, 3]
list2 = list1.copy()  # shallow copy
list3 = list1[:]      # slicing copy
```

> ⚠️ Assignment (`list2 = list1`) copies the **reference**, not the data.

---

## 9. Combining Lists

```python
a = [1, 2]
b = [3, 4]
combined = a + b        # concatenation
repeated = a * 2        # repetition → [1, 2, 1, 2]
```

---

## 10. Iterating Through Lists

```python
nums = [10, 20, 30]

# By value
for n in nums:
    print(n)

# By index
for i in range(len(nums)):
    print(i, nums[i])

# Enumerate
for i, n in enumerate(nums):
    print(i, n)
```

---

## 11. List Comprehensions

A concise way to create or transform lists.

```python
# Squares
squares = [x*x for x in range(5)]

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]

# Nested loop comprehension
pairs = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]
```

---

## 12. Useful Built-in Functions

| Function                | Description                     |
| ----------------------- | ------------------------------- |
| `len(lst)`              | Returns number of elements      |
| `sum(lst)`              | Sums all elements               |
| `min(lst)` / `max(lst)` | Smallest / largest element      |
| `sorted(lst)`           | Returns sorted copy             |
| `reversed(lst)`         | Returns reversed iterator       |
| `any(lst)`              | True if any element is truthy   |
| `all(lst)`              | True if all elements are truthy |

---

## 13. Nested Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # 6

# Flatten nested list
flat = [num for row in matrix for num in row]
```

---

## 14. Common Interview Questions

1. **Reverse a list** without using built-in functions.
2. **Find duplicates** in a list.
3. **Rotate a list** by `k` positions.
4. **Find second largest** element.
5. **Flatten a nested list**.
6. **Pair sum** problems using two-pointer technique.

---

## 15. Example: Find Duplicates

```python
def find_duplicates(nums):
    seen = set()
    dup = set()
    for n in nums:
        if n in seen:
            dup.add(n)
        else:
            seen.add(n)
    return list(dup)
```

---

## 16. Time Complexity (Common Ops)

| Operation                | Average Complexity |
| ------------------------ | ------------------ |
| Index access             | O(1)               |
| Append                   | O(1)               |
| Insert / Delete (middle) | O(n)               |
| Search                   | O(n)               |
| Slice copy               | O(k)               |
| Sort                     | O(n log n)         |

---

## 17. Key Takeaways

* Lists are **dynamic arrays**.
* Average O(1) append, O(n) insert/delete.
* Use **list comprehensions** for concise transformations.
* Avoid modifying a list while iterating over it.
* For heavy numerical ops → use **NumPy arrays** for performance.

---

## 18. Quick Reference

```python
lst.append(x)     # Add one item
lst.extend(L)     # Add multiple
lst.insert(i, x)  # Insert at index
del lst[i]        # Delete by index
x in lst          # Membership test
lst.sort()        # Sort in place
lst.reverse()     # Reverse in place
```

---

**Tip:** Practice list manipulation problems on LeetCode — *Two Sum*, *Rotate Array*, *Move Zeroes*, *Merge Sorted Lists*, etc.








🧠 Difference Between Shallow Copy and Deep Copy in Python
1. Shallow Copy

Creates a new object, but references the elements of the original object.

If the original object contains mutable nested objects (like lists inside lists), both copies share those inner objects.

import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]]  ← inner list changed in both


➡️ Changes in nested objects reflect in the original, because only the top-level container was copied.

2. Deep Copy

Creates a new object and recursively copies all nested objects.

The new object is completely independent of the original.

import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 99
print(original)  # [[1, 2], [3, 4]]  ← unchanged


➡️ Changes in nested structures do not affect the original.