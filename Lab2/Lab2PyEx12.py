# 12. Write a function that will receive a list of words  as parameter and will return a list of lists of words, grouped by rhyme. 
# Two words rhyme if both of them end with the same 2 letters.
# 	Example:
#          group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]

def rhyme(word1,word2):
    if word1[-2:] == word2[-2:]:
        return True
    return False

def doTheyRhyme(words):
    final_list = []
    for word in words:
        match = 0
        new_list = []
        for matches in range(words.index(word)+1,len(words)):
            if rhyme(word, words[matches]):
                match = 1
                new_list.append(word)
                new_list.append(words[matches])
        if new_list:
            final_list.append(new_list)
        new_list = []
        if match == 0:
            find = [item for item in final_list if word in item]
            if not find:
                new_list.append(word)
                final_list.append(new_list)     

    return final_list            
    


print(doTheyRhyme(['ana','banana','carte','arme','parte']))