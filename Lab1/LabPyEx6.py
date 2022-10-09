# Write a function that validates if a number is a palindrome
#  Ex : 16461 



n = int(input("Plase enter the number: "))

def check_palindrome(n):
    temp = n
    rev = 0
    while (n > 0):
        digit = n%10
        rev = rev*10+digit
        n = n//10
    if temp == rev :
        print("Your number is a palindrome!")
    else :
        print(" Your number is NOT a palindrome! ")
        

check_palindrome(n)