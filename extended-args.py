#!/usr/bin/python3

# When number of argements to a function is unknown, use
#     *args (Positional Arguments)
#     **kwargs (Keyword Arguments)
# args (tuple) and kwargs (dict) become iteratables

from decorator import print_separator

####==== Argument packing: * for tuples and ** for dictionaries

######## 0 or more positional arguments ########
@print_separator
def func_0_or_more_args(*args): 
    for arg in args: 
        print(arg)

# zero argument
func_0_or_more_args()

# one argument
func_0_or_more_args("Hello")

# multiple arguments
func_0_or_more_args('Hello, ', 'the', 'world', '!') 


@print_separator
def func_0_or_more_args2(*args):
    value_no_next = "No More Args"    # default value when iterator is exhausted
    i = iter(args)
    arg = next(i, value_no_next)    # use default value so it won't raise StopIteration exception when exhausted
    while arg != value_no_next:
        print(arg)
        arg = next(i, value_no_next)
    else:
        print(value_no_next)

# zero argument
func_0_or_more_args2()

# one argument
func_0_or_more_args2("Hello")

# multiple arguments
func_0_or_more_args2('Hello, ', 'the', 'world', '!') 


######## 1 or more positional arguments ########
@print_separator
def func_1_or_more_args(arg1, *args):
    print("First argument :", arg1)
    if len(args) > 0:
        print("Rest of the args:")
    for arg in args:
        print(arg)

# zero argument: TypeError: func_1_or_more_args() missing 1 required positional argument: 'arg1'
# func_1_or_more_args()

# one argument
func_1_or_more_args("Hello")

# multiple arguments
func_1_or_more_args('Hello, ', 'the', 'world', '!')


######## 0 or more keyword arguments ########
@print_separator
def func_0_or_more_kwargs(**kwargs):
    for k, w in kwargs.items():
        print(k, w)

# zero argument
func_0_or_more_kwargs()

# one argument
func_0_or_more_kwargs(virus = "Flu")

# multiple arguments
func_0_or_more_kwargs(virus = "COVID", year = "2019", wish = "for it to disappear")        


######## 1 or more keyword arguments ########
@print_separator
def func_1_or_more_kwargs(arg1 = "1stArg", **kwargs):
    print(f"First arg: {arg1}")
    for k, w in kwargs.items():
        print(k, w)

# "zero" argument: arg1 takes default value unless passed in a different value
func_1_or_more_kwargs()
func_1_or_more_kwargs(arg1 = "Cold")

# "one" argument
func_1_or_more_kwargs(virus = "Flu")
func_1_or_more_kwargs(arg1 = "Cold", virus = "Flu")

# multiple arguments
func_1_or_more_kwargs(virus = "COVID", year = "2019", wish = "for it to disappear")
func_1_or_more_kwargs(arg1 = "Cold", virus = "COVID", year = "2019", wish = "for it to disappear")
func_1_or_more_kwargs(virus = "COVID", year = "2019", wish = "for it to disappear", arg1 = "Cold")


######## 1 positional argument and 0 or more keyword arguments ########
@print_separator
def func_1_or_more_kwargs(arg1, **kwargs):
    print(f"First arg: {arg1}")
    for k, w in kwargs.items():
        print(k, w)

# zero argument: TypeError: func_1_or_more_kwargs() missing 1 required positional argument: 'arg1'
# func_1_or_more_kwargs()

# one argument
func_1_or_more_kwargs("Cold")
func_1_or_more_kwargs(arg1 = "Cold")
# func_1_or_more_kwargs(virus = "Flu")    # TypeError: func_1_or_more_kwargs() missing 1 required positional argument: 'arg1'
func_1_or_more_kwargs(arg1 = "Cold", virus = "Flu")
func_1_or_more_kwargs(virus = "Flu", arg1 = "Cold")

# multiple arguments
func_1_or_more_kwargs(arg1 = "Cold", virus = "COVID", year = "2019", wish = "for it to disappear")
func_1_or_more_kwargs(virus = "COVID", year = "2019", wish = "for it to disappear", arg1 = "Cold")


######## 0 or more positional arguments and 0 or more keyword arguments ########
@print_separator
def func_0_or_more_args_kwargs(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

func_0_or_more_args_kwargs()

func_0_or_more_args_kwargs("Cold")

func_0_or_more_args_kwargs("Cold", "Flu")

func_0_or_more_args_kwargs(virus = "COVID")

# func_0_or_more_args_kwargs(virus = "COVID", "Cold")    # SyntaxError: positional argument follows keyword argument
func_0_or_more_args_kwargs("Cold", virus = "COVID")

func_0_or_more_args_kwargs(virus = "COVID", year = "2019", wish = "for it to disappear")



####==== Argument unpacking: * for tuples and ** for dictionaries

######## use *args and **kwargs to call a function ######
@print_separator
def func_with_args(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

args = ("Cold", "Flu", "COVID")
kwargs = {"arg1" : "Cold", "arg2" : "Flu", "arg3" : "COVID"}

# Unpacking list into three argument: number of arguments must be equal to the length of the list
func_with_args(*args)

func_with_args(**kwargs)

