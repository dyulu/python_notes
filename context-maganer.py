#!/usr/bin/python3

# Context manager: mechanism for the automatic setup and teardown of resources, 
#                  e.g., open file handles, database connections, resource locks
# Use cases:
#    Open - close: open and close a resource automatically, e.g., file, socket
#    Lock - release: acquire a lock and release it automatically
#    Start - stop: e.g., start a timer and stop it automatically
#    Change - reset: e.g., resource has a default; use context mgr to change the resurce; then reset it to default when done

# Create an open-close context manager with class
class FileContextManager():
    def __init__(self, filename, method):
        print('init method called to set up resource')
        self.file = open(filename, method)
         
    def __enter__(self):
        print('enter method called')
        return self.file
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called to clean up resource')
        self.file.close()
        return True  # True: Do not raise exception; gracefully handled
                     # Any other value: raise exception if any exception occurred in with-block
                     # When no exception, exc_type is None
 
with FileContextManager(__file__, 'r') as f:
    print('with statement block')
    print(f.read())
print(f.closed)
'''
init method called to set up resource
enter method called
with statement block
#### contents of this file here####

exit method called to clean up resource
True
'''

# Create a start-stop context manager with class
from time import perf_counter, sleep
class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start

with Timer() as timer:
    sleep(5)             # sleep 5 seconds
print(timer.elapsed)     # 5.000982435

# Two equivalent ways to reading a file
#     1. Use context manager
with open(__file__, 'r') as f:
    f.read()
print(f.closed)          # True
#     2. Use try-except-finally
try:
    f = open(__file__, 'r')
    f.read()
except:
    print(f"Oops! Exception: {sys.exc_info()[0]}")
finally:
    f.close()
print(f.closed)          # True

# Create context manager with decorator and generator
from contextlib import contextmanager

@contextmanager
def open_it(filename, method):
    f = open(filename, method)
    try:
        yield f
    finally:
        f.close()

with open_it(__file__, "r") as f:
    f.read()
print(f.closed)          # True
