'''
Create a function named remove_middle which has three parameters named lst, start, and end.

The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.
'''


def remove_middle(lst, start, end):
    del lst[start: end+1]
    return lst
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))