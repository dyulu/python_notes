#!/usr/bin/python3

# empty tuple
tuple_empty = ()
tuple_empty2 = tuple()
print(tuple_empty == tuple_empty2)  # True

# tuple having same datetype
# Item:          0  1  2  3  4  5  6  7
# Item:          -8 -7 -6 -5 -4 -3 -2 -1
tuple_uniform = (1, 2, 3, 4, 5, 6, 7, 8)

# tuple with mixed datatypes
tuple_mixed = (1, "Hello", 3.14)

# nested tuple
tuple_nested = ("Hello", [8, 4, 6], (1, 2, 3))

# tuple packing: create tuple w/o using parentheses
tuple_packing = 1, "Hello", 3.14

# tuple unpacking
a, b, c = tuple_packing
print(b)                          # Hello

# tuple w/ one element; note the comma
tuple_one = ('Hello', )
tuple_one2 = 'Hello',

# using tuple()
tuple_construct = tuple(('Steve', 'Tim', 'Tom'))

# Access tuple element
print(tuple_uniform[5])           # 6
print(tuple_uniform[-1])          # 8
print(tuple_uniform[-5])          # 4
print(tuple_uniform[2:5])         # Item 2, 3, and 4, not including Item 5: (3, 4, 5)
print(tuple_uniform[2:])          # (3, 4, 5, 6, 7, 8)
print(tuple_uniform[:5])          # Not including Item 5: (1, 2, 3, 4, 5)
print(tuple_uniform[:])           # (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple_nested[2][2])         # 3

# tuple is immutable: elements of a tuple cannot be changed once assigned
# tuple_uniform[0] = 10           # TypeError: 'tuple' object does not support item assignment
tuple_nested[1][2] = 10           # Mutable tuple element can be changed
print(tuple_nested)               # ('Hello', [8, 4, 10], (1, 2, 3))
tuple_empty = tuple_nested        # Tuple reassignment
print(tuple_empty)                # ('Hello', [8, 4, 10], (1, 2, 3))

# + and *: concatenation and repeat
tuple_concat = tuple_mixed + tuple_nested
print(tuple_concat)               # (1, 'Hello', 3.14, 'Hello', [8, 4, 10], (1, 2, 3))
print(('Hello',) * 3)             # ('Hello', 'Hello', 'Hello')

# tuple is immutable: cannot delete tuple elements
# del tuple_uniform[0]            # TypeError: 'tuple' object doesn't support item deletion
del tuple_uniform                 # Tuple itself can be deleted
# print(tuple_uniform)            # NameError: name 'tuple_uniform' is not defined

# tuple is immutable: no sort method
tuple_uniform = (11, 2, 33, 4, 55, 6, 77, 8)
# tuple_uniform.sort()                 # AttributeError: 'tuple' object has no attribute 'sort'
print(sorted(tuple_uniform))           # Returns an array: [2, 4, 6, 8, 11, 33, 55, 77]

# count(): returns the count of specified item
# index(): returns the index of the first matched item
print(tuple_concat.count('Hello'))     # 2
print(tuple_concat.index('Hello'))     # 1

# Tuple membership test
print('Hello' in tuple_concat)         # True
print('world' in tuple_concat)         # False
print('world' not in tuple_concat)     # True

# Iterate through a tuple
for item in tuple_concat:
    print(item)

# len(): tuple length
print(len(tuple_concat))               # 6

# all(): returns True if all items are true or if the tuple is empty
# any(): returns True if any item is true. If tuplle is empty, return false
print(all(tuple_concat))               # True
print(any(tuple_concat))               # True

# sum(): sums items in the tuple
# max(): returns the max item in the tuple
# min(): returns the min item in the tuple
print(sum(tuple_uniform))              # 197
print(max(tuple_uniform))              # 77
print(min(tuple_uniform))              # 2

# enumerate(): returns enumerate object of tuple
print(enumerate(tuple_uniform))        # <enumerate object at 0x7fb1e7d0bc18>
print([item for item in enumerate(tuple_uniform)])  # [(0, 11), (1, 2), (2, 33), (3, 4), (4, 55), (5, 6), (6, 77), (7, 8)]
