#!/usr/bin/python3
import tkinter



root = tkinter.Tk()

def gui_init():
    root.title('serial com')
    root.geometry('100x100')

def gui_lable_dispaly(name,x,y):
        serial_label = tkinter.Label(root,text=name,bg='green')
        serial_label.place(relx=x,rely=y)

def gui_loop():
    root.mainloop()