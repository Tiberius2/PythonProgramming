import math
 
def GcdOfArray(arr, idx):
    if idx == len(arr)-1:
        return arr[idx]
       
    a = arr[idx]
    b = GcdOfArray(arr,idx+1)
     
    return math.gcd(a, b)
 
v = [int(x) for x in input("Enter numbers here : ").split(" ")]
x = len(v)

print(GcdOfArray(v,0))