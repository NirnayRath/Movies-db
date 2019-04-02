"""This is a movie directory gui """

from tkinter import *
from backend import Database
database=Database()
window=Tk()
window.wm_title("Movies db")
def get_selected_row(event):
    try:
        global selected_tuple
        index=lb1.curselection()[0]
        selected_tuple=lb1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END,selected_tuple[4])
    except(IndexError):
        pass

def view_command():
    lb1.delete(0,END)
    for row in database.view():
        lb1.insert(END,row)

def search_command():
    lb1.delete(0,END)
    for row in database.search(movie_text.get(),genre_text.get()):
        lb1.insert(END,row)

def add_command():
    database.add(movie_text.get(),genre_text.get(),qual_text.get(),path_text.get())
    lb1.delete(0,END)
    lb1.insert(END,(movie_text.get(),genre_text.get(),qual_text.get(),path_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],movie_text.get(),genre_text.get(),qual_text.get(),path_text.get())


lb1=Label(window,text="Movie:")                            #Movie label
lb1.grid(row=0,column=0)

lb2=Label(window,text="Genre:")                            #Genre label
lb2.grid(row=1,column=0)

lb3=Label(window,text="Quality:")                             #Size label
lb3.grid(row=0,column=2)

lb4=Label(window,text="Path:")                              #Path label
lb4.grid(row=1,column=2)

lb5=Label(window,text="Description:")
lb5.grid(row=2,column=0)

movie_text=StringVar()
e1=Entry(window,textvariable=movie_text)
e1.grid(row=0,column=1)

genre_text=StringVar()
e2=Entry(window,textvariable=genre_text)
e2.grid(row=1,column=1)

qual_text=StringVar()
e3=Entry(window,textvariable=qual_text)
e3.grid(row=0,column=3)

path_text=StringVar()
e4=Entry(window,textvariable=path_text)
e4.grid(row=1,column=3)

lb1=Listbox(window,height=6,width=40)
lb1.grid(row=2,column=1,rowspan=6,columnspan=4)

sb1=Scrollbar(window)
sb1.grid(row=2,column=4,rowspan=6)

lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)

lb1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="Search",command=search_command)
b1.grid(row=8,column=0)

b2=Button(window,text="Add",command=add_command)
b2.grid(row=8,column=1)

b3=Button(window,text="Delete",command=delete_command)
b3.grid(row=8,column=2)

b4=Button(window,text="Update",command=update_command)
b4.grid(row=8,column=3)

b5=Button(window,text="View all",command=view_command)
b5.grid(row=9,column=1)

b6=Button(window,text="Close",command=window.destroy)
b6.grid(row=9,column=3)

window.mainloop()