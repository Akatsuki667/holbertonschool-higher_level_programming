# Python - Hello, World

## 0. Hello, print
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

### Objectives
- Use the function print.

### Expectation
```Python
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
```
### Result
```bash
"Programming is like building a multilingual puzzle
```

## 1. Print integer
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.
### Source code
```Python
#!/usr/bin/python3
number = 98
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
```

### Objectives

- The output of the script should be:
	- The number, followed by Battery street
	- Followed by a new line.
- You are not allowed to cast the variable number into a string.
- Your code must be 3 lines long.
- You have to use f-strings.

### Expectation
```Python
#!/usr/bin/python3
number = 98
print(f"{98} Battery street")
```
### Result
```bash
98 Battery street
```

## 2. Print float
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.
### Source code
```Python
#!/usr/bin/python3
number = 3.14159
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
```

### Objectives
- The output of the program should be:
	- Float: followed by the float with only 2 digits
	- Followed by a new line.
- You are not allowed to cast number to string.
- You have to use f-strings.

### Expectation
```Python
#!/usr/bin/python3
number = 3.14159
print(f"Float : {number:.2f}")
```
### Result
```bash
Float : 3.14
```

## 3. Print string
Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
### Source code
```Python
#!/usr/bin/python3
str = "Holberton School"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
```

### Objectives
- The output of the program should be:
	- 3 times the value of str.
	- Followed by a new line.
	- Followed by the 9 first characters of str.
	- Followed by a new line.
- You are not allowed to use any loops or conditional statement.
- Your program should be maximum 5 lines long.

### Expectation
```Python
#!/usr/bin/python3
str = "Holberton School"
print(f"{str * 3}")
print(str[:9])
```
### Result
```bash
Holberton SchoolHolberton SchoolHolberton School
Holberton
```

## 4. Play with strings
Complete this source code to print Welcome to Holberton School!
### Source code
```Python
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"Welcome to {str1}!")
```

### Objectives
- You are not allowed to use any loops or conditional statements.
- You have to use the variables str1 and str2 in your new line of code.
- Your program should be exactly 5 lines long.

### Expectation
```Python
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2
print(f"Welcome to {str1}!")
```

### Result
```bash
Welcome to Holberton School!
```

## 5. Copy - Cut - Paste
Complete this source code.
### Source code
```Python
#!/usr/bin/python3
word = "Holberton"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```

### Objectives
- You are not allowed to use any loops or conditional statements.
- Your program should be exactly 8 lines long.
- word_first_3 should contain the first 3 letters of the variable word.
- word_last_2 should contain the last 2 letters of the variable word.
- middle_word should contain the value of the variable word without the first and last letters.
