# 3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
list_C = []
def intersection_of_lists(list_A,list_B) :
    global list_C
    list_C = [value for value in list_A if value in list_B]
    print(list_C)

def reunion_of_lists(list_A, list_B) :
    global list_C
    list_C = list_A + list_B
    print(list_C)

def remove_listB_from_listA(list_A, list_B):
    global list_C
    list_C = list(set(list_B).difference(set(list_A)))
    print(list_C)

def remove_listA_from_listB(list_A, list_B):
    global list_C
    list_C = list(set(list_A).difference(set(list_B)))
    print(list_C)



list_A = [int(x) for x in input("Enter elements of first list here: ").split(" ")]

list_B = [int(x) for x in input("Enter elements of second list here: ").split(" ")]

print("Intersection of lists : ")
intersection_of_lists(list_A, list_B)
print()
print("Reunion of lists : ")
reunion_of_lists(list_A, list_B)
print()
print("List A - List B : ")
remove_listA_from_listB(list_A, list_B)
print()
print("List B - List A : ")
remove_listB_from_listA(list_A, list_B)