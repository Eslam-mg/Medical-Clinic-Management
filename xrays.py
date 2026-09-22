import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class XraysClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("995x550+50+120")
        self.root.title("X-rays")
        self.root.resizable(False,False)
        self.root.config(bg='white')

        # ---------- variables -----------
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_gender = StringVar()
        self.var_age = StringVar()
        self.var_date = StringVar()
        self.var_state = StringVar()
        self.var_price = StringVar()
        self.var_contact = StringVar()
        self.var_address = StringVar()

        # ---------- search frame ------------
        search_frame = LabelFrame(self.root, text='البحث', font=('goudy old style', 12, 'bold'), bd=2, relief=RIDGE, bg='white')
        search_frame.place(x=370, y=20, width=600, height=70)

        cmb_search = ttk.Combobox(search_frame, textvariable=self.var_searchby, values=("Select","Name","Contact"), justify=CENTER, state='readonly', font=('goudy old style', 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        self.text_search = Entry(search_frame, textvariable=self.var_searchtxt, font=("tajwal", 15), bg='lightyellow', justify=CENTER)
        self.text_search.place(x=200, y=10, width=210)
        self.btn_search = Button(search_frame, command=self.search, text='بحث', font=('goudy old style', 15), bg='#005c78', fg='white', cursor='hand2')
        self.btn_search.place(x=420, y=9, width=150, height=30)

        # ------------ title ------------
        self.title = Label(self.root, text='الـتــفـاصـيل', font=('goudy old style', 15), bg='#005c78', fg='white').place(x=340, y=100, width=645)

        #  ------------ image ----------
        self.logo = Image.open("images/xray.webp").resize((325, 200))
        self.logo = ImageTk.PhotoImage(self.logo)
        lbl_img = Label(self.root, image=self.logo)
        lbl_img.place(x=5, y=5, width=325, height=200)

        # -------- labels + entrys -------
        lbl_name = Label(self.root, text='الاسم', font=('tajwal', 15), bg='white').place(x=940, y=150)
        en_name = Entry(self.root, textvariable=self.var_name, font=('tajwal', 15), bg='lightyellow', justify=CENTER).place(x=560, y=150, width=360)

        lbl_gender = Label(self.root, text='الجنس', font=('tajwal', 15), bg='white').place(x=505, y=150)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "ذكر", "انثى"), state='readonly', justify=CENTER, font=('tajwal', 15))
        cmb_gender.place(x=350, y=150, width=145)
        cmb_gender.current(0)

        lbl_age = Label(self.root, text='العمر', font=('tajwal', 15), bg='white').place(x=940, y=195)
        en_age = Entry(self.root, textvariable=self.var_age, font=('tajwal', 15), bg='lightyellow', justify=CENTER).place(x=770, y=200, width=150)
        
        lbl_state = Label(self.root, text='الحالة', font=('tajwal', 15), bg='white').place(x=720, y=200)
        en_state = Entry(self.root, textvariable=self.var_state, font=('tajwal', 15), bg='lightyellow', justify=CENTER).place(x=560, y=200, width=150)

        lbl_price = Label(self.root, text='المبلغ', font=('tajwal', 15), bg='white').place(x=505, y=200)
        en_price = Entry(self.root, textvariable=self.var_price, font=('tajwal', 15), bg='lightyellow', justify=CENTER).place(x=350, y=200, width=145)
        
        lbl_date = Label(self.root, text='التاريخ', font=('tajwal', 15), bg='white').place(x=930, y=250)
        en_date = Entry(self.root, textvariable=self.var_date, font=('tajwal', 15), bg='lightyellow', justify=CENTER).place(x=770, y=250, width=150)
        
        lbl_contact = Label(self.root, text='الهاتف', font=('tajwal', 15), bg='white').place(x=715, y=250)
        en_contact = Entry(self.root, textvariable=self.var_contact, font=('tajwal', 15), bg='lightyellow', justify=CENTER).place(x=560, y=250, width=150)

        lbl_address = Label(self.root, text='العنوان', font=('tajwal', 15), bg='white').place(x=500, y=250)
        en_address = Entry(self.root, textvariable=self.var_address, font=('tajwal', 15), bg='lightyellow', justify=CENTER).place(x=350, y=250, width=145)

        #  -------- buttons --------
        btn_add = Button(self.root, command=self.add, text='اضافة', font=('goudy old style', 15), bg='#005c78', fg='white', cursor='hand2').place(x=175, y=215, width=155, height=28)
        btn_update = Button(self.root, command=self.update, text='تعديل', font=('goudy old style', 15), bg='#005c78', fg='white', cursor='hand2').place(x=5, y=215, width=155, height=28)
        btn_delete = Button(self.root, command=self.delete, text='حذف', font=('goudy old style', 15), bg='#005c78', fg='white', cursor='hand2').place(x=5, y=250, width=155, height=28)
        btn_clear = Button(self.root, command=self.clear, text='تفريغ', font=('goudy old style', 15), bg='#005c78', fg='white', cursor='hand2').place(x=175, y=250, width=155, height=28)

        # ------- treeview frame --------
        xray_frame = Frame(self.root, bd=3, relief=RIDGE)
        xray_frame.place(x=0, y=290, width=995, height=260)
        scrolly = Scrollbar(xray_frame, orient=VERTICAL)
        scrollx = Scrollbar(xray_frame, orient=HORIZONTAL)

        self.Xray_Table = ttk.Treeview(xray_frame, columns=("address", "contact", "price", "state","date", "age", "gender", "name", "xid"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrollx.config(command=self.Xray_Table.xview)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Xray_Table.yview)

        self.Xray_Table.heading("address", text="العنوان")
        self.Xray_Table.heading("contact", text="الهاتف")
        self.Xray_Table.heading("price", text="المبلغ")
        self.Xray_Table.heading("state", text="الحالة")
        self.Xray_Table.heading("date", text="التاريخ")
        self.Xray_Table.heading("age", text="العمر")
        self.Xray_Table.heading("gender", text="الجنس")
        self.Xray_Table.heading("name", text="الاسم")
        self.Xray_Table.heading("xid", text="رقم")

        self.Xray_Table["show"] = "headings"
        self.Xray_Table.column("xid", width=20, anchor=NE)
        self.Xray_Table.column("name", width=100, anchor=NE)
        self.Xray_Table.column("gender", width=40, anchor=NE)
        self.Xray_Table.column("age", width=30, anchor=NE)
        self.Xray_Table.column("date", width=100, anchor=NE)
        self.Xray_Table.column("state", width=100, anchor=NE)
        self.Xray_Table.column("price", width=50, anchor=NE)
        self.Xray_Table.column("contact", width=100, anchor=NE)
        self.Xray_Table.column("address", width=100, anchor=NE)

        self.Xray_Table.pack(fill=BOTH, expand=1)
        self.Xray_Table.bind("<ButtonRelease-1>", self.get_data)
        self.show()

    # ---------- Add X-ray Record ----------
    # Checks that all required fields are filled, then saves the X-ray patient information into the SQLite database.
    def add(self):
        if (self.var_address.get() == "" or
            self.var_contact.get() == "" or
            self.var_price.get() == "" or
            self.var_state.get() == "" or
            self.var_date.get() == "" or
            self.var_age.get() == "" or
            self.var_gender.get() == "Select" or
            self.var_gender.get() == "" or
            self.var_name.get() == ""):
            messagebox.showerror("Error", "Please Enter All the Data")
            return

        con = sqlite3.connect('clinic.db')
        cur = con.cursor()
        cur.execute("""
            INSERT INTO xrays
            (address, contact, price, state, date, age, gender, name)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            self.var_address.get(),
            self.var_contact.get(),
            self.var_price.get(),
            self.var_state.get(),
            self.var_date.get(),
            self.var_age.get(),
            self.var_gender.get(),
            self.var_name.get()
        ))
        con.commit()
        con.close()
        self.show()
        self.clear()
        messagebox.showinfo("Success", "تمت الإضافة بنجاح")

    # ---------- Display X-ray Records ----------
    # Retrieves all X-ray records from the SQLite database and displays them in the Treeview table.
    def show(self):
        con = sqlite3.connect('clinic.db')
        cur = con.cursor()

        try:
            cur.execute("SELECT * FROM xrays")
            rows = cur.fetchall()

            self.Xray_Table.delete(*self.Xray_Table.get_children())

            for row in rows:
                self.Xray_Table.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error xrays to: {str(ex)}")

        finally:
            con.close()

    # ---------- Clear Input Fields ----------
    # Resets all input fields to their default values and refreshes the X-ray records displayed in the table.
    def clear(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_gender.set("Select")
        self.var_age.set("")
        self.var_date.set("")
        self.var_state.set("")
        self.var_price.set("")
        self.var_contact.set("")
        self.var_address.set("")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")

    # ---------- Get Selected X-ray Data ----------
    # Retrieves the selected record from the Treeview and displays its data in the input fields.
    def get_data(self, ev):
        f = self.Xray_Table.focus()
        content = (self.Xray_Table.item(f))
        row = content['values']

        if not row:
            return

        self.var_address.set(row[0])
        self.var_contact.set(row[1])
        self.var_price.set(row[2])
        self.var_state.set(row[3])
        self.var_date.set(row[4])
        self.var_age.set(row[5])
        self.var_gender.set(row[6])
        self.var_name.set(row[7])
        self.var_id.set(row[8])

    # ---------- Update ----------
    # Updates the selected X-ray record in the SQLite database using the record ID and the values entered in the input fields.
    def update(self):
        if not self.var_id.get():
            messagebox.showerror("Error", "الرجاء اختيار سجل من الجدول أولاً")
            return

        if (self.var_address.get() == "" or
            self.var_contact.get() == "" or
            self.var_price.get() == "" or
            self.var_state.get() == "" or
            self.var_date.get() == "" or
            self.var_age.get() == "" or
            self.var_gender.get() == "" or
            self.var_name.get() == ""):
            messagebox.showerror("Error", "Please Enter All the Data")
            return

        con = sqlite3.connect('clinic.db')
        cur = con.cursor()
        cur.execute("""
            UPDATE xrays
            SET address=?, contact=?, price=?, state=?, date=?,
                age=?, gender=?, name=?
            WHERE xid=?
        """, (
            self.var_address.get(),
            self.var_contact.get(),
            self.var_price.get(),
            self.var_state.get(),
            self.var_date.get(),
            self.var_age.get(),
            self.var_gender.get(),
            self.var_name.get(),
            self.var_id.get()
        ))
        con.commit()
        con.close()
        self.show()
        self.clear()
        messagebox.showinfo("Success", "تم التعديل بنجاح")

    # ---------- delete ----------
    # delete the selected X-ray record in the SQLite database using by selected record from the Treeview
    def delete(self):
        con = sqlite3.connect('clinic.db')
        cur = con.cursor()
        op = messagebox.askyesno("Confirm", "Do you really want to delete=?")
        
        if op:
            cur.execute("DELETE FROM xrays WHERE xid=?", (self.var_id.get(),))
            con.commit()
            con.close()
            self.clear()
            messagebox.showinfo("Success", "delete successfully")
        else:
            con.close()

    # ---------- Search X-ray Records ----------
    # Searches for X-ray records by name or contact and displays the matching records in the Treeview.
    def search(self):
        con = sqlite3.connect('clinic.db')
        cur = con.cursor()

        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select a field to search")
            
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Enter a value to search")

            else:
                cur.execute(
                    f"SELECT * FROM xrays WHERE {self.var_searchby.get()} LIKE ?",
                    ('%' + self.var_searchtxt.get() + '%',)
                )

                rows = cur.fetchall()

                self.Xray_Table.delete(*self.Xray_Table.get_children())

                if len(rows) != 0:
                    for row in rows:
                        self.Xray_Table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No result found")

        except Exception as ex:
            messagebox.showerror("Error", f"Error: {str(ex)}")

        finally:
            con.close()


if __name__ == "__main__":
    root = Tk()
    obj = XraysClass(root)
    root.mainloop()