#!/usr/bin/python3

# Iterable: objects can be passed to the built-in iter() function to get an iterator
#           e.g., sequential collections like lists, tuples, and strings
#                 non-sequential collections like dictionaries and sets
#                 generators which do not ever store all of their members in memory at once
# Iterator: objects can be passed to the built-in next() function to fetch the next item
#    iterator = iter(iterable)
#    item = next(iterator)
iterable_str = "abcd"
iterator_str = iter(iterable_str)
print(next(iterator_str))   # a
print(next(iterator_str))   # b
print(next(iterator_str))   # c
print(next(iterator_str))   # d
# print(next(iterator_str)) # Raise StopIteration exception 

# The built-in functions that accept iterables as arguments:
#    list, tuple, dict, set: construct a list, tuple, dictionary, or set, respectively, from the contents of an iterable
#    sum: sum the contents of an iterable
#    sorted: return a list of the sorted contents of an interable
#    any: returns True and ends the iteration immediately if bool(item) was True for any item in the iterable
#    all: returns True only if bool(item) was True for all items in the iterable
#    max: return the largest value in an iterable
#    min: return the smallest value in an iterable
list_sort = sorted('return a list of the sorted contents of an interable')
set_construct = set(list_sort)
list_sort2 = sorted(set_construct)
print(list_sort)             # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'b', 'c', 'd', 'e', 'e', 'e', 'e', 'e', 'e',
                             #  'f', 'f', 'h', 'i', 'i', 'l', 'l', 'n', 'n', 'n', 'n', 'n', 'o', 'o', 'o', 'o', 'r', 'r', 'r', 'r', 's',
                             #  's', 's', 't', 't', 't', 't', 't', 't', 't', 'u']
print(set_construct)         # {' ', 'b', 'i', 't', 'l', 'n', 'e', 'd', 'r', 'u', 'c', 'o', 'f', 'h', 's', 'a'}
print(list_sort2)            # [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']

# Iteratable unpacking
list_odd = [1, 3, 5, 7]
# a, b, c = list_odd         # ValueError: too many values to unpack (expected 3)
# a, b, c, d, e = list_odd   # ValueError: not enough values to unpack (expected 5, got 4) 
a, b, c, d = list_odd
print(a, b, c, d)            # 1 3 5 7
a, *b, c = list_odd
print(a, b, c)               # 1 [3, 5] 7

list_name_grades = [("Steve", 98), ("Tom", 100), ("Tim", 50)]
for name, grade in list_name_grades:
    print(name, grade)
'''
Steve 98
Tom 100
Tim 50
'''

list_name_grades = [("Steve", 98, "A"), ("Tom", 100, "A"), ("Tim", 50, "D")]
for name, *grade in list_name_grades:
    print(name, grade)
'''
Steve [98, 'A']
Tom [100, 'A']
Tim [50, 'D']
'''

# The built-in enumerate function: accepts an iterable as an input, and returns a new iterable that produces a tuple of the iteration-count and
#                                  the corresponding item from the original iterable
for item in enumerate("abcd"):
    print(item)
'''
(0, 'a')
(1, 'b')
(2, 'c')
(3, 'd')
'''

for item_index, item in enumerate("abcd"):
    print(item_index, item)
'''
0 a
1 b
2 c
3 d
'''

for item in "abcd":
    print(item)
'''
a
b
c
d
'''

