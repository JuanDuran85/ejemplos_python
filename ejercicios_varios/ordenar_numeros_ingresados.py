"""[summary]

This is an example to sort numbers in a list manually.

In this case used loop, list comprehension and functions.

"""

def quick_sort(list_in):
    if not list_in:
        return list_in
    else:
        mark_in = list_in[len(list_in)//2]
        left_mark = [x for x in list_in if x < mark_in]
        center_mark = [x for x in list_in if x == mark_in]
        right_mark = [x for x in list_in if x > mark_in]
        return quick_sort(left_mark)+center_mark+quick_sort(right_mark)

list_in_numbers = []
try:
    number_order = int(input("Ingrese la cantidad de numeros que desea ordenar: "))
    for x in range(0, number_order):
        number_in = int(input(f"Ingrese el numero a ordenar {str(x+1)}: "))
        list_in_numbers.append(number_in)
    print("\n")
    print(quick_sort(list_in_numbers))
except Exception as e:
    print(f"Error --> {e}")