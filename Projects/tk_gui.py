
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from numpy import sin ,cos,exp,log,sqrt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
class mclass:
    def __init__(self,  window):
        self.window = window
        self.fr1 = Frame(window,highlightbackground="gray", highlightthickness=2, width=100, height=100, bd= 5)
        self.fr2 = Frame(window,highlightbackground="darkgray", highlightthickness=2, width=100, height=100, bd= 5)
        self.func_txt=StringVar()
        self.func_txt.set("L'expression de f :")
        self.label_func=Label(self.fr1, textvariable=self.func_txt,justify=RIGHT, height=4)
        self.label_func.grid(row=1,column=0)
        self.a_txt=StringVar()
        self.a_txt.set("a:")
        self.label_a=Label(self.fr1, textvariable=self.a_txt,justify=RIGHT, anchor="w", height=4)
        self.label_a.grid(sticky = E,row=2,column=0)
        self.boxa = Entry(self.fr1,width=10,borderwidth=3,bg="powder blue")
        self.boxa.grid(sticky = W,row=2,column=1)
        self.b_txt=StringVar()
        self.b_txt.set("b:")
        self.label_b=Label(self.fr1, textvariable=self.b_txt,justify=RIGHT, anchor="w", height=4)
        self.label_b.grid(sticky = E,row=3,column=0)
        self.boxb = Entry(self.fr1,width=10,borderwidth=3,bg="powder blue")
        self.boxb.grid(sticky = W,row=3,column=1)
        self.box = Entry(self.fr1,borderwidth=3,bg="powder blue")
        self.box.grid(row=1,column=1)
        self.button = Button (self.fr1, width =35,text="plot",bg="powder blue", command=self.plot)
        self.button.grid(row=4,column=0,columnspan=3)
        self.fr1.grid(row=1,column=0,padx=10,pady=10,sticky="ns")
        self.fr2.grid(row=1,column=1,padx=10,pady=10)
        self.fig = Figure(figsize=(6,6))
        self.a = self.fig.add_subplot(111)
        self.a.set_title ("Graphe de f", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)
        self.a.set_facecolor("gray")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fr2)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

    def plot (self):
        f= lambda x: eval(self.box.get())
        x=np.linspace(float(self.boxa.get()), float(self.boxb.get()), 1001)
        pp=f(x)
        self.a.cla()
        self.a.set_ylim([float(self.boxa.get()), float(self.boxb.get())])
        self.a.xaxis.set_ticks(np.arange(float(self.boxa.get()), float(self.boxb.get())+1, 1))
        self.a.yaxis.set_ticks(np.arange(float(self.boxa.get()), float(self.boxb.get())+1, 1))
        self.a.set_title ("Graphe de f", fontsize=16)
        self.a.set_ylabel("y=f(x)", fontsize=14)
        self.a.set_xlabel("x", fontsize=14)
        self.a.grid(True)
        self.a.plot(x, f(x),color='blue')
        self.canvas.draw()


window= Tk()

start= mclass(window)

window.mainloop()





