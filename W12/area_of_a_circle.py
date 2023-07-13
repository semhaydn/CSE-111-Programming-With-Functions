# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of a Circle Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Radius:"
    lbl_radius = Label(frm_main, text="Radius of the circle is ")

    # Create an integer entry box where the user will enter the radius of the circle.
    ent_radius = IntEntry(frm_main, width=4, lower_bound=0,)

    # Create a label that displays "Radius"
    lbl_radius_units = Label(frm_main, text="metric units")

    # Create a label that displays "Area:"
    lbl_areas = Label(frm_main, text="Area:")

    # Create labels that will display the results.
    lbl_area = Label(frm_main, width=15)
    lbl_area_units = Label(frm_main, text="square metric unit")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(      row=0, column=0, padx=3, pady=3)
    ent_radius.grid(      row=0, column=1, padx=3, pady=3)
    lbl_radius_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_areas.grid(     row=1, column=0, padx=(30,3), pady=3)
    lbl_area.grid(      row=1, column=2, padx=4, pady=4)
    lbl_area_units.grid(row=1, column=3, padx=0, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")


    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the area
        """
        try:
            # Get the radius from the input.
            radius = ent_radius.get()

            # Compute the circles area
            area = math.pi * (radius * radius)


            # Display the area
            lbl_area.config(text=f"{area:.4f}")

        except ValueError:
            # When the user deletes all the digits in the radius
            # entry box, clear the slowest and fastest labels.
            lbl_area.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_radius.clear()
        lbl_area.config(text="")
        ent_radius.focus()

    # Bind the calculate function to the radius entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_radius.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the radius entry box.
    ent_radius.focus()


# If this file is executed like this:
# > python area_of_a_circle.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
