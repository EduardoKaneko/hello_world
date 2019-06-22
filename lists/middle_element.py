def middle_element(lst):
    if len(lst)%2 == 0:
        e1 = (len(lst)/2) - 1
        e2  = len(lst)/2
        median = (lst[e1] + lst[e2])/2
    elif len(lst)%2 != 0:
        e1 = int(len(lst)/2)
        median = lst[e1]
    return median

print(middle_element([5, 2, -10, -4, 4]))