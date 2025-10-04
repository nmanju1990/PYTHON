# Python String Notes

Comprehensive **Python String** notes for interview preparation — Markdown-ready for GitHub.

---

## 1. What is a String?

A **string** in Python is an **immutable sequence** of Unicode characters.

```python
s = "Hello, World!"
```

* Strings are **immutable** — once created, they cannot be changed.
* Can contain letters, digits, symbols, and spaces.

---

## 2. Creating Strings

```python
s1 = 'Hello'
s2 = "World"
s3 = '''Multiline
String'''
```

* Use **single ('')**, **double ("")**, or **triple quotes (''' or """)** for multiline strings.

---

## 3. Accessing Characters

```python
s = "Python"
print(s[0])    # P
print(s[-1])   # n (last character)
```

* Strings support **indexing** and **slicing** like lists.

```python
print(s[1:4])   # yth
print(s[::-1])  # reversed string
```

---

## 4. String Immutability

Strings **cannot be changed** after creation.

```python
s = "Hello"
# s[0] = 'h'  ❌ TypeError

# You must create a new string
s = 'h' + s[1:]
print(s)  # hello
```

---

## 5. String Concatenation and Repetition

```python
a = "Hello"
b = "World"
print(a + b)   # HelloWorld
print(a * 3)   # HelloHelloHello
```

---

## 6. String Methods

| Method                                        | Description                      |
| --------------------------------------------- | -------------------------------- |
| `s.lower()`                                   | Convert to lowercase             |
| `s.upper()`                                   | Convert to uppercase             |
| `s.title()`                                   | Capitalize each word             |
| `s.capitalize()`                              | Capitalize first letter          |
| `s.strip()`                                   | Remove whitespace from both ends |
| `s.lstrip()` / `s.rstrip()`                   | Remove left/right spaces         |
| `s.replace(old, new)`                         | Replace substring                |
| `s.split(sep)`                                | Split string into list           |
| `sep.join(list)`                              | Join list into string            |
| `s.find(sub)` / `s.index(sub)`                | Find substring position          |
| `s.startswith(prefix)` / `s.endswith(suffix)` | Check start/end                  |
| `s.count(sub)`                                | Count occurrences                |
| `s.isdigit()` / `s.isalpha()` / `s.isalnum()` | Character tests                  |

Example:

```python
s = "  Python Basics  "
print(s.strip())       # 'Python Basics'
print(s.upper())       # '  PYTHON BASICS  '
print(s.replace('Python', 'Java'))  # '  Java Basics  '
```

---

## 7. String Formatting

### f-Strings (Python 3.6+)

```python
name = "Alice"
age = 25
print(f"My name is {name}, I am {age} years old.")
```

### format()

```python
print("My name is {} and I am {}.".format(name, age))
print("{0} is {1} years old.".format(name, age))
```

### % Formatting

```python
print("My name is %s and I am %d years old." % (name, age))
```

---

## 8. Escape Sequences

| Sequence | Meaning      |
| -------- | ------------ |
| `\n`     | Newline      |
| `\t`     | Tab          |
| `\'`     | Single quote |
| `\"`     | Double quote |
| `\\`     | Backslash    |

Example:

```python
print('Hello\nWorld')  # New line
```

---

## 9. String Slicing Examples

```python
s = "Interview"
print(s[:5])   # Inter
print(s[5:])   # view
print(s[::-1]) # weivretnI
```

---

## 10. Checking Substrings

```python
s = "python programming"
print('python' in s)   # True
print('java' not in s) # True
```

---

## 11. Useful Built-in Functions

| Function            | Description                                    |
| ------------------- | ---------------------------------------------- |
| `len(s)`            | Length of string                               |
| `min(s)` / `max(s)` | Smallest/largest character (lexicographically) |
| `sorted(s)`         | Returns sorted list of characters              |
| `reversed(s)`       | Returns reversed iterator                      |

Example:

```python
s = "abc"
print(sorted(s))  # ['a', 'b', 'c']
```

---

## 12. Raw Strings

Used to avoid escaping backslashes.

```python
path = r"C:\\Users\\Admin"
print(path)  # C:\Users\Admin
```

---

## 13. String Iteration

```python
for ch in "abc":
    print(ch)
```

---

## 14. Common Interview Questions

1. Reverse a string without using slicing.
2. Check if a string is a palindrome.
3. Count vowels and consonants.
4. Find the first non-repeating character.
5. Remove duplicates while preserving order.
6. Find all substrings of a string.

---

## 15. Example: Palindrome Check

```python
def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]

print(is_palindrome('Racecar'))  # True
```

---

## 16. Performance Tips

* Strings are **immutable** → concatenation in loops is costly.
* Use `''.join(list_of_strings)` for efficient concatenation.

```python
# Inefficient
s = ''
for i in range(1000):
    s += str(i)

# Efficient
s = ''.join(str(i) for i in range(1000))
```

---

## 17. Summary Table

| Concept          | Description                  |
| ---------------- | ---------------------------- |
| Mutable          | ❌ Immutable                  |
| Indexing/Slicing | ✅ Supported                  |
| Concatenation    | `+`, `join()`                |
| Formatting       | `f-string`, `.format()`, `%` |
| Performance      | Avoid repeated concatenation |
| Type             | Sequence (str)               |

---

## 18. Key Takeaways

* Strings are immutab
