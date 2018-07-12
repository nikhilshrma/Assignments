from tkinter import*
#Q1

master=Tk()
Label(master,text='Hello World').grid(row=0)
button=Button(master,text='EXIT',command=master.destroy).grid(row=0,column=1)
mainloop()
#Q2
master=Tk()
def abc():
    Label(master, text='Haha NO ESCAPE!!!!!!').grid(row=1)
Label(master,text='Hello World').grid(row=0)
button=Button(master,text='EXIT',command=abc).grid(row=0,column=1)
mainloop()

#Q3
root=Tk()
frame=Frame(root)
frame.pack()
def b():
      lbl.config(text="Halo Fraands, Chai Peelo!!")
def f():
    frame.destroy()
    root.destroy()
lbl=Label(frame,text='Hello World')
lbl.pack()
bb=Button(frame,text='Change Label',fg='blue',command=b)
bb.pack(side=LEFT)
bb=Button(frame,text='EXIT',fg='black',command=f)
bb.pack(side=BOTTOM)
root.mainloop()

#Q4

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(master, text='Quit', command=master.quit).grid(row=3, column=0)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1)
mainloop( )
