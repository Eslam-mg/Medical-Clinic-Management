from tkinter import *
from tkinter import ttk

class XraysClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("995x550+50+120")
        self.root.title("X-rays")
        self.root.resizable(False,False)
        self.root.config(bg='white')

        # ---------- search frame ------------
        search_frame = LabelFrame(self.root, text='البحث', font=('goudy old style', 12, 'bold'), bd=2, relief=RIDGE, bg='white')
        search_frame.place(x=370, y=20, width=600, height=70)

        cmb_search = ttk.Combobox(search_frame, values=("Select","Name","Contact"), justify=CENTER, state='readonly', font=('goudy old style', 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

if __name__ == "__main__":
    root = Tk()
    obj = XraysClass(root)
    root.mainloop()