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
        self.minsize(width=666, height=666)
        self.maxsize(width=666, height=666)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        button = Tkinter.Button(self,text=u"Choose file !",
                                command=self.OnButtonClick)
        button.grid(column=0,row=0, sticky="EW")


        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Label(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=1,sticky='EW')
        self.entryVariable.set(u"Your output will appear here")

        # self.labelVariable = Tkinter.StringVar()
        # label = Tkinter.Label(self,textvariable=self.labelVariable,
        #                       anchor="w",fg="white",bg="blue")
        # label.grid(column=0,row=1,columnspan=2,sticky='EW')
        # self.labelVariable.set(u"Hello !")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)

    def OnButtonClick(self):
        # self.labelVariable.set( self.entryVariable.get()+" (You clicked the button)" )
        # self.entry.focus_set()
        # self.entry.selection_range(0, Tkinter.END)
        filename = askopenfilename(parent=self)
        proc = subprocess.Popen("python detect_walking2.py "+ filename+ " | python predict.py", stdout=subprocess.PIPE, shell=True)
        for line in proc.stdout:
            sys.stdout.write(line)            
        proc.wait()
        


    # def OnPressEnter(self,event):        
    #     # self.entry.focus_set()
    #     # self.entry.selection_range(0, Tkinter.END)

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
