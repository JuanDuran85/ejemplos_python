"""_summary_

    Calculadora con Tkinter

"""
from tkinter import Tk, Label, Entry, Button, Frame, StringVar, IntVar, END, W, E, S, N, messagebox

root: Tk = Tk()
root.title("Calculadora")
root.resizable(False, False)

# variables
i: int = 0
reset_variable: StringVar = StringVar()

# display calculator
display: Entry = Entry(root, textvariable=reset_variable)
display.grid(row=1, columnspan=6, sticky=W + E)

# functions

# get numbers from keyboard
def get_numbers_keyboard(n: int) -> None:
    global i
    display.insert(i,n)
    i+=1

# get operations
def get_operations(op: str) -> None:
    global i
    operatior_len: int = len(op)
    display.insert(i,op)
    i+=operatior_len
    
def reset_display() -> None:
    # display.delete(0, END)
    reset_variable.set('')
    
def undo_functions() -> None:
    display_state: str = display.get()
    if len(display_state):
        displa_new_state: str = display_state[:-1]
        reset_display()
        display.insert(0,displa_new_state)
    else:
        reset_display()
        display.insert(0,"Error")
        
def calculate_functions() -> None:
    display_state: str = display.get()
    try:
        result = eval(display_state)
        print(result)
        reset_display()
        display.insert(0,result)
    except Exception as e:
        reset_display()
        print(f"Error: {e}")
    
# numeric bottons
Button(root, text="1", command=lambda: get_numbers_keyboard(1)).grid(row=2, column=0, sticky=W + E)
Button(root, text="2", command=lambda: get_numbers_keyboard(2)).grid(row=2, column=1, sticky=W + E)
Button(root, text="3", command=lambda: get_numbers_keyboard(3)).grid(row=2, column=2, sticky=W + E)

Button(root, text="4", command=lambda: get_numbers_keyboard(4)).grid(row=3, column=0, sticky=W + E)
Button(root, text="5", command=lambda: get_numbers_keyboard(5)).grid(row=3, column=1, sticky=W + E)
Button(root, text="6", command=lambda: get_numbers_keyboard(6)).grid(row=3, column=2, sticky=W + E)

Button(root, text="7", command=lambda: get_numbers_keyboard(7)).grid(row=4, column=0, sticky=W + E)
Button(root, text="8", command=lambda: get_numbers_keyboard(8)).grid(row=4, column=1, sticky=W + E)
Button(root, text="9", command=lambda: get_numbers_keyboard(9)).grid(row=4, column=2, sticky=W + E)

# other buttons
Button(root, text="AC",command=lambda: reset_display()).grid(row=5, column=0, sticky=W + E)
Button(root, text="0", command=lambda: get_numbers_keyboard(0)).grid(row=5, column=1, sticky=W + E)
Button(root, text="%", command=lambda: get_operations("%")).grid(row=5, column=2, sticky=W + E)

# operations buttons
Button(root, text="+", command=lambda: get_operations("+")).grid(row=2, column=3, sticky=W + E)
Button(root, text="-", command=lambda: get_operations("-")).grid(row=3, column=3, sticky=W + E)
Button(root, text="*", command=lambda: get_operations("*")).grid(row=4, column=3, sticky=W + E)
Button(root, text="/", command=lambda: get_operations("/")).grid(row=5, column=3, sticky=W + E)

# others operations buttons
Button(root, text="←", command=lambda: undo_functions()).grid(row=2, column=4, columnspan=2, sticky=W + E)
Button(root, text="exp", command=lambda: get_operations("**")).grid(row=3, column=4, sticky=W + E)
Button(root, text="^2", command=lambda: get_operations("^2")).grid(row=3, column=5, sticky=W + E)
Button(root, text="(", command=lambda: get_operations('(')).grid(row=4, column=4, sticky=W + E)
Button(root, text=")", command=lambda: get_operations(')')).grid(row=4, column=5, sticky=W + E)
Button(root, text="=", command=lambda: calculate_functions()).grid(row=5, column=4, columnspan=2, sticky=W + E)

root.mainloop()