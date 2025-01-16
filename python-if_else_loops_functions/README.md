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
    print("{:02d}, ".format(i), end="")
```
### Result
```bash
00, 01, 02, 03, 04, 05...96, 97, 98, 99, %
```
