# working with images, icons, and exit buttons

from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('Simple Image Viewer')

my_img = ImageTk.PhotoImage(Image.open('giphy.gif'))
my_label = Label(image=my_img)
my_label.grid(row=0, column=0)

button_quit = Button(root, text='Exit Program', command=root.quit)
button_quit.grid(row=1, column=0)


root.mainloop ()
