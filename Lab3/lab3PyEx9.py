def exercise9(*positional_arguments, **keyword_arguments):
    counter = 0
    for x in keyword_arguments:
        if keyword_arguments[x] in positional_arguments: # for every item in keyword_arguments, check wether the item value is in the list of positional arguments , if it is, the increment the counter 
            counter += 1 
    return counter


print (exercise9(1, 2,3, 4, x=1, y=2, z=3, w=5))


