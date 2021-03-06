import tkinter as t
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

class Application(t.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.txtEdit = t.Text(self)
        self.txtEdt = t.Text(self)
        self.btnFrame = t.Frame(self)
        self.btnOpen = t.Button(self.btnFrame, text="Open", command=self.openFile)
        self.btnSave = t.Button(self.btnFrame, text="Save As", command=self.saveFile)
        
        
        self.txtEdit.grid(row=0, column=1, sticky="ns")
        self.txtEdt.grid(row=0, column=2, sticky="ew")
        self.btnFrame.grid(row=0, column=0, sticky="ns")
        self.btnOpen.grid(row=0, column=0, sticky="ew")
        self.btnSave.grid(row=1, column=0, sticky="ew")
    def saveFile(self):
        files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
        file = asksaveasfilename(filetypes=files)
    def openFile(self):
        fp = askopenfilename(filetypes=[("CharlieFiles", "*.txt"), ("Who cares about All Files", "*.*")])
        if not fp:
            return
        self.txtEdit.delete(1.0, t.END)
        self.txtEdt.delete(1.0, t.END)
        with open(fp, "r") as inFile:
            txt = inFile.read()
            self.txtEdit.insert(t.END, txt)
            self.txtEdt.insert(t.END, txt)
root = t.Tk()
root.title("Charlie's Text Editor")
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=600, weight=1)
app = Application(master=root)
app.mainloop()
