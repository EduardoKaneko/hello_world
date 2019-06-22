'''
Write a function named combine_sort that has two parameters named lst1 and lst2.

The function should combine these two lists into one new list and sort the result. Return the new sorted list.
'''

def combine_sort(lst1, lst2):
    return sorted(lst1 + lst2 )

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))


# Difference between list.sort() and sorted(list)
'''
sorted() returns a new sorted list, leaving the original list unaffected. list.sort() sorts the list in-place, mutating the list indices, and returns None (like all in-place operations).

sorted() works on any iterable, not just lists. Strings, tuples, dictionaries (you'll get the keys), generators, etc., returning a list containing all elements, sorted.

Use list.sort() when you want to mutate the list, sorted() when you want a new sorted object back. Use sorted() when you want to sort something that is an iterable, not a list yet.

For lists, list.sort() is faster than sorted() because it doesn't have to create a copy. For any other iterable, you have no choice.

No, you cannot retrieve the original positions. Once you called list.sort() the original order is gone.

ref: https://stackoverflow.com/questions/22442378/what-is-the-difference-between-sortedlist-vs-list-sort
'''
