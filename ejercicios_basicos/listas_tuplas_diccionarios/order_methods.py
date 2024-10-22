"""_summary_
    Ordered list with methods like bubbling

"""


def bubble_method(list_in: list):
    """_summary_

    Args:
        list_in (list): _description_
    """
    # First: go through each element of the list
    for i in range(len(list_in)):
        # Second: compare the elements of the list thar are not sorted yet and
        # swap them if necessary
        for j in range(len(list_in)-i-1):
            if list_in[j] > list_in[j+1]:
                # using tuples assignment
                list_in[j], list_in[j+1] = list_in[j+1], list_in[j]


if __name__ == '__main__':
    list_to_order: list = [5, 7, 3, 6, 8, 1, 0, -5, -6, -3]
    bubble_method(list_to_order)
    print(f"{list_to_order=}")
