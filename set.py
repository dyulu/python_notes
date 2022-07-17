#!/usr/bin/python3

# empty set
dict_empty = {}
set_empty = set()
print(dict_empty == set_empty)         # False

# set of uniform datatype
set_uniform = {11, 2, 33, 4, 55, 6, 77, 8, 99, 10}
print(set_uniform)                     # {33, 2, 99, 4, 6, 8, 10, 11, 77, 55}
set_uniform2 = {'Hello', 'world'}
print(set_uniform2)                    # {'world', 'Hello'}
set_uniform3 = {'Hello'}
print(set_uniform3)                    # {'Hello'}
set_uniform4 = set('Hello')
print(set_uniform4)                    # {'H', 'e', 'l', 'o'}

# set of mixed datatypes
set_mixed = {1, 2, 3, 4, 'Hello world', 3.14}
print(set_mixed)                       # {1, 2, 3, 4, 3.14, 'Hello world'}

# no duplicated items
set_dup = {11, 2, 11}
print(set_dup)                         # {2, 11}

# list is mutable and cannot be a set item
# set_mutable_item = {11, 2, [33, 4]}  # TypeError: unhashable type: 'list'

# set from list
set_from_list = set([11, 2, 11, 2])
print(set_from_list)                   # {2, 11}

# set comprehension
set_comprehension1 = {2 ** x for x in range(10)}
set_comprehension2 = {2 ** x for x in range(10) if x % 2 == 0}
print(set_comprehension1)              # {32, 1, 2, 64, 4, 128, 256, 512, 8, 16}
print(set_comprehension2)              # {64, 1, 256, 4, 16}

# no indexing and slicing

# add(): add one element; duplicates are avoided
# update(): add multiple elements; duplicates are avoided
set_from_list.add(22)
print(set_from_list)                   # {2, 11, 22}
set_from_list.update('Hello', (77, 99), [2, 11], {'Hello'})
print(set_from_list)                   # {2, 'H', 99, 'Hello', 'o', 11, 77, 'l', 'e', 22}

# discard(): removes an item; if the item does not exist, leave the set unchanged
# remove(): removes an item; if the item does not exist, raise an error
set_from_list.discard(99)
print(set_from_list)                   # {2, 'H', 'Hello', 'o', 11, 77, 'l', 'e', 22}
set_from_list.remove(77)
print(set_from_list)                   # {2, 'H', 'Hello', 'o', 11, 'l', 'e', 22}

# pop(): remove a random element
print(set_from_list.pop())             # 2
print(set_from_list)                   # {'e', 11, 'H', 'l', 'o', 22, 'Hello'}

# clear(): remove all elements
set_from_list.clear()
print(set_from_list)                   # set()

# union() or | operator: set union
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A | B)                            # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))                       # {1, 2, 3, 4, 5, 6, 7, 8}
print(B.union(A))                       # {1, 2, 3, 4, 5, 6, 7, 8}
print(A)                                # {1, 2, 3, 4, 5}
print(B)                                # {4, 5, 6, 7, 8}

# intersection() or & operator: set intersection
# intersection_update(): updates the set with the intersection of itself and another
print(A & B)                            # {4, 5}
print(A.intersection(B))                # {4, 5}
print(B.intersection(A))                # {4, 5}
print(A)                                # {1, 2, 3, 4, 5}
print(B)                                # {4, 5, 6, 7, 8}
print(A.intersection_update(B))         # None
print(A)                                # {4, 5}
print(B)                                # {4, 5, 6, 7, 8}
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(B.intersection_update(A))         # None
print(A)                                # {1, 2, 3, 4, 5}
print(B)                                # {4, 5}

# difference() or - operator: set difference
# difference_update(): removes all elements of another set from this set
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A - B)                            # {1, 2, 3}
print(B - A)                            # {8, 6, 7}
print(A.difference(B))                  # {1, 2, 3}
print(B.difference(A))                  # {8, 6, 7}
print(A.difference_update(B))           # None
print(A)                                # {1, 2, 3}
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(B.difference_update(A))           # None
print(B)                                # {6, 7, 8}

# symmetric_difference() or ^ operator: a set of elements in A and B but not in both (excluding the intersection)
# symmetric_difference_update(): updates a set with the symmetric difference of itself and another
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A ^ B)                            # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))        # {1, 2, 3, 6, 7, 8}
print(B.symmetric_difference(A))        # {1, 2, 3, 6, 7, 8}
print(A)                                # {1, 2, 3, 4, 5}
print(B)                                # {4, 5, 6, 7, 8}
print(A.symmetric_difference_update(B)) # None
print(A)                                # {1, 2, 3, 6, 7, 8}
print(B)                                # {4, 5, 6, 7, 8}
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(B.symmetric_difference_update(A)) # None
print(A)                                # {1, 2, 3, 4, 5}
print(B)                                # {1, 2, 3, 6, 7, 8}

