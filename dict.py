#!/usr/bin/python3

# empty dictionary
dict_empty = {}
dict_empty2 = dict()
print(dict_empty == dict_empty2)       # True

# dictionary with integer keys
dict_int_key = {1 : 'Apple', 2 : 'Steve Jobs'}

# dictionary with mixed keys
dict_mixed_key = {'name' : 'Steve Jobs', 1 : [2, 4, 3]}

# using dict()
dict_construct = dict({1 : 'Apple', 2 : 'Steve Jobs'})

# from sequence having each item as a pair
dict_from_list = dict([(1, 'Apple'), (2, 'Steve Jobs')])

# from list of zipped key-value pairs
keys = ['name', 'age', 'job']
values = ['Bob', 25, 'Engineer']
dict_zip_list = dict(zip(keys, values))
print(dict_zip_list)                    # {'name': 'Bob', 'age': 25, 'job': 'Engineer'}

# using dict fromkeys()
dict_from_keys_default_val = {}.fromkeys(['name', 'age', 'address'])
dict_from_keys_val = {}.fromkeys(['name', 'age', 'address'], "UNKNOWN")
print(dict_from_keys_default_val)       # {'name': None, 'age': None, 'address': None}
print(dict_from_keys_val)               # {'name': 'UNKNOWN', 'age': 'UNKNOWN', 'address': 'UNKNOWN'}

# Dict comprehension
dict_comprehension_1 = { x : x * x for x in range(10) }
dict_comprehension_2 = { x : x * x for x in range(10) if x % 2 == 0 }
print(dict_comprehension_1)             # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print(dict_comprehension_2)             # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Access dict element: get()
print(dict_int_key[2])
print(dict_mixed_key[1])
print(dict_mixed_key['name'])
print(dict_mixed_key.get('name'))
print(dict_mixed_key.get('Age'))         # Returns None
print(dict_mixed_key.get('Age', 'No key found'))    # Returns "No key found"
# print(dict_mixed_key['Age'])           # KeyError: 'Age'
print(dict_construct[1])
print(dict_from_list[2])

# Change dict element: existing key
dict_construct[2] = 'Tim Cook'
print(dict_construct)

# Add dict element: new key
dict_construct['Apple founder'] = 'Steve Jobs'
print(dict_construct)

# Remove dict element: pop(), popitem(), del(), clear()
print(dict_construct.pop(2))            # Remove a particular element, rerutn its value
print(dict_construct)
# print(dict_construct.pop(2))          # KeyError: 2
print(dict_construct.pop(2, 'No key found'))  # No exception, but assign "No key found" to removed value
print(dict_construct.popitem())         # Remove an arbitrary element, return (key, value)
print(dict_construct)
print(dict_construct.clear())           # Remove all elements, return None
print(dict_construct)                   # Empty dict now: {}
del dict_construct                      # Delete the dict itself
# print(dict_construct)                 # NameError: name 'dict_construct' is not defined
del dict_from_list[1]                   # Remove a particular element
print(dict_from_list)
# del dict_from_list[1]                 # KeyError: 1

# items(): Return a new object of the dictionary's items in (key, value) format
print(dict_int_key.items())             # dict_items([(1, 'Apple'), (2, 'Steve Jobs')])

# keys(): Returns a new object of the dictionary's keys
print(dict_int_key.keys())              # dict_keys([1, 2])

# values(): Returns a new object of the dictionary's values
print(dict_int_key.values())            # dict_values(['Apple', 'Steve Jobs'])

# update(other): Updates the dictionary with the key/value pairs from other, overwriting existing keys
dict_int_key.update(dict_from_keys_default_val)
print(dict_int_key)                     # {1: 'Apple', 2: 'Steve Jobs', 'name': None, 'age': None, 'address': None}

# setdefault(key[,d]): Returns the corresponding value if the key is in the dict. If not, inserts the key with a value of d and returns d (defaults to None)
print(dict_int_key.setdefault('name', 'Tim Cook'))    # None
print(dict_int_key.setdefault('Name', 'Tim Cook'))    # Tim Cook
print(dict_int_key)                    # {1: 'Apple', 2: 'Steve Jobs', 'name': None, 'age': None, 'address': None, 'Name': 'Tim Cook'}

# copy(): Returns a shallow copy of the dict
dict_copy = dict_int_key.copy()
print(dict_copy)

# Operator =: creates a new reference to the original dict
dict_new = dict_int_key
print(dict_new)                        # {1: 'Apple', 2: 'Steve Jobs', 'name': None, 'age': None, 'address': None, 'Name': 'Tim Cook'}
dict_new.clear()
print(dict_new)                        # {}
print(dict_int_key)                    # {}
print(dict_copy)                       # {1: 'Apple', 2: 'Steve Jobs', 'name': None, 'age': None, 'address': None, 'Name': 'Tim Cook'}

# sorted(): Return a new sorted list of keys in the dictionary; only works when keys are of the same type
# print(sorted(dict_copy))             # TypeError: '<' not supported between instances of 'str' and 'int'

# len(): Return the length (the number of items) in the dictionary
print(len(dict_empty))                 # 0
print(len(dict_copy))                  # 6

# all(): Return True if all keys of the dictionary are True (or if the dictionary is empty)
print(all(dict_empty))                 # True
print(all(dict_copy))                  # True

# any(): Return True if any key of the dictionary is true. If the dictionary is empty, return False
print(any(dict_empty))                 # False
print(any(dict_copy))                  # True

# Dict membership test
print(1 in dict_copy)                  # True
print(3 in dict_copy)                  # False
print('name' in dict_copy)             # True

# Iterate through a dict
for k in dict_copy:
    print(dict_copy[k])                # Apple, Steve Jobs, None, None, None, Tim Cook
for k, v in dict_copy.items():
    print(k, ':', v)                   # 1 : Apple, 2 : Steve Jobs, name : None, age : None, address : None, Name : Tim Cook
for k, _ in dict_copy.items():
    print(k)                           # 1, 2, name, age, address, Name

# Multi-dimensional dict
student1 = {"name" : "Steve", "age" : 22, "marks" : 60}
student2 = {"name" : "Tim", "age" : 23, "marks" : 85}
student3 = {"name" : "Tom", "age" : 20, "marks" : 90}
students = {1 : student1, 2 : student2, 3 : student3}
print(students[2]['age'])              # 23

