#!/usr/bin/python3

# lambda function:
#     an anonymous function
#     can take any number of arguments
#     can only have one expression
# syntax:
#     lambda arguments : expression

lambda_multiply = lambda a, b : a * b
print(lambda_multiply)                  # <function <lambda> at 0x7fa5e58d01e0>
print(lambda_multiply(10, 10))          # 100

lambda_double = lambda a, b : (a * 2, b * 2)
print(lambda_double(10, 10))            # (20, 20)

def func_lambda(n):
    return lambda a: a * n 

func_lambda_double = func_lambda(2)
print(func_lambda_double(10))           # 20

func_lambda_triple = func_lambda(3)
print(func_lambda_triple(10))           # 30

# Use lambda functions along with built-in functions, e.g., filter(), map(), reduce()
list_original = list(range(10))
list_filtered = list(filter(lambda x: x % 2 == 0, list_original))
list_mapped   = list(map(lambda x: x * x, list_original))
from functools import reduce
list_reduced_sum  = reduce(lambda x, y: x + y, list_original)
list_reduced_max  = reduce(lambda x, y: x if x > y else y, list_original)
print(list_original)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_filtered)                    # [0, 2, 4, 6, 8]
print(list_mapped)                      # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list_reduced_sum)                 # 45
print(list_reduced_max)                 # 9

# Set comprehension
set_comprehension = {(lambda x: x * x)(a) for a in range(10)}
set_comprehension2 = set((lambda x: x * x)(a) for a in range(10))
print(set_comprehension)                # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(set_comprehension2)               # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# List comprehension
list_comprehension = [(lambda x: x * x)(a) for a in range(10)]
list_comprehension2 = list((lambda x: x * x)(a) for a in range(10))
print(list_comprehension)               # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list_comprehension2)              # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

