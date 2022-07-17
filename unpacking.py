#!/usr/bin/python3

# For argument packing and unpacking, see extended-args.py
# Unpacking: assign an iterable of values to a tuple or list of variables in a single assignment statement
# Packing:   collect several values in a single variable using the iterable unpacking operator, i.e., *

# List unpacking: number of variables needs to be the same as the length of the list
colors = ["red", "white", "blue", "purple"]
red, white, blue, purple = colors
print(red, white, blue, purple)     # red white blue purple

(red, white, blue, purple) = colors
print(red, white, blue, purple)     # red white blue purple

# Unpack selected elements and pack the rest into another list
red, *other = colors
print(red, other)                   # red ['white', 'blue', 'purple']

red, white, *other = colors
print(red, white, other)            # red white ['blue', 'purple']

red, *other, purple = colors
print(red, other, purple)           # red ['white', 'blue'] purple

*other, purple = colors
print(other, purple)                # ['red', 'white', 'blue'] purple


# Tuple unpacking
colors = ("red", "white", "blue", "purple")
red, white, blue, purple = colors
print(red, white, blue, purple)     # red white blue purple

(red, white, blue, purple) = colors
print(red, white, blue, purple)     # red white blue purple

(red, *other, purple) = colors
print(red, other, purple)           # red ['white', 'blue'] purple


# String unpacking
r, e, d = 'red'
print(r, e, d)                      # r e d

r, *other = 'red'
print(r, other)                     # r ['e', 'd']


# Unpacking dict keys
colors = {"red" : 1, "white" : 2, "blue" : 3, "purple": 4}
red, white, blue, purple = colors
print(red, white, blue, purple)     # red white blue purple

red, *other, purple = colors
print(red, other, purple)           # red ['white', 'blue'] purple

# Unpacking dict values
red, white, blue, purple = colors.values()
print(red, white, blue, purple)     # 1 2 3 4

# Unpacking dict items
red, white, blue, purple = colors.items()
print(red, white, blue, purple)     # ('red', 1) ('white', 2) ('blue', 3) ('purple', 4)

(red, white, blue, purple) = colors.items()
print(red, white, blue, purple)     # ('red', 1) ('white', 2) ('blue', 3) ('purple', 4)


# Unpacking generators
colors = ["red", "white", "blue", "purple"]
gen_color = (color for color in colors)
print(type(gen_color))              # <class 'generator'>
print(gen_color)                    # <generator object <genexpr> at 0x7fbf43bd69a8>
red, white, blue, purple = gen_color
print(red, white, blue, purple)     # red white blue purple


# Packing
colors = "red", "white", "blue", "purple"
print(type(colors))                 # <class 'tuple'>
print(colors)                       # ('red', 'white', 'blue', 'purple')


*colors, = "red", "white", "blue", "purple"   # Note the extra , after colors: starred assignment target must be in a list or tuple
print(type(colors))                 # <class 'list'>
print(colors)                       # ['red', 'white', 'blue', 'purple']


# Swap values
red, white = white, red             # Same as: temp = white; white = red; red = temp
print(red, white)                   # white red


# Drop values with dummy variable _
colors = "red", "white", "blue", "purple"
red, *_ = colors
print(red, _)                       # red ['white', 'blue', 'purple']


# Merge iterables with *
colors = "red", "white", "blue", "purple"
more_colors = ["green", *colors, "yellow"]
print(more_colors)                  # ['green', 'red', 'white', 'blue', 'purple', 'yellow']

more_colors = ("green", *colors, "yellow")
print(more_colors)                  # ('green', 'red', 'white', 'blue', 'purple', 'yellow')

more_colors = {"green", *colors, "yellow"}
print(more_colors)                  # {'green', 'yellow', 'red', 'purple', 'white', 'blue'}

colors_2 = ["green", "yellow"]
more_colors = [*colors, *colors_2]
print(more_colors)                  # ['red', 'white', 'blue', 'purple', 'green', 'yellow']


# Merge iterables with **
colors = {"red" : 1, "white" : 2, "blue" : 3, "purple": 4}
more_colors = {"green" : 0, **colors, "yellow" : 5}
print(more_colors)                  # {'green': 0, 'red': 1, 'white': 2, 'blue': 3, 'purple': 4, 'yellow': 5}

colors_2 = {"green" : 0, "yellow" : 5}
more_colors = {**colors, **colors_2}
print(more_colors)                  # {'red': 1, 'white': 2, 'blue': 3, 'purple': 4, 'green': 0, 'yellow': 5}


# Unpacking in loops
colors = [("red", 1), ("white", 2), ("blue", 3), ("purple", 4)]
for color, number in colors:
    print(color, number)
'''
red 1
white 2
blue 3
purple 4
'''

colors = [("red", 1), ("white", 2), ("blue", 3), ("purple", 4)]
for color, _ in colors:
    print(color)
'''
red
white
blue
purple
'''

