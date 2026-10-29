"""
A package in python is to organize files. 
Files inside a package are referred as modules
modules can have functions, variables, classes.

by default : __init__.py (Dunder = double underscore) - why every package has it:
  1. Marks the folder as a regular package, so Python can import its modules
     (without it the folder is only a "namespace package", which can behave differently)
  2. Runs once, the first time the package is imported - used for setup code
     e.g. setting package-level variables, logging config
  3. Controls what the package exposes - names imported in __init__.py can be used directly
     e.g. 'from foundation.x import read_data' instead of 'from foundation.x.reader import read_data'
  4. Can define __all__ = ['read_data'] to decide what 'from package import *' brings in
  5. Can be empty - an empty __init__.py is fine and very common

python-pandas-etl
   foundation (package)
       __init__.py # treat this a package
        error.py (modules)

       x (package)
         __init__.py

       y (package)
         __init__.py  


"""

# ---------------------------------------------------------------
# 1. Importing a module from the SAME package
# ---------------------------------------------------------------
# Example: package.py and function_dates.py are both in 'foundation'
#
# a) Absolute import - full path starting from the top package
#       import foundation.function_dates
#       foundation.function_dates.standardize_date('29/10/2026')
#
# b) Import only what you need from the module
#       from foundation.function_dates import standardize_date, get_quarter
#       standardize_date('29/10/2026')
#
# c) Import with an alias (short name)
#       import foundation.function_dates as fd
#       fd.get_quarter(date(2026, 10, 29))
#
# d) Relative import - '.' means "the package I am in"
#       from .function_dates import standardize_date
#       from . import function_strings
#    Works only when the file is run as part of the package:
#       uv run python -m foundation.package      (works)
#       uv run python src/foundation/package.py  (fails: no parent package)
#
# ---------------------------------------------------------------
# 2. Importing a module from a DIFFERENT package
# ---------------------------------------------------------------
# Example structure:
#   foundation
#       __init__.py
#       x (package)
#           __init__.py
#           reader.py      -> def read_data()
#       y (package)
#           __init__.py
#           writer.py      -> wants to use read_data() from x
#
# Inside y/writer.py:
#
# a) Absolute import (recommended)
#       from foundation.x.reader import read_data
#
# b) Relative import - '..' means "go up one package level"
#       from ..x.reader import read_data      # up to foundation, then into x
#
# c) Importing an installed / third-party package works the same way
#       import pandas as pd
#       from datetime import date
#
# ---------------------------------------------------------------
# 3. What __init__.py does
# ---------------------------------------------------------------
# - Marks a folder as a package
# - Runs once, the first time the package is imported
# - Can expose names for shorter imports, e.g. in x/__init__.py:
#       from foundation.x.reader import read_data
#   then other modules can write:
#       from foundation.x import read_data
#
# ---------------------------------------------------------------
# 4. Best practices
# ---------------------------------------------------------------
# - Prefer absolute imports: clear, and they work from anywhere in the project
# - Use relative imports only inside a package, for close neighbour modules
# - Put all imports at the top of the file, in this order (blank line between groups):
#       1. standard library  (datetime, os, string)
#       2. third-party       (pandas, numpy)
#       3. your own project  (foundation.function_dates)
# - Import only what you need: 'from module import name'
# - Avoid 'from module import *' - hides where names come from and can overwrite names
# - Use common aliases: 'import pandas as pd', 'import numpy as np'
# - Never name your file the same as a standard library module
#   (e.g. collections.py, string.py, datetime.py) - it hides the real module
# - Avoid circular imports (a imports b, b imports a) - move shared code to a third module
# - Put test / demo code under: if __name__ == "__main__":
#   so it does not run when the module is imported
# - Run package modules with -m from the project directory:
#       uv run python -m foundation.<module_name>
# ---------------------------------------------------------------


