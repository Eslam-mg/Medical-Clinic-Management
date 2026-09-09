from tkinter import *
from PIL import Image, ImageTk
from time import strftime

from xrays import XraysClass
class Clinic:
    # -------------- Update Date & Time --------------
    def timed(self):
        current_time = strftime("%I:%M:%S %p")
        current_date = strftime("%d/%m/%Y")

        self.lbl_date.config(
            text=f"Date: {current_date}\t\t\t\t"
                 f"Time: {current_time}\t\t\t\t"
                 f"نظام ادارة عيادة اسنان"
        )

        self.lbl_date.after(1000, self.timed)
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x650+50+20")
        self.root.resizable(False, False)
        self.root.title("Medical Clinic Management")
        self.root.config(bg="white")

        # -------------- Date & Time --------------
        self.lbl_date = Label(
            self.root,
            font=('times new roman', 15, 'bold'),
            bg='#005c78',
            fg='white'
        )
        self.lbl_date.place(x=0, y=0, width=1200, height=70)

        self.timed()

        # ------------- sidebar --------------
        sidebar = Frame(
            self.root,
            bd=2,
            relief=RIDGE,
            bg='white'
        )
        sidebar.place(x=998, y=70, width=200, height=578)

        # ------------- logo img --------------
        self.menu_img = Image.open("images/logo.webp")
        self.menu_img = self.menu_img.resize((200, 200))
        self.menu_img = ImageTk.PhotoImage(self.menu_img)

        lbl_img = Label(sidebar, image=self.menu_img)
        lbl_img.pack(side=TOP, fill=X)

        # ------------- menu label --------------
        lbl_menu = Label(
            sidebar,
            text="Menu",
            font=('times new roman', 20),
            bg='white',
            fg='#005c78',
            relief=RIDGE
        )
        lbl_menu.pack(fill=X)

        # ------------- button --------------
        btn1 = Button(
            sidebar,
            text='الاشعة',
            font=('times new roman', 20),
            bg='#005C78',
            fg='white',
            bd=3,
            cursor='hand2',
            command=self.xrays
        )
        btn1.pack(side=TOP, fill=X)
        
        btn2 = Button(
            sidebar,
            text='الحجوزات',
            font=('times new roman', 20),
            bg='#005C78',
            fg='white',
            bd=3,
            cursor='hand2'
        )
        btn2.pack(side=TOP, fill=X)

        btn3 = Button(
            sidebar,
            text='قسم الحشوات',
            font=('times new roman', 20),
            bg='#005C78',
            fg='white',
            bd=3,
            cursor='hand2'
        )
        btn3.pack(side=TOP, fill=X)

        btn4 = Button(
            sidebar,
            text='الزراعة',
            font=('times new roman', 20),
            bg='#005C78',
            fg='white',
            bd=3,
            cursor='hand2'
        )
        btn4.pack(side=TOP, fill=X)

        btn5 = Button(
            sidebar,
            text='اغلاق',
            font=('times new roman', 20),
            bg='#005C78',
            fg='white',
            bd=3,
            cursor='hand2'
        )
        btn5.pack(side=BOTTOM, fill=X)
        
        # ----------- main img ------------
        frame_img = Frame(self.root, bd=2, relief=RIDGE, bg='gray')
        frame_img.place(x=1, y=72, width=995, height=577)
        self.logo = Image.open("images/main_img.webp")
        self.log = self.logo.resize((995,577))
        self.log = ImageTk.PhotoImage(self.log)

        lbl_log_img = Label(frame_img, image=self.log)
        lbl_log_img.place(x=0, y=0, width=995, height=577)

    def xrays(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = XraysClass(self.new_win)


if __name__ == "__main__":
    root = Tk()
    obj = Clinic(root)
    root.mainloop()