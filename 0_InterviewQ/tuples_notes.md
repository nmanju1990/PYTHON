# Python Tuple Notes

Comprehensive **Python Tuple** notes for interview preparation — Markdown-ready for GitHub.

---

## 1. What is a Tuple?

A **tuple** in Python is an **ordered**, **immutable**, and **heterogeneous** collection of elements.

```python
t = (1, 2, 3)
```

* **Ordered** → preserves insertion order.
* **Immutable** → cannot be modified after creation.
* **Heterogeneous** → can store different data types.

---

## 2. Creating Tuples

```python
# Using parentheses
t = (1, 2, 3)

# Without parentheses (tuple packing)
t = 1, 2, 3

# Empty tuple
empty = ()

# Single element tuple — add a comma!
one = (5,)  # not (5)

# Using tuple() constructor
t = tuple([1, 2, 3])
```

---

## 3. Accessing Elements

```python
t = (10, 20, 30, 40)
print(t[0])    # 10
print(t[-1])   # 40
```

* Tuples support **indexing** and **slicing** just like lists.

```python
print(t[1:3])  # (20, 30)
```

---

## 4. Immutability

Tuples cannot be modified (no append, remove, etc.):

```python
t = (1, 2, 3)
# t[0] = 9  # ❌ TypeError
```

However, if a tuple contains a **mutable object** (like a list), that inner object can be changed:

```python
t = (1, [2, 3], 4)
t[1][0] = 99
print(t)  # (1, [99, 3], 4)
```

---

## 5. Tuple Operations

```python
t1 = (1, 2)
t2 = (3, 4)

# Concatenation
t3 = t1 + t2  # (1, 2, 3, 4)

# Repetition
print(t1 * 2)  # (1, 2, 1, 2)

# Membership
print(2 in t1)  # True

# Length
print(len(t1))  # 2
```

---

## 6. Tuple Methods

| Method     | Description                              |
| ---------- | ---------------------------------------- |
| `count(x)` | Returns the number of occurrences of `x` |
| `index(x)` | Returns the first index of `x`           |

Example:

```python
t = (1, 2, 3, 2)
print(t.count(2))  # 2
print(t.index(3))  # 2
```

---

## 7. Tuple Unpacking

You can unpack tuples directly into variables:

```python
t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # 1 2 3
```

With variable-length unpacking:

```python
a, *b = (1, 2, 3, 4)
print(a)  # 1
print(b)  # [2, 3, 4]
```

---

## 8. Nested Tuples

Tuples can contain other tuples:

```python
nested = ((1, 2), (3, 4))
print(nested[1][0])  # 3
```

---

## 9. Converting Between Lists and Tuples

```python
nums = [1, 2, 3]
t = tuple(nums)   # list → tuple
lst = list(t)     # tuple → list
```

---

## 10. Tuple vs List

| Feature     | List                         | Tuple                  |
| ----------- | ---------------------------- | ---------------------- |
| Mutability  | Mutable                      | Immutable              |
| Syntax      | `[]`                         | `()`                   |
| Methods     | Many (`append`, `pop`, etc.) | Few (`count`, `index`) |
| Performance | Slower                       | Faster (less overhead) |
| Use Case    | Dynamic data                 | Fixed or constant data |

---

## 11. When to Use Tuples

* When data **should not change**.
* For **dictionary keys** (since they are hashable).
* When working with **fixed records** (e.g., database rows, coordinates).

---

## 12. Common Interview Questions

1. Difference between list and tuple.
2. Can tuples contain mutable objects?
3. How to use tuples as dictionary keys?
4. How to unpack nested tuples?
5. Performance advantages of tuples.

---

## 13. Example: Swap Two Variables

```python
a, b = 10, 20
a, b = b, a
print(a, b)  # 20 10
```

---

## 14. Memory and Performance

* Tuples are **memory efficient** and **faster** than lists.
* Used for data that doesn't need modification.

```python
import sys
lst = [1, 2, 3]
tpl = (1, 2, 3)
print(sys.getsizeof(lst), sys.getsizeof(tpl))  # tuple uses less memory
```

---

## 15. Key Takeaways

* Tuples are immutable sequences.
* Faster and more memory-efficient than lists.
* Suitable for fixed data or as dictionary keys.
* Support unpacking, slicing, and basic operations.

---

**Tip:** Practice tuple-related problems like *coordinate storage*, *multiple return values*, and *immutable data handling*.
