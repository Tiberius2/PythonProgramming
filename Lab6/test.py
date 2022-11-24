import os
import re

def cenzurare(string):
    myList = re.findall(r'\b[aeiou]+\w*[aeiou]+\b',string,flags=re.IGNORECASE)
    print(string)
    res = string.split()
    result_list =[]
    for word in myList:
        if word in res:
            position = res.index(word)
            for i in range(0,len(word), 2):
                word = word[:i] + "*" + word[i+1:]
            result_list.append(word)
            res[position] = word
    return " ".join(res)

print(cenzurare("Ana cu alune duce ata la elefanti"))