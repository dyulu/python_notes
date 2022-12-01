#!/usr/bin/python3

# id() is a built-in function
# syntax: id(object)
# The identity of an object has to be unique and constant for the object during the lifetime. 

# In Python, variables are more properly called names.
#            assignment is really the binding of a name to an object.
#            Each binding has a scope that defines its visibility, usually the block in which the name originates.

# Mutable objects:   list, dict, set, byte array
# Immutable objects: int, float, complex, string, tuple, frozen set [note: immutable version of set], bytes

# Example of immutable object: names str1 and str2 refer to the same object
str1 = "ABCD"
str2 = "ABCD"
print(id(str1), str1)          # 140409853194792 ABCD
print(id(str2), str2)          # 140409853194792 ABCD
print(str1 == str2)            # True
print(id(str1) == id(str2))    # True

# Example of immutable object: reassignment binds str1 to a different object, but str2 does not change
str1 = "abcd"
str2 = str1
print(id(str1), str1)          # 140409853338544 abcd
print(id(str2), str2)          # 140409853338544 abcd
print(str1 == str2)            # True
print(id(str1) == id(str2))    # True
str1 = "ABCD"
print(id(str1), str1)          # 140409853194792 ABCD
print(id(str2), str2)          # 140409853338544 abcd
print(str1 == str2)            # False
print(id(str1) == id(str2))    # False

# Example of mutable object: names list1 and list2 refer to different objects that have the same value
list1 = [1, 2]
list2 = [1, 2]
print(id(list1), list1)        # 140409846685576 [1, 2]
print(id(list2), list2)        # 140409846685640 [1, 2]
print(list1 == list2)          # True
print(id(list1) == id(list2))  # False


# Example of immutable object: reassignment binds list1 to a different object, but list2 does not change
list1 = [12, 34]
list2 = list1
print(id(list1), list1)        # 140409853518152 [12, 34]
print(id(list2), list2)        # 140409853518152 [12, 34]
print(list1 == list2)          # True
print(id(list1) == id(list2))  # True
list1 = [56, 78]
print(id(list1), list1)        # 140409846685640 [56, 78]
print(id(list2), list2)        # 140409853518152 [12, 34]
print(list1 == list2)          # False
print(id(list1) == id(list2))  # False

# When identity changes?
list1 = [0, 1]
print(id(list1))               # 140409846685576
# += does not change identity
list1 += [3, 4]
print(id(list1))               # 140409846685576
# = changes identity, even if the value is the same
list1 = [3, 4]
print(id(list1))               # 140409846685640
# = changes identity
list1  = list1 + [3, 4]
print(id(list1))               # 140409853518024
# = changes identity. In this case, not a list any more
list1 = 3
print(id(list1))               # 4372659264


# Pass-by-object-reference: Python function call is not pass-by-value and not pass-by-reference, but Pass-by-object-reference.
# In Python,Values are passed to function by object reference.
#     If object is immutable, the modified value is not available outside the function.
#     If object is mutable, modified value is available outside the function.

def test1(a, b):     # assume a and b are mutable in this case
    a += b           # a's identity does not change: modification can be seen outside the function
    b = 7            # b's identity changes: modification cannot be seen outside the function

x = [1]
y = [2]
test1(x, y)
print(x)             # [1, 2]
print(y)             # [2]


def test2(a, b):     # assume a and b are mutable in this case
    a = a + b        # a's identity changes: modification cannot be seen outside the function
    b = [7, 8]       # b's identity changes: modification cannot be seen outside the function

x = [1]
y = [2]
test2(x, y)
print(x)             # [1]
print(y)             # [2]


def test3(a, b):     # assume a and b are mutable in this case
    a.append(1111)   # a's identity does not change: modification can be seen outside the function
    b[0] = 2222      # b's identity does not change: modification can be seen outside the function

x = [1]
y = [2]
test3(x, y)
print(x)             # [1, 1111]
print(y)             # [2222]
