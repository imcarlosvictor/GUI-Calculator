from tkinter import *
from tkinter import ttk
from tkinter import messagebox


inputs = []


def button_click(e):
    """
    Appends and displays the value of the inputs.

    inputs displays value entered
    equation display the entire equation
    """
    inputs.append(e)
    # display.config(text=e)
    # Print equation
    inputs_to_string = map(str, inputs)
    equation = ''.join(inputs_to_string)
    equation_display.config(text=equation)


def delete():
    """Removes most recent element appended."""
    inputs.pop()
    display.config(text='')
    inputs_to_string = map(str, inputs)
    equation = ''.join(inputs_to_string)
    equation_display.config(text=equation)


def clear():
    """Removes all elements in inputs."""

    inputs.clear()
    display.config(text='')
    equation_display.config(text='')


def equals():
    """
    Evaluates the equation and returns the value.

    Mutates the element into strings, joins them and evaluates the equation.
    """
    input_strings = map(str, inputs)
    input_equation = ''.join(input_strings)
    try:
        total = eval(input_equation)
        display.config(text=total)
    except SyntaxError:
        messagebox.showinfo(message='Invalid format')
    else:
        display.config(text=total)


# Application window
root = Tk()
root.title('Calculator')


# Frame
mainframe = ttk.Frame(root)
screen = ttk.Frame(mainframe)
keypad = ttk.Frame(mainframe, padding='5')
keypad.configure(relief='raised')


# Output screen
# Placed in grid | frame: screen
display = ttk.Label(screen, text='')
display.config(font='30')
display.grid(column=0, row=0)

equation_display = ttk.Label(screen, text='')
equation_display.grid(column=0, row=1)

# Keypads
# Numbers
decimal = ttk.Button(keypad, text='.',
                     command=lambda: button_click('.')).grid(column=1, row=6)
zero = ttk.Button(keypad, text='0',
                  command=lambda: button_click(0)).grid(column=2, row=6)
one = ttk.Button(keypad, text='1',
                 command=lambda: button_click(1)).grid(column=1, row=5)
two = ttk.Button(keypad, text='2',
                 command=lambda: button_click(2)).grid(column=2, row=5)
three = ttk.Button(keypad, text='3',
                   command=lambda: button_click(3)).grid(column=3, row=5)
four = ttk.Button(keypad, text='4',
                  command=lambda: button_click(4)).grid(column=1, row=4)
five = ttk.Button(keypad, text='5',
                  command=lambda: button_click(5)).grid(column=2, row=4)
six = ttk.Button(keypad, text='6',
                 command=lambda: button_click(6)).grid(column=3, row=4)
seven = ttk.Button(keypad, text='7',
                   command=lambda: button_click(7)).grid(column=1, row=3)
eight = ttk.Button(keypad, text='8',
                   command=lambda: button_click(8)).grid(column=2, row=3)
nine = ttk.Button(keypad, text='9',
                  command=lambda: button_click(9)).grid(column=3, row=3)


# Operators
btn_divide = ttk.Button(keypad, text='/',
                        command=lambda: button_click('/')).grid(column=4, row=2)
btn_multiply = ttk.Button(keypad, text='*',
                          command=lambda: button_click('*')).grid(column=4, row=3)
btn_subtract = ttk.Button(keypad, text='-',
                          command=lambda: button_click('-')).grid(column=4, row=4)
btn_plus = ttk.Button(keypad, text='+',
                      command=lambda: button_click('+')).grid(column=4, row=5)
btn_equals = ttk.Button(keypad, text='=',
                        command=lambda: equals()).grid(column=4, row=6)


# Special
btn_clear = ttk.Button(keypad, text='C',
                       command=lambda: clear()).grid(column=1, row=1)
btn_open_brackets = ttk.Button(keypad, text='(',
                               command=lambda: button_click('(')).grid(column=1, row=2)
btn_close_bracket = ttk.Button(keypad, text=')',
                               command=lambda: button_click(')')).grid(column=2, row=2)
btn_delete = ttk.Button(keypad, text='Del',
                        command=lambda: delete()).grid(column=3, row=6)
btn_percent = ttk.Button(keypad, text='%',
                         command=lambda: button_click('%')).grid(column=3, row=2)


# Grid
mainframe.grid(column=0, row=2)  # Define grid
screen.grid(column=0, row=1)  # Placement in grid
keypad.grid(column=0, row=2)  # Placement in grid


if __name__ == '__main__':
    root.mainloop()
