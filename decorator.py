#!/usr/bin/python3

# Decorator examples from:
# https://realpython.com/primer-on-python-decorators/
# https://www.freecodecamp.org/news/python-decorators-explained-with-examples/

import functools           # wraps: to keep the identity of the decorated function
import tracemalloc
import time
import datetime

### START of decorator definitions

def print_separator(func):
    def wrapper(*args, **kwargs):
        print("####################")
        result = func(*args, **kwargs)
        print("####################")
        return result
    return wrapper

ListMakeFuncs = dict()
def register_list_make_func(func):    # Decorator w/o wrapping, simply registering
    '''Register list making functions'''
    global ListMakeFuncs
    ListMakeFuncs[func.__name__] = func
    return func

def log_datetime(func):
    '''Log the date and time of a function'''
    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-" * 40}')
        func()
    return wrapper

def log_datetime2(func):
    '''Log the date and time of a function'''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Function2: {func.__name__}\nRun on: {datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-" * 40}')
        func(*args, **kwargs)
    return wrapper

def check_args(*types):               # Decorator with arguments
    '''Make sure function have expected argument types'''
    def wrapper(func):
        assert len(types) == func.__code__.co_argcount, f"types:{types}, #args:{func.__code__.co_argcount}"   # num of positional arguments, including ones with default values
        @functools.wraps(func)
        def new_func(*args, **kwargs):
            for (a, t) in zip(args, types):
                assert isinstance(a, t), f"arg {a!r} does not match {t}"
            return func(*args, **kwargs)
        new_func.__name__ = func.__name__                       # Keep the function name
        return new_func
    return wrapper

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # list of the positional arguments
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # list of the keyword arguments
        signature = ", ".join(args_repr + kwargs_repr)           # all agruments separated by comma
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # !s: apply str(); !r: apply repr()
        return value
    return wrapper

def measure_performance(func):
    '''Measure performance of a function'''

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        finish_time = time.perf_counter()
        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print(f'Memory usage:\t\t {current / 10**6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10**6:.6f} MB ')
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
        print(f'{"-" * 40}')
    return wrapper

### END of decorator definitions

@log_datetime
def daily_backup():
    print('Daily backup job has finished.\n')  

@log_datetime2                  # Works w/o any arguments
def daily_backup2():
    print('Daily backup job has finished.\n') 

@log_datetime2                  # Cannot switch the order of decorators log_datetime2 and check_args here
@check_args(int, (int,float))
def multiply2(arg1, arg2):
    return arg1 * arg2


@debug
@measure_performance
@check_args(int)
@register_list_make_func
def make_list1(num):
    '''Range'''
    my_list = list(range(num))


@measure_performance
@register_list_make_func
def make_list2(num):
    '''List comprehension'''
    my_list = [l for l in range(num)]


@measure_performance
@register_list_make_func
def make_list3(num):
    '''Append'''
    my_list = []
    for item in range(num):
        my_list.append(item)


@measure_performance
@register_list_make_func
def make_list4(num):
    '''Concatenation'''
    my_list = []
    for item in range(num):
        my_list = my_list + [item]

@log_datetime2                  # Cannot switch the order of decorators log_datetime2 and check_args here
@check_args(int, (int,float))
def multiply2(arg1, arg2):
    return arg1 * arg2

if __name__ == '__main__':
    daily_backup()
    daily_backup2()

    print(multiply2(10, 10.55))
    print(multiply2(10, 1055))

    print(make_list1.__name__)    # w/o @functools.wraps, this prints "wrapper"
                                  # w/ @functools.wraps, this prints "make_list1"

    [ print(k, ':', v) for k, v in ListMakeFuncs.items() ]

    num = 100000
    make_list1(num)
    make_list2(num)
    make_list3(num)
    make_list4(num)


