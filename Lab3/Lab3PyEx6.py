# 6. Write a function that receives as a parameter a list and returns a tuple (a, b), 
# representing the number of unique elements in the list, 
# and b representing the number of duplicate elements in the list (use sets to achieve this objective).

# a ---> unique number of elements in the list
# b ---> number of duplicate elements in the list

from collections import Counter


def exercise6(mylist):
    # return len(Counter(mylist).keys())
    #return len(set(mylist)),len(mylist) - len(set(mylist))

    a = len(set(mylist))
    b = 0
    for values in Counter(mylist).values():
            if values == 2:
                b +=1
    return a,b
    





mylist = [12,31,12,512,623,564,23,54,23,1,13,2,31,13]

print(exercise6(mylist))