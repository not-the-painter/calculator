import tkinter

#  create window
root = tkinter.Tk()
root.title("Calculator App")

expression = ""


# create the functions (global variables are bad but this works for now)
def write(val):
    global expression
    if expression == "0":
        expression = ""
    expression += val
    label_result.config(text=expression)


def clear():
    global expression
    expression = "0"
    label_result.config(text=expression)


def calculate():
    global expression
    if expression == "ERROR":
        result = "ERROR"
    elif expression != "":
        try:
            # eval can be bad but should be harmless in this case
            result = eval(expression)
        except (ZeroDivisionError, SyntaxError):
            result = "ERROR"
    else:
        result = ""
    label_result.config(text=result)
    expression = str(result)


label_result = tkinter.Label(root, text="0")
label_result.grid(row=0, column=0, columnspan=4)

button7 = tkinter.Button(root, text="7", command=lambda: write("7"))
button7.grid(row=1, column=0)

button8 = tkinter.Button(root, text="8", command=lambda: write("8"))
button8.grid(row=1, column=1)

button9 = tkinter.Button(root, text="9", command=lambda: write("9"))
button9.grid(row=1, column=2)

button_div = tkinter.Button(root, text="/", command=lambda: write("/"))
button_div.grid(row=1, column=3)

button4 = tkinter.Button(root, text="4", command=lambda: write("4"))
button4.grid(row=2, column=0)

button5 = tkinter.Button(root, text="5", command=lambda: write("5"))
button5.grid(row=2, column=1)

button6 = tkinter.Button(root, text="6", command=lambda: write("6"))
button6.grid(row=2, column=2)

button_mult = tkinter.Button(root, text="*", command=lambda: write("*"))
button_mult.grid(row=2, column=3)

button1 = tkinter.Button(root, text="1", command=lambda: write("1"))
button1.grid(row=3, column=0)

button2 = tkinter.Button(root, text="2", command=lambda: write("2"))
button2.grid(row=3, column=1)

button3 = tkinter.Button(root, text="3", command=lambda: write("3"))
button3.grid(row=3, column=2)

button_add = tkinter.Button(root, text="+", command=lambda: write("+"))
button_add.grid(row=3, column=3)

button_clear = tkinter.Button(root, text="C", command=lambda: clear())
button_clear.grid(row=4, column=0)

button0 = tkinter.Button(root, text="0", command=lambda: write("0"))
button0.grid(row=4, column=1)

button_dot = tkinter.Button(root, text=".", command=lambda: write("."))
button_dot.grid(row=4, column=2)

button_subt = tkinter.Button(root, text="-", command=lambda: write("-"))
button_subt.grid(row=4, column=3)

button_eq = tkinter.Button(root, text="=", width=16,
                           command=lambda: calculate())
button_eq.grid(row=5, column=0, columnspan=4)

root.mainloop()
