def sum_prod_pow(pairs):
    list_of_dicts = []
    for pair in pairs:
        my_dict = {"sum":[],"product":[],"power":[]}
        my_dict["sum"].append(pair[0]+pair[1])
        my_dict["product"].append(pair[0]*pair[1])
        my_dict["power"].append(pair[0] ** pair[1])
        list_of_dicts.append(my_dict)
    return list_of_dicts


print(sum_prod_pow(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)]))
