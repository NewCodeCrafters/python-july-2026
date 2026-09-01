# Python Data Types — A Beginner's Guide

Every value in Python has a **type**. The type tells Python what kind of data it is, and what you're allowed to do with it. Understanding data types is the foundation for everything else in Python.

You can always check a value's type with the built-in `type()` function:

```python
print(type(5))        # <class 'int'>
print(type("hello"))  # <class 'str'>
print(type(3.14))     # <class 'float'>
```

---

## 1. Integers (`int`)

Whole numbers — positive, negative, or zero. No decimal point.

```python
age = 25
temperature = -10
score = 0

print(type(age))   # <class 'int'>
print(age + 5)      # 30
print(age * 2)      # 50
```

**Things to try:**
```python
x = 10
y = 3

print(x + y)   # 13  -> addition
print(x - y)   # 7   -> subtraction
print(x * y)   # 30  -> multiplication
print(x / y)   # 3.333... -> division (always returns a float)
print(x // y)  # 3   -> floor division (drops the remainder)
print(x % y)   # 1   -> modulus (the remainder)
print(x ** y)  # 1000 -> exponent (x to the power of y)
```

---

## 2. Floats (`float`)

Numbers with a decimal point. Used when precision beyond whole numbers matters (money, measurements, percentages).

```python
price = 9.99
pi = 3.14159
temperature = -2.5

print(type(price))   # <class 'float'>
print(price * 3)     # 29.97
```

**Careful:** mixing an `int` and a `float` in a calculation always produces a `float`:

```python
result = 10 + 2.5
print(result)         # 12.5
print(type(result))   # <class 'float'>
```

---

## 3. Strings (`str`)

Text — always wrapped in quotes (single `' '` or double `" "`, both work the same).

```python
name = "Spider"
message = 'Hello, world!'

print(type(name))   # <class 'str'>
```

**Common string operations:**

```python
first = "Cyber"
second = "Security"

print(first + second)         # 'CyberSecurity' -> concatenation
print(first + " " + second)   # 'Cyber Security'
print(len(first))             # 5 -> length
print(first.upper())          # 'CYBER'
print(second.lower())         # 'security'
print(first[0])               # 'C' -> indexing (first character)
print(first[-1])              # 'r' -> last character
print(second[0:4])            # 'Secu' -> slicing
```

**f-strings** (the modern, recommended way to build strings with variables):

```python
username = "spiderxploit"
level = 5

print(f"User {username} is at level {level}")
# Output: User spiderxploit is at level 5
```

---

## 4. Booleans (`bool`)

Only two possible values: `True` or `False`. Used for conditions and logic.

```python
is_admin = True
is_locked = False

print(type(is_admin))   # <class 'bool'>
```

Booleans are usually the *result* of a comparison:

```python
x = 10
y = 20

print(x > y)     # False
print(x < y)     # True
print(x == y)    # False -> equality check (note: double equals!)
print(x != y)    # True -> not equal
```

Used in `if` statements:

```python
password_correct = True

if password_correct:
    print("Access granted")
else:
    print("Access denied")
```

---

## 5. Lists (`list`)

An **ordered**, **changeable** collection of items. Items can be different types, and duplicates are allowed. Written with square brackets `[ ]`.

```python
tools = ["nmap", "burpsuite", "wireshark"]

print(type(tools))   # <class 'list'>
print(tools[0])       # 'nmap' -> first item
print(tools[-1])      # 'wireshark' -> last item
print(len(tools))     # 3
```

**Modifying a list:**

```python
tools.append("metasploit")     # add to the end
print(tools)   # ['nmap', 'burpsuite', 'wireshark', 'metasploit']

tools.remove("burpsuite")      # remove a specific item
print(tools)   # ['nmap', 'wireshark', 'metasploit']

tools[0] = "rustscan"          # change an item by index
print(tools)   # ['rustscan', 'wireshark', 'metasploit']
```

**Looping through a list:**

```python
for tool in tools:
    print(f"Loading: {tool}")
```

Lists can hold mixed types too:

```python
mixed = ["Spider", 25, True, 3.14]
```

---

## 6. Tuples (`tuple`)

Like a list, but **unchangeable (immutable)** once created. Written with parentheses `( )`. Used when you want data that shouldn't be modified — e.g. coordinates, fixed settings.

```python
coordinates = (10.5, 20.3)

print(type(coordinates))   # <class 'tuple'>
print(coordinates[0])       # 10.5
```

```python
coordinates[0] = 5   # This will raise an error!
# TypeError: 'tuple' object does not support item assignment
```

Why use a tuple instead of a list? Because it signals "this data is fixed" and prevents accidental changes — and tuples are slightly faster than lists.

---

## 7. Dictionaries (`dict`)

A collection of **key-value pairs**. Instead of accessing items by position (like a list), you access them by a unique **key**. Written with curly braces `{ }`.

```python
user = {
    "username": "spiderxploit",
    "role": "admin",
    "active": True
}

print(type(user))          # <class 'dict'>
print(user["username"])    # 'spiderxploit'
print(user["role"])        # 'admin'
```

**Modifying a dictionary:**

```python
user["role"] = "superadmin"      # change a value
user["level"] = 10               # add a new key-value pair
print(user)
# {'username': 'spiderxploit', 'role': 'superadmin', 'active': True, 'level': 10}
```

**Looping through a dictionary:**

```python
for key, value in user.items():
    print(f"{key}: {value}")

# Output:
# username: spiderxploit
# role: superadmin
# active: True
# level: 10
```

---

## 8. Sets (`set`)

An **unordered** collection of **unique** items — duplicates are automatically removed. Written with curly braces `{ }` (like a dict, but no key-value pairs).

```python
ports = {22, 80, 443, 443, 80}

print(type(ports))   # <class 'set'>
print(ports)          # {80, 443, 22} -> duplicates removed, order not guaranteed
```

Sets are useful for removing duplicates or checking membership quickly:

```python
scanned_ips = {"192.168.1.1", "192.168.1.2"}

print("192.168.1.1" in scanned_ips)   # True -> fast membership check
scanned_ips.add("192.168.1.3")
print(scanned_ips)
```

---

## 9. NoneType (`None`)

Represents "nothing" or "no value yet." Often used as a placeholder before a variable gets a real value.

```python
result = None

print(type(result))   # <class 'NoneType'>

if result is None:
    print("No result yet")
```

---

## Quick Reference Table

| Type | Example | Mutable? | Ordered? | Notes |
|---|---|---|---|---|
| `int` | `42` | N/A | N/A | Whole numbers |
| `float` | `3.14` | N/A | N/A | Decimal numbers |
| `str` | `"hello"` | No | Yes | Text |
| `bool` | `True` | N/A | N/A | True/False only |
| `list` | `[1, 2, 3]` | Yes | Yes | Can change, allows duplicates |
| `tuple` | `(1, 2, 3)` | No | Yes | Fixed, can't change |
| `dict` | `{"a": 1}` | Yes | Yes (3.7+) | Key-value pairs |
| `set` | `{1, 2, 3}` | Yes | No | Unique items only |
| `NoneType` | `None` | N/A | N/A | Represents "nothing" |

---

## Practice Exercise

Try predicting the output before running this:

```python
# What type is each of these?
a = 100
b = 100.0
c = "100"
d = [100]
e = (100,)
f = {100}
g = {"value": 100}
h = True
i = None

for var in [a, b, c, d, e, f, g, h, i]:
    print(var, "->", type(var))
```

**Tip for students:** a common beginner mistake is confusing `(100)` (just the integer 100 in parentheses) with `(100,)` (a tuple with one item — the comma is what makes it a tuple).
