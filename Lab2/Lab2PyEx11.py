    #  11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. 
    #  Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def sort_tuples(lists):

    if len([l for l in lists if len(l) < 2]) != 0:
        print("Not valid list")
        return
    return sorted(lists, key=lambda i: i[1][2])

