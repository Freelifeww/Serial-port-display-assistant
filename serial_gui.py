#!/usr/bin/python3

import tkinter


root = tkinter.Tk()

def gui_init():
    root.title('serial com display tool')
    root.geometry('500x500')

def gui_lable_dispaly(name,x,y):
    serial_label = tkinter.Label(root,text=name,bg='green')
    serial_label.place(relx=x,rely=y)

def gui_button_callback():
     print("button test")

def gui_button_dispaly():
    button = tkinter.Button(root, text ="uart tool", bg='green',command=gui_button_callback)
    button.pack()
    
def gui_Lable_dispaly():
    button = tkinter.Label(root, text ="gui lable", bg='green')
    button.pack()

def gui_loop():
    gui_button_dispaly()
    gui_Lable_dispaly()
    root.mainloop()
