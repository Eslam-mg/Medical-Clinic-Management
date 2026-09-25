from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

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

        # ------------ title ------------
        self.title = Label(self.root, text='ادخال البيانات', font=('arial', 15), bg='#005c78', fg='white')
        self.title.place(x=340, y=100, width=645)
        
        # ------------ photo ------------
        self.logo = Image.open("images/dental_img.jpg").resize((325,200))
        self.log = ImageTk.PhotoImage(self.logo)
        lbl_image = Label(self.root, image=self.log)
        lbl_image.place(x=5, y=5, width=325, height=200)


if __name__ == "__main__":
    root = Tk()
    obj = DentalClass(root)
    root.mainloop()