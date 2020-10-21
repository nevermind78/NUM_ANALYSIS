#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon, Dec 10 2018

@author: Tass
"""

from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class mclass:

    def __init__(self, window):
        self.window = window

        varTitle = StringVar()
        varTitle.set("Phenomène de  Runge")
        labelTitle = Label(window, textvariable=varTitle, fg="#2F4F4F", height=2)
        labelTitle.grid(row=0, columnspan=3, sticky=S, padx=10)

        var1 = StringVar()
        var1.set("Construire sur [a, b] le polynôme d’interpolation de Lagrange de la fonction f(x),") #\n
        label1 = Label(window, textvariable=var1, height=1)
        label1.grid(row=1, columnspan=3, sticky=W, padx=20)

        var2 = StringVar()
        var2.set("d’une part en prenant des abscisses d’interpolation équidistants, d’autre part en  ")
        label2 = Label(window, textvariable=var2, height=1)
        label2.grid(row=2, columnspan=3, sticky=W, padx=20)

        var3 = StringVar()
        var3.set("choisissant les points de Tchebychev. ")
        label3 = Label(window, textvariable=var3, height=1)
        label3.grid(row=3, columnspan=3, sticky=W, padx=20)
        varF = StringVar()

        varF.set("La fonction, f(x) :")
        labelF = Label(window, textvariable=varF, height=2)
        labelF.grid(row=4, sticky=W, pady=10, padx=20)

        idF = StringVar()
        self.boxF = Entry(window, bd=4, width=40, textvariable=idF)
        self.boxF.grid(row=4, column=2, pady=10, padx=10)

        varA = StringVar()
        varA.set("La borne inférieur, a :")
        labelA = Label(window, textvariable=varA, height=2)
        labelA.grid(row=5, sticky=W, pady=10, padx=20)

        idA = StringVar()
        self.boxA = Entry(window, bd=4, width=40, textvariable=idA)
        self.boxA.grid(row=5, column=2, pady=10, padx=10)

        varB = StringVar()
        varB.set("La borne supérieur, b :")
        labelB = Label(window, textvariable=varB, height=2)
        labelB.grid(row=6, sticky=W, pady=10, padx=20)

        idB = StringVar()
        self.boxB = Entry(window, bd=4, width=40, textvariable=idB)
        self.boxB.grid(row=6, column=2, pady=10, padx=10)

        varN = StringVar()
        varN.set("N (Points de Tchebychev) :")
        labelN = Label(window, textvariable=varN, height=2)
        labelN.grid(row=7, sticky=W, pady=10, padx=20)

        idN = StringVar()
        self.boxN = Entry(window, bd=4, width=40, textvariable=idN)
        self.boxN.grid(row=7, column=2, pady=10, padx=10)

        self.button1 = Button(window, text="  PLOT  ", bg="#2F4F4F", fg="white",width=20, command=self.plot)
        self.button1.grid(row=8, column=2, sticky=E, pady=20, padx=20)

    def plot(self):
        try:
            N = int(self.boxN.get())
            a = float(self.boxA.get())
            b = float(self.boxB.get())
            F = self.boxF.get().lower().replace(' ', '')

            f = lambda x: eval(F)

            X = np.linspace(a, b, N)
            p = np.polyfit(X, f(X), N - 1)
            t = np.linspace(a, b, 1000)

            self.fig = plt.figure(figsize=(7, 5.5))
            self.a = self.fig.add_subplot(211)
            self.a.grid(True)
            self.a.plot(t, f(t), 'r', label='f(x)')
            self.a.plot(X, f(X), '.b')
            self.a.plot(t, np.polyval(p, t), 'g', label='interpolation polynômiale de f(x)')
            self.a.plot(t, f(t) - np.polyval(p, t), 'b', label='Erreur d interpolation')
            self.a.set_title("Interpolation Equidistante", color="#5F4C0B")
            self.a.set_xlabel('x')
            self.a.legend()

            xi = [None] * N
            yi = [None] * N
            for k in range(0,N):
                xi[k] = (a + b) / 2 + (a - b) / 2 * math.cos((k) / (N-1) * math.pi)
                yi[k] = f(xi[k])

            pt = np.polyfit(xi, yi, N)

            self.b = self.fig.add_subplot(212)
            self.b.grid(True)
            self.b.plot(t, f(t), 'r', label='f(x)')
            self.b.plot(xi, yi, '.b')
            self.b.plot(t, np.polyval(pt, t),'g', label='interpolation polynômiale de f(x)')
            self.b.plot(t, f(t) - np.polyval(pt, t), 'b', label='Erreur d interpolation')
            self.b.set_title('Interpolation Tchebychev', color="#5F4C0B")
            self.b.set_xlabel('x')
            self.b.legend()

            self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
            self.canvas.get_tk_widget().grid(row=3, column=3, rowspan=6, pady=10, padx=10)
        except ValueError:
            messagebox.showwarning("ValueError", "Veuillez vérifier votre saisie")


if __name__ == '__main__':
    window = Tk()
    window.title('Phénomène de  Runge')
    window.resizable(width=True, height=True)
    window.geometry('+0+0')
    start = mclass(window)
    window.mainloop()





