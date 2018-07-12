#Q1

d={'name':'nikhil','Phn':'7087'}
from tkinter import *
root=Tk()
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
myList=Listbox(root,yscrollcommand=scrollbar.set)
for l in d.keys():
    myList.insert(END,str(l))
myList.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=myList.yview)
mainloop()

#Q2
d={'name':'nikhil','Phn':'7087'}
from tkinter import *
root=Tk()
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
myList=Listbox(root,yscrollcommand=scrollbar.set)
for l in d.keys():
    myList.insert(END,str(l))
myList.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=myList.yview)
e1=Entry(root)
e2=Entry(root)
e1.pack()
e2.pack()
def ins():
    d['name']=e1.get()
    d['Phn']=e2.get()
    print(d)
button=Button(root,text="OK",command=ins)
button.pack()
mainloop()