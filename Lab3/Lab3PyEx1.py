# 1.Write a function that receives as parameters two lists a and b and returns a list of sets containing: 
# (a intersected with b, a reunited with b, a - b, b - a)


# O metoda mai usoara ar fi sa folosim operatiilor clasei "set" intr-o linie precum:
# return set(a) & set(b), set(a) | set(b), set(a) - set(b), set(b)-set(a)

def intersection_of_lists(list_A,list_B) :
    global list_C
    list_C = [value for value in list_A if value in list_B]
    return list_C

def reunion_of_lists(list_A, list_B) :
    global list_C
    list_C=list(set().union(list_A,list_B))
    return list_C

def remove_listB_from_listA(list_A, list_B):
    global list_C
    list_C = list(set(list_B).difference(set(list_A)))
    return list_C

def remove_listA_from_listB(list_A, list_B):
    global list_C
    list_C = list(set(list_A).difference(set(list_B)))
    return list_C

def setsOperations(firstList, secondList):
    finalList = []
    finalList.append(intersection_of_lists(firstList,secondList))
    finalList.append(reunion_of_lists(firstList,secondList))
    finalList.append(remove_listA_from_listB(firstList,secondList))
    finalList.append(remove_listB_from_listA(firstList,secondList))
    return finalList

if __name__ == "__main__" :
    firstList = [int(x) for x in input("Enter elements of first list here: ").split(" ")]
    secondList = [int(x) for x in input("Enter elements of second list here: ").split(" ")]
    print (setsOperations(firstList,secondList))
    
