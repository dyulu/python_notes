#!/usr/bin/python3

# List:  a collection which is ordered and changeable. Allows duplicate members.
# Tuple: a collection which is ordered and unchangeable. Allows duplicate members.
# Set:   a collection which is unordered, unchangeable, and unindexed. No duplicate members.
# Dict:  a collection which is ordered** and changeable. No duplicate members.

# empty list
list_empty = []
list_empty2 = list()
print(list_empty == list_empty2)    # True

# list with mixed data types
# Item:            0  1  2  3  4              5
# Item:            -6 -5 -4 -3 -2             -1
list_mixed_data = [1, 2, 3, 4, 'Hello world', 3.14]

# nested list
# Item:        0              1             2
# Item:        -3             -2            -1
list_nested = ['Hello world', [8, 4, 6, 2], ['Python3']]

# list comprehension
list_comprehension1 = [2 ** x for x in range(10)]
list_comprehension2 = [2 ** x for x in range(10) if x % 2 == 0]

# using list()
list_construct = list(('Steve', 'Tim', 'Tom'))
list_construct2 = list(['Steve', 'Tim', 'Tom'])
print(list_construct)                # ['Steve', 'Tim', 'Tom']
print(list_construct2)               # ['Steve', 'Tim', 'Tom']

# Access list element(s)
print(list_mixed_data[4])            # Item 4:                             Hello world
print(list_nested[1][3])             # Item 3 of Item 1:                   2
print(list_nested[-1])               # last item:                          ['Python3']
print(list_nested[-3])               # 3rd item from the end:              Hello world
print(list_mixed_data[2:4])          # Items from 2 to 3, not including 4: [3, 4]
print(list_mixed_data[2:])           # Items from 2 to the last:           [3, 4, 'Hello world', 3.14]
print(list_mixed_data[:2])           # Items from 0 to 2:                  [1, 2]
print(list_mixed_data[:])            # All items:                          [1, 2, 3, 4, 'Hello world', 3.14]

# Change list element(s)
list_nested[1] = 'Python2'           # Change item 1
print(list_nested)                   #                                     ['Hello world', 'Python2', ['Python3']]
list_nested[1] = ['1', '2']          # Change item 1
print(list_nested)                   #                                     ['Hello world', ['1', '2'], ['Python3']]
print(list_nested[1])                # ['1', '2'] 
print(list_nested[1:2])              # [['1', '2']]
list_nested[1:2] = ['1.0', '2.0']
print(list_nested)                   #                                     ['Hello world', '1.0', '2.0', ['Python3']]
list_nested[1:4] = ['1.00', '2.00', '3.00']
print(list_nested)                   #                                     ['Hello world', '1.00', '2.00', '3.00']

# append(): adds an element to the end of the list
# extend(): adds all elements of a list to another list
list_nested.append(['Python3'])
print(list_nested)                   #                                     ['Hello world', '1.00', '2.00', '3.00', ['Python3']]
list_nested.extend(['4.0', '5.0'])
print(list_nested)                   #                                     ['Hello world', '1.00', '2.00', '3.00', ['Python3'], '4.0', '5.0']

# + and *: concatenation and repeat
list_empty = list_empty + ['Hello']
print(list_empty)                    #                                     ['Hello']
list_empty = list_empty * 4
print(list_empty)                    #                                     ['Hello', 'Hello', 'Hello', 'Hello']

# delete list item(s)
del list_empty[1]
print(list_empty)                    #                                     ['Hello', 'Hello', 'Hello']
del list_empty[1:2]
print(list_empty)                    #                                     ['Hello', 'Hello']

# insert(): inserts an item at the specified index
list_empty.insert(1, "world")
print(list_empty)                    #                                     ['Hello', 'world', 'Hello']

# count(): returns the count of specified item
# index(): returns the index of the first matched item
# remove(): removes a first matched item from the list
print(list_empty.count('Hello'))     #                                     2
print(list_empty.index('Hello'))     #                                     0
list_empty.remove('Hello')
print(list_empty)                    #                                     ['world', 'Hello']

# pop(): returns and removes an element at the given index
list_empty.insert(0, 'Hello')
print(list_empty)                    #                                     ['Hello', 'world', 'Hello']
list_empty.pop(0)                    # remove Item 0
print(list_empty)                    #                                     ['world', 'Hello']
list_empty.pop()                     # remove the last item
print(list_empty)                    #                                     ['world']

# clear(): removes all items from the list
# del: delete the list
list_empty.clear()
print(list_empty)                    #                                     []
del list_empty
# print(list_empty)                  # NameError: name 'list_empty' is not defined

# reverse(): reverse the order of items in the list
print(list_comprehension1)           # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
list_comprehension1.reverse()
print(list_comprehension1)           # [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

# sort(): sort items in a list in ascending order
print(list_comprehension1.sort())    # None
print(list_comprehension1)           # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(list_nested)                   # ['Hello world', '1.00', '2.00', '3.00', ['Python3'], '4.0', '5.0']
# list_nested.sort()                 # TypeError: '<' not supported between instances of 'list' and 'str'
print(list_mixed_data)               # [1, 2, 3, 4, 'Hello world', 3.14]
# list_mixed_data.sort()             # TypeError: '<' not supported between instances of 'str' and 'int'

# =: creates a reference to the list
# copy(): returns a shallow copy of the list
list_assign = list_comprehension1
list_copy = list_comprehension1.copy()
print(list_assign)                   # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(list_copy)                     # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
list_comprehension1.clear()
print(list_assign)                   # []
print(list_copy)                     # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# List membership test
print(512 in list_copy)              # True
print(1024 in list_copy)             # False
print(1024 not in list_copy)         # True

# Iterate through a list
for item in list_copy:
    print(item)

# len(): list length
print(len(list_copy))                # 10

# sum(): sums items in the list
# max(): returns the max item in the list
# min(): returns the min item in the list
print(sum(list_copy))                # 1023
print(max(list_copy))                # 512
print(min(list_copy))                # 1

# all(): returns True if all items are true or if the list is empty
# any(): returns True if any item is true. If list is empty, return false
print(all(list_copy))               # True
print(any(list_copy))               # True

# reduce(func, list): reduce a list into a single value by applying func
from functools import reduce
def sum(a, b):
    return a+b
print(reduce(sum, list_copy))                  # 1023
print(reduce(lambda a, b: a + b, list_copy))   # 1023

# map(func, list): applies func to each item in the list
import math
print(map(math.sqrt, list_copy))                               # <map object at 0x7fb7e6110ac8>
print([f'{item:.2f}' for item in map(math.sqrt, list_copy)])   # ['1.00', '1.41', '2.00', '2.83', '4.00', '5.66', '8.00', '11.31', '16.00', '22.63']

# filter(func, list): applies func to each item in the list; returns an iterator that is already filtered
print(filter(lambda a: a >= 32, list_copy))                    # <filter object at 0x7fcf89f10c18>
print(list(filter(lambda a: a >= 32, list_copy)))              # [32, 64, 128, 256, 512]
print([item for item in filter(lambda a: a >= 32, list_copy)]) # [32, 64, 128, 256, 512]

