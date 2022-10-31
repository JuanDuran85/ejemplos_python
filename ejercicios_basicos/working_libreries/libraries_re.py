"""_summary_

    Working with re library
    
    Regular expression operations library: This module provides regular expression matching operations similar to those found in Perl.

"""

import re

# ----------------------------------------------------------------------------
# Find all python errors using re library
# ----------------------------------------------------------------------------

for i in dir(__builtins__):
    if re.match('^[A-Z]',i):
        print(i)
# ----------------------------------------------------------------------------