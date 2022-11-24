import re

def reg_match(regex_string, text_string, x):
    result = re.findall(regex_string,text_string,flags=re.IGNORECASE)
    print(result)
    final_list = []    
    for item in result:
        if len(item) == x:
            final_list.append(item)
    return final_list


print(reg_match("\d", "dogs dog dog 1 4 0 1 was encoded by six bits, called B,A", 1))