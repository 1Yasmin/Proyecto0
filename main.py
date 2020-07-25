import tkinter
from tkinter import filedialog as fd
import os
from tree import createTree

def onClickgrammar():
    filename = fd.askopenfilename(initialdir = "/")
    command = "antlr4 -Dlanguage=Python3 " + str(filename)[slice(40, len(filename))]
    os.system(command)

def onClickprogram():
    filename = fd.askopenfilename(initialdir = "/")


def onClickTree():
    filename = fd.askopenfilename(initialdir = "/")
    createTree(filename)

parent_widget = tkinter.Tk()

parent_widget.geometry("800x480")
canvas_widget = tkinter.Canvas(parent_widget,
                               bg="white",
                               width=800,
                               height= 480)

canvas_widget.pack()

label_widget = tkinter.Label(canvas_widget, text="Proyecto 0")
label_widget.pack()

button_grammar = tkinter.Button(canvas_widget, compound="left",
    text="Abrir Gramática",
    command=onClickgrammar)
button_grammar.pack()

button_program = tkinter.Button(canvas_widget, compound="left",
    text="Abrir Programa",
    command=onClickprogram)
button_program.pack()

button_tree = tkinter.Button(canvas_widget, compound="left",
    text="Imprimir Arbol",
    command=onClickTree)
button_tree.pack()

tkinter.mainloop()

