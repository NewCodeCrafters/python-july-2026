# Python Functions & Built-in Modules — Exercise Workbook

**How to use this workbook**

- Part A builds function skills from scratch.
- Part B covers the standard library, one module at a time.
- Part C combines both into small projects.

Difficulty markers: 🟢 beginner · 🟡 intermediate · 🔴 stretch

Every exercise should be written as a **named function** with a docstring, unless stated otherwise. Trainees should test their work with the sample calls given.

---

# PART A — Functions

## A1. Defining and returning 🟢

1. Write `celsius_to_fahrenheit(celsius)` that returns the converted temperature.
   `celsius_to_fahrenheit(37)` → `98.6`

2. Write `is_even(number)` that returns `True` or `False`. Do not use an `if` statement.

3. Write `greet(name, greeting="Hello")` that returns `"Hello, Ada!"`.
   `greet("Ada")` → `"Hello, Ada!"`
   `greet("Ada", "Good morning")` → `"Good morning, Ada!"`

4. Write `rectangle_area(length, width)` and `rectangle_perimeter(length, width)`. Then write `describe_rectangle(length, width)` that calls both and returns a sentence.

5. **Spot the bug.** Why does this print `None`?
   ```python
   def double(n):
       print(n * 2)

   result = double(5)
   print(result)
   ```

## A2. Returning multiple values 🟢

6. Write `min_max_avg(numbers)` that returns a tuple of three values.
   `min_max_avg([4, 8, 15, 16, 23, 42])` → `(4, 42, 18.0)`

7. Write `split_name(full_name)` that returns `(first, last)`. Handle a single-word name by returning an empty string for the last name.

8. Write `divide(a, b)` that returns `(quotient, remainder)`. Return `None` if `b` is zero.

## A3. Default arguments and the mutable-default trap 🟡

9. Write `format_price(amount, currency="₦", decimals=2)` returning `"₦1,250.00"` for `format_price(1250)`.

10. **Predict the output**, run it, then explain the result:
    ```python
    def add_item(item, basket=[]):
        basket.append(item)
        return basket

    print(add_item("rice"))
    print(add_item("beans"))
    ```
    Now rewrite `add_item` so each call starts with a fresh basket unless one is passed in.

11. Write `make_tag(text, tag="p", **attributes)` that returns HTML:
    `make_tag("Hi", "a", href="/home")` → `'<a href="/home">Hi</a>'`

## A4. `*args` and `**kwargs` 🟡

12. Write `sum_all(*numbers)` that returns the total of any number of arguments. Return `0` when called with none.

13. Write `longest(*words)` returning the longest string. On a tie, return the first one.

14. Write `build_profile(first, last, **details)` returning a dictionary that includes the name plus every extra keyword.
    `build_profile("Ada", "Lovelace", field="maths", born=1815)`

15. Write `apply_to_all(func, *values)` that returns a list of `func` applied to each value.
    `apply_to_all(str.upper, "a", "b")` → `["A", "B"]`

16. 🔴 Write `merge_dicts(*dicts, **extras)` that merges every dictionary left to right, with `extras` winning any conflict.

## A5. Keyword-only and positional-only parameters 🔴

17. Rewrite `create_user(name, age, *, is_admin=False)` so `is_admin` **cannot** be passed positionally. Show the `TypeError` that results from trying.

18. Write `power(base, exponent, /)` using positional-only syntax and explain when this is useful.

## A6. Scope and closures 🟡

19. **Predict the output** and explain:
    ```python
    count = 0

    def increment():
        count = count + 1
        return count

    increment()
    ```
    Fix it two different ways: once with `global`, once by returning a value instead.

20. Write `make_counter(start=0)` that returns a *function*. Each call to the returned function increases the count by one and returns it.
    ```python
    tally = make_counter()
    tally()  # 1
    tally()  # 2
    ```

21. 🔴 Write `make_multiplier(factor)` returning a function that multiplies its argument by `factor`. Use it to build `double` and `triple`.

## A7. Lambdas and functional built-ins 🟡

22. Sort `[("Ada", 36), ("Bola", 24), ("Chidi", 41)]` by age, using `sorted` and a `lambda`.

23. Use `filter` and a lambda to keep only words longer than 4 characters from a list.

24. Use `map` to convert `["1", "2", "3"]` into integers, then `sum` them.

25. Sort a list of filenames by their extension, then by name, using a single `sorted` call.

26. 🔴 Rewrite exercises 22–24 using list comprehensions instead. Which version reads better, and why?

