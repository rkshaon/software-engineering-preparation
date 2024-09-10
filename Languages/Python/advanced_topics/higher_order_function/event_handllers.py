# Example of Event Handlers

import tkinter as tk


def on_click():
    print("Button clicked!")


root = tk.Tk()
# Event handler: on_click
button = tk.Button(root, text="Click Me", command=on_click)
button.pack()
root.mainloop()
