# The *args and **kwargs is a common idiom to allow arbitrary number of arguments to functions,
#  in our case , an arbitrary number of key-value elements given as name-parameters
# PS, m-a ajutat un coleg la acest exercitiu :(


# must return the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

# <a 
# href=\"http://python.org \ "
# _class = \" my-link \ "
# id = \" someid \ "> 
# Hello there </a>

def build_xml_element(tag, content, **dictionary):
    finalstring = "<" + tag
    for key in dictionary:
        finalstring = finalstring + key + "=\"" + dictionary[key] + "\""
    finalstring = finalstring + ">" + content + "</" + tag + ">"
    return finalstring

print( build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))
