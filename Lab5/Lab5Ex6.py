def get_Odds_Even(my_list):
    odd_list = []
    even_list = []
    final_list = []
    for x in my_list:
        if x % 2 == 0:
            even_list.append(x)
        else:
            odd_list.append(x)
    
   # for x,y in zip(even_list,odd_list):
        #final_list.append(tuple((x,y)))
    

    return list(zip(odd_list,even_list))


print(get_Odds_Even([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))