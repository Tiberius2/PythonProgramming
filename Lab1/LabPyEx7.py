# There are two ways to do this. First and easiest one would be using regular expressions by importing re

# -----------

# import re
# string = str(input("Please input your sentence: "))

# print(re.search(r'\d+', string).group())


# The other, more meticulous way would be

# ----------- 



string = str(input("Please input your sentence: "))

number_string = ''

for x in range(len(string)):
    if string[x] >= '0' and string[x] <= '9' :
        number_string = number_string + string[x]
        print (string[x+1])
        if string[x+1].isalpha():   # verificam daca urmatorul caracter din acest sir de caractere este o litera din alfabet sau nu
            break 

print(number_string)
