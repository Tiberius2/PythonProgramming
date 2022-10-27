
from typing import Iterable




def check_el(element):
    if isinstance(element, Iterable) and type(element) != str:  # if the given paramaeter/element is iterable and is not a string
        values = []
        if type(element) == dict:  # if the parameter is actually a dictionary, for every element in the dictionary, access the value of every key 
            for el in element.values():
                values += check_el(el) # recursively cover each element of the dictionary in the case the dict contains other dicts or lists or containers etc
        else:  # if the element is not a dictionary type but is iterable and is not a string
            for el in element: # for every element in this dict's element:  be it a list, a container , a set etc 
                values += check_el(el) # recursively cover each element of this list/container/set etc
        return values # this is a list of dict values which will be returned upon completion of recursive dict coverage
    return [element]


def dictCompare(first_dict, second_dict):
    # using operations learned at the logics for computer science class  :) (p ^ q)
    return list(set(check_el(first_dict)) ^ set(check_el(second_dict)))



x = dict(a=2,b=3,c=4)
y = dict(p=2,q=4,r=5)
print (dictCompare(x,y))