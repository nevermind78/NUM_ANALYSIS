from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import tkinter as Tk

"""
These dictionaries serve the purpose of storing the space varying and
time varying functions to be plotted.
"""

initFuncts = {0: '(np.exp(-0.5 * x ** 2) +'
                 '2 * x * np.exp(-0.5 * x ** 2)) ** 2',
              1: 'x**2'}
varyFuncts = {0: '((1 / (4 * np.pi)) ** (1 / 4)) * '
                 '((np.exp(-0.5 * x ** 2) * np.cos(0.5 * i) + '
                 '2 * x * np.exp(-0.5 * x ** 2) *'
                 'np.cos(1.5 * i)) ** 2)',
              1: 'x**2 + np.cos(i)'}


def addInitFunct(textField, options, strings):
    initFuncts[len(initFuncts)] = textField.get()
    expr = parse_expr(initFuncts[len(initFuncts)-1].replace('np.', ''))    
    options.children['menu'].delete(0, 'end')
    strings.set('')
    for key in initFuncts:
        options.children['menu'].add_command(
            label=str(key),
            command=Tk._setit(strings, str(key)))


def addVaryFunct(textField):
    varyFuncts[len(varyFuncts)] = textField.get()
