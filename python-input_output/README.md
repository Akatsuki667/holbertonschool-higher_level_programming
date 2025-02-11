# Python - Input/Output

## 0. Read file
Write a function that reads a text file (`UTF8`) and prints it to stdout:

### Objectives
- Prototype: `def read_file(filename=""):`
- You must use the `with` statement
- You don’t need to manage `file permission` or `file doesn't exist` exceptions.
- You are not allowed to import any module
### Expectation
```python3
#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        contenu = f.read()
        print(contenu, end="")
```
### Result
```bash
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers.

A school every software engineer would have dreamt of!%                                                                       
```

## 1. Write to a file
Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:

### Objectives
- Prototype: `def write_file(filename="", text=""):`
- You must use the `with` statement
- You don’t need to manage file permission exceptions.
- Your function should create the file if doesn’t exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3

def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
```
### Result
```bash
24
```

## 2. Append to a file
Write a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:

### Objectives
- Prototype: `def append_write(filename="", text=""):`
- If the file doesn’t exist, it should be created
- You must use the `with` statement
- You don’t need to manage `file permission` or `file doesn't exist` exceptions.
- You are not allowed to import any module

### Expectation
```python3
#!/usr/bin/python3

def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        f.write("\n" + text)
        return len(text)
```
### Result
```bash
24
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```

##
### Objectives
### Expectation
```python3
```
### Result
```bash
```