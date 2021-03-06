'''
Create a function named more_frequent_item that has three parameters named lst, item1, and item2.

Return either item1 or item2 depending on which item appears more often in lst.

If the two items appear the same number of times, return item1.
'''

def more_frequent_item(lst, item1, item2):
    c_i1 = lst.count(item1)
    c_i2 = lst.count(item2)
    if c_i1 >= c_i2:
        return item1
    elif c_i2 > c_i1:
        return item2
    
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))