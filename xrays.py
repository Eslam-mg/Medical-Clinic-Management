from tkinter import *

class XraysClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("995x550+50+120")
        self.root.title("X-rays")
        self.root.resizable(False,False)
        self.root.config(bg='white')


if __name__ == "__main__":
    root = Tk()
    obj = XraysClass(root)
    root.mainloop()