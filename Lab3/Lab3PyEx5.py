def validate_dict(rules, dictionary):
    for d_key in dictionary:
        for tuple in rules:
            if d_key in tuple:
                if tuple[1] != "":  #if the first tuple is not an empty string
                    if dictionary[d_key].startswith(tuple[1]) == False:  # and the dict matches the tuple from the rules and starts with it, otherwise return false
                        return False
                if tuple[2] != "": # if the second tuple is not empty string
                    if dictionary[d_key].find(tuple[2]) == -1: # if we find the tuple in the dictionary[d_key] , we move forward, otherwise return false
                        return False
                    if dictionary[d_key].startswith(tuple[2]) and tuple[1] != "": # check if it starts with tuple[2] and tuple[1] is not empty string
                        return False
                    if dictionary[d_key].endswith(tuple[2]) and tuple[3] != "": # check if it ends with tuple[2] and tuple[3] is not empty string
                        return False
                if tuple[3] != "": # if third tuple is not empty string
                    if dictionary[d_key].endswith(tuple[3]) == False: #check if it ends with tuple[3] (suffix)
                        return False
            else:
                return False
    return True


rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionary = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}

print(validate_dict(rules,dictionary))