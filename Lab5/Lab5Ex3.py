def get_vowels_from_string(string):
    #first method
    def vowels_list(string):
        string = string.casefold()
        vowels = []
        for char in string:
            if char in "aeiou":
                vowels.append(char)
        return vowels
    
    #second method
    anonymous_function = lambda string: [char for char in string if char in "aeiou"]
    #third method
    filter_function = lambda string : list(filter(lambda char: char in "aeiou", string))
    ####

    first_method = vowels_list(string)
    second_method = anonymous_function(string)
    third_method = filter_function(string)

    return first_method,second_method,third_method

print(get_vowels_from_string("Programming in Python is fun"))


    