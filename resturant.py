from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("restaurant management system")

text_Input = StringVar()
operator= ""



Tops = Frame(root,width=1600,height=100,bg="red",relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=900,height=500,bg="red",relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width=400,height=500,bg="red",relief=SUNKEN)
f2.pack(side=RIGHT)
#============================time===========================================
localtime=time.asctime(time.localtime(time.time()))
#==========================information========================
lblInfo = Label(Tops, font=('arial',50,'bold'),text="restaurant management system",fg="green",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial',20,'bold'),text=localtime,fg="green",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)
#==============================calculator==============================
def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

txtDisplay = Entry(f2, font=('arial',20,'bold'), textvariable=text_Input, bd=30, insertwidth=4)
txtDisplay.grid(columnspan=4)


btn7 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="red", command=lambda: btnclick(7)).grid(row=2,column=0)

btn8 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="red", command=lambda: btnclick(8)).grid(row=2,column=1)

btn9 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="red", command=lambda: btnclick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="red", command=lambda: btnclick("+")).grid(row=2,column=3)
#===================================================================================================================================

btn4 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",bg="red", command=lambda: btnclick(4)).grid(row=3,column=0)

btn5 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",bg="red", command=lambda: btnclick(5)).grid(row=3,column=1)

btn6 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",bg="red", command=lambda: btnclick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",bg="red", command=lambda: btnclick("-")).grid(row=3,column=3)
#==============================================================================================================================================

btn1 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",bg="red", command=lambda: btnclick(1)).grid(row=4,column=0)

btn2 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",bg="red", command=lambda: btnclick(2)).grid(row=4,column=1)

btn3 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",bg="red", command=lambda: btnclick(3)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",bg="red", command=lambda: btnclick("*")).grid(row=4,column=3)
#======================================================================================================================================

btn7 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",bg="red", command=lambda: btnclick(7)).grid(row=2,column=0)

btn8 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",bg="red", command=lambda: btnclick(8)).grid(row=2,column=1)

btnEquals = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",bg="red", command=lambda: btnclick(9)).grid(row=2,column=2)

Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",bg="red", command=lambda: btnclick("+")).grid(row=2,column=3)





root.mainloop()
