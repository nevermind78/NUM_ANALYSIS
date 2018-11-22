#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 00:35:33 2018

@author: nevermind
"""

from tkinter import*

class MyGUI:
  def __init__(self):
    self.__mainWindow = Tk()
    #self.fram1 = Frame(self.__mainWindow)
    self.labelText = 'Enter amount to deposit'
    self.depositLabel = Label(self.__mainWindow, text = self.labelText)
    self.depositEntry = Entry(self.__mainWindow, width = 10)
    self.depositEntry.bind('<Return>', self.depositCallBack)
    self.depositLabel.pack()
    self.depositEntry.pack()

    mainloop()

  def depositCallBack(self,event):
    self.depositLabel['text'] = 'change the value'
    print(self.labelText)

myGUI = MyGUI()