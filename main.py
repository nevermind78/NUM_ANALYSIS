import tkinter as Tk
import numpy as np
import animationObj
import dictionaries


def _quit(mast):
    """
    Quits the entire application.

    Keyword arguments:
    mast -- the root Tk instance
    """
    mast.quit()
    mast.destroy()

root = Tk.Tk()  # root Tk instance
t1 = Tk.Toplevel(root)
t2 = Tk.Toplevel(root)  # Tk Toplevel instance to separate windows

# add frames to windows
f1 = Tk.Frame(t1)
f2 = Tk.Frame(t2)
f = Tk.Frame(root)
label1 = Tk.Label(f, text="Superposition State").pack()

# set each frames' geometry
t2.geometry("%dx%d+%d+%d" % (250, 300, 650, 625))
t1.geometry("%dx%d+%d+%d" % (250, 300, 650, 300))
root.geometry("%dx%d+%d+%d" % (500, 500, 150, 300))

# drop down menu
options = Tk.StringVar()
options.set('0')
w = Tk.OptionMenu(f1, options, '0', '1')
w.pack(side=Tk.BOTTOM)

# string to display time
timeString = Tk.StringVar()
timeString.set('t = 0')
l = Tk.Label(f1, textvariable=timeString, font=("Courier", 24))

# make and pack quit button
button = Tk.Button(master=f1, text='Quit',
                   command=lambda: _quit(root), height=2)
button.pack(side=Tk.BOTTOM)

# pack time string
l.pack(side=Tk.TOP)

x = np.arange(-6, 6, 0.005)  # range of x values
aniObj = animationObj.animationObj(f, 0, x, timeString)

# other buttons
button3 = Tk.Button(master=f1, text='Make',
                    command=lambda: aniObj.addIt(int(options.get())), height=2)
stopIt = Tk.Button(master=f1, text='Stop', command=aniObj.stopIt, height=1)
startIt = Tk.Button(master=f1, text='Start',
                    command=aniObj.startIt, height=1)

# pack frames
f.pack()
f1.pack()
f2.pack()

# pack buttons
button3.pack(side=Tk.BOTTOM)
stopIt.pack(side=Tk.LEFT)
startIt.pack(side=Tk.LEFT)

e = Tk.Entry(f2)

button4 = Tk.Button(master=f2, text='Add Initial Function',
                    command=lambda: dictionaries.addInitFunct(e, w, options),
                    height=1)
button5 = Tk.Button(master=f2, text='Add Varying Function', command=lambda:
                    dictionaries.addVaryFunct(e), height=1)
button4.pack(side=Tk.BOTTOM)
button5.pack(side=Tk.BOTTOM)
e.pack(side=Tk.TOP)

# execute main loop on base instance
root.mainloop()
