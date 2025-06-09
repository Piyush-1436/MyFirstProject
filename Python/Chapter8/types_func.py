# -------------------------------
# 📘 FUNCTIONS IN PYTHON (NOTES)
# -------------------------------

# ✅ What is a Function?
# A function is a reusable block of code that performs a specific task.

# ✅ Syntax of a Function:
# def function_name(parameters):
#     # code block
#     return value  # (optional)

# ✅ 1. Function with No Arguments and No Return
def greet():
    print("Hello, welcome to Python!")

greet()  # Calling the function

# ✅ 2. Function with Arguments but No Return
def welcome(name):
    print("Hello", name)

welcome("Piyush")

# ✅ 3. Function with Arguments and Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)

# ✅ 4. Function with Default Arguments
def multiply(a, b=2):
    return a * b

print("Multiply with default:", multiply(5))       # uses default b=2
print("Multiply with both:", multiply(5, 4))       # b=4

# ✅ 5. Function with Keyword Arguments
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info(age=18, name="Piyush")  # keyword arguments (order doesn't matter)

# ✅ 6. Function with Variable-Length Arguments
# *args → multiple positional arguments
def total_sum(*args):
    print("Arguments received:", args)
    return sum(args)

print("Total Sum:", total_sum(1, 2, 3, 4, 5))

# **kwargs → multiple keyword arguments
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="Piyush", course="Python", age=18)

# ✅ 7. Recursive Function
# A function that calls itself
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# ✅ Notes:
# - Use return to send values back from a function.
# - Use parameters inside the function, arguments outside when calling it.
# - Use def keyword to define a function.
# - 1) Built-in functions like print(),len(),range().
# - 2) User-defined functions are written by any user.