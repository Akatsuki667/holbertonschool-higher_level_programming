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
    new_list = my_list.copy()
    for idx, item in enumerate(new_list):
        if item == search:
            new_list[idx] = replace
    return new_list
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
    return set_1.symmetric_difference(set_2)
```
### Result
```bash
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
```

## 5. Number of keys
Write a function that returns the number of keys in a dictionary.

### Objectives
- Prototype: `def number_keys(a_dictionary):`
- You are not allowed to import any module

### Expectation
```Python
#!/usr/bin/python3
def number_keys(a_dictionary):
    sum_of_keys = 0
    for key in a_dictionary:
        sum_of_keys += 1
    return sum_of_keys
```
### Result
```bash
Number of keys: 3
```

## 6. Print sorted dictionary
Write a function that prints a dictionary by ordered keys.

### Objectives
- Prototype: `def print_sorted_dictionary(a_dictionary):`
- You can assume that all keys are strings
- Keys should be sorted by alphabetic order
- Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
- Dictionary values can have any type
- You are not allowed to import any module

### Expectation
```Python
#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
```
### Result
```bash
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
```

## 7. Update dictionary
Write a function that replaces or adds key/value in a dictionary.

### Objectives
- Prototype: `def update_dictionary(a_dictionary, key, value):`
- `key` argument will be always a string
- `value` argument will be any type
- If a key exists in the dictionary, the value will be replaced
- If a key doesn’t exist in the dictionary, it will be created
- You are not allowed to import any module

### Expectation
```Python
```
### Result
```bash
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
```

## 8. Simple delete by key
Write a function that deletes a key in a dictionary.

### Objectives
- Prototype: `def simple_delete(a_dictionary, key=""):`
- `key` argument will be always a string
- If a key doesn’t exist, the dictionary won’t change
- You are not allowed to import any module

### Expectation
```Python
```
### Result
```bash
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
```

## 9. Multiply by 2
Write a function that returns a new dictionary with all values multiplied by 2.

### Objectives
- Prototype: `def multiply_by_2(a_dictionary):`
- You can assume that all values are only integers
- Returns a new dictionary
- You are not allowed to import any module

### Expectation
```Python
#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = {key: value * 2 for key, value in a_dictionary.items()}
    return b_dictionary
```
### Result
```bash
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
```
## 10. Best score
Write a function that returns a key with the biggest integer value.

### Objectives
- Prototype: `def best_score(a_dictionary):`
- You can assume that all values are only integers
- If no score found, return `None`
- You can assume all students have a different score
- You are not allowed to import any module

### Expectation
```Python
```
### Result
```bash
Best score: Molly
Best score: None
```

## 11. Multiply by using map
Write a function that returns a list with all values multiplied by a number without using any loops.

### Objectives
- Prototype: `def multiply_list_map(my_list=[], number=0):`
- Returns a new list:
    - Same length as `my_list`
    - Each value should be multiplied by `number`
- Initial list should not be modified
- You are not allowed to import any module
- You have to use `map`
- Your file should be max 3 lines

### Expectation
```Python
#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
```
### Result
```bash
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
```

## 12. Roman to Integer
Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.

### Objectives
- You can assume the number will be between 1 to 3999.
- `def roman_to_int(roman_string)` must return an integer
- If the `roman_string` is not a string or `None`, return 0

### Expectation
```Python
```
### Result
```bash
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
```
