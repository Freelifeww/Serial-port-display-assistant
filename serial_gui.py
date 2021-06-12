#!/usr/bin/python3
import tkinter

root = tkinter.Tk()

def gui_lable_dispaly(name,x,y):
        root.title('serial com')
        root.geometry('200x200')
        serial_label = tkinter.Label(root,text=name)
        serial_label.place(relx=x,rely=y)

def gui_loop():
    root.mainloop()