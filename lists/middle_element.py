'''
Create a function called middle_element that has one parameter named lst.

If there are an odd number of elements in lst, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.
'''

def middle_element(lst):
  
    if len(lst)%2 == 0:
        e1 = int((len(lst)/2) - 1)
        e2 = int(len(lst)/2)
        median = (lst[e1] + lst[e2])/2
    
    elif len(lst)%2 != 0:
        e1 = int(len(lst)/2)
        median = lst[e1]
    
    return median

print(middle_element([5, 2, -10, -4, 4, 5]))