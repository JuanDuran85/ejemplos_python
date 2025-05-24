"""_summary_

 Working with random library

"""

import random

print("")
print("----------------------------------------------------------------------------")
# ----------------------------------------------------------------------------
print("using random - randint and shuffle")
# ----------------------------------------------------------------------------
print("----------------------------------------------------------------------------")
print("")


def list_load_fn() -> list[int]:
    """
    List load function.

    This function will return a list of ten random numbers between 1 and 100.
    """

    list_load_in: list[int] = []
    for _ in range(10):
        list_load_in.append(random.randint(1, 100))
    return list_load_in


def print_out(list_in: list) -> None:
    """
    Print out function.

    This function will print out the list that is passed in.
    """

    print(list_in)


def mix_fn(list_mix_in: list) -> None:
    """
    Shuffle the elements of a list in place.

    Args:
        list_mix_in (list): The list whose elements are to be shuffled.

    Returns:
        None: This function returns nothing. It modifies the input list in place.
    """

    random.shuffle(list_mix_in)


if __name__ == '__main__':
    list_load: list[int] = list_load_fn()
    print("List Done...")
    print_out(list_load)
    mix_fn(list_load)
    print("Mix List...")

print("")
print("----------------------------------------------------------------------------")
# ----------------------------------------------------------------------------
print("using random - choice to generate a password")
# ----------------------------------------------------------------------------
print("----------------------------------------------------------------------------")
print("")

PASSWORD_RESULT = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)') for _ in range(10)])
print(f"Result = {PASSWORD_RESULT}")
