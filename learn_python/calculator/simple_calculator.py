from tkinter import *

root = Tk()
root.title("Simple calculator")

display = Entry(root, width=20, borderwidth=4)
display.grid(row=0, column=0, columnspan=3)
display.insert(0, "0") # Insert 0 as default number

zero = True
operation = 0

#MATHEMATICAL OPERATIONS
def add(num):                                       # Save first number and set operation on "add"
    global operation, f_num
    f_num = int(num)
    display.delete(0, END)
    operation = 1

def minus(num):                                     # Save first number and set operation on "minus"
    global operation, f_num
    f_num = int(num)
    display.delete(0, END)
    operation = 2

def multiply(num):                                  # Save first number and set operation on "multiply"
    global operation, f_num
    f_num = int(num)
    display.delete(0, END)
    operation = 3

def divide(num):                                    # Save first number and set operation on "divide"
    global operation, f_num
    f_num = int(num)
    display.delete(0, END)
    operation = 4


#DISPLAY FUNCTIONS
def add_number(number):
    global zero
    if zero:                                        # To delete default first number, which is 0
        display.delete(0, END)
        zero = False
    
    i = display.get()
    display.delete(0, END)          
    display.insert(0, str(i) + str(number))         # Add numbers next to it selfs

def clean():                                        # Clean Entry and set first number to 0
    display.delete(0, END)
    f_num = 0

def equel(sec_num):                                 # Execute operations with first and second number
    display.delete(0, END)
    
    if operation == 1:
        display.insert(0, f_num + int(sec_num))
    elif operation == 2:
        display.insert(0, f_num - int(sec_num))
    elif operation == 3:
        display.insert(0, f_num * int(sec_num))
    elif operation == 4:
        display.insert(0, int(f_num / int(sec_num))) # Insure that result won't be in float
      

#####BUTTONS#####
button_0 = Button(root, text="0", padx=20, pady=10, command=lambda: add_number(0)).grid(row=4, column=0)
button_1 = Button(root, text="1", padx=20, pady=10, command=lambda: add_number(1)).grid(row=3, column=0)
button_2 = Button(root, text="2", padx=20, pady=10, command=lambda: add_number(2)).grid(row=3, column=1)
button_3 = Button(root, text="3", padx=20, pady=10, command=lambda: add_number(3)).grid(row=3, column=2)
button_4 = Button(root, text="4", padx=20, pady=10, command=lambda: add_number(4)).grid(row=2, column=0)
button_5 = Button(root, text="5", padx=20, pady=10, command=lambda: add_number(5)).grid(row=2, column=1)
button_6 = Button(root, text="6", padx=20, pady=10, command=lambda: add_number(6)).grid(row=2, column=2)
button_7 = Button(root, text="7", padx=20, pady=10, command=lambda: add_number(7)).grid(row=1, column=0)
button_8 = Button(root, text="8", padx=20, pady=10, command=lambda: add_number(8)).grid(row=1, column=1)
button_9 = Button(root, text="9", padx=20, pady=10, command=lambda: add_number(9)).grid(row=1, column=2)

button_add = Button(root, text="+", padx=20, pady=10, command=lambda: add(display.get())).grid(row=1, column=3)
button_minus = Button(root, text="-", padx=20, pady=10, command=lambda: minus(display.get())).grid(row=2, column=3)
button_multiply = Button(root, text="*", padx=20, pady=10, command=lambda: multiply(display.get())).grid(row=3, column=3)
button_divide = Button(root, text="÷", padx=20, pady=10, command=lambda: divide(display.get())).grid(row=4, column=3)

button_clean = Button(root, text="CL", padx=20, pady=10, command=clean).grid(row=4, column=1)
button_equel = Button(root, text="=", padx=20, pady=10, command=lambda: equel(display.get())).grid(row=4, column=2)
#####BUTTONS#####

root.mainloop() # Looping screen
