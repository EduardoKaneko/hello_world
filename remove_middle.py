def remove_middle(lst, start, end):
    del lst[start: end+1]
    return lst
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))