import math
from tkinter import *
from tkinter import font
import tkinter.messagebox
from tkinter import ttk
from turtle import *
import time
import turtle
import os
from square import *

window = Tk()

#window configure
window.geometry("900x600")
window.config(background="azure")
window.resizable(False, False)
window.title("Turtle w/ client inputs")
Icon = PhotoImage(file = os.path.join('icon.png'))
window.iconphoto(False, Icon)

tabControl = ttk.Notebook(window)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='square')
tabControl.add(tab2, text ='circle')
tabControl.pack(expand = 1, fill ="both")

main(tab1)

window.mainloop()