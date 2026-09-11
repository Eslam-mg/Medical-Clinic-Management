from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

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

        self.text_search = Entry(search_frame, font=("tajwal", 15), bg='lightyellow', justify=CENTER).place(x=200, y=10, width=210)
        self.btn_search = Button(search_frame, text='بحث', font=('goudy oid style', 15), bg='#005c78', fg='white', cursor='hand2').place(x=420, y=9, width=150, height=30)

        # ------------ title ------------
        self.title = Label(self.root, text='النفاصيل', font=('goudy oid style', 15), bg='#005c78', fg='white').place(x=340, y=100, width=645)

        #  ------------ image ----------
        self.logo = Image.open("images/xray.webp").resize((325, 200))
        self.logo = ImageTk.PhotoImage(self.logo)
        lbl_img = Label(self.root, image=self.logo)
        lbl_img.place(x=5, y=5, width=325, height=200)

        # -------- labels + entrys -------
        lbl_name = Label(self.root, text='الاسم', font=('tajwal', 15), bg='white').place(x=940, y=150)
        en_name = Entry(self.root, font=('tajwal', 15), bg='lightyellow', justify=CENTER).place(x=560, y=150, width=360)

        lbl_gender = Label(self.root, text='الجنس', font=('tajwal', 15), bg='white').place(x=505, y=150)
        cmb_gender = ttk.Combobox(self.root, values=("Select", "ذكر", "انثى"), state='readonly', justify=CENTER, font=('tajwal', 15))
        cmb_gender.place(x=350, y=150, width=145)
        cmb_gender.current(0)

        lbl_age = Label(self.root, text='العمر', font=('tajwal', 15), bg='white').place(x=940, y=195)
        en_age = Entry(self.root, font=('tajwal', 15), bg='lightyellow', justify=CENTER).place(x=770, y=200, width=150)
        
        lbl_state = Label(self.root, text='الحالة', font=('tajwal', 15), bg='white').place(x=720, y=200)
        en_state = Entry(self.root, font=('tajwal', 15), bg='lightyellow', justify=CENTER).place(x=560, y=200, width=150)

        lbl_price = Label(self.root, text='المبلغ', font=('tajwal', 15), bg='white').place(x=505, y=200)
        en_price = Entry(self.root, font=('tajwal', 15), bg='lightyellow', justify=CENTER).place(x=350, y=200, width=145)
        
        lbl_date = Label(self.root, text='التاريخ', font=('tajwal', 15), bg='white').place(x=930, y=250)
        en_date = Entry(self.root, font=('tajwal', 15), bg='lightyellow', justify=CENTER).place(x=770, y=250, width=150)
        
        lbl_contact = Label(self.root, text='الهاتف', font=('tajwal', 15), bg='white').place(x=715, y=250)
        en_contact = Entry(self.root, font=('tajwal', 15), bg='lightyellow', justify=CENTER).place(x=560, y=250, width=150)

        lbl_address = Label(self.root, text='العنوان', font=('tajwal', 15), bg='white').place(x=500, y=250)
        en_address = Entry(self.root, font=('tajwal', 15), bg='lightyellow', justify=CENTER).place(x=350, y=250, width=145)

        #  -------- buttons --------
        btn_add = Button(self.root, text='اضافة', font=('goudy old style', 15), bg='#005c78', fg='white', cursor='hand2').place(x=175, y=215, width=155, height=28)
        btn_update = Button(self.root, text='تعديل', font=('goudy old style', 15), bg='#005c78', fg='white', cursor='hand2').place(x=5, y=215, width=155, height=28)
        btn_delete = Button(self.root, text='حذف', font=('goudy old style', 15), bg='#005c78', fg='white', cursor='hand2').place(x=5, y=250, width=155, height=28)
        btn_clear = Button(self.root, text='تفريغ', font=('goudy old style', 15), bg='#005c78', fg='white', cursor='hand2').place(x=175, y=250, width=155, height=28)
if __name__ == "__main__":
    root = Tk()
    obj = XraysClass(root)
    root.mainloop()