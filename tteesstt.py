#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 22:37:56 2018

@author: nevermind
"""
from tkinter import *
import matplotlib.pyplot as mpl
import tkinter as tk 
import numpy as np 
outl=[]
index = []
list_rep = []
def on_pick(event):
        thisline = event.artist
        xdata, ydata = thisline.get_data()
        tmp = []

        index.append(i)
        ind = event.ind
        tmp.append(list(xdata[ind])[0])
        tmp.append(list(ydata[ind])[0])
        outl.append(tmp)


        #print('on pick line:', zip(xdata[ind], ydata[ind]))

new_ydata1 = []
new_ydata2 = []
new_ydata3 = []
root = tk.Tk()
for i in range(3):
        win = tk.Toplevel(master=root)
        #win.title(text="Embed in Tk")
        ydata1 = np.array(Max_Correct_1[i])
        ydata2 = np.array(Max_Correct_2[i])
        ydata3 = np.array(Max_Correct_3[i])

        Aveg=np.array(Avg[i])


        f = Figure(figsize=(5,4), dpi=100)
        ax1 = f.add_subplot(111)

        ax1.axis([-9.5,-4.0,-10,105])
        ax1.plot(Log_Values_Array,ydata1,'o',picker=7)
        ax1.plot(Log_Values_Array,ydata2,'*',picker=7)
        ax1.plot(Log_Values_Array,ydata3,'^',picker=7)
        ax1.plot(Log_Values_Array,Aveg,'b--')

        canvas = FigureCanvasTkAgg(f, master=root)

        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=Tk.BOTH, expand=1)


        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        canvas.mpl_connect('pick_event',on_pick)




        print(outl)



        canvas.get_tk_widget().delete("all")
        outl=[]
        index = []
root.mainloop()