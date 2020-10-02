#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:42:55 2018

@author: nevermind
"""

from tkinter import *

root = Tk()

entry = []

def command(entry):
    output = []
    for i in range(len(entry)):
        output.append(entry[i].get())
    print(output)

for i in range(10):
    entry.append(Entry(root))
    entry[i].pack()

Button(root, text="Ok", command=lambda:command(entry)).pack()

root.mainloop()
