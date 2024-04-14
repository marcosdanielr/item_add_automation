import tkinter as tk

class Checkbox(tk.Checkbutton):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(font=('Sans-serif', 12)) 
        self.configure(bg='#282828')
        self.configure(highlightbackground='#282828', highlightcolor='#282828', bg='#282828') 
        self.configure(activebackground='#282828')
        self.configure(selectcolor='white')