def find_numbers(my_list):
    new_list = [num for num in my_list if isinstance(num, (int,float))]
    return new_list


print(find_numbers([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

