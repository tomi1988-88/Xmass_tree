import tkinter as tk
from tkinter import ttk


class MyButton(ttk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pack(self, *args, **kwargs):
        super().pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        super().pack(*args, **kwargs)


class MyLabel(ttk.Label):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pack(self, *args, **kwargs):
        super().pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        super().pack(*args, **kwargs)


class MyEntry(ttk.Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pack(self, *args, **kwargs):
        super().pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        super().pack(*args, **kwargs)


class Interface(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_frame = ttk.Frame(master=self)

    def menu(self):
        ...
