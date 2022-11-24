import re
# re.findall -- pattern(in regex), the string in which to look for the pattern and the flag set to ignorecase
# re.IGNORECASE	Perform case-insensitive matching
def extract(text):
    print("Original string is: " + text)
    print("The list of extracted words is : ")
    result = re.findall("[a-z0-9]\+",text,flags=re.IGNORECASE)
    return result

print(extract("Each alphanumeric character in the 1401 was encoded by six bits, called B,A,8,4,2,1"))

