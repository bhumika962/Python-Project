
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        lbltitle = tk.Label(self.root, text="Library Management System", bg="powder blue",
                            fg="green", bd=20, relief=tk.RIDGE, font=("times new roman", 50, "bold"),
                            padx=2, pady=6)
        lbltitle.pack(side=tk.TOP, fill=tk.X)

        frame = tk.Frame(self.root, bd=12, relief=tk.RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft = tk.LabelFrame(frame, text="Library Membership Information", bg="powder blue",
                                       fg="green", bd=12, relief=tk.RIDGE, font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        # Entry fields
        self.entries = {}  # Dictionary to hold references to entry widgets
        self.create_entry(DataFrameLeft, "Member Type:", 0)
        self.create_entry(DataFrameLeft, "PRN No:", 1)
        self.create_entry(DataFrameLeft, "ID No:", 2)
        self.create_entry(DataFrameLeft, "Firstname:", 3)
        self.create_entry(DataFrameLeft, "Lastname:", 4)
        self.create_entry(DataFrameLeft, "Address1:", 5)
        self.create_entry(DataFrameLeft, "Address2:", 6)
        self.create_entry(DataFrameLeft, "PostCode:", 7)
        self.create_entry(DataFrameLeft, "Mobile:", 8)

        self.create_entry(DataFrameLeft, "Book Id:", 0, column_offset=2)
        self.create_entry(DataFrameLeft, "Book Title:", 1, column_offset=2)
        self.create_entry(DataFrameLeft, "Author Name:", 2, column_offset=2)
        self.create_entry(DataFrameLeft, "Date Borrowed:", 3, column_offset=2)
        self.create_entry(DataFrameLeft, "Date Due:", 4, column_offset=2)
        self.create_entry(DataFrameLeft, "Days on Book:", 5, column_offset=2)
        self.create_entry(DataFrameLeft, "Date Over Due:", 6, column_offset=2)
        self.create_entry(DataFrameLeft, "Late Return Fine:", 7, column_offset=2)
        self.create_entry(DataFrameLeft, "Actual Price:", 8, column_offset=2)

        self.create_button_frame()
        self.create_database()
        self.create_table()

    def create_database(self):
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS library (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                membertype TEXT,
                prnno TEXT,
                firstname TEXT,
                lastname TEXT,
                address1 TEXT,
                address2 TEXT,
                postid TEXT,
                mobile TEXT,
                bookid TEXT,
                booktitle TEXT,
                author TEXT,
                dateborrowed TEXT,
                datedue TEXT,
                days INTEGER,
                latereturnfine REAL,
                dateoverdue TEXT,
                finalprice REAL
            )
        ''')
        self.conn.commit()

    def create_entry(self, parent, label_text, row, column_offset=0):
        lbl = tk.Label(parent, bg="powder blue", text=label_text, font=("arial", 12, "bold"), padx=2, pady=6)
        lbl.grid(row=row, column=column_offset, sticky=tk.W)
        entry = tk.Entry(parent, font=("arial", 13, "bold"), width=29)
        entry.grid(row=row, column=column_offset + 1)
        self.entries[label_text] = entry  # Store entry reference

    def create_button_frame(self):
        Framebutton = tk.Frame(self.root, bd=12, relief=tk.RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        btnAddData = tk.Button(Framebutton, command=self.add_data, text="Add Data", font=("arial", 12, "bold"),
                               width=23, bg="blue", fg="white")
        btnAddData.grid(row=0, column=0)

        btnShowData = tk.Button(Framebutton, command=self.show_data, text="Show Data", font=("arial", 12, "bold"),
                                width=23, bg="blue", fg="white")
        btnShowData.grid(row=0, column=1)

        btnUpdate = tk.Button(Framebutton, command=self.update, text="Update", font=("arial", 12, "bold"),
                              width=23, bg="blue", fg="white")
        btnUpdate.grid(row=0, column=2)

        btnDelete = tk.Button(Framebutton, command=self.delete, text="Delete", font=("arial", 12, "bold"),
                              width=23, bg="blue", fg="white")
        btnDelete.grid(row=0, column=3)

        btnReset = tk.Button(Framebutton, command=self.reset, text="Reset", font=("arial", 12, "bold"),
                             width=23, bg="blue", fg="white")
        btnReset.grid(row=0, column=4)

        btnExit = tk.Button(Framebutton, command=self.exit_program, text="Exit", font=("arial", 12, "bold"),
                            width=23, bg="blue", fg="white")
        btnExit.grid(row=0, column=5)

    def create_table(self):
        FrameDetails = tk.Frame(self.root, bd=12, relief=tk.RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=600, width=1530, height=195)

        Table_frame = tk.Frame(FrameDetails, bd=6, relief=tk.RIDGE, bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=tk.HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=tk.VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, columns=("membertype", "prnno", "firstname", "lastname",
                                                                "address1", "address2", "postid",
                                                                "mobile", "bookid", "booktitle", "author",
                                                                "dateborrowed", "datedue", "days", "latereturnfine",
                                                                "dateoverdue", "finalprice"), 
                                           xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        xscroll.pack(side=tk.BOTTOM, fill=tk.X)
        yscroll.pack(side=tk.RIGHT, fill=tk.Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN NO.")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address1")
        self.library_table.heading("address2", text="Address2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days On Book")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=tk.BOTH, expand=1)

        self.fetch_data()

    def add_data(self):
        membertype = self.entries["Member Type:"].get()
        prnno = self.entries["PRN No:"].get()
        firstname = self.entries["Firstname:"].get()
        lastname = self.entries["Lastname:"].get()
        address1 = self.entries["Address1:"].get()
        address2 = self.entries["Address2:"].get()
        postid = self.entries["PostCode:"].get()
        mobile = self.entries["Mobile:"].get()
        bookid = self.entries["Book Id:"].get()
        booktitle = self.entries["Book Title:"].get()
        author = self.entries["Author Name:"].get()
        dateborrowed = self.entries["Date Borrowed:"].get()
        datedue = self.entries["Date Due:"].get()
        days = self.entries["Days on Book:"].get()
        latereturnfine = self.entries["Late Return Fine:"].get()
        dateoverdue = self.entries["Date Over Due:"].get()
        finalprice = self.entries["Actual Price:"].get()

        self.cursor.execute('''
            INSERT INTO library (membertype, prnno, firstname, lastname, address1, address2, postid, mobile,
                                 bookid, booktitle, author, dateborrowed, datedue, days, latereturnfine,
                                 dateoverdue, finalprice)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
            (membertype, prnno, firstname, lastname, address1, address2, postid, mobile,
             bookid, booktitle, author, dateborrowed, datedue, days, latereturnfine,
             dateoverdue, finalprice))
        
        self.conn.commit()
        self.fetch_data()
        self.reset()

    def show_data(self):
        self.fetch_data()

    def update(self):
        selected_item = self.library_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a record to update")
            return

        item_id = self.library_table.item(selected_item)['values'][0]  # Assuming the ID is the first column
        membertype = self.entries["Member Type:"].get()
        prnno = self.entries["PRN No:"].get()
        firstname = self.entries["Firstname:"].get()
        lastname = self.entries["Lastname:"].get()
        address1 = self.entries["Address1:"].get()
        address2 = self.entries["Address2:"].get()
        postid = self.entries["PostCode:"].get()
        mobile = self.entries["Mobile:"].get()
        bookid = self.entries["Book Id:"].get()
        booktitle = self.entries["Book Title:"].get()
        author = self.entries["Author Name:"].get()
        dateborrowed = self.entries["Date Borrowed:"].get()
        datedue = self.entries["Date Due:"].get()
        days = self.entries["Days on Book:"].get()
        latereturnfine = self.entries["Late Return Fine:"].get()
        dateoverdue = self.entries["Date Over Due:"].get()
        finalprice = self.entries["Actual Price:"].get()

        self.cursor.execute('''
            UPDATE library
            SET membertype=?, prnno=?, firstname=?, lastname=?, address1=?, address2=?, postid=?, mobile=?,
                bookid=?, booktitle=?, author=?, dateborrowed=?, datedue=?, days=?, latereturnfine=?,
                dateoverdue=?, finalprice=?
            WHERE id=?
        ''', (membertype, prnno, firstname, lastname, address1, address2, postid, mobile,
              bookid, booktitle, author, dateborrowed, datedue, days, latereturnfine,
              dateoverdue, finalprice, item_id))
        
        self.conn.commit()
        self.fetch_data()
        self.reset()

    def delete(self):
        selected_item = self.library_table.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a record to delete")
            return

        item_id = self.library_table.item(selected_item)['values'][0]  # Assuming the ID is the first column
        self.cursor.execute('DELETE FROM library WHERE id=?', (item_id,))
        self.conn.commit()
        self.fetch_data()

    def reset(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def exit_program(self):
        self.conn.close()
        exit_confirm = messagebox.askyesno("Library Management System", "Do you want to exit?")
        if exit_confirm > 0:
            self.root.destroy()

    def fetch_data(self):
        self.cursor.execute('SELECT * FROM library')
        rows = self.cursor.fetchall()
        self.library_table.delete(*self.library_table.get_children())
        for row in rows:
            self.library_table.insert("", tk.END, values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
