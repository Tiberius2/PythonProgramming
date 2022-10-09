import re

string_name  = str(input("Please input your sentence here : " ))

pattern = re.compile(r'(?<!^)(?=[A-Z])')

string_name = pattern.sub('_', string_name).lower()


print(string_name)

