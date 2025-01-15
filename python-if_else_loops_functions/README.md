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