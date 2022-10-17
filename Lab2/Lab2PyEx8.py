# 8. Write a function that receives a number x, default value equal to 1, a list of strings, 
# and a boolean flag set to True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True,
#  otherwise it should contain characters that have the ASCII code not divisible by x.

# Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" . Note: The function must return list of lists.

def function_ascii(listOfStrings: list[str], x: int = 1, flag: bool = True) -> list[list[str]]: 
     result: list[list[str]] = [] 
  
     for string in listOfStrings: 
         current_list: list[str] = [] 
         for char in string: 
             if (ord(char) % x) != flag: 
                 current_list.append(char) 
         result.append(current_list) 
  
     return result


print(function_ascii(["test","hello","lab002"], x = 2, flag = False))

