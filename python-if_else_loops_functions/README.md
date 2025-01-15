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

### Expectations
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