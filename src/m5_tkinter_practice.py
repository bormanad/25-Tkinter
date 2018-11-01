"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Drew Borman.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    root = tkinter.Tk()

    # ------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame = ttk.Frame(root, padding=30)
    frame.grid()

    # ------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    go_forward_button = ttk.Button(frame, text='Forward')
    go_forward_button.grid()
    # ------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    go_forward_button['command'] = (lambda:
                                    own_function())

    # ------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    my_entry_box = ttk.Entry(frame)
    my_entry_box.grid()
    print_entry_button = ttk.Button(frame, text='Print Entry')
    print_entry_button.grid()
    print_entry_button['command'] = (lambda:
                                     print_contents(my_entry_box))
    # ------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    second_entry = ttk.Entry(frame)
    second_entry.grid()
    print_all_button = ttk.Button(frame, padding=10)
    print_all_button.grid()
    print_all_button['command'] = (lambda: print_all(my_entry_box, second_entry))



    # ------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    root.mainloop()


def own_function():
    print('hello')


def print_contents(my_entry):
    contents = my_entry.get()
    if contents == 'ok':
        print('Hello')
    else:
        print('Goodbye')




def print_all(first, second):
    contents = first.get()
    contents_second = second.get()
    n = int(contents_second)
    print(n*contents)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
