# Types of errors in python 
# There are mainly three types of errors in python
# 1. Syntax Error
# 2. Logical Error
# 3. Runtime Error
# Let's discuss each of them one by one
# 1. Syntax Error:
# Syntax errors occur when the code you write does not conform to the rules of the Python programming language. These errors are detected by the Python interpreter before the program is run.
# Example of Syntax Error:
# print("Hello World"  # Missing closing parenthesis
# 2. Logical Error:
# Logical errors occur when the code runs without crashing, but produces incorrect results. These errors are
# often the most difficult to detect and fix because the program does not provide any error messages.
# Example of Logical Error:
# def add_numbers(a, b):
#     return a - b  # Incorrect operation, should be addition
# result = add_numbers(5, 3)
# print(result)  # Output will be 2 instead of 8
# 3. Runtime Error:
# Runtime errors occur while the program is running. These errors can be caused by various factors, such as invalid input, resource limitations, or other unexpected conditions.
# Example of Runtime Error:
# num = int(input("Enter a number: "))
# result = 10 / num  # This will raise a ZeroDivisionError if num is 0
# print(result)

