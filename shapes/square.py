import math
from tkinter import *
from tkinter import font
import tkinter.messagebox
from tkinter import ttk
from turtle import *
import time
import turtle
import os

def square(tab1):
    
    #square side labels
    side1Label = Label(tab1, text="side 1 x", font = 10).place(relx=0.38, rely=0.2)
    side2Label = Label(tab1, text="side 2 y", font = 10).place(relx=0.38, rely=0.3)
    side3Label = Label(tab1, text="side 3 x", font = 10).place(relx=0.38, rely=0.4)
    side4Label = Label(tab1, text="side 4 y", font = 10).place(relx=0.38, rely=0.5)
    side4Label = Label(tab1, text="Amount of loops", font = 10).place(relx=0.4, rely=0.6)

    #entry intvars
    side1var = IntVar()
    side2var = IntVar()
    side3var = IntVar()
    side4var = IntVar()
    loopsinputvar = IntVar()

    side1var.set(10)
    side2var.set(10)
    side3var.set(10)
    side4var.set(10)
    loopsinputvar.set(3)

    #square entry labels
    side1Entry = Entry(tab1, textvariable=side1var).place(relx=0.47, rely=0.21)
    side2Entry = Entry(tab1, textvariable=side2var).place(relx=0.47, rely=0.31)
    side3Entry = Entry(tab1, textvariable=side3var).place(relx=0.47, rely=0.41)
    side4Entry = Entry(tab1, textvariable=side4var).place(relx=0.47, rely=0.51)
    loopsentry = Entry(tab1, textvariable=loopsinputvar).place(relx=0.4, rely=0.64)

    #turtlefunc
    def turtlefunc():
        loops = 0

        while loops < loopsinputvar.get():
            forward(side1var.get())
            left(90)

            forward(side2var.get())
            left(90)

            forward(side3var.get())
            left(90)

            forward(side4var.get())
            left(90)

            loops += 1

    #enter
    Enter = Button(tab1, text="Enter", width=20, height=4, background="lightgreen", command=turtlefunc).place(relx=0.5, rely=0.8, anchor=CENTER)
