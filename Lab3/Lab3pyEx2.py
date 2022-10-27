# first we need to create the dictionary of the given string
def occurrencesDict(string):
    return {char: string.count(char) for char in string}  # return a set of key:value dict where key is the character in the character string and the value is the number of occurences in the string




string = "Eu invat programare Python"
print (occurrencesDict(string))