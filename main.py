#!/usr/bin/python3
import serial
import serial.tools.list_ports
import serial_gui               #user file

plist = list(serial.tools.list_ports.comports())  #get serial list
com_num = len(plist)                              #serial list number

lable_x = 0
lable_y = 0

if com_num <= 0:
    print ("The Serial port can't find!")
else:
    print ("system all com number is",com_num)
    for index in range(com_num):
        plist_com =list(plist[index])
        serial_name = plist_com[0]
        serial_gui.gui_lable_dispaly(serial_name,lable_x,lable_y)
        lable_y=lable_y+0.1
        print ("com name is:",serial_name)

serial_gui.gui_loop()


