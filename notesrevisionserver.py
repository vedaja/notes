from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import pytz
timezone=pytz.timezone("US/Pacific")
from datetime import datetime
import socket
from threading import Thread
import os

root=Tk()
root.title("Notes")
root.geometry("400x400")

noteslist=[]

fileslist=os.listdir(r"/Users/vjanga/PycharmProjects/Algorithms/client1")
print(fileslist)


host=""
port=2357
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
con,address=s.accept()


class Notes:
    def __init__(self,text,title):
        self.title=title
        self.text=text
        current=datetime.now(timezone)
        self.time=current.strftime('%Y-%m-%d %I:%M:%S %p%Z')

    def display(self):
     print(self.text+", "+self.time)


# def create():
#     global entry,textbox,note_window
#     note_window=Toplevel(root)
#     entry=Entry(note_window)
#     entry.grid(row=0,column=0)
#
#     textbox=Text(note_window)
#     textbox.grid(row=1,column=0)
#
#     submit=Button(note_window,text="Submit",command=enter)
#     submit.grid(row=2,column=0)

#def enter():
    #global entry,textbox,note_window,n,title
    #title = entry.get()
    #note = textbox.get("1.0", END)
    #noteslist.append(Notes(note,title))
    #listbox.insert(END,title)

    #n=open(title+".txt","w")
    #n.write(note)
    #n.close()

    #note_window.destroy()
    #messagebox.showinfo("Note recieved","Your note has been added to the list.")
    #root.update()

def opennote():
    #global n,title

    #t=Label(open_window,text=title)
    #t.grid(row=0,column=0)

    #o=Label(open_window,text=words)
    #o.grid(row=1,column=0)
    while True:
        data=con.recv(1024)
        data=data.decode()

        n = open(r"/Users/vjanga/PycharmProjects/Algorithms/client1/"+data + ".txt", "r")
        f1=Frame(cframe,bg="red")
        f1.pack(fill=X)

        name=n.readline()
        namelabel=Label(f1,text=name)
        title =n.readline()
        tlabel=Label(f1,text=title)
        tlabel.pack()
        note = n.readline()
        nlabel=Label(f1,text=note,justify=LEFT)
        nlabel.pack()
        namelabel.pack(side=RIGHT)

        canvas.yview_moveto(1)
        canvas.config(scrollregion=canvas.bbox('all'))


canvas=Canvas(root,width=390,height=400)
canvas.pack(side=LEFT)

cframe=Frame(canvas)
canvas.create_window((0,0),window=cframe,anchor=NW,width=400)

scroll=Scrollbar(root,orient=VERTICAL)
scroll.config(command=canvas.yview)
#canvas.config(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT,fill=Y)


for i in fileslist:
    f2=Frame(cframe,bg='#beebee')

    k=open(r"/Users/vjanga/PycharmProjects/Algorithms/client1/"+i,"r")
    user=k.readline()
    userlabel=Label(f2,text="User: "+user,bg='#beebee')


    title=k.readline()
    titlelabel=Label(f2,text="Title: "+title,bg='#ddeadd')
    titlelabel.pack(fill='both')

    note=k.readline()
    notelabel=Label(f2,text="Note: "+note,bg='#abcdef')
    notelabel.pack(fill='both')

    userlabel.pack(side=RIGHT,fill='x')
    f2.pack(fill='both')
    canvas.yview_moveto(1)
    canvas.config(scrollregion=canvas.bbox('all'))

t1=Thread(target=opennote)
t1.start()

# button1=Button(root,text="Create",command=create)
# button1.grid(row=0,column=0)
#
# button2=Button(root,text="Open",command=opennote)
# button2.grid(row=0,column=1)
#
# listbox=Listbox(root,height=15)
# listbox.grid(row=1,column=0)



root.mainloop()


# CREATE TABLE busbooking(BookID INTEGER PRIMARY KEY, PassengerName TEXT NOT NULL, Departure TIME, Arrival TIME, SeatNumber INTEGER UNIQUE, Price REAL);
# INSERT INTO busbooking(PassengerName, Departure, Arrival, SeatNumber, Price) VALUES('John Doe', '12:30', '14:30', 12, 200);
# INSERT INTO busbooking(PassengerName, Departure, Arrival, SeatNumber, Price) VALUES('Jane Doe', '12:30', '14:30', 13, 300);
# INSERT INTO busbooking(PassengerName, Departure, Arrival, SeatNumber, Price) VALUES('John Doe', '15:30', '17:30', 15, 600);
#
#
# CREATE TABLE departments (deptID INTEGER NOT NULL PRIMARY KEY, deptName TEXT);
# INSERT INTO departments VALUES (123, 'Sales');
# INSERT INTO departments VALUES (456, 'Marketing');
# #
# #
# # CREATE TABLE EmployeeDetails (empID INTEGER NOT NULL PRIMARY KEY, empName TEXT, deptID INTEGER NOT NULL, FOREIGN KEY(deptID) references departments(deptID));
# INSERT INTO EmployeeDetails VALUES (1111, 'John Doe', 123);
# INSERT INTO EmployeeDetails VALUES (2222, 'Jane Doe', 456);
# INSERT INTO EmployeeDetails VALUES (3333, 'Josephine Doe', 789);
#
# CREATE TABLE customers (custID INTEGER NOT NULL PRIMARY KEY, Name TEXT, Address TEXT);
# CREATE TABLE  orderDetails (orderID INTEGER NOT NULL PRIMARY KEY, custID INTEGER NOT NULL, FOREIGN KEY(custID) references customers(custID));
# INSERT INTO customers VALUES (123, 'John Doe', 'Park Lane');
# INSERT INTO customers VALUES (456, 'Jane Doe', 'Baldur Square');
# INSERT INTO customers VALUES (789, 'Josephine Doe', 'Leicester Square');
# INSERT INTO customers VALUES (111, 'Jackson Doe', 'Times Square');
# INSERT INTO orderDetails VALUES (1, 123);
# INSERT INTO orderDetails VALUES (2, 456);
# INSERT INTO orderDetails VALUES (3, 789);
