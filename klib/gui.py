from tkinter import *

# UNCOMMENT "del" IF YOU don't WANNA HAVE VERSION AVAIABLE
GUI_KLIB_VERSION = "0.1 - BETA"
#del GUI_KLIB_VERSION

# MAIN WINDOW
root = Tk()

def setWindowTitle(title):
    global root

    root.title(str(title))

def keepOpen():
    global root
    root.mainloop()

def size(sizeString = "STD"):
    global root
    if sizeString == "STD":
        root.geometry("400x400")
    else:
        root.geometry(sizeString)
def not_resizable(tell = False):
    global root
    root.resizable(width=False, height=False)
    if tell == True: print("[!][ Your Window No Longer Resizable ]")

class howto:
    def label():
        print("Syntax: ")
        print("Label(root, text=txt).grid(row=Row, column=Column, sticky=NW)")
        print("first arg = root (always root)")
        print("second arg = text=txt (What you wanna have in your label)")
        print("third arg = .grid (your geometry manager, Almost always wanna be grid)")
        print("4th arg = row (Pretty self explanatory)")
        print("5th arg = column (Pretty self explanatory)")
        print("6th arg = sticky [anchor..., dock...,  ...to](where it should stick to. NW = North West, SW = South West etc...) (NOT NEEDED)")
    def button():
        print("Syntax: ")
        print("Button(root, text=txt, command=function).grid(row=Row, column=Column, sticky=NW)")
        print("first arg = root (always root)")
        print("second arg = text=txt (What you wanna have in your button)")
        print("3th arg = command=function (function that will be called when clicked)")
        print("4th arg = .grid (your geometry manager, Almost always wanna be grid)")
        print("5th arg = row (Pretty self explanatory)")
        print("6th arg = column (Pretty self explanatory)")
        print("7th arg = sticky [anchor..., dock...,  ...to](where it should stick to. NW = North West, SW = South West etc...) (NOT NEEDED)")

def addLabel(txt = "Empty Label", pRow = 1, pColumn = 1):
    global root

    label = Label(root, text=str(txt)).grid(row = pRow, column = pColumn)
    return label

def addButton(txt = "Empty Button", pRow = 1, pColumn = 1):
    global root

    button = Button(root, text=str(txt)).grid(row = pRow, column = pColumn)
    return button

def init_window(windowTitle = "Window", wSize = "STD", resizable = False):
    setWindowTitle(windowTitle)
    if resizable == False:
        not_resizable(True)
    size(wSize)
def auto_init():
    init_window()

class kbutton:
    ktext = StringVar()

    def setup():
        global ktext
        ktext = StringVar()
        ktext.set("Empty String")

    def addButton(self, root, txt = "Empty Button", pRow = 1, pColumn = 1):
        global ktext
        ktext.set(txt)

        button = Button(root, text=ktext).grid(row = pRow, column = pColumn)
        return button

    # You should set text with button.text.set("Text Here")
    # But this works aswell
    def setText(self, txt = "Invalid Input"):
        global ktext

        ktext.set(txt)


















"""
def addButton1(text, layout = "GRID"):
    global root
    global ttk

    if layout == "GRID": ttk.Button(root, text=str(text)).grid()
def addButton2(text, layout = "GRID"):
    global root
    global ttk
    global frame

    if layout == "GRID": ttk.Button(frame, text=str(text)).grid()

def addLabel(text, layout = "GRID"):
    global root
    #global frame

    Label(root, textvariable=str(text))
def label(txt = "", Row = 0, Column = 0, anchor = "None"):
    global root

    _sticky = anchor.lower()
    del anchor

    if _sticky == "none" or _sticky == "center" or _sticky == "c":
        Label(root, text=txt).grid(row=Row, column=Column)
    elif _sticky == "nw":
        Label(root, text=txt).grid(row=Row, column=Column, sticky=NW)
        print("NW Selected...")
    elif _sticky == "w":
        Label(root, text=txt).grid(row=Row, column=Column, sticky=W)
    elif _sticky == "e":
        Label(root, text=txt).grid(row=Row, column=Column, sticky=E)
    elif _sticky == "ne":
        Label(root, text=txt).grid(row=Row, column=Column, sticky=NE)
    elif _sticky == "sw":
        Label(root, text=txt).grid(row=Row, column=Column, sticky=SW)
    elif _sticky == "se":
        Label(root, text=txt).grid(row=Row, column=Column, sticky=SE)
        print("SE Selected...")
    else:
        print("UNKNOWN LOCATION IN LABEL")
        exit(0)
class labels:

    label = None
    root = None
    labelText = StringVar()

    def __init__(self, giveRoot):
        root = giveRoot

    def addLabel(self, text = "Empty Label"):
        global root
        #global frame

        lableText.set(str(text))

        label = Label(root, textvariable=lableText)
    def changeText(text = "Nothing!"):
        global root

        labelText.set(str(text))
"""
