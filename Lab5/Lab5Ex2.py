def simple_function(*args, **kwargs):
    sum = 0
    for key in kwargs.keys():
        x = int(kwargs[key])
        sum = sum + x
    return sum

anonymous_function = lambda *args, **kwargs: sum([value for value in kwargs.values()])

print(simple_function(1, 2, c=3, d=4))
print(anonymous_function(1, 2, c=3, d=4))
