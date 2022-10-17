# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

list_of_numbers = []

n = int(input("Enter number of elements : "))
  
for i in range(0, n):

    ele = int(input("Enter element: "))
  
    list_of_numbers.append(ele)
      
print(list_of_numbers)

prime_numbers = []

for i in list_of_numbers :
    c = 0
    for j in range(1,i) :
        if i%j == 0:
            c +=1
    if c == 1 :
        prime_numbers.append(i)

print (prime_numbers)
