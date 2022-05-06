"""_summary_

    Working with types library
    
    MappingProxyType: is a proxy class that is used to create read-only views of mappings, like a read-only dictionary.

"""

from types import MappingProxyType


mutable_dictionary: dict = {
    'a': 1,
    'b': 2, 
    'c': 3,
    'd': 4,
}

inmutable_dictionary: MappingProxyType = MappingProxyType(mutable_dictionary)
# are the same
print(f"{mutable_dictionary = }")
print(f"{inmutable_dictionary = }")
# but, if you want to change a value in the read-only dictionary, you will get an error

try:
    inmutable_dictionary['a'] = 10
except Exception as e:
    print(f"Error: {e}")