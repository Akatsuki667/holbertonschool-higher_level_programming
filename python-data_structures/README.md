# Python - Data Structures: Lists, Tuples

## 0. Print a list of integers
Write a function that prints all integers of a list.

### Objectives
- Prototype: `def print_list_integer(my_list=[]):`
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
        print("{:d}".format(x))
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
- Prototype: `def element_at(my_list, idx):`
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
    elif idx >= len(my_list):
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
- Prototype: `def replace_in_list(my_list, idx, element):`
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
    elif idx >= len(my_list):
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
- Prototype: `def print_reversed_list_integer(my_list=[]):`
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
        print("{:d}".format(x))
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
- Prototype: `def new_in_list(my_list, idx, element):`
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
    elif idx >= len(my_list):
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
- Prototype: `def no_c(my_string):`
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
- Prototype: `def print_matrix_integer(matrix=[[]]):`
- Format: see example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers

### Expectation
```Python
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        n = 0
        for j in i:
            if n == len(i) - 1:
                print("{:d}".format(j), end="")
                n += 1
            else:
                print("{:d}".format(j), end=" ")
                n += 1
        print()
```
### Result
```bash
1 2 3$
4 5 6$
7 8 9$
--$
$
```

## 7. Tuples addition
Write a function that adds 2 tuples.

### Objectives
- Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
- Returns a tuple with 2 integers:
- The first element should be the addition of the first element of each argument
- The second element should be the addition of the second element of each argument
- You are not allowed to import any module
- You can assume that the two tuples will only contain integers
- If a tuple is smaller than 2, use the value 0 for each missing integer
- If a tuple is bigger than 2, use only the first 2 integers

### Expectation
```Python
#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    a, b = tuple_a[:2]
    c, d = tuple_b[:2]

    new_tuple = (a + c, b + d)

    return new_tuple
```
### Result
```bash
(89, 100)
(2, 89)
(1, 89)
```

## 8. More returns!
Write a function that returns a tuple with the length of a string and its first character.

### Objectives
- Prototype: `def multiple_returns(sentence):`
- If the sentence is empty, the first character should be equal to `None`
- You are not allowed to import any module

### Expectation
```Python
#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        return (len(sentence), sentence[0])
    else:
        return (0, None)
```
### Result
```bash
Length: 22 - First character: A
```

## 9. Find the max
Write a function that finds the biggest integer of a list.

### Objectives
- Prototype: `def max_integer(my_list=[]):`
- If the list is empty, return `None`
- You can assume that the list only contains integers
- You are not allowed to import any module
- You are not allowed to use the builtin `max()`

### Expectation
```Python
#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    
    max = my_list[0]

    for i in my_list:
        if i > max:
            max = i
            
    return max
```
### Result
```bash
Max: 90
```

## 10. Only by 2
Write a function that finds all multiples of 2 in a list.

### Objectives
- Prototype: `def divisible_by_2(my_list=[]):`
- Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
- The new list should have the same size as the original list
- You are not allowed to import any module

### Expectation
```Python
#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    new_list = []

    for i in my_list:
        if i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list
```
### Result
```bash
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
```

## 11. Delete at
Write a function that deletes the item at a specific position in a list.

### Objectives
Prototype: `def delete_at(my_list=[], idx=0):`
If `idx` is negative or out of range, nothing change (returns the same list)
You are not allowed to use `pop()`
You are not allowed to import any module

### Expectation
```Python
#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
    return my_list
```
### Result
```bash
[1, 2, 3, 5]
[1, 2, 3, 5]
```

## 12. Switch
Complete the source code in order to switch value of a and b.

### Objectives
- You can find the source code here
- Your code should be inserted where the comment is (line 4)
- Your program should be exactly 5 lines long

### Expectation
```Python
#!/usr/bin/python3
a = 89
b = 10
b, a = a, b
print("a={:d} - b={:d}".format(a, b))
```
### Result
```bash
a=10 - b=89
```
