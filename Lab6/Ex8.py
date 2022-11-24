import re
import os

def directory_match(directory,regex):
    for files in os.walk(directory):
        for file in files:
            if re.search(regex,file):
                print(">>" + file)
            else:
                print(file)