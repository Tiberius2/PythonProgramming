firstString = str(input("Input first String: "))
secondString = str(input("Input the second String: "))


# Aici am gasit o functie ce rezolva direct 

countOccurences = firstString.count(secondString)

print("Occurence of the word ' " + secondString + " ' in the first string is : " + str(countOccurences))