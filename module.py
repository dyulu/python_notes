#!/usr/bin/python3

import os
import sys
import functools
from pprint import pprint

# Environment variables
pprint(f"Env: {os.environ}")
pprint(f'Env USER: {os.environ.get("USER")}')
pprint(f'Env PYTHONPATH: {os.environ.get("PYTHONPATH")}')
print()

# Module search path:
#    current working directory
#    env PYTHONPATH
#    installation dependent default directory
pprint(f"Module search paths: {sys.path}")
print()

# Help dir()
pprint(f"Help dir():")
help(dir)

# List names in current scope
pprint(f"Names in current scope: {dir()}")
print()

# Help pages for module functools
help(functools)
print()

# List of all attributes and functions in a module
# pprint(f"All attributes and functions in module functools: {dir(functools)}\n")
print(f"All attributes and functions in module functools:")
for entry in dir(functools):
    print(repr(entry))
print()

pprint(f"Module name and location of module functools: {functools.__file__}")
pprint(f"Module name of module functools: {functools.__name__}")
pprint(f"Module docstring of module functools: {functools.__doc__}")
pprint(f"Built-in attributes accessible from module functools: {functools.__builtins__}")
pprint(f"Name and location of the cached file associated with module functools: {functools.__cached__}")
print()

# List all installed/availablle modules
help("modules")

# List of modules imported currently
pprint(f"sys.modules: {sys.modules}")

# Names in global and local namespaces
pprint(f"globals: {globals()}")
pprint(f"locals: {locals()}")

