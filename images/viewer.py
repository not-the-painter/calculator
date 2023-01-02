from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewewr App")
root.iconbitmap("images/imagefile.icns")

my_img1 = ImageTk.PhotoImage(Image.open("images/giphy.gif"))
my_img2 = ImageTk.PhotoImage(Image.open("images/38 Via Lambruschini, Capistrano, Italy.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/IMG_0134_cropped.JPG"))
my_img4 = ImageTk.PhotoImage(Image.open("images/IMG_0135.JPG"))
my_img5 = ImageTk.PhotoImage(Image.open("images/IMG_0159_cropped.JPG"))
my_img6 = ImageTk.PhotoImage(Image.open("images/my_loulou.JPG"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_num+1))
    button_back = Button(root, text="<<", command=lambda: back(image_num-1)) 

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    if image_num == my_img6:
        button_forward = Button(root, text=">>", state=DISABLED)

def back(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_num+1))
    button_back = Button(root, text="<<", command=lambda: back(image_num-1)) 

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    if image_num == my_img1:
        button_back = Button(root, text="<<", state=DISABLED)


button_back = Button(root, text = "<<", command=back, state=DISABLED)
button_exit = Button(root, text = "Exit Program", command=root.quit)
button_forward = Button(root, text = ">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
 