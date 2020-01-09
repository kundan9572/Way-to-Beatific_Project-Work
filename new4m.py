from Tkinter import *
import  Tkinter as tk
import tkMessageBox
#top=Tk()

import sqlite3
db = sqlite3.connect('WAB')
cursor1 = db.cursor()
cursor2 = db.cursor()

#cursor1.execute('''CREATE TABLE customers(name TEXT,email TEXT, phone_no TEXT, password TEXT)''')
#cursor2.execute('''CREATE TABLE flight(name TEXT,source TEXT,destination TEXT, total INTEGER,booked INTEGER,cancelled INTEGER,available INTEGER)''')

if cursor2.execute('''INSERT INTO flight(name,source,destination,total,booked,cancelled,available) VALUES(?,?,?,?,?,?,?)''', ('Beatific-CM',
'Chennai(MAA)','Mumbai(BOM)',150,0,0,150)):
     print 'Record inserted successfully'
if cursor2.execute('''INSERT INTO flight(name,source,destination,total,booked,cancelled,available) VALUES(?,?,?,?,?,?,?)''', ('Beatific-CK',
'Chennai(MAA)','Kolkata(CCU)',150,0,0,150)):
     print 'Record inserted successfully'
if cursor2.execute('''INSERT INTO flight(name,source,destination,total,booked,cancelled,available) VALUES(?,?,?,?,?,?,?)''', ('Beatific-CD',
'Chennai(MAA)','Delhi(DEL)',150,0,0,150)):
     print 'Record inserted successfully'
if cursor2.execute('''INSERT INTO flight(name,source,destination,total,booked,cancelled,available) VALUES(?,?,?,?,?,?,?)''', ('Beatific-DM',
'Delhi(DEL)','Mumbai(BOM)',150,0,0,150)):
     print 'Record inserted successfully'
if cursor2.execute('''INSERT INTO flight(name,source,destination,total,booked,cancelled,available) VALUES(?,?,?,?,?,?,?)''', ('Beatific-DK',
'Delhi(DEL)','Kolkata(CCU)',150,0,0,150)):
     print 'Record inserted successfully'
if cursor2.execute('''INSERT INTO flight(name,source,destination,total,booked,cancelled,available) VALUES(?,?,?,?,?,?,?)''', ('Beatific-DC',
'Delhi(DEL)','Chennai(MAA)',150,0,0,150)):
     print 'Record inserted successfully'
if cursor2.execute('''INSERT INTO flight(name,source,destination,total,booked,cancelled,available) VALUES(?,?,?,?,?,?,?)''', ('Beatific-KM',
'Kolkata(CCU)','Mumbai(BOM)',150,0,0,150)):
     print 'Record inserted successfully'
if cursor2.execute('''INSERT INTO flight(name,source,destination,total,booked,cancelled,available) VALUES(?,?,?,?,?,?,?)''', ('Beatific-KC',
'Kolkata(CCU)','Chennai(MAA)',150,0,0,150)):
     print 'Record inserted successfully'
if cursor2.execute('''INSERT INTO flight(name,source,destination,total,booked,cancelled,available) VALUES(?,?,?,?,?,?,?)''', ('Beatific-KD',
'Kolkata(CCU)','Delhi(DEL)',150,0,0,150)):
     print 'Record inserted successfully'
if cursor2.execute('''INSERT INTO flight(name,source,destination,total,booked,cancelled,available) VALUES(?,?,?,?,?,?,?)''', ('Beatific-MC',
'Mumbai(BOM)','Chennai(MAA))',150,0,0,150)):
     print 'Record inserted successfully'
if cursor2.execute('''INSERT INTO flight(name,source,destination,total,booked,cancelled,available) VALUES(?,?,?,?,?,?,?)''', ('Beatific-MD',
'Mumbai(BOM)','Delhi(DEL)',150,0,0,150)):
     print 'Record inserted successfully'
if cursor2.execute('''INSERT INTO flight(name,source,destination,total,booked,cancelled,available) VALUES(?,?,?,?,?,?,?)''', ('Beatific-MK',
'Mumbai(BOM)','Kolkata(CCU)',150,0,0,150)):
     print 'Record inserted successfully'

