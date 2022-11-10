def real_dicts(*args,**kwargs):
    dict_list = []
    # we iterate ovar the args

    for current_arg in args:
        if type(current_arg) == dict:
            if len(current_arg.keys()) >= 2:
                for arg_key in current_arg.keys():
                    if type(arg_key) == str and len(arg_key) >= 3:
                        dict_list.append(current_arg)

    #we iterate over the kwargs
    for current_kwarg in kwargs.keys():
        if type(kwargs[current_kwarg]) == dict:
            if len(kwargs[current_kwarg].keys()) >= 2:
                for kwarg_key in kwargs[current_kwarg].keys():
                    if type(kwarg_key) == str and len(kwarg_key) >=3:
                        dict_list.append(kwargs[current_kwarg])
    
    return dict_list

print(real_dicts({1: 2, 3: 4, 5: 6}, 
 {'a': 5, 'b': 7, 'c': 'e'}, 
 {2: 3}, 
 [1, 2, 3],
 {'abc': 4, 'def': 5},
 3764,
 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
 test={1: 1, 'test': True}))