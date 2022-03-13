from tkinter import *
import sqlite3
import sys


def mains():
    global STUDENTS

    def connection():
        try:

            conn = sqlite3.connect("libraries.db")
        except:
            print("cannot connect to the database")
        return conn

    def verifier2():
        a = 0
        if not student_name.get():
            t1.insert(END, "<>Student name is required<>\n")
            a = 1
        if a == 1:
            return 1
        else:
            return 0

    def verifier():
        a = b = c = d = e = f = g = h = 0
        if not student_name.get():
            t7.insert(END, "<>Student name is required<>\n")
            a = 1
        if not roll_no.get():
            t7.insert(END, "<>Roll no is required<>\n")
            b = 1
        if not branch.get():
            t7.insert(END, "<>Branch is required<>\n")
            c = 1
        if not phone.get():
            t7.insert(END, "<>Phone number is requrired<>\n")
            d = 1
        if not book.get():
            t7.insert(END, "<>Book name is required<>\n")
            e = 1
        if not day.get():
            t7.insert(END, "<>Day is Required<>\n")
            f = 1
        if not day.get():
            t7.insert(END, "<>Months is Required<>\n")
            g = 1
        if not day.get():
            t7.insert(END, "<>Year is Required<>\n")
            h = 1
        if a == 1 or b == 1 or c == 1 or d == 1 or e == 1 or f == 1 or g == 1 or h == 1:
            return 1
        else:
            return 0

    def waithere(a):
        var = IntVar()
        root.after(a * 1000, var.set, 1)
        root.wait_variable(var)

    def add_student():
        ret = verifier()
        if ret == 0:
            conn = connection()
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS STUDENTS(NAME TEXT,ROLL_NO INTEGER,BRANCH TEXT,PHONE_NO INTEGER,BOOK TEXT,DAY TEXT,MONTH TEXT,YEAR TEXT,RDAY TEXT,RMONTH TEXT,RYEAR TEXT)")
            cur.execute("insert into STUDENTS values(?,?,?,?,?,?,?,?,?,?,?)", (
                student_name.get(), int(roll_no.get()), branch.get(), int(phone.get()), book.get(), int(day.get()),
                int(month.get()), int(year.get()), int(rday.get()), int(rmonth.get()), int(ryear.get())))
            conn.commit()
            conn.close()
            t7.insert(END, "ADDED SUCCESSFULLY !!!\n")

            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e7.delete(0, END)
            e8.delete(0, END)
            e9.delete(0, END)
            e10.delete(0, END)
            e11.delete(0, END)

            e1.insert(0, "  ")
            e2.insert(0, "  ")
            e3.insert(0, "  ")
            e4.insert(0, "  ")
            e5.insert(0, "  ")
            e6.insert(0, "  ")
            e7.insert(0, "  ")
            e8.insert(0, "  ")
            e9.insert(0, "  ")
            e10.insert(0, "  ")
            e11.insert(0, "  ")

            waithere(5)
            t7.delete(1.0, END)

    def view_student():
        conn = connection()
        cur = conn.cursor()
        cur.execute("select * from STUDENTS")
        data = cur.fetchall()
        conn.close()
        t1.delete(1.0, END)
        t2.delete(1.0, END)
        t3.delete(1.0, END)
        t4.delete(1.0, END)
        t5.delete(1.0, END)
        t6.delete(1.0, END)
        t8.delete(1.0, END)
        for i in data:
            t1.insert(END, str(i[0]) + "\n")
            t2.insert(END, str(i[1]) + "\n")
            t3.insert(END, str(i[2]) + "\n")
            t4.insert(END, str(i[3]) + "\n")
            t5.insert(END, str(i[4]) + "\n")
            t6.insert(END, f"{str(i[5])}/{str(i[6])}/{str(i[7])} \n")
            t8.insert(END, f"{str(i[8])}/{str(i[9])}/{str(i[10])} \n")

    def delete_student():
        ret = verifier()
        if ret == 0:
            conn = connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM STUDENTS WHERE ROLL_NO=?", (int(roll_no.get()),))
            conn.commit()
            conn.close()
            t7.insert(END, "SUCCESSFULLY DELETED THE USER\n")
            e2.delete(0, END)
            waithere(5)
            t7.delete(1.0, END)

    def delete_Record():
        try:
            conn = connection()
            cur = conn.cursor()

            sql_delete_query = "DELETE FROM STUDENTS WHERE ROLL_NO!=0"
            cur.execute(sql_delete_query)
            conn.commit()
            cur.close()

        except sqlite3.Error as error:
            print("Failed to delete record from sqlite table", error)
        finally:
            if conn:
                conn.close()
        t7.insert(END, "Record deleted successfully ")
        waithere(5)
        t7.delete(1.0, END)

    def clse():
        sys.exit()

    def show():
        global a
        if clicked.get() == "Dark":
            root.configure(bg='#111111')
            a, b = 'cyan', 'black'
            c = a
        elif clicked.get() == 'Light':
            root.configure(bg='white')
            a, b = 'lightblue', 'black'
            c = a
        elif clicked.get() == 'Earth':
            root.configure(bg='Blue')
            a, b = 'Green', 'yellow'
            c = a
        elif clicked.get() == 'Fire':
            root.configure(bg='Red')
            a, b = 'yellow', 'blue'
            c = a
        elif clicked.get() == 'Default':
            root.configure(bg='lightgray')
            a, b, c = 'lightgray', 'black', 'white'
        n = 11
        b1.configure(bg=a, fg=b, font=("bold", n))
        b2.configure(bg=a, fg=b, font=("bold", n))
        b3.configure(bg=a, fg=b, font=("bold", n))
        b4.configure(bg=a, fg=b, font=("bold", n))
        b5.configure(bg=a, fg=b, font=("bold", n))
        button.configure(bg=a, fg=b, font=("bold", n))
        e1.configure(bg=c, fg=b, font=("bold", n))
        e2.configure(bg=c, fg=b, font=("bold", n))
        e3.configure(bg=c, fg=b, font=("bold", n))
        e4.configure(bg=c, fg=b, font=("bold", n))
        e5.configure(bg=c, fg=b, font=("bold", n))
        e6.configure(bg=c, fg=b, font=("bold", n))
        e7.configure(bg=c, fg=b, font=("bold", n))
        e8.configure(bg=c, fg=b, font=("bold", n))
        e9.configure(bg=c, fg=b, font=("bold", n))
        e10.configure(bg=c, fg=b, font=("bold", n))
        e11.configure(bg=c, fg=b, font=("bold", n))
        label1.configure(bg=a, fg=b, font=("bold", n))
        label2.configure(bg=a, fg=b, font=("bold", n))
        label3.configure(bg=a, fg=b, font=("bold", n))
        label4.configure(bg=a, fg=b, font=("bold", n))
        label5.configure(bg=a, fg=b, font=("bold", n))
        label6.configure(bg=a, fg=b, font=("bold", n))
        label7.configure(bg=a, fg=b, font=("bold", n))
        drop.configure(bg=a, fg=b, font=("bold", n))
        t1.configure(bg=c, fg=b, font=("bold", n))
        t2.configure(bg=c, fg=b, font=("bold", n))
        t3.configure(bg=c, fg=b, font=("bold", n))
        t4.configure(bg=c, fg=b, font=("bold", n))
        t5.configure(bg=c, fg=b, font=("bold", n))
        t6.configure(bg=c, fg=b, font=("bold", n))
        t7.configure(bg=c, fg=b, font=("bold", n))
        t8.configure(bg=c, fg=b, font=("bold", n))
        l1.configure(bg=c, fg=b, font=("bold", n))
        l2.configure(bg=c, fg=b, font=("bold", n))
        l3.configure(bg=c, fg=b, font=("bold", n))
        l4.configure(bg=c, fg=b, font=("bold", n))
        l5.configure(bg=c, fg=b, font=("bold", n))
        l6.configure(bg=c, fg=b, font=("bold", n))
        l7.configure(bg=c, fg=b, font=("bold", n))

    if _name == "main_":
        global root
        root = Tk()
        root.title("Library Management System Powered by: RrepelX")
        root.geometry("1417x530")

        global student_name
        global roll_no
        global branch
        global phone
        global book
        global day
        global month
        global year
        global rday
        global rmonth
        global ryear
        student_name = StringVar()
        roll_no = StringVar()
        branch = StringVar()
        phone = StringVar()
        book = StringVar()
        day = StringVar()
        month = StringVar()
        year = StringVar()
        rday = StringVar()
        rmonth = StringVar()
        ryear = StringVar()

        label1 = Label(root, text="Student name:", font=("bold", 11))
        label1.place(x=0, y=0)

        label2 = Label(root, text="Roll no:", font=("bold", 11))
        label2.place(x=0, y=30)

        label3 = Label(root, text="Branch:", font=("bold", 11))
        label3.place(x=0, y=60)

        label4 = Label(root, text="Phone Number:", font=("bold", 11))
        label4.place(x=0, y=90)

        label5 = Label(root, text="Book Name:", font=("bold", 11))
        label5.place(x=0, y=120)

        label6 = Label(root, text="Issue Date:", font=("bold", 11))
        label6.place(x=0, y=150)

        label7 = Label(root, text="Reutn Date:", font=("bold", 11))
        label7.place(x=0, y=180)

        l1 = Label(root, text="Student Name", font=("bold", 11))
        l1.place(x=380, y=0)

        l2 = Label(root, text="Roll No.", font=("bold", 11))
        l2.place(x=530, y=0)

        l3 = Label(root, text="Branch", font=("bold", 11))
        l3.place(x=680, y=0)

        l4 = Label(root, text="Phone Number:", font=("bold", 11))
        l4.place(x=830, y=0)

        l5 = Label(root, text="Book Name", font=("bold", 11))
        l5.place(x=980, y=0)

        l6 = Label(root, text="Issue Date", font=("bold", 11))
        l6.place(x=1130, y=0)

        l7 = Label(root, text="Return Date", font=("bold", 11))
        l7.place(x=1280, y=0)

        e1 = Entry(root, textvariable=student_name, font=("bold", 11))
        e1.insert(0, "  ")
        e1.place(x=150, y=0)

        e2 = Entry(root, textvariable=roll_no, font=("bold", 11))
        e2.insert(0, "  ")
        e2.place(x=150, y=30)

        e3 = Entry(root, textvariable=branch, font=("bold", 11))
        e3.insert(0, "  ")
        e3.place(x=150, y=60)

        e4 = Entry(root, textvariable=phone, font=("bold", 11))
        e4.insert(0, "  ")
        e4.place(x=150, y=90)

        e5 = Entry(root, textvariable=book, font=("bold", 11))
        e5.insert(0, "  ")
        e5.place(x=150, y=120)

        e6 = Entry(root, textvariable=day, font=("bold", 11), width=6)
        e6.insert(0, "  ")
        e6.place(x=150, y=150)

        e7 = Entry(root, textvariable=month, font=("bold", 11), width=6)
        e7.insert(0, "  ")
        e7.place(x=205, y=150)

        e8 = Entry(root, textvariable=year, font=("bold", 11), width=6)
        e8.insert(0, "  ")
        e8.place(x=260, y=150)

        e9 = Entry(root, textvariable=rday, font=("bold", 11), width=6)
        e9.insert(0, "  ")
        e9.place(x=150, y=180)

        e10 = Entry(root, textvariable=rmonth, font=("bold", 11), width=6)
        e10.insert(0, "  ")
        e10.place(x=205, y=180)

        e11 = Entry(root, textvariable=ryear, font=("bold", 11), width=6)
        e11.insert(0, "  ")
        e11.place(x=260, y=180)

        t1 = Text(root, width=20, height=20, font=("bold", 11))
        t1.place(x=370, y=30)

        t2 = Text(root, width=20, height=20, font=("bold", 11))
        t2.place(x=520, y=30)

        t3 = Text(root, width=20, height=20, font=("bold", 11))
        t3.place(x=670, y=30)

        t4 = Text(root, width=20, height=20, font=("bold", 11))
        t4.place(x=820, y=30)

        t5 = Text(root, width=20, height=20, font=("bold", 11))
        t5.place(x=970, y=30)

        t6 = Text(root, width=20, height=20, font=("bold", 11))
        t6.place(x=1100, y=30)

        t7 = Text(root, width=111, height=5, font=("bold", 11))
        t7.place(x=370, y=377)

        t8 = Text(root, width=20, height=20, font=("bold", 11))
        t8.place(x=1250, y=30)

        b1 = Button(root, text="ADD STUDENT", command=add_student, width=40, font=("bold", 11))
        b1.place(x=0, y=375)

        b2 = Button(root, text="VIEW ALL STUDENTS", command=view_student, width=40, font=("bold", 11))
        b2.place(x=0, y=405)

        b3 = Button(root, text="DELETE STUDENT", command=delete_student, width=40, font=("bold", 11))
        b3.place(x=0, y=435)

        b4 = Button(root, text="Close", command=clse, width=40, font=("bold", 11))
        b4.place(x=0, y=495)

        b5 = Button(root, text="Clear", command=delete_Record, width=40, font=("bold", 11))
        b5.place(x=0, y=465)

        options = ["Default", "Dark", "Light", "Earth", "Fire"]
        clicked = StringVar()
        clicked.set("Default")
        drop = OptionMenu(root, clicked, *options)
        drop.configure(width=8, height=1, font=("bold", 11))
        drop.place(x=370, y=465)
        a = 'white'
        button = Button(root, text="THEMES", command=show)
        button.configure(width=11, height=1, font=("bold", 11))
        button.place(x=370, y=495)

        root.mainloop()


def login():
    uname = username.get()
    pwd = password.get()
    if uname == '' or pwd == '':
        message.set("fill the empty field!!!")
    else:
        if uname == "RrepelX" and pwd == "123456":
            message.set("Login success")
            login_screen.destroy()
            mains()

        else:
            message.set("Wrong username or password!!!")


def Loginform():
    global login_screen
    login_screen = Tk()

    login_screen.title("Login Form")

    login_screen.geometry("300x250")

    global message
    global username
    global password
    username = StringVar()
    password = StringVar()
    message = StringVar()

    la = Label(login_screen, width="300", text="Please enter details below").pack()

    lb = Label(login_screen, text="Username * ").place(x=20, y=40)

    ea = Entry(login_screen, textvariable=username).place(x=90, y=42)

    lc = Label(login_screen, text="Password * ").place(x=20, y=80)

    eb = Entry(login_screen, textvariable=password, show="*").place(x=90, y=82)

    ld = Label(login_screen, text="", textvariable=message).place(x=95, y=100)

    ba = Button(login_screen, text="Login", width=10, height=1, command=login).place(x=105, y=130)
    login_screen.mainloop()


Loginform()