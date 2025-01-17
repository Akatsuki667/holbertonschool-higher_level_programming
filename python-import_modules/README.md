# Python - import & modules

## 0. Import a simple function from a simple file
Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3.
### add_0.py
```Python
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)
```

### Objectives
- You have to use print function with string format to display integers.
- You have to assign:
	- the value 1 to a variable called a.
	- the value 2 to a variable called b.
	- and use those two variables as arguments when calling the functions add and print.
- a and b must be defined in 2 different lines: a = 1 and another b = 2.
- Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line.
- You can only use the word add_0 once in your code.
- You are not allowed to use * for importing or __import__.
- Your code should not be executed when imported - by using __import__, like the example below.

### Expectation
```Python
#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, add(a, b)))

```
### Result
```bash
1 + 2 = 3
```

## 1. My first toolbox!
Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.
### calculator_1.py
```Python
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)
```

### Objectives
- Do not use the function print (with string format to display integers) more than 4 times.
- You have to define:
    - the value 10 to a variable a
    - the value 5 to a variable b
    - and use those two variables only, as arguments when calling functions (including print)
- a and b must be defined in 2 different lines: a = 10 and another b = 5
- Your program should call each of the imported functions. See example below for format
- the word calculator_1 should be used only once in your file
- You are not allowed to use * for importing or __import__
- Your code should not be executed when imported

### Expectation
```Python
#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
```
### Result
```bash
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```

## 2. How to make a script dynamic!
Write a program that prints the number of and the list of its arguments.

### Objectives
- The output should be:
    - Number of argument(s) followed by `argument` (if number is one) or `arguments` (otherwise), followed by
    - `:` (or . if no arguments were passed) followed by
    - a new line, followed by (if at least one argument),
    - one line per argument:
        - the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
- Your code should not be executed when imported
- The number of elements of argv can be retrieved by using: len(argv)
- You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

### Expectation
```Python
#!/usr/bin/python3
import sys

if __name__ == "__main__":

    arg = len(sys.argv) - 1

    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg))
    for i in range(0, arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
```
### Result
```bash
➜  python-import_modules git:(main) ✗ ./2-args.py hello bonjour
2 arguments:
1: hello
2: bonjour
```

## 3. Infinite addition
Write a program that prints the result of the addition of all arguments.

### Objectives
- The output should be the result of the addition of all arguments, followed by a new line
- You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
- Your code should not be executed when imported

### Expectation
```Python
#!/usr/bin/python3
import sys

if __name__ == "__main__":

    result = 0
    for i in range(1, len(sys.argv)):
        result += int(sys.argv[i])
    print("{}".format(result))
```
### Result
```bash
➜  python-import_modules git:(main) ✗ ./3-infinite_add.py 3 3 33 
39
```