db.commit()


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self,bg = 'white')

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        l = tk.Label(self,text = "WAY TO BEATIFIC",fg = 'white',bg = 'blue')
        l.config(font= ("Courier",30),height =3 ,width = 200)
        l.grid(row = 1,column = 0)
        l.pack(pady=10,padx=10)
        label = tk.Label(self, text="HOME",fg = 'blue', bg = 'white')
        label.config(font=("Courier", 20), height=1, width=200)
        label.grid(row=1, column=0)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="REGISTER",
                   command=lambda: controller.show_frame(PageOne),bg = 'black', fg = 'white')
        button.config(font=("Courier", 20), height=1, width=10)
        button.grid(row=1, column=0)
        button.pack(pady=10, padx=10)


        button2 = tk.Button(self, text="LOGIN",
                    command=lambda: controller.show_frame(PageTwo),bg = 'black', fg = 'white')
        button2.config(font=("Courier", 20), height=1, width=10)
        button2.grid(row=1, column=0)
        button2.pack(pady=10, padx=10)


        m = tk.Label(self, text = "Way to Beatific is a major Indian airline with its headquarters in Chennai.",fg = 'blue',bg = 'white')
        m.config(font=("Courier", 20), height=1, width=400)
        m.grid(row=1, column=0)
        m.pack()
        m1 = tk.Label(self, text = "It is currently connecting four meteropolitan cities of India.",fg = 'blue', bg = 'white')
        m1.config(font=("Courier", 20), height=1, width=400)
        m1.grid(row=1, column=0)
        m1.pack()
        m2 = tk.Label(self, text="It was started in June 2k18", fg='blue',bg='white')
        m2.config(font=("Courier", 20), height=1, width=400)
        m2.grid(row=1, column=0)
        m2.pack()
        m3 = tk.Label(self, text="Fleet Size: 109", fg='blue',bg='white')
        m3.config(font=("Courier", 20), height=1, width=400)
        m3.grid(row=1, column=0)
        m3.pack()
        m4 = tk.Label(self, text="Company Slogan : ThE JoY Of FlYiNg", fg='blue', bg='white')
        m4.config(font=("Courier", 20), height=1, width=400)
        m4.grid(row=1, column=0)
        m4.pack()
        m5 = tk.Label(self, text="Destinations : 4", fg='blue', bg='white')
        m5.config(font=("Courier", 20), height=1, width=400)
        m5.grid(row=1, column=0)
        m5.pack()
        m6 = tk.Label(self, text="Headquarters: Chennai", fg='blue', bg='white')
        m6.config(font=("Courier", 20), height=1, width=400)
        m6.grid(row=1, column=0)
        m6.pack()
        m7 = tk.Label(self, text="Customer Service : 044 44018798", fg='blue', bg='white')
        m7.config(font=("Courier", 20), height=1, width=400)
        m7.grid(row=1, column=0)
        m7.pack()
        m8 = tk.Label(self, text="Contact us : wayToBeatific@gmail.com", fg='blue', bg='white')
        m8.config(font=("Courier", 20), height=1, width=400)
        m8.grid(row=1, column=0)
        m8.pack()
        m9 = tk.Label(self, text="copyright 2018 Way To Beatific", fg='blue', bg='white')
        m9.config(font=("Courier", 20), height=1, width=400)
        m9.grid(row=1, column=0)
        m9.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="REGISTER YOURSELF!!!", fg='white', bg='blue')
        label.config(font=("Courier", 30), height=3, width=200)
        label.grid(row=1, column=0)
        label.pack(pady=10, padx=10)
        button = tk.Button(self, text="Back to Home",
                   command=lambda: controller.show_frame(StartPage),bg = 'black', fg = 'white')
        button.config(font=("Courier", 20), height=1, width=20)
        button.grid(row=1, column=0)
        button.pack(pady=10, padx=10)

        button = tk.Button(self, text="LOGIN",
                   command=lambda: controller.show_frame(PageTwo),bg = 'black', fg = 'white')
        button.config(font=("Courier", 20), height=1, width=10)
        button.grid(row=1, column=0)
        button.pack(pady=10, padx=10)


        leftframe=Frame(self,bg = 'white')
        leftframe.pack(side=LEFT)
        rightframe=Frame(self, bg = 'white')
        rightframe.pack(side=RIGHT)
        bottomframe=Frame(self, bg = 'white')
        bottomframe.pack(side=BOTTOM)
        L1=Label(leftframe,text="UserName",height=2,width=10, fg='black', bg='white')
        L1.config(font=("Courier", 20), height=1, width=40)
        L1.grid(row=1, column=0)
        L1.pack(pady=10, padx=10)

        E1=Entry(rightframe,bd=8,fg = "black",bg= "white")
        E1.config(font = ("Courier",15),width = 30)
        E1.grid(row = 5, column = 0)
        E1.pack(pady = 10,padx = 10)

        L2 = Label(leftframe, text="Email ID", height=2, width=10, fg='black', bg='white')
        L2.config(font=("Courier", 20), height=1, width=40)
        L2.grid(row=1, column=0)
        L2.grid(row=1, column=0)
        L2.pack(pady=10, padx=10)

        E2 = Entry(rightframe, bd=8, fg="black", bg="white")
        E2.config(font=("Courier", 15), width=30)
        E2.grid(row=5, column=0)
        E2.pack(pady=10, padx=10)

        L3 = Label(leftframe, text="Phone Number", height=2, width=10, fg='black', bg='white')
        L3.config(font=("Courier", 20), height=1, width=40)
        L3.grid(row=1, column=0)
        L3.pack(pady=10, padx=10)

        E3 = Entry(rightframe, bd=8, fg="black", bg="white")
        E3.config(font=("Courier", 15), width=30)
        E3.grid(row=5, column=0)
        E3.pack(pady=10, padx=10)

        L4 = Label(leftframe, text="Password", height=2, width=10, fg='black', bg='white')
        L4.config(font=("Courier", 20), height=1, width=40)
        L4.grid(row=1, column=0)
        L4.pack(pady=10, padx=10)

        E4 = Entry(rightframe, bd=8, fg="black", bg="white")
        E4.config(font=("Courier", 15), width=30)
        E4.grid(row=5, column=0)
        E4.pack(pady=10, padx=10)



        def ok():
            tkMessageBox.showwarning("Submission", "Registered successfully")
            if cursor1.execute('''INSERT INTO customers(name,email,phone_no,password)VALUES(?,?,?,?)''',(E1.get(),E2.get(),
            E3.get(),E4.get())):
                print "Values inserted successfully"
            db.commit()
            controller.show_frame(PageTwo)


        button3=tk.Button(bottomframe,text="REGISTER",command=ok,bg = 'black', fg = 'white')
        button3.config(font=("Courier", 20), height=1, width=10)
        button3.grid(row=1, column=0)
        button3.pack(side = LEFT,pady=10, padx=10)


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        label = tk.Label(self, text="PLEASE LOGIN!!!", bg="blue", fg="white")
        label.config(font=("Courier", 50), height=2, width=800)
        label.grid(row=0, column=100)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage), bg="black", fg="white")
        button1.config(font=("Courier", 20), height=1, width=15)
        button1.grid(row=1, column=0)
        button1.pack(pady=10, padx=10)

        button2 = tk.Button(self, text="REGISTER",
                            command=lambda: controller.show_frame(PageOne), bg="black", fg="white")
        button2.config(font=("Courier", 20), height=1, width=15)
        button2.grid(row=1, column=4000)
        button2.pack(pady=10, padx=10)

        leftframe = Frame(self)
        leftframe.pack(side=LEFT)
        rightframe = Frame(self)
        rightframe.pack(side=RIGHT)
        bottomframe = Frame(self)
        bottomframe.pack(side=BOTTOM)
        L5 = Label(leftframe, text="UserName", fg="black", bg="white")
        L5.config(font=("Courier", 30), width=10)
        L5.grid(row=5, column=0)
        L5.pack(pady=10, padx=10)
        E5 = Entry(rightframe, bd=8, fg="black", bg="white")
        E5.config(font=("Courier", 20), width=20)
        E5.grid(row=5, column=0)
        E5.pack(pady=10, padx=10)
        L6 = Label(leftframe, text="Password", fg="black", bg="white")
        L6.config(font=("Courier", 30), width=10)
        L6.grid(row=5, column=0)
        L6.pack(pady=10, padx=10)
        E6 = Entry(rightframe, bd=8, fg="black", bg="white")
        E6.config(font=("Courier", 20), width=20)
        E6.grid(row=5, column=0)
        E6.pack(pady=10, padx=10)

        def ok3():
            if cursor1.execute('''SELECT password FROM customers WHERE name=?''', (E5.get(),)):
                print "Record fetched successfully"

            pwd = str(cursor1.fetchone())
            print pwd
            pwd1 = str(E6.get())
            print pwd1
            pwd2 = "(u'" + pwd1 + "',)"

            if (pwd2 == pwd):
                tkMessageBox.showwarning("Correct", "You have successfully logged in")
                controller.show_frame(PageThree)
            else:
                tkMessageBox.showwarning("Incorrect", "Incorrect username or password")

        button4 = tk.Button(self, text="Log In", command=ok3, bg="black", fg="white")
        button4.config(font=("Courier", 20), height=1, width=15)

        button4.grid(row=50, column=4000)
        button4.pack(side=BOTTOM, pady=10, padx=10)


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="white")
        label = tk.Label(self, text="WAY TO BEATIFIC!!!",fg="white",bg="blue")
        label.config(font=("Courier", 50),height=2,width=800)
        label.grid(row=0,column=50)
        label.pack(pady=5, padx=5)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage),bg="blue",fg="white")
        button1.config(font=("Courier", 15), height=1, width=15)
        button1.grid()
        button1.pack(pady=10, padx=10)

        leftframe = Frame(self,bg="white")
        leftframe.pack(side=LEFT)
        rightframe = Frame(self,bg="white")
        rightframe.pack(side=RIGHT)
        bottomframe = Frame(self,bg="white")
        bottomframe.pack(side=BOTTOM)
        L7 = Label(leftframe, text="Enter the source terminal:",fg="black",bg="white")
        L7.config(font=("Courier", 15), width=30)
        L7.grid(row=5, column=0)
        L7.pack(pady=5, padx=5)

        mn1 = Menubutton(self, text="FROM", relief=RAISED,fg="black",bg="white")
        mn1.config(font=("Courier", 15), width=30)
        mn1.grid(row=5, column=0)
        mn1.menu = Menu(mn1, tearoff=0)
        mn1["menu"] = mn1.menu
        c = IntVar()
        d = IntVar()
        k = IntVar()
        m = IntVar()

        mn1.menu.add_checkbutton(label="Chennai(MAA)", variable=c)
        mn1.menu.add_checkbutton(label="Delhi(DEL)", variable=d)
        mn1.menu.add_checkbutton(label="Kolkata(CCU)", variable=k)
        mn1.menu.add_checkbutton(label="Mumbai(BOM)", variable=m)

        mn1.pack(side=RIGHT,pady=10, padx=10)

        E8 = Entry(rightframe, bd=8,fg="black",bg="white")
        E8.config(font=("Courier", 15), width=30)
        E8.grid(row=5, column=0)
        E8.pack(pady=10, padx=10)

        L8 = Label(leftframe, text="Enter the destination terminal:",fg="black",bg="white")
        L8.config(font=("Courier", 15), width=30)
        L8.grid(row=5, column=0)
        L8.pack(pady=5, padx=5)

        mn2 = Menubutton(self, text="TO", relief=RAISED,fg="black",bg="white")
        mn2.config(font=("Courier", 15), width=30)
        mn2.grid()
        mn2.menu = Menu(mn2, tearoff=0)
        mn2["menu"] = mn2.menu
        c = IntVar()
        d = IntVar()
        k = IntVar()
        m = IntVar()

        mn2.menu.add_checkbutton(label="Chennai(MAA)", variable=c)
        mn2.menu.add_checkbutton(label="Delhi(DEL)", variable=d)
        mn2.menu.add_checkbutton(label="Kolkata(CCU)", variable=k)
        mn2.menu.add_checkbutton(label="Mumbai(BOM)", variable=m)

        mn2.pack(side=RIGHT,pady=10, padx=10)

        E9 = Entry(rightframe, bd=8,fg="black",bg="white")
        E9.config(font=("Courier", 15), width=30)
        E9.grid(row=5, column=0)
        E9.pack(pady=10, padx=10)

        l8 = Label(leftframe, text="Price per ticket:", fg="black", bg="white")
        l8.config(font=("Courier", 15), width=30)
        l8.grid(row=5, column=0)
        l8.pack(pady=10, padx=10)

        l9 = Label(rightframe, text="2499", fg="black", bg="white")
        l9.config(font=("Courier", 15), height = 1,width=30)
        l9.grid(row=5, column=0)
        l9.pack(pady=5, padx=5)

        L9 = Label(leftframe, text="Enter the no of Tickets you want to book:",fg="black",bg="white")
        L9.config(font=("Courier", 15), width=42)
        L9.grid(row=5, column=0)
        L9.pack(pady=10, padx=10)
        E10 = Entry(rightframe, bd=8,fg="black",bg="white")
        E10.config(font=("Courier", 15), width=30)
        E10.grid(row=5, column=0)
        E10.pack(pady=10, padx=10)

        L10 = Label(leftframe, text="Enter the no of Tickets you want to cancel:",fg="black",bg="white")
        L10.config(font=("Courier", 15), width=42)
        L10.grid(row=5, column=0)
        L10.pack(pady=5, padx=5)
        E11 = Entry(rightframe, bd=8,fg="black",bg="white")
        E11.config(font=("Courier", 15), width=30)
        E11.grid(row=5, column=0)
        E11.pack(pady=10, padx=10)

        var1 = StringVar()
        var2 = StringVar()
        #msg1 = Message(rightframe, textvariable=var1, relief=RAISED,fg="black",bg="white")
        #msg1.config(font=("Courier", 10))
        #msg2 = Message(rightframe, textvariable=var2, relief=RAISED,fg="black",bg="white")
        #msg2.config(font=("Courier", 10))
        msg1 = Label(rightframe, textvariable=var1,text = " ", relief=RAISED,fg="black",bg="white")
        msg1.config(font=("Courier", 10),height = 1,width = 20)
        msg1.pack()
        msg2 = Label(rightframe, textvariable=var2,text =" ", relief=RAISED,fg="black",bg="white")
        msg2.config(font=("Courier", 10),height = 1,width = 20)
        msg2.pack()

        def ok4():
            if cursor2.execute('''SELECT name FROM flight WHERE source=? AND destination=?''',(E8.get(),E9.get(),)):
                print 'Record fetched successfully!'
            record1 = cursor2.fetchone()
            print record1
            var1.set(record1)
            if cursor2.execute('''SELECT available FROM flight WHERE source=? AND destination=?''',(E8.get(),E9.get(),)):
                print 'Record fetched successfully!'
            c1= cursor2.fetchone()
            c1=str(c1)
            if (len(c1)==6):
                c1=c1[1:4]
                print c1
            elif (len(c1)==5):
                c1 = c1[1:3]
                print c1
            elif (len(c1)==4):
                c1 = c1[1:2]
                print c1

            c1=int(c1)

            var2.set(c1 )
            msg1.pack()
            msg2.pack()


        button5=Button(bottomframe,text='Show Flights',command=ok4,bg="black",fg="white")
        button5.config(font=("Courier", 15), height=1, width=15)
        button5.grid()
        button5.pack(pady=10, padx=10)

        L7 = Label(leftframe, text="Your Flight ",fg="black",bg="white")
        L7.config(font=("Courier", 15), width=30)
        L7.grid(row=5, column=0)
        L7.pack(pady=10, padx=10)

        L8 = Label(leftframe, text="Available Seats ",fg="black",bg="white")
        L8.config(font=("Courier", 15), width=30)
        L8.grid(row=5, column=0)
        L8.pack(pady=10, padx=10)



        def ok1():
            tkMessageBox.showwarning("Booking", "Booked successfully")
            if cursor2.execute('''SELECT booked FROM flight WHERE source=? AND destination=?''',(E8.get(),E9.get(),)):
                print 'Record fetched successfully!'
            a1= cursor2.fetchone()
            a1=str(a1)
            if (len(a1)==4):
                a1=a1[1:2]
                print a1
            elif (len(a1)==5):
                a1 = a1[1:3]
                print a1
            elif (len(a1)==6):
                a1 = a1[1:4]
                print a1
            a1=int(a1)
            d = int(E10.get())
            print d
            a1=a1+d

            if cursor2.execute('''SELECT available FROM flight WHERE source=? AND destination=?''',(E8.get(),E9.get(),)):
                print 'Record fetched successfully!'
            c1= cursor2.fetchone()
            c1=str(c1)
            if (len(c1)==6):
                c1=c1[1:4]
                print c1
            elif (len(c1)==5):
                c1 = c1[1:3]
                print c1
            elif (len(c1)==4):
                c1 = c1[1:2]
                print c1

            c1=int(c1)
            c1=c1-d



            if cursor2.execute('''UPDATE flight SET booked=? WHERE source=? AND destination=?''',(a1,E8.get(),E9.get(),)):
                print 'Record fetched successfully!'
            if cursor2.execute('''UPDATE flight SET available=? WHERE source=? AND destination=?''',(c1,E8.get(),E9.get(),)):
                print 'Record fetched successfully!'
            db.commit()


        def ok2():
            tkMessageBox.showwarning("Cancelling", "Cancelled successfully")
            if cursor2.execute('''SELECT cancelled FROM flight WHERE source=? AND destination=?''',(E8.get(),E9.get(),)):
                print 'Record fetched successfully!'
            b1= cursor2.fetchone()
            b1=str(b1)
            if (len(b1)==4):
                b1=b1[1:2]
                print b1
            elif (len(b1)==5):
                b1 = b1[1:3]
                print b1
            elif (len(b1)==6):
                b1 = b1[1:4]
                print b1
            b1=int(b1)
            e = int(E11.get())
            print e
            b1=b1+e

            if cursor2.execute('''SELECT available FROM flight WHERE source=? AND destination=?''',(E8.get(),E9.get(),)):
                print 'Record fetched successfully!'
            c1= cursor2.fetchone()
            c1=str(c1)
            if (len(c1)==6):
                c1=c1[1:4]
                print c1
            elif (len(c1)==5):
                c1 = c1[1:3]
                print c1
            elif (len(c1)==4):
                c1 = c1[1:2]
                print c1

            c1=int(c1)
            c1=c1+e



            if cursor2.execute('''UPDATE flight SET cancelled=? WHERE source=? AND destination=?''',(b1,E8.get(),E9.get(),)):
                print 'Record fetched successfully!'
            if cursor2.execute('''UPDATE flight SET available=? WHERE source=? AND destination=?''',(c1,E8.get(),E9.get(),)):
                print 'Record fetched successfully!'
            db.commit()

        button6 = tk.Button(bottomframe, text="Book", command=ok1,bg="black",fg="white")
        button6.config(font=("Courier", 15), height=1, width=15)
        button6.grid(row=50, column=4000)
        button6.pack(side=BOTTOM, pady=10, padx=10)

        button7 = tk.Button(bottomframe, text="Cancell", command=ok2,bg="black",fg="white")
        button7.config(font=("Courier", 15), height=1, width=15)
        button7.grid(row=50, column=4000)
        button7.pack(side=BOTTOM, pady=10, padx=10)


app=SeaofBTCapp()
app.mainloop()

