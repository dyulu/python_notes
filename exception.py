#!/usr/bin/python3

# try:
#     business logic
# exception E1[, E2[, ...]]:
#     execute in case of any of the listed exceptions
# exception E:
#     execute in case of exception e
# exception:
#     execute in case of any other exception
# else:
#    execute in case of no exception
# finally:
#    always executed
import traceback

try:
    a = 4 / 0
except ZeroDivisionError:
    traceback.print_exc()
else:
    print("Cannot be here")
'''
Traceback (most recent call last):
  File "exception.py", line 18, in <module>
    a = 4 / 0
ZeroDivisionError: division by zero
'''

try:
    f = open("nonexisting-file.txt", "r")
    # f.readline()
except Exception as e:
    print("Exception: {}".format(e))         # Exception: [Errno 2] No such file or directory: 'nonexisting-file.txt'
    print("    Type: {}".format(type(e)))    # Type: <class 'FileNotFoundError'>
    print("    Args: {}".format(e.args))     # Args: (2, 'No such file or directory')
else:
    print("Cannot be here")
finally:
    try:
        f.close()
    except Exception as e:
        print("Exception: {}".format(e))        # Exception: name 'f' is not defined
        print("    Type: {}".format(type(e)))   # Type: <class 'NameError'>
        print("    Args: {}".format(e.args))    # Args: ("name 'f' is not defined",)


try:
    a = int("hello")
except ValueError:
    traceback.print_exc()
else:
    print("Cannot be here")
'''
Traceback (most recent call last):
  File "exception.py", line 49, in <module>
    a = int("hello")
ValueError: invalid literal for int() with base 10: 'hello'
'''

import sys

try:
    a = int("hello")
except ValueError:
    type, value, tb = sys.exc_info()
    print(f"type: {type}")
    print(f"value: {value}")
    print(f"traceback:")
    tbs = traceback.extract_tb(tb)
    for item in tbs:
        print(f"    File: {item[0]}, Line: {item[1]}, Function: {item[2]}, Message: {item[3]}")
else:
    print("Cannot be here")
'''
type: <class 'ValueError'>
value: invalid literal for int() with base 10: 'hello'
traceback:
    File: exception.py, Line: 64, Function: <module>, Message: a = int("hello")
'''

class UserDefinedException(RuntimeError):
    def __init__(self, arg):
        self.arg = arg

try:
    raise UserDefinedException("Caught COVID")
except UserDefinedException as e:
    print(e.arg)                                # Caught COVID

