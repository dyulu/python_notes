#!/usr/bin/python3

# https://realpython.com/introduction-to-python-generators/
# https://www.pythontutorial.net/advanced-python/python-generators/

import cProfile

from decorator import measure_performance

def file_reader_list(filename):
    '''Read file contents to a list'''
    file = open(filename, "r")        # open: returns a generator object for iterating file line by line
    result = file.read().split("\n")  # load everything into memory all at once
    file.close()
    return result

def file_reader_generator(filename):
    ''''Read file contents using a generator'''
    file = open(filename, "r")
    for line in file.readlines():
        yield line                    # yield: function is paused and control is transferred to the caller
    else:                             #        local variables and their states are remembered between successive calls
        file.close()

@measure_performance
def count_lines(filename, func_reader):
    '''Count number of lines in a file using the reader method provided
       Use generator expression/comprehension if no reader method provided
    '''
    if func_reader is None:
        result = (line for line in open(filename, "r"))
    else:
        result = func_reader(filename)

    row_count = 0
    for row in result:                            # Iterate over generator/list with for statement
        row_count += 1

    print(f"Row count in file {filename} is {row_count}")

def infinite_sequence():
    '''Generating an infinite sequence'''
    num = 0
    while True:
        yield num
        num += 1

def print_seq(max_num):
    '''Print the aequence from 0 up to max_num'''
    gen = infinite_sequence()
    num = next(gen)                               # Iterate over generator with next call
    while num <= max_num:
        print(num)
        num = next(gen)
    else:                                         # num > max_num
        print("All done!")

def fibonacci_numbers(max_num):
    '''Generator for max_num of Fibonacci numbers'''
    x, y = 0, 1
    for _ in range(max_num):
        x, y = y, x + y                           # temp = x; x = y; y = temp + y
        yield x

def square(nums):
    '''Generator for squares'''
    for i in nums:
        yield i ** 2

def number_square(nums):
    '''Generator for squares'''
    for i in nums:
        yield i, i ** 2

# Define an iterator that returns a square number of an integer
class Squares:
    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current ** 2
        self.current += 1
        if self.current > self.length:
            raise StopIteration
        return result

# Define an iterator that returns a square number of an integer
class NumberSquares:
    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        current = self.current
        self.current += 1
        if self.current > self.length:
            raise StopIteration
        return current, current ** 2

if __name__ == '__main__':
    count_lines(__file__, file_reader_list)                                 # __file__: filename of this file
    count_lines(__file__, file_reader_generator)
    count_lines(__file__, None)
    cProfile.run('print_seq(10)')
    print([ num for num in fibonacci_numbers(10) ])                         # List comprehension
    print([ num for num in square(fibonacci_numbers(10)) ])                 # Pileline generators
    print([ square for square in Squares(10) ])
    print({ number : square for (number, square) in NumberSquares(10) })    # Dictionary comprehension
    print({ number : square for (number, square) in number_square(range(10)) })
    print({ number : square for (number, square) in number_square(range(10)) if number % 2 == 0 })
