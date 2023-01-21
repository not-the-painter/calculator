from tkinter import *

root = Tk()
root.minsize(height=300, width=400)
root.title("Test App")

BLANK = " "*40


def redraw():
    l = Label(root, text=("You clicked the button!!"))
    # l.pack()
    l.grid(row=0, column=0)


def redraw2():
    l = Label(root, text=(BLANK))
    l.grid(row=0, column=0)


theLabel = Label(root, text="DO NOT click the button.")
# theLabel.pack()
theLabel.grid(row=0, column=0)
theButton = Button(root, padx=5, pady=5, text="Click Me", command=redraw)
# theButton.pack()
theButton.grid(row=1, column=0)
theButton2 = Button(root, padx=5, pady=5, text="Clear", command=redraw2)
# theButton2.pack()
theButton2.grid(row=1, column=1)


root.mainloop()
