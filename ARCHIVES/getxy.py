#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 22:30:35 2018

@author: nevermind
"""

from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import tkinter.simpledialog

root = Tk()

#setting up a tkinter canvas
w = Canvas(root, width=1000, height=1000)
w.pack()

#adding the image
File = askopenfilename(parent=root, initialdir="./",title='Select an image')
original = Image.open(File)
original = original.resize((1000,1000)) #resize image
img = ImageTk.PhotoImage(original)
w.create_image(0, 0, image=img, anchor="nw")

#ask for pressure and temperature extent
xmt = tkinter.simpledialog.askfloat("Temperature", "degrees in x-axis")
ymp = tkinter.simpledialog.askfloat("Pressure", "bars in y-axis")

#ask for real PT values at origin
xc = tkinter.simpledialog.askfloat("Temperature", "Temperature at origin")
yc = tkinter.simpledialog.askfloat("Pressure", "Pressure at origin")

#instruction on 3 point selection to define grid
tkinter.messagebox.showinfo("Instructions", "Click: \n" 
                                            "1) Origin \n"
                                            "2) Temperature end \n"
                                            "3) Pressure end")

# From here on I have no idea how to get it to work...

# Determine the origin by clicking
def getorigin(eventorigin):
    global x0,y0
    x0 = eventorigin.x
    y0 = eventorigin.y
    print(x0,y0)
    w.bind("<Button 1>",getextentx)
#mouseclick event
w.bind("<Button 1>",getorigin)

# Determine the extent of the figure in the x direction (Temperature)
def getextentx(eventextentx):
    global xe
    xe = eventextentx.x
    print(xe)
    w.bind("<Button 1>",getextenty)

# Determine the extent of the figure in the y direction (Pressure)
def getextenty(eventextenty):
    global ye
    ye = eventextenty.y
    print(ye)
    tkinter.messagebox.showinfo("Grid", "Grid is set. You can start picking coordinates.")
    w.bind("<Button 1>",printcoords)

#Coordinate transformation into Pressure-Temperature space
def printcoords(event):
    xmpx = xe-x0
    xm = xmt/xmpx
    ympx = ye-y0
    ym = -ymp/ympx

    #coordinate transformation
    newx = (event.x-x0)*(xm)+xc
    newy = (event.y-y0)*(ym)+yc

    #outputting x and y coords to console
    print (newx,newy)

root.mainloop()
