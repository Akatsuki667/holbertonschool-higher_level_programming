# Python - Exceptions

## 0. Safe list printing
Write a function that prints x elements of a list.

### Objectives
- Prototype: `def safe_print_list(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- All elements must be printed on the same line followed by a new line.
- `x` represents the number of elements to print
- `x` can be bigger than the length of `my_list`
- Returns the real number of elements printed
- You have to use `try: / except:`
- You are not allowed to import any module
- You are not allowed to use `len()`

### Expectation
```Python
#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for idx in range(x):
        try:
            print("{}".format(my_list[idx]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
```
### Result
```bash
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
```

## 1. Safe printing of an integers list
Write a function that prints an integer with "{:d}".format().

### Objectives
- Prototype: `def safe_print_integer(value):`
- `value` can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns `True` if `value` has been correctly printed (it means the value is an integer)
- Otherwise, returns `False`
- You have to use `try: / except:`
- You have to use `"{:d}".format()` to print as integer
- You are not allowed to import any module
- You are not allowed to use `type()`

### Expectation
```Python
#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
```
### Result
```bash
89
-89
School is not an integer
```

## 2. Print and count integers
Write a function that prints the first x elements of a list and only integers.

### Objectives
- Prototype: `def safe_print_list_integers(my_list=[], x=0):`
- `my_list` can contain any type (integer, string, etc.)
- All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
- `x` represents the number of elements to access in `my_list`
- `x` can be bigger than the length of `my_list - if it’s the case, an exception is expected to occur
- Returns the real number of integers printed
- You have to use `try: / except:`
- You have to use `"{:d}".format()` to print an integer
- You are not allowed to import any module
- You are not allowed to use `len()`

### Expectation
```Python
#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for idx in range(x):
        try:
            "{:d}".format(my_list[idx])
            count += 1
        except IndexError:
            break
        except (ValueError, TypeError):
            continue
        else:
            print("{:d}".format(my_list[idx]), end="")
    print()
    return count
```
### Result
```bash
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "//2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
```

## 3. Integers division with debug
### Objectives
### Expectation
```Python
```
### Result
```bash
```

##
### Objectives
### Expectation
```Python
```
### Result
```bash
```

##
### Objectives
### Expectation
```Python
```
### Result
```bash
```

##
### Objectives
### Expectation
```Python
```
### Result
```bash
```