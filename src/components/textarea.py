import tkinter as tk

class TextArea(tk.Text):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

        self.config(
            background='#424242',
            foreground='#FFFFFF',
            insertbackground='#FFFFFF',
            font=('sans-serif', 12),
            padx=10,
            pady=5
        )
