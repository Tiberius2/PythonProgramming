def print_arguments(function):
    def builtin_function(*args, **kwargs):
        print("Args and kwargs are : ")
        print(*args, **kwargs)
        return function(*args,**kwargs)
    return builtin_function


def multiply_output(function):
    def another_function(*args, **kwargs):
        return 2*function(*args, **kwargs)
    return another_function

def add_numbers(a, b):
    return a + b

augmented_add_numbers = print_arguments(add_numbers)

x = augmented_add_numbers(3, 4)  # this will print: Arguments are: (3, 4), {} and will return 7.

print(x)