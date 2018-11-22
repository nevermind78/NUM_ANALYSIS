#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 23:01:32 2018

@author: nevermind
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 22:23:57 2018

@author: nevermind
"""
import matplotlib.pyplot as plt
#import matplotlib
#matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

from sympy.polys.polyfuncs import interpolate

from fractions import Fraction
from sympy import *
from sympy.abc import x
init_printing()

from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)



class mclass:

    def __init__(self, window):
        self.mylist = []
        self.mylist1 = []
        self.supp=[]

        self.window = window

        self.button3 = Button(window, text="Finish & Plot", command=self.plot)
        self.button3.pack()

        var1 = StringVar()
        var1.set("X Values:")
        label1 = Label(window, textvariable=var1, height=2)
        label1.pack()


        ID1 = StringVar()
        self.box1 = Entry(window, bd=2,width=80, textvariable=ID1)
        self.box1.pack()

        var2 = StringVar()
        var2.set("Y Values:")
        label2 = Label(window, textvariable=var2, height=2)
        label2.pack()

        ID2 = StringVar()
        self.box2 = Entry(window, bd=2,width=80, textvariable=ID2)
        self.box2.pack()
        def onclick(event):
            self.a.cla()
            self.a.set_xlim([-10, 10])
            self.a.set_ylim([-10, 10])
            self.a.xaxis.set_ticks(np.arange(-10, 10, 1))
            self.a.yaxis.set_ticks(np.arange(-10, 10, 1))
            self.a.grid(True)
            #print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %(event.button, event.x, event.y, event.xdata, event.ydata))
            plt.plot(round(event.xdata), round(event.ydata), 'bo')
            self.mylist.append(str(round(event.xdata)))
            self.mylist1.append(str(round(event.ydata)))
            self.supp.append((int(round(event.xdata)),int(round(event.ydata))))
            self.a.scatter([u for u,v in iter(self.supp)],[v for u,v in iter(self.supp)], color='red')
            f=lambdify(((x,),), interpolate(self.supp,x))
            T=np.linspace(-10,10,1000)
            ft=[f(i) for i in T]
            plt.plot(T,ft,'g')
            plt.title(r"$P_n(x)="+latex(interpolate(self.supp,x))+"$",fontsize=12, color='red')
            ID1.set(self.mylist)
            ID2.set(self.mylist1)
            self.fig.canvas.draw()
            print(self.supp)
            print(interpolate(self.supp,x))
        self.fig = plt.figure()
        self.a = self.fig.add_subplot(111)
        self.a.set_xlim([-10, 10])
        self.a.set_ylim([-10, 10])
        self.a.xaxis.set_ticks(np.arange(-10, 10, 1))
        self.a.yaxis.set_ticks(np.arange(-10, 10, 1))
        self.a.grid(True)
        self.a.grid(True)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.cid = self.fig.canvas.mpl_connect('button_press_event', onclick)
        self.canvas.get_tk_widget().pack()

    def read_inputs(self):
        x_input = self.box1.get()
        y_input = self.box2.get()


        def convert_to_float_list(x_in):
            x_input_list = x_in.split(' ')
            x_floats = [float(x) for x in x_input_list]
            return x_floats
        
        x_array = np.array(convert_to_float_list(x_input))
        y_array = np.array(convert_to_float_list(y_input))

        return x_array,y_array


    def plot(self):
        self.a.cla()
        self.a.set_xlim([-10, 10])
        self.a.set_ylim([-10, 10])
        self.a.xaxis.set_ticks(np.arange(-10, 10, 1))
        self.a.yaxis.set_ticks(np.arange(-10, 10, 1))
        self.a.grid(True)
        x,v = self.read_inputs()
        self.a.scatter(x, v, color='red')

        self.a.set_title ("Scatter Plot)", fontsize=16)
        self.a.set_ylabel("Y", fontsize=14)
        self.a.set_xlabel("X", fontsize=14)

        self.canvas.draw()

window = Tk()
start = mclass(window)
window.mainloop()
