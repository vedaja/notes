from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import ttk
import pytz
timezone=pytz.timezone("US/Pacific")
from datetime import datetime
import socket
from threading import Thread

host="localhost"
port=2357

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

root=Tk()
root.title("Notes")

noteslist=[]


class Notes:
    def __init__(self,text,title):
        self.title=title
        self.text=text
        current=datetime.now(timezone)
        self.time=current.strftime('%Y-%m-%d %I:%M:%S %p%Z')

    def display(self):
     print(self.text+", "+self.time)


def create():
    global entry,textbox,note_window,name
    note_window=Toplevel(root)
    entry=Entry(note_window)
    entry.grid(row=0,column=0)

    name=Entry(note_window)
    name.grid(row=1,column=0)

    textbox=Text(note_window)
    textbox.grid(row=2,column=0)

    submit=Button(note_window,text="Submit",command=enter)
    submit.grid(row=3,column=0)

def enter():
    global entry,textbox,note_window,n,title,name
    title = entry.get()
    note = textbox.get("1.0", END)
    noteslist.append(Notes(note,title))
    listbox.insert(END,title)

    username=name.get()

    n=open(r"/Users/vjanga/PycharmProjects/Algorithms/client1/"+title+".txt","w")
    n.write(username+"\n"+title+"\n"+note+"\n")
    n.close()

    v=title
    s.sendall(v.encode())

    note_window.destroy()
    messagebox.showinfo("Note recieved","Your note has been added to the list.")
    root.update()



button1=Button(root,text="Create",command=create)
button1.pack()


listbox=Listbox(root,height=15)
listbox.pack()



root.mainloop()


