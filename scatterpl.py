#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 22:23:57 2018

@author: nevermind
"""

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

class mclass:

    def __init__(self, window):
        self.mylist = []
        self.mylist1 = []

        self.window = window

        self.button3 = Button(window, text="Finish & Plot", command=self.plot)
        self.button3.pack()

        var1 = StringVar()
        var1.set("X Values:")
        label1 = Label(window, textvariable=var1, height=2)
        label1.pack()


        ID1 = StringVar()
        self.box1 = Entry(window, bd=4, textvariable=ID1)
        self.box1.pack()

        var2 = StringVar()
        var2.set("Y Values:")
        label2 = Label(window, textvariable=var2, height=2)
        label2.pack()

        ID2 = StringVar()
        self.box2 = Entry(window, bd=4, textvariable=ID2)
        self.box2.pack()

        self.fig = Figure(figsize=(6, 6))
        self.a = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.get_tk_widget().pack()

    def read_inputs(self):
        x_input = self.box1.get()
        y_input = self.box2.get()


        def convert_to_float_list(x_in):
            x_input_list = x_in.split(',')
            x_floats = [float(x) for x in x_input_list]
            return x_floats


        x_array = np.array(convert_to_float_list(x_input))
        y_array = np.array(convert_to_float_list(y_input))

        return x_array,y_array


    def plot(self):
        self.a.cla()
        x,v = self.read_inputs()
        self.a.scatter(x, v, color='red')

        self.a.set_title ("Scatter Plot)", fontsize=16)
        self.a.set_ylabel("Y", fontsize=14)
        self.a.set_xlabel("X", fontsize=14)

        self.canvas.draw()

window = Tk()
start = mclass(window)
window.mainloop()