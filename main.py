#!/usr/bin/python3
import serial
import serial.tools.list_ports
import time
import threading

import serial_gui                #user file

def serial_loop():
    while True:
        lable_x = 0
        lable_y = 0
        plist = list(serial.tools.list_ports.comports())  #get serial list
        com_num = len(plist)                              #serial list number
        if com_num <= 0:
            print ("The Serial port can't find!")
        else:
            for index in range(com_num):
                plist_com =list(plist[index])
                serial_name = plist_com[0]
                serial_gui.gui_lable_dispaly(serial_name,lable_x,lable_y)
                lable_y=lable_y+0.1
    time.sleep(1500)

serial_gui.gui_init()

serial_thread = threading.Thread(target=serial_loop)
serial_thread.start()

gui_thread = threading.Thread(target=serial_gui.gui_loop())
gui_thread.start()
