# 7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. 
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.


def isPalindrome(s):
    return s == s[::-1]


def function(my_list):
    nr_palindrom = []
    result : list[int | None] = []
    length = len(my_list)
    for i in range(length):
        if my_list[i]> 9:
            if isPalindrome(str(my_list[i])):
                nr_palindrom.append(my_list[i])
    result.append(len(nr_palindrom))
    result.append(max(nr_palindrom))
    return result

if __name__ == "__main__":
    lista = [121,12321,4234,6,7]
    print(function(lista))



