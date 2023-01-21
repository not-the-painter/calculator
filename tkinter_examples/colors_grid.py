# colors_grid.py


from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

ROWS = 5
COLUMNS = 1
PADX = 0
PADY = 0
SIDE_LENGTH = 100

colors = ['red', 'green', 'blue', 'orange']

if len(colors) != ROWS*COLUMNS:  # If not enough colors are given
    print('WARNING: Did not recieve a valid color list, using custom list')
    if len(colors) > ROWS*COLUMNS:
        colors = colors[:ROWS*COLUMNS]
    else:
        if (ROWS*COLUMNS)-len(colors) == 1:
            colors.append(colors[0])
        else:
            # Repeat the list enough times
            colors = colors*((ROWS*COLUMNS)-len(colors))

img = PhotoImage(height=1, width=1)  # To use pixels with label
for i in range(ROWS):
    for j in range(COLUMNS):
        each_color = colors[COLUMNS*i+j]  # Index each item in list
        l = Label(frame, bg=each_color, image=img, width=SIDE_LENGTH,
                  height=SIDE_LENGTH)  # Create label
        l.grid(row=i, column=j, padx=PADX, pady=PADY)

root.mainloop()
