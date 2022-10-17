# Write a function to return a list of the first n numbers in the Fibonacci string.


def Fibonacci(n) :
    if n < 0 :
        print ("Wrong input")
    elif n == 0 :
        return 0
    elif n == 1 or n == 2 :
        return 1
    else :
        return Fibonacci(n-1) + Fibonacci(n-2)


n = int(input("First n number in the Fibonacci string you want to print : "))
list = []
for i in range(0, n) :
    list.append(Fibonacci(i))

print(list)
