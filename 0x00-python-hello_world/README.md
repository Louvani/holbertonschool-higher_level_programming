# 0x00. Python - Hello, World
## Learning Objectives
### General
- Why Python programming is awesome
- Who created Python
- Who is Guido van Rossum
- Where does the name ‘Python’ come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Holberton Python coding style and how to check your code with PEP 8

## Tasks

### 0. Run Python file

Write a Shell script that runs a Python script.
The Python file name will be saved in the environment variable $PYFILE

### 1. Run inline

Write a Shell script that runs Python code.
The Python code will be saved in the environment variable $PYCODE

### 2. Hello, print

Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

### 3. Print integer

Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

    * You can find the source code here (https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py)
    * The output of the script should be:
        * the number, followed by Battery street,
        * followed by a new line
    * You are not allowed to cast the variable number into a string
    * Your code must be 3 lines long
    * You have to use the new print numbers tips (with .format(...))


### 4. Print float

Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

###  5. Print string

Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

    You can find the source code here (https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py)

###  6. Play with strings

Complete this source code to print Welcome to Holberton School!

    * You can find the source code here https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py
    * You are not allowed to use any loops or conditional statements.
    * You have to use the variables str1 and str2 in your new line of code
    * Your program should be exactly 5 lines long

###  Copy - Cut - Paste

Complete this source code

    * You can find the source code here https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py
    * You are not allowed to use any loops or conditional statements
    * Your program should be exactly 8 lines long
    * word_first_3 should contain the first 3 letters of the variable word
    * word_last_2 should contain the last 2 letters of the variable word
    * middle_word should contain the value of the variable word without the first and last letters

###  8. Create a new sentence

Complete this source code to print object-oriented programming with Python, followed by a new line.
* 
    * You can find the source code here https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py
    * You are not allowed to use any loops or conditional statements
    * Your program should be exactly 5 lines long
    * You are not allowed to create new variables
    * You are not allowed to use string literals


###  Easter Egg

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

    * Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

###  10. Linked list cycle

Write a function in C that checks if a singly linked list has a cycle in it.

    Prototype: int check_cycle(listint_t *list);
    Return: 0 if there is no cycle, 1 if there is a cycle

Requirements:

    Only these functions are allowed: write, printf, putchar, puts, malloc, free

## Advanced tasks

###  11. Hello, write
Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

    * Use the function write from the sys module
    * You are not allowed to use print
    * Your script should print to stderr
    * Your script should exit with the status code 1
    * (Dora Korpar was a Holberton student in Cohort 0 of San Francisco)

###  12. Compile (not finished)
Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)
###  13. ByteCode -> Python #1
Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:\
|**** | **** | **** |
|---|--------|-------|
| 3 | 0 LOAD_CONST | 1 (98) |
|   | 3 LOAD_FAST  | 0 (a)  |
|   | 6 LOAD_FAST  | 1 (b)  |
|   | 9 BINARY_POWER |      |
|   | 10 BINARY_ADD  |      |
|   | 11 RETURN_VALUE|      |
`
