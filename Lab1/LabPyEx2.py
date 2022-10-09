
inputString = str(input("Please type a sentence: "))

print(inputString)


def countVowels(string):
    num_vowels = 0
    for char in string:
        if char in "aeiouAEIOU" : 
            num_vowels += 1
    return num_vowels

print("The number of vowels in the string is : " + str(countVowels(inputString)))