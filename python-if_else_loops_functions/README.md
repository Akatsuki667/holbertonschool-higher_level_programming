# Python - if/else, loops, functions

## 0. Positive anything is better than negative nothing
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

### Source code
```Python
#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
```

### Objectives
- The variable number will store a different value every time you will run this program.
- You don’t have to understand what import, random. randint do. Please do not touch this code.
- The output of the program should be:
	- The number, followed by:
		- If the number is greater than 0: is positive.
		- If the number is 0: is zero.
		- If the number is less than 0: is negative.
	- Followed by a new line.

### Expectations
```Python
#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
```
### Result
```bash
➜  python-if_else_loops_functions git:(main) ✗ ./0-positive_or_negative.py
-9 is negative
➜  python-if_else_loops_functions git:(main) ✗ ./0-positive_or_negative.py
7 is positive
```

## 1. The last digit
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

### Source code
```Python
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
```

### Objectives
- The variable number will store a different value every time you will run this program.
- You don’t have to understand what import, random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000).
- The output of the program should be:
	- The string Last digit of, followed by
	- the number, followed by
	- the string is, followed by the last digit of number, followed by
		- if the last digit is greater than 5: the string and is greater than 5.
		- if the last digit is 0: the string and is 0.
		- if the last digit is less than 6 and not 0: the string and is less than 6 and not 0.
	- Followed by a new line.

### Expectation
```Python
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
str = "Last digit of"
if last_digit > 5:
    print(f"{str} {number} is {last_digit} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"{str} {number} is {last_digit} and is less than 6 and not 0")
else:
    print(f"{str} {number} is {last_digit} and is 0")
```
### Result
```bash
➜  python-if_else_loops_functions git:(main) ✗ ./1-last_digit.py
Last digit of 8251 is 1 and is less than 6 and not 0
➜  python-if_else_loops_functions git:(main) ✗ ./1-last_digit.py
Last digit of 2546 is 6 and is greater than 5
```

## 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

### Objectives
- Use only one print function with string format.
- Use only one loop in your code.
- You are not allowed to store characters in a variable.
- You are not allowed to import any module.

### Expectation
```Python
#!/usr/bin/python3
for a in range(97, 123):
    print("{}".format(chr(a)), end="")
```
### Result
```bash
abcdefghijklmnopqrstuvwxyz%
```

## 3. When I was having that alphabet soup, I never thought that it would pay off
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

### Objectives
- Print all the letters except q and e.
- You can only use one print function with string format.
- You can only use one loop in your code.
- You are not allowed to store characters in a variable.
- You are not allowed to import any module.

### Expectation
```Python
#!/usr/bin/python3
for a in range(97, 123):
    if chr(a) not in {'e', 'q'}:
        print("{}".format(chr(a)), end="")
```
### Result
```bash
abcdfghijklmnoprstuvwxyz%
```

## 4. Hexadecimal printing
Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example).

### Objectives
- You can only use one print function with string format.
- You can only use one loop in your code.
- You are not allowed to store numbers or strings in a variable.
- You are not allowed to import any module.

### Expectation
```Python
#!/usr/bin/python3
for i in range(99):
    print("{} = {}".format(i, hex(i)))

```
### Result
```bash
0 = 0x0
1 = 0x1
2 = 0x2
...
96 = 0x60
97 = 0x61
98 = 0x62
```

## 5. 00...99
Write a program that prints numbers from 0 to 99.

### Objectives
- Numbers must be separated by ,, followed by a space.
- Numbers should be printed in ascending order, with two digits.
- The last number should be followed by a new line.
- You can only use no more than 2 print functions with string format.
- You can only use one loop in your code.
- You are not allowed to store numbers or strings in a variable.
- You are not allowed to import any module.

### Expectation
```Python
#!/usr/bin/python3
for i in range(100):
    if i < 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
```
### Result
```bash
00, 01, 02, 03, 04, 05...96, 97, 98, 99
```

## 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
Write a program that prints all possible different combinations of two digits.

### Objectives
- Numbers must be separated by `,`, followed by a space.
- The two digits must be different.
- 01 and 10 are considered the same combination of the two digits 0 and 1.
- Print only the smallest combination of two digits.
- Numbers should be printed in ascending order, with two digits.
- The last number should be followed by a new line.
- You can only use no more than 3 print functions with string format.
- You can only use no more than 2 loops in your code.
- You are not allowed to store numbers or strings in a variable.
- You are not allowed to import any module.

### Expectation
```Python
#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
```
### Result
```bash
01, 02, 03, 04, 05,...69, 78, 79, 89
```

## 7. islower
Write a function that checks for lowercase character.

### Objectives
- Prototype: `def islower(c)`:
- Returns True if c is lowercase.
- Returns False otherwise.
- You are not allowed to import any module.
- You are not allowed to use str.upper() and str.isupper().
- Tips: ord().

### main.py
```Python
#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
```
### Expectation
```Python
#!/usr/bin/python3
def islower(c):
    conversion = ord(c)
    if conversion in range(97, 123):
        return True
    else:
        return False
```
### Result
```bash
a is lower
H is upper
A is upper
3 is upper
g is lower
```

## 8. To uppercase
Write a function that prints a string in uppercase followed by a new line.

### Objectives
- Prototype: `def uppercase(str)`:
- You can only use no more than 2 print functions with string format.
- You can only use one loop in your code.
- You are not allowed to import any module.
- You are not allowed to use str.upper() and str.isupper().
- Tips: ord().

### main.py
```Python
#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")
```
### Expectation
```Python
#!/usr/bin/python3
def uppercase(str):
    result = ""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            result += chr(ord(ch) - 32)
        else:
            result += ch
    print("{}".format(result))
```
### Result
```bash
BEST
BEST SCHOOL 98 BATTERY STREET
```

## 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
Write a function that prints the last digit of a number.

### Objectives
- Prototype: `def print_last_digit(number)`:
- Returns the value of the last digit
- You are not allowed to import any module

### main.py
```Python
#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
```
### Expectation
```Python
#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
```
### Result
```bash
8044
```

## 10. a + b
Write a function that adds two integers and returns the result.

### Objectives
- Prototype: `def add(a, b)`:
- Returns the value of a + b
- You are not allowed to import any module

### main.py
```Python
#!/usr/bin/env python3
add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))
```
### Expectation
```Python
#!/usr/bin/python3
def add(a, b):
    return a + b
```
### Result
```bash
3
98
98
```

## 11. a ^ b
Write a function that computes a to the power of b and return the value.

### Objectives
- Prototype: `def pow(a, b)`:
- Returns the value of a ^ b.
- You are not allowed to import any module.

### main.py
```Python
#!/usr/bin/env python3
pow = __import__('11-pow').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
```
### Expectation
```Python
#!/usr/bin/python3
def pow(a, b):
    return a ** b
```
### Result
```bash
4
9604
1
0.0001
-1024

```

## 12. Fizz Buzz
Write a function that prints the numbers from 1 to 100 separated by a space.

### Objectives
- For multiples of three print Fizz instead of the number and for multiples of five print Buzz.
- For numbers which are multiples of both three and five print FizzBuzz.
- Prototype: `def fizzbuzz()`:
- Each element should be followed by a space.
- You are not allowed to import any module.

### main.py
```Python
#!/usr/bin/env python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")
```
### Expectation
```Python
#!/usr/bin/python3
def fizzbuzz():
    for i in range(100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{}".format(i), end=" ")

```
### Result
```bash
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz 
```