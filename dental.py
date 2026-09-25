from tkinter import *
from tkinter import ttk

class DentalClass():
    def __init__(self, root):
        self.root = root
        self.root.geometry("995x549+51+121")
        self.root.title("Dental")
        self.root.resizable(False,False)
        self.root.config(bg='white')


        # ---------- search frame ------------
        search_frame = LabelFrame(self.root, text='البحث', font=('goudy old style', 12, 'bold'), bd=2, relief=RIDGE, bg='white')
        search_frame.place(x=370, y=20, width=600, height=70)

        cmb_search = ttk.Combobox(search_frame, values=("Select","Name","Contact"), justify=CENTER, state='readonly', font=('tajwal', 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        self.text_search = Entry(search_frame, font=("tajwal", 15), bg='lightyellow', justify=CENTER)
        self.text_search.place(x=200, y=10, width=210)
        self.btn_search = Button(search_frame, text='بحث', font=('tajwal', 15), bg='#005c78', fg='white', cursor='hand2')
        self.btn_search.place(x=420, y=9, width=150, height=30)



if __name__ == "__main__":
    root = Tk()
    obj = DentalClass(root)
    root.mainloop()