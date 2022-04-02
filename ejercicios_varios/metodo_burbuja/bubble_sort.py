"""_summary_

    Implementation of the Bubble Sort algorithm

"""

def bubble_sort(our_list: list) -> None:
    # we go through the list as many times as there are elements
    for _ in range(len(our_list)):
        # we want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            # if the first element is greater than the second element
            if our_list[j] > our_list[j + 1]:
                # we swap them
                our_list[j], our_list[j + 1] = our_list[j + 1], our_list[j]
                print(our_list)


list_number: list = [4,3,1,5,6,2,7,9,8]
bubble_sort(list_number)