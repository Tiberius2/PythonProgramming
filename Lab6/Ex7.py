import re

def validate_CNP(string):
    return re.match(r"[0-8]\d\d(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])[0-4][0-8]\d{4}$",string) != None


print(validate_CNP("1870818340915"))