def validate_dict(rules, dictionary):
    for d_key in dictionary:
        for tuple in rules:
            if d_key in tuple:
                if tuple[2] != "":
                    print (dictionary[d_key].find(tuple[2]))
                    















rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionary = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}

print(validate_dict(rules,dictionary))