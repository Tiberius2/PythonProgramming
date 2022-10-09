# We can use the collections module, a high performance data structures module

#----------
import collections
from hashlib import new



string = str(input("Please input your sentence: "))

string = string.lower()
new_string = string.replace(" ","")

print(collections.Counter(new_string).most_common(1)[0])
#-----------