## A8. Recursion 🔴

27. Write `factorial(n)` recursively. Add a guard that raises `ValueError` for negatives.

28. Write `fibonacci(n)` recursively, then measure how slow it gets at `n = 35`. (You'll speed it up in Part B with `functools`.)

29. Write `flatten(nested_list)` that turns `[1, [2, [3, [4]]], 5]` into `[1, 2, 3, 4, 5]`.

30. Write `count_down(n)` that prints from `n` to 1 then prints `"Liftoff!"`.

## A9. Documentation and hints 🟢

31. Add type hints and a proper docstring to `min_max_avg` from exercise 6. Then print `min_max_avg.__doc__`.

32. Write `bmi(weight_kg: float, height_m: float) -> float` with a docstring containing an `Example:` section.

## A10. Decorators 🔴

33. Write a `logged` decorator that prints the function name and its arguments before calling it, then prints the return value.

34. Write a `repeat(times)` decorator factory so that `@repeat(3)` runs the decorated function three times.

35. Explain what `functools.wraps` fixes. Demonstrate by printing `__name__` with and without it.

---

# PART B — Built-in Modules

## B1. `math` 🟢

36. Write `hypotenuse(a, b)` using `math.sqrt`, then rewrite it with `math.hypot`.
37. Write `circle_stats(radius)` returning `(area, circumference)` rounded to 2 decimals, using `math.pi`.
38. Write `round_both_ways(n)` returning `(math.floor(n), math.ceil(n))`.
39. Why does `0.1 + 0.2 == 0.3` return `False`? Fix the comparison with `math.isclose`.
40. Use `math.gcd` and `math.lcm` to write `simplify_fraction(numerator, denominator)` returning a reduced tuple.

## B2. `random` 🟢

41. Write `roll_dice(sides=6, count=2)` returning a list of rolls.
42. Write `pick_winners(participants, n=3)` using `random.sample` — no duplicate winners.
43. Explain the difference between `random.choice`, `random.choices`, and `random.sample`. Give one example each.
44. Build a 52-card deck as a list of strings, shuffle it, and deal 5 cards.
45. Call `random.seed(42)` before generating numbers, run the script twice, and explain why the output is identical.

## B3. `datetime` 🟡

46. Print today's date formatted as `"Tuesday, 01 September 2026"`.
47. Write `days_until(target_date)` returning the number of days from today.
48. Write `calculate_age(birthdate)` returning age in whole years. Watch the birthday-not-yet-happened edge case.
49. Parse `"2026-09-01 14:30"` into a `datetime` with `strptime`, then add 90 minutes with `timedelta`.
50. Write `next_friday()` returning the date of the coming Friday.
51. 🔴 Write `business_days_between(start, end)` that excludes Saturdays and Sundays.

## B4. `os` and `pathlib` 🟡

52. Print the current working directory two ways: `os.getcwd()` and `Path.cwd()`.
53. Write `list_files(folder)` returning only files (not sub-folders).
54. Write `count_extensions(folder)` returning a dict like `{".py": 4, ".txt": 2}`.
55. Build a safe file path from `"data"`, `"reports"`, `"july.csv"` using `os.path.join`, then again with `Path`.
56. Write `ensure_folder(path)` that creates the folder only if it doesn't already exist.
57. Read an environment variable with `os.environ.get`, falling back to a default when it's missing.

## B5. `sys` 🟡

58. Print the Python version and the platform from `sys`.
59. Write a script that reads two numbers from `sys.argv` and prints their sum. Exit with a message if the arguments are missing.
60. Explain the difference between `sys.exit(0)` and `sys.exit(1)`.

## B6. `collections` 🟡

61. Use `Counter` to find the 3 most common words in a paragraph. Strip punctuation and ignore case.
62. Use `defaultdict(list)` to group names by their first letter.
63. Create a `namedtuple` called `Point` with `x` and `y`, then write `distance(p1, p2)`.
64. Use `deque` to build a `recent_searches` list that never holds more than 5 items.
65. 🔴 Compare `Counter` against a hand-written `dict` word-count loop. Which is clearer, and what does `Counter` give you for free?

## B7. `itertools` 🔴

66. Use `combinations` to list every pair of trainees from a group of 5.
67. Use `permutations` to count how many 3-letter arrangements `"abcd"` allows.
68. Use `groupby` to group a list of dictionaries by a `"department"` key. **Sort first** — explain why that's mandatory.
69. Use `accumulate` to turn `[10, 20, 30]` into a running total.
70. Use `chain` to flatten `[[1, 2], [3], [4, 5]]` into one sequence.
71. Use `islice` with `count` to produce the first 10 even numbers.

## B8. `json` 🟡

72. Save a dictionary of settings to `config.json` with `indent=2`.
73. Load it back and print one nested value.
74. Write `safe_load(path)` that returns `{}` if the file is missing or malformed. Catch the *specific* exceptions.
75. Convert a `datetime` to JSON. Explain the error you get, then fix it with a `default=` function.

## B9. `re` 🔴

76. Write `is_valid_email(text)` using `re.fullmatch`.
77. Extract every Nigerian phone number (`0801 234 5678`, `+234 801 234 5678`) from a block of text.
78. Use `re.sub` to redact all digits in a string, replacing them with `*`.
79. Use a named group to pull `day`, `month`, and `year` out of `"01/09/2026"`.
80. Explain the difference between `re.match`, `re.search`, and `re.findall` with one example each.

## B10. `statistics` 🟢

81. Given a list of test scores, print the mean, median, mode, and standard deviation.
82. Explain why `statistics.mode` raises an error on some datasets, and what `multimode` does instead.
83. Write `describe(numbers)` returning a dictionary of all four measures. Handle an empty list gracefully.

## B11. `string` 🟢

84. Print `string.ascii_letters`, `string.digits`, and `string.punctuation`.
85. Write `strip_punctuation(text)` using `str.translate` and `str.maketrans`.
86. Use `string.Template` to build a greeting from a dictionary of values.

## B12. `time` and `functools` 🔴

87. Write a `timer` decorator using `time.perf_counter` that reports how long a function takes.
88. Apply `functools.lru_cache` to the recursive `fibonacci` from exercise 28. Time it before and after.
89. Use `functools.reduce` to multiply every number in a list together.
90. Use `functools.partial` to create `double = partial(multiply, 2)` from a two-argument `multiply`.

## B13. `csv` 🟡

91. Write a list of dictionaries to `trainees.csv` using `csv.DictWriter`.
92. Read it back with `csv.DictReader` and print each row's name.
93. Explain why `newline=""` is passed to `open()` when working with CSV files.

---

# PART C — Mini Projects

Each project should be a single `.py` file, split into small functions, with an `if __name__ == "__main__":` block.

## C1. Contact Book 🟡
`json` · `os` · functions

- Store contacts as a list of dictionaries in `contacts.json`.
- Functions: `load_contacts()`, `save_contacts(contacts)`, `add_contact(name, phone, email)`, `find_contact(query)`, `delete_contact(name)`.
- Search should be case-insensitive and match partial names.
- The file must be created automatically on first run.

## C2. Log Analyser 🔴
`re` · `collections` · `datetime`

Given log lines like:
```
2026-09-01 08:14:22 ERROR Database connection failed
2026-09-01 08:14:25 INFO Retrying connection
```
- Parse each line into a dictionary with a real `datetime` object.
- Report counts per log level using `Counter`.
- Report the busiest hour.
- List every `ERROR` message in chronological order.

## C3. Password Toolkit 🟡
`random` · `string` · `re`

- `generate_password(length=12)` — must guarantee at least one lowercase, uppercase, digit, and symbol.
- `check_strength(password)` — returns `"weak"`, `"medium"`, or `"strong"` based on rules you define with `re`.
- `generate_passphrase(word_count=4)` — picks random words from a word list.

## C4. Quiz Game 🟡
`json` · `random` · `time` · functions

- Questions stored in `questions.json`.
- Shuffle the question order and the answer options.
- Time each answer; award bonus points for speed.
- Print a summary at the end: score, percentage, time taken, and which questions were missed.

## C5. Folder Report 🔴
`pathlib` · `collections` · `datetime` · `statistics`

Point the script at a folder and produce a report containing:
- Total number of files and total size in MB.
- A breakdown by file extension, sorted by count.
- The 5 largest files.
- The most recently modified file, with a human-readable timestamp.

---

# Discussion Questions

Use these to close each session.

1. When should something be a function versus repeated inline code?
2. What makes a good function name? Rewrite three badly named functions.
3. Why does Python ship with a "batteries included" standard library? Name three modules you'd otherwise have to write yourself.
4. What is the difference between `import math`, `from math import sqrt`, and `from math import *`? Why is the last one discouraged?
5. How do you find out what a module can do without leaving the terminal? (`dir()`, `help()`, `__doc__`)
6. A function has 8 parameters. What would you change, and why?