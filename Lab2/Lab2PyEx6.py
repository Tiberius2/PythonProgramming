# 6. Write a function that receives as a parameter a variable number of lists and a whole number x. 
# Return a list containing the items that appear exactly x times in the incoming lists. 

# def occurences_in_lists(*lists: list[int], x: int) -> list[int | None]:
#     resulting_list : list[int | None] = []

#     for lst in lists:
#         current_freq: dict[int, int] = {}
#         for item in lst:
#             try:
#                 current_freq[item] += 1
#             except KeyError:
#                 current_freq[item] = 1
#         for item in current_freq:
#             if current_freq[item] == x:
#                 resulting_list.append(item)
#                 break
#         else:
#             resulting_list.append(None)

#     return resulting_list

def occurences_in_lists(*lists: list, x: any) -> list:
    current_freq: dict[int, int] = {}
    for lst in lists:
        for item in lst:
            try:
                current_freq[item] += 1
            except KeyError:
                current_freq[item] = 1

    return [item for item in current_freq if current_freq[item] == x]


list1 = [1,2,2,3]
list2 = [1,2,3,4,6]
list3 = [2,3,3,4]
print(occurences_in_lists(list1,list2,list3, x=2))