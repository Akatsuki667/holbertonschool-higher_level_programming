# Python - More Data Structures: Set, Dictionary

## 0. Squared simple
Write a function that computes the square value of all integers of a matrix.

### Objectives
- Prototype: `def square_matrix_simple(matrix=[]):`
- `matrix` is a 2 dimensional array
- Returns a new matrix:
	- Same size as `matrix`
	- Each value should be the square of the value of the input
- Initial matrix should not be modified
- You are not allowed to import any module
- You are allowed to use regular loops, `map`, etc.

### Expectation
```Python
```
### Result
```bash
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## 1. Search and replace
Write a function that replaces all occurrences of an element by another in a new list.

### Objectives
- Prototype: `def search_replace(my_list, search, replace):`
- `my_list` is the initial list
- `search` is the element to replace in the list
- `replace` is the new element
- You are not allowed to import any module

### Expectation
```Python
#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for idx, item in enumerate(my_list):
        if item == search:
            my_list[idx] = replace
    return my_list
```
### Result
```bash
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
```

## 2. Unique addition
Write a function that adds all unique integers in a list (only once for each integer).

### Objectives
- Prototype: `def uniq_add(my_list=[]):`
- You are not allowed to import any module

### Expectation
```Python
#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = sum(set(my_list))
    return new_list
```
### Result
```bash
Result: 15
```

## 3. Present in both
Write a function that returns a set of common elements in two sets.

### Objectives
- Prototype: `def common_elements(set_1, set_2):`
- You are not allowed to import any module

### Expectation
```Python
#!/usr/bin/python3
def common_elements(set_1, set_2):
    return set_1.intersection(set_2)
```
### Result
```bash
['C']
```

## 4. Only differents
Write a function that returns a set of all elements present in only one set.

### Objectives
- Prototype: `def only_diff_elements(set_1, set_2):`
- You are not allowed to import any module

### Expectation
```Python
#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return set_1.union(set_2)
```
### Result
```bash
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
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

##
### Objectives
### Expectation
```Python
```
### Result
```bash
```
