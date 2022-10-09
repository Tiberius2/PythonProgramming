
# We could use the bin() function to convert an int to its binary format

# number = int(input("Enter a number: "))

# print(bin(number))


# Or the hard way 

count = 0 

def DecimalToBinary(number):
    global count
    if number >= 1:
        DecimalToBinary(number // 2)
    if number % 2 == 1: 
        count +=1 
    print (number%2, end= '')
    


if __name__ == '__main__':
    decimal_number = int(input("Enter your number: "))
    DecimalToBinary(decimal_number)
    print()
    print(count)