from tkinter import *
import os

class displayAcc :
    @staticmethod
    def createDisplay():
        return Tk()

    @staticmethod
    def createLabel (master, text, bgcolor="white", fgcolor="black", fontfamily="Times", fontsize=16, fontargs=""):
        stringvar = StringVar()
        stringvar.set(text)
        return Label(master, textvariable=stringvar, relief="RAISED".lower(), fg=fgcolor, bg=bgcolor, font="%s %d %s"%(fontfamily, fontsize, fontargs))
    
    @staticmethod
    def button(master, text, fg, command):
        return Button(master, text=text, fg=fg, command=command)
    '''
    @staticmethod
    def entry (master, row, column, get=1):
        a=Entry(master).grid(row=row, column=column);print(a)
        if get:
            return a, str(a.get())
        else:
            return a, None
    '''
