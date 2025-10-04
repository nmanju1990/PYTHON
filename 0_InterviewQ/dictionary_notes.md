# Python Dictionary Notes

A concise Markdown reference for **Python Dictionaries**, ideal for interview prep or quick revision.

---

## 1. What is a Dictionary?

A **dictionary** in Python is an **unordered**, **mutable** collection that stores data as **key–value pairs**.

```python
student = {"name": "Alice", "age": 22, "course": "CS"}
```

* Keys must be **unique** and **immutable** (e.g., string, number, tuple).
* Values can be **any data type**.

---

## 2. Creating Dictionaries

```python
# Literal
person = {"name": "John", "age": 30}

# Using dict() constructor
data = dict(country="India", capital="Delhi")

# Empty dictionary
empty = {}
```

---

## 3. Accessing Values

```python
person = {"name": "John", "age": 30}
print(person["name"])       # John
print(person.get("age"))     # 30
print(person.get("city", "N/A"))  # returns default if key missing
```

### KeyError vs get()

* `person['city']` → ❌ raises error if key doesn’t exist
* `person.get('city')` → ✅ safe, returns `None` or default value

---

## 4. Adding / Updating / Removing Items

```python
# Add or update
person["city"] = "New York"

# Update multiple keys
person.update({"age": 31, "email": "john@example.com"})

# Remove key
person.pop("age")

# Remove last inserted item (Python 3.7+)
person.popitem()

# Delete specific key or entire dictionary
del person["city"]
# del person  # deletes entire dict

# Clear all items
person.clear()
```

---

## 5. Looping Through a Dictionary

```python
user = {"name": "Bob", "age": 25, "city": "Paris"}

# Keys
for k in user:
    print(k)

# Values
for v in user.values():
    print(v)

# Keys and Values
for k, v in user.items():
    print(k, v)
```

---

## 6. Dictionary Methods

| Method                      | Description                           |
| --------------------------- | ------------------------------------- |
| `dict.keys()`               | Returns view of all keys              |
| `dict.values()`             | Returns view of all values            |
| `dict.items()`              | Returns view of key-value pairs       |
| `dict.get(key, default)`    | Safe access                           |
| `dict.update(other_dict)`   | Merge/update values                   |
| `dict.pop(key[, default])`  | Remove key and return value           |
| `dict.popitem()`            | Remove last inserted pair             |
| `dict.clear()`              | Empty dictionary                      |
| `dict.copy()`               | Shallow copy                          |
| `dict.fromkeys(seq, value)` | Create new dict from sequence of keys |

---

## 7. Dictionary Comprehension

Powerful and concise way to create or transform dictionaries.

```python
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtering
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
```

---

## 8. Nested Dictionaries

```python
students = {
    101: {"name": "Alice", "grade": "A"},
    102: {"name": "Bob", "grade": "B"}
}

print(students[101]["name"])  # Alice
```

---

## 9. Useful Tricks

```python
# Merge two dicts (Python 3.9+)
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
merged = a | b       # {'x': 1, 'y': 3, 'z': 4}

# Check existence
if 'x' in a:
    print('key exists')

# Dictionary length
len(a)  # number of key-value pairs
```

---

## 10. Interview Tips

* **Hashing:** Dictionaries use **hash tables** internally → O(1) average lookup.
* **Mutability:** Keys must be immutable (e.g., str, tuple), values can change.
* **Order:** Since Python 3.7+, insertion order is preserved.
* **Copy vs Reference:** `copy()` makes a shallow copy; direct assignment shares reference.
* **Comprehension & Merging:** Know the modern merge syntax (`|`, `|=`) and comprehension pattern.

---

## 11. Example Practice Questions

1. Count frequency of elements in a list.
2. Invert a dictionary `{key: value} → {value: key}`.
3. Merge two dictionaries and sum values of common keys.
4. Find the most frequent word in a string.
5. Group items by a certain key from a list of dicts.

---

## 12. Example: Word Frequency

```python
text = "apple banana apple orange banana apple"
words = text.split()
count = {}
for w in words:
    count[w] = count.get(w, 0) + 1
print(count)  # {'apple': 3, 'banana': 2, 'orange': 1}
```

---

### ✅ Summary

| Concept       | Key Points                         |
| ------------- | ---------------------------------- |
| Creation      | `{}` or `dict()`                   |
| Access        | `[]`, `.get()`                     |
| Modify        | `update()`, `pop()`                |
| Iterate       | `.keys()`, `.values()`, `.items()` |
| Comprehension | `{k:v for ...}`                    |
| Performance   | Avg O(1) lookup/insertion          |
| Ordered       | Yes (since 3.7)                    |

---

**Tip:** Practice dictionary problems on LeetCode (e.g., *Two Sum*, *Group Anagrams*, *Top K Frequent Elements*).
