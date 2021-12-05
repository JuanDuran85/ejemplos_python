# prueba de la funcion match con python 3.10
numbers = [1,2,3,4]
for n in numbers:
    match n:
        case 1:
            print("Number is 1")
        case 2:
            print("Number is 2")
        case 3:
            print("Number is 3")
        case _:
            print("Number is not 1,2 or 3")