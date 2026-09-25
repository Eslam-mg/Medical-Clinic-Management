from tkinter import *
from tkinter import ttk

class DentalClass():
    def __init__(self, root):
        self.root = root
        self.root.geometry("995x549+51+121")
        self.root.title("Dental")
        self.root.resizable(False,False)
        self.root.config(bg='white')




if __name__ == "__main__":
    root = Tk()
    obj = DentalClass(root)
    root.mainloop()