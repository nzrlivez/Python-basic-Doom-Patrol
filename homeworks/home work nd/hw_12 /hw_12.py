# 1. double_result
# This decorator function should return the result of another function multiplied by two

#
def add(a, b):
    return a + b


add(5, 5)  # 10


def double_result(num):
    def inner(method):
        def multiply_method(a, b):
            return method(a, b) * num
        return multiply_method
    return inner

@double_result(2)
def add(a, b):
    return a + b


print(add(5, 5))  # 20


# 2. only_odd_parameters

# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise, return the string "Please use only odd numbers!"

def only_odd_parameters(func):
    def inner(*args):
        for i in args:
            if i % 2 != 0:
                return func(*args)
            else:
                return "Please use only odd numbers!"

    return inner


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5))  # 10
print(add(4, 4))  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print(multiply(5, 5, 5, 5, 5))
print(multiply(1, 2, 3, 4, 5))


# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):

def logged(func):
    def inner(*args):
        result = func(*args)
        return result

    return inner
    # log function arguments and its return value


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(correct_type):
    def inner(func3):
        def wrapper(*args):
            if isinstance(args[0], correct_type):
                return func3(args[0])
            else:
                return f'Wrong Type: {type(args[0])}'
        return wrapper
    return inner


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function