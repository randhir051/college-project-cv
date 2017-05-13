#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
from tkFileDialog import *
import subprocess
import sys

filename = ""

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.minsize(width=400, height=500)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.var = Tkinter.IntVar()
        c = Tkinter.Checkbutton(self, text="Show detection window", variable=self.var)
        c.grid(column=0,row=0, columnspan=1, pady=20, padx=20)

        button = Tkinter.Button(self,text=u"Choose file !",
                                command=self.OnButtonClick)
        button.grid(column=1,row=0, columnspan=1)

        button = Tkinter.Button(self,text=u"Process!",
                                command=self.OnProcessClick)
        button.grid(column=2,row=0, columnspan=1, padx=20)


        self.outputLabel = Tkinter.StringVar()
        self.outputL = Tkinter.Label(self,textvariable=self.outputLabel)
        self.outputL.grid(column=0,row=1,sticky='EW', columnspan = 3, pady=20, padx=20)
        self.outputLabel.set(u"Your output will appear here")

        # self.labelVariable = Tkinter.StringVar()
        # label = Tkinter.Label(self,textvariable=self.labelVariable,
        #                       anchor="w",fg="white",bg="blue")
        # label.grid(column=0,row=1,columnspan=2,sticky='EW')
        # self.labelVariable.set(u"Hello !")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)

    def OnButtonClick(self):
        # self.labelVariable.set( self.outputLabel.get()+" (You clicked the button)" )
        # self.outputL.focus_set()
        # self.outputL.selection_range(0, Tkinter.END)
        self.filename = askopenfilename(parent=self)        
        self.outputLabel.set("You selected: "+ self.filename.split("/")[-1])

        

    def OnProcessClick(self):
        file_to_open = ""
        if self.var.get() == 1:
            file_to_open = "detect_walking.py"
        else:
            file_to_open = "detect_walking2.py"
        cmd = "python "+ file_to_open +" "+ self.filename + " | python predict.py"
        # print cmd
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)        
        
        str_op = ""
        for line in proc.stdout:
            str_op += line 
            sys.stdout.write(line)
        self.outputLabel.set(str_op)
        


    # def OnPressEnter(self,event):        
    #     # self.outputL.focus_set()
    #     # self.outputL.selection_range(0, Tkinter.END)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Computer Vision')
    app.mainloop()
