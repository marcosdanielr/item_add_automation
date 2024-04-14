import tkinter as tk

class Button(tk.Button):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

        self.config(
            background='#007ACC',
            foreground='#FFFFFF',
            relief='flat',
            borderwidth=0,
            activebackground='#005f8b',
            font=('Poppins', 12),
            padx=10,
            pady=5,
            cursor='hand2'
        )

        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)

    def on_enter(self, event):
        self.config(
            background='#005f8b'
        )

    def on_leave(self, event):
        self.config(
            background='#007ACC'
        )