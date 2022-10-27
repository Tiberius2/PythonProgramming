


def operationOnSets(*sets):
    result = {}
    for index1 in range(0, len(sets) - 1):
        for index2 in range(index1 + 1, len(sets)):        # aici in loc sa folosim chiar metodele .union  , .intersection, .difference , am folosit direct operatorii pentru a face operatiile intre seturi
            result.update({(str(sets[index1]) + " | " + str(sets[index2])): (sets[index1] | sets[index2]),   # a | b  
                           (str(sets[index1]) + " & " + str(sets[index2])): (sets[index1] & sets[index2]),   # a & b
                           (str(sets[index1]) + " - " + str(sets[index2])): (sets[index1] - sets[index2]),   # a - b
                           (str(sets[index2]) + " - " + str(sets[index1])): (sets[index2] - sets[index1])})  # b - a
    return result

#folosind update, adaugam la dictionar un key-value pair
# inseram cate un item in dictionar mai bine spus
# in cazul nostru de mai sus, inseram chiar un dictionar construit pe baza acelor operatii , si acelor foruri


set1 = set((1,2))
set2 = set((2,3))

print (operationOnSets(set1, set2))