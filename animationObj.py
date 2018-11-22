from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as Tk, numpy as np
import matplotlib.pyplot as plt, matplotlib.animation as animation
import dictionaries as dicts

class animationObj:
    def __init__(self, mainframe, num, x, timeString):
        """
        Create instance of animationObj class, enabling the animation of
        matplotlib based figures.

        Keyword arguments:
        mainframe -- the frame the animation will appear in
        num -- the function number in the dictionaries
        x -- spacial range of the animation
        timeString -- string which will report current time to user
        """

        self._master = mainframe  # set frame
        self.timeString, self.num, self.x = timeString, num, x
        self.fig = plt.Figure()  # create pyplot figure
        # add figure to canvas and connect canvas to frame
        self.canvas = FigureCanvasTkAgg(self.fig, master=self._master)
        # get widget then pack
        self.tkwidget = self.canvas.get_tk_widget()
        self.tkwidget.pack()
        # add subplot to actually animate on
        self.ax = self.fig.add_subplot(111)
        # generate initial plot, note the syntax: 'self.line,', comma
        # after variable means returning as a tuple
        self.line, = self.ax.plot(self.x,
                                  eval(dicts.initFuncts[self.num]))
        # set bounds on plot
        self.ax.axis([-6, 6, -5, 5])
        # animate the animation
        self.ani = animation.FuncAnimation(self.fig, self.animate,
                                           np.arange(0, 200, 0.01),
                                           interval=1, blit=False)

    def animate(self, i):
        """
        Animation function which executes every 'interval given in the
        FuncAnimation instantiation.

        Keyword arguments:
        i -- the current time
        """
        # must create a (not technically called this...) 'local global'
        # version of x because set_ydata expects a global variable x
        x = self.x
        self.timeString.set('t = ' + '{:3.2f}'.format(i))  # report time
        # generate plot at next time interval
        self.line.set_ydata(eval(dicts.varyFuncts[self.num]))
        # return line tuple
        return self.line,

    def stopIt(self):
        """Pause the current animation shown."""
        self.ani.event_source.stop()

    def startIt(self):
        """Resume the current animation shown."""
        self.ani.event_source.start()

    def removeIt(self):
        """Remove the current animation from the window."""
        self.tkwidget.pack_forget()
        self.ani.event_source.stop()

    def addIt(self, num):
        """
        Add a new plot to the plotting window.

        Keyword arguments:
        num -- the function number in the dictionaries
        """
        if (num in dicts.initFuncts) and (num in dicts.varyFuncts):
            self.removeIt()  # remove old plot
            x = self.x  # same as before, expects a global x
            i = 0  # reset time to zero
            self.num = int(num)  # update instance variable
            #reinitialize all needed components
            self.fig = plt.Figure()
            self.canvas = FigureCanvasTkAgg(self.fig, master=self._master)
            self.tkwidget = self.canvas.get_tk_widget()
            self.tkwidget.pack()
            self.ax = self.fig.add_subplot(111)
            self.line, = self.ax.plot(self.x,
                                      eval(dicts.initFuncts[self.num]))
            self.ax.axis([-6, 6, -5, 5])
            self.ani = animation.FuncAnimation(self.fig, self.animate,
                                               np.arange(0, 200, 0.01),
                                               interval=1, blit=False)
