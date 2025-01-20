# Python - Data Structures: Lists, Tuples

## 0. Print a list of integers
Write a function that prints all integers of a list.

### Objectives
- Prototype: `def print_list_integer(my_list=[])`:
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers

### Expectation
```Python
#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for x in my_list:
        print("{}".format(x))
```
### Result
```bash
1
2
3
4
5
```

## 1. Secure access to an element in a list
Write a function that retrieves an element from a list.

### Objectives
- Prototype: `def element_at(my_list, idx)`:
- If `idx` is negative, the function should return `None`
- If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
- You are not allowed to import any module
- You are not allowed to use `try/except`

### Expectation
```Python
#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return my_list[idx]
```
### Result
```bash
Element at index 3 is 4
```

## 2. Replace element
Write a function that replaces an element of a list at a specific position.

### Objectives
- Prototype: `def replace_in_list(my_list, idx, element)`:
- If `idx` is negative, the function should not modify anything, and returns the original list
- If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
- You are not allowed to import any module
- You are not allowed to use `try/except`

### Expectation
```Python
#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
```
### Result
```bash
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
```

## 3. Print a list of integers... in reverse!
Write a function that prints all integers of a list, in reverse order.

### Objectives
- Prototype: `def print_reversed_list_integer(my_list=[])`:
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers

### Expectation
```Python
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for x in my_list[::-1]:
        print("{}".format(x))
```
### Result
```bash
5
4
3
2
1
```

## 4. Replace in a copy
Write a function that replaces an element in a list at a specific position without modifying the original list.

### Objectives
- Prototype: `def new_in_list(my_list, idx, element)`:
- If `idx` is negative, the function should return a copy of the original `list`
- If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`
- You are not allowed to import any module
- You are not allowed to use `try/except`

### Expectation
```Python
#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list.copy()
    elif idx > len(my_list):
        return my_list.copy()
    else:
        copy_list = my_list.copy()
        copy_list[idx] = element
        return copy_list
```
### Result
```bash
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
```

## 5. Can you C me now?
Write a function that removes all characters c and C from a string.

### Objectives
- Prototype: `def no_c(my_string)`:
- The function should return the new string
- You are not allowed to import any module
- You are not allowed to use `str.replace()`

### Expectation
```Python
#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for a in my_string:
        if a not in {'c', 'C'}:
            result += a
    return result
```
### Result
```bash
Best Shool
hiago
 is fun!
```

## 6. Lists of lists = Matrix
Write a function that prints a matrix of integers.

### Objectives
- Prototype: `def print_matrix_integer(matrix=[[]])`:
- Format: see example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers

### Expectation
```Python
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    j = 0
    for i in matrix:
        for j in i:
            print("{} ".format(j), end=" ")
        print("\n")
```
### Result
```bash
1 2 3$
4 5 6$
7 8 9$
--$
$
```

