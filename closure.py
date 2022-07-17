#!/usr/bin/python3

# Python LEGB scope resolution rule: highest to lowest/narrowest to broadest order
#    Local(L): defined inside function/class
#    Enclosed(E): defined inside enclosing functions(nested function concept)
#    Global(G): defined at the uppermost level
#    Built-in(B): reserved names in Python built-in modules


from decorator import print_separator


######## Nested function and nonlocal variable ########
@print_separator
def func_enclosing1(arg):
    # This is the outer enclosing function
    # arg and var_local are both in enclosing scope
    var_local = "Local to func_enclosing"

    def func_nested():
        # This is the nested function
        # Can access variables of the enclosing scope
        # However, w/o nonlocal declaration, it creates local variables to the nested function
        print("func nested:")
        arg = 1111
        var_local = 2222
        print(arg)
        print(var_local)

    func_nested()
    print("func_enclosing:")
    print(arg)
    print(var_local)

func_enclosing1("Hello")
'''
####################
func nested:
1111
2222
func_enclosing:
Hello
Local to func_enclosing
####################
'''

@print_separator
def func_enclosing2(arg):
    # This is the outer enclosing function
    # arg and var_local are both in enclosing scope
    var_local = "Local to func_enclosing"

    def func_nested():
        # This is the nested function
        # Can access variables of the enclosing scope
        # Note the difference that nonlocal keyword makes
        nonlocal arg, var_local
        print("func nested:")
        arg = 1111
        var_local = 2222
        print(arg)
        print(var_local)

    func_nested()
    print("func_enclosing:")
    print(arg)
    print(var_local)

func_enclosing2("Hello")
'''
####################
func nested:
1111
2222
func_enclosing:
1111
2222
####################
'''

######## Criteria to create a closure ########
# must have a nested function
# nested function must refer to a value defined in the enclosing function
# enclosing function must return the nested function

@print_separator
def func_enclosing3(arg):
    var_local = "Local to func_enclosing"

    def func_nested():
        nonlocal arg, var_local
        print("func nested:")
        print(arg)
        print(var_local)

    return func_nested

func_hello = func_enclosing3("Hello")
print(func_enclosing3.__closure__)                   # (<cell at 0x7fe6c001f528: function object at 0x7fe6c0069268>>,)
print(func_enclosing3.__closure__[0].cell_contents)  # <function func_enclosing3 at 0x7fe6c0069268>
print(func_hello)                                    # <function func_enclosing3.<locals>.func_nested at 0x7fe6c0069378>
func_hello()

del func_enclosing3                                  # delete the function
# func_enclosing3("HelloAgain")                      # NameError: name 'func_enclosing3' is not defined
func_hello()                                         # still works

######## Application of closures ########
# Closures can avoid the use of global values and provides some form of data hiding
# Closures can also provide an object oriented solution to the problem
@print_separator
def closure_adder():
    total = 0
    def add(number):
        nonlocal total
        total += number
        return total
    return add

adder = closure_adder();
print(adder(10))              # 10
print(adder(50))              # 60
print(adder(100))             # 160


@print_separator
class ClassAdder:
    def __init__(self):
        self.total = 0
    
    def __call__(self,number):
        self.total += number
        return self.total

adder = ClassAdder();
print(adder(10))              # 10
print(adder(50))              # 60
print(adder(100))             # 160

@print_separator
def func_call_counter(func):
    count = 0
    def closure(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} times.")
        return func(*args, **kwargs)
    return closure

def add(a,b):
    print('Sum: ',a+b)

counter_add = func_call_counter(add)
counter_add(1, 2)               # add has been called 1 times.
                                # Sum:  3
counter_add(10, 20)             # add has been called 2 times.
                                # Sum:  30

