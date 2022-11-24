import re

def match_regex(text_char, list_of_regex):
    results_match = []
    for element in text_char:
        if any([re.search(regex,element) for regex in list_of_regex]):
            results_match.append(element)
    return results_match