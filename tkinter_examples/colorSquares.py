# colorSquares.py


from tkinter import *


class SquareGenerator(Frame):  # Inherit from tkinter Frame
    def __init__(self, parent: Tk, color_lst: list, rows: int, columns: int, side: int, padx: int = 0, pady: int = 0, *args, **kwargs):

        Frame.__init__(self, parent, *args, **kwargs)
        img = PhotoImage(height=1, width=1)  # To use pixels with label

        if len(color_lst) != rows*columns:  # If not enough colors are given
            print('WARNING: Did not recieve a valid color list, using custom list')
            if len(color_lst) < rows*columns:
                if (rows*columns)-len(color_lst) == 1:
                    color_lst.append(color_lst[0])
                else:
                    # Repeat the list enough times
                    color_lst = color_lst*((rows*columns)-len(color_lst))
            else:
                color_lst = color_lst[:rows*columns]

        # Table loop
        for i in range(rows):
            for j in range(columns):
                each_color = color_lst[columns*i+j]  # Index each item in list
                l = Label(self, bg=each_color, image=img,
                          width=side, height=side)  # Create label
                l.grid(row=i, column=j, padx=padx, pady=pady)


if __name__ == '__main__':
    root = Tk()

    colors = ['red', 'green', 'blue', 'orange']
    # Replicate microsoft logo ;)
    gen = SquareGenerator(root, colors, rows=5, columns=1, side=100)
    gen.pack()

    root.mainloop()
