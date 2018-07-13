from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x1600+0+0")
root.title("Mitran Da Dhaba")

text_Input = StringVar()
operator= ""



Tops = Frame(root,width=1600,height=100,bg="red",relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=900,height=500,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width=400,height=500,bg="red",relief=SUNKEN)
f2.pack(side=RIGHT)
#============================time===========================================
localtime=time.asctime(time.localtime(time.time()))
#==========================information========================
lblInfo = Label(Tops, font=('Helvetica',50,'bold'),text="Mitran Da Dhaba",fg="green",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
lblDateTime = Label(Tops, font=('Helvetica',20,'bold'),text=localtime,fg="green",bd=10,anchor='w')
lblDateTime.grid(row=1,column=0)
#==============================calculator==============================
def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator= ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator =""

def Ref():
    x= random.randint(12345, 999999)
    randomRef = str(x)
    rand.set(randomRef)


    Cof = float(Fries.get())
    Colfries=float(Pavbhaji.get())
    Cob =float(Burger.get())
    CoChicBurger =float(Chicken_Burger.get())
    CoDosa =float(Dosa.get())
    CoIdli =float(Idli.get())

    CostofFries = Cof * 100
    CostofPavbhaji = CostofFries * 60
    CostofBurger = Cob * 40
    CostofChicken_Burger = CoChicBurger * 70
    CostofDosa = CoDosa * 80
    CostofIdli = CoIdli * 60

    CostofMeal = "Rs.", str('%.2f' %( CostofFries + CostofPavbhaji +  CostofBurger +  CostofChicken_Burger +
                                     CostofDosa +  CostofIdli))

    PayTax = (( CostofFries + CostofPavbhaji +  CostofBurger +  CostofChicken_Burger +
                                     CostofDosa +  CostofIdli) * 5)

    TotalCost = ( CostofFries + CostofPavbhaji +  CostofBurger +  CostofChicken_Burger +
                                     CostofDosa +  CostofIdli)

    Ser_Charge = (( CostofFries + CostofPavbhaji +  CostofBurger +  CostofChicken_Burger +
                                     CostofDosa +  CostofIdli)/3)

    Service = "Rs.", str('%.2f' % Ser_Charge)


    OverAllCost = "Rs.", str('%.2f' % (PayTax + TotalCost + Ser_Charge))

    PaidTax = "Rs.", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set( CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)


def qExit():
    root.destroy()

def Reset():
    rand.set(0)
    Fries.set(0)
    Burger.set(0)
    Dosa.set(0)
    Idli.set(0)
    Pavbhaji.set(0)
    SubTotal.set(0)
    Total.set(0)
    Service_Charge.set(0)
    Tax.set(0)
    Cost.set(0)
    Chicken_Burger.set(0)



txtDisplay = Entry(f2, font=('Helvetica',20,'bold'), textvariable=text_Input, bd=30, insertwidth=4)
txtDisplay.grid(columnspan=4)


btn7 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="7",bg="red", command=lambda: btnclick(7)).grid(row=2,column=0)

btn8 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="8",bg="red", command=lambda: btnclick(8)).grid(row=2,column=1)

btn9 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="9",bg="red", command=lambda: btnclick(9)).grid(row=2,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="+",bg="red", command=lambda: btnclick("+")).grid(row=2,column=3)
#===================================================================================================================================

btn4 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="4",bg="red", command=lambda: btnclick(4)).grid(row=3,column=0)

btn5 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="5",bg="red", command=lambda: btnclick(5)).grid(row=3,column=1)

btn6 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="6",bg="red", command=lambda: btnclick(6)).grid(row=3,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="-",bg="red", command=lambda: btnclick("-")).grid(row=3,column=3)
#==============================================================================================================================================

btn1 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="1",bg="red", command=lambda: btnclick(1)).grid(row=4,column=0)

btn2 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="2",bg="red", command=lambda: btnclick(2)).grid(row=4,column=1)

btn3 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="3",bg="red", command=lambda: btnclick(3)).grid(row=4,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="*",bg="red", command=lambda: btnclick("*")).grid(row=4,column=3)
#======================================================================================================================================

btn0 = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="0",bg="red", command=lambda: btnclick(0)).grid(row=5,column=0)

btnClear = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="C",bg="red", command =btnClearDisplay).grid(row=5,column=1)

btnEquals = Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="=",bg="red", command =btnEqualsInput).grid(row=5,column=2)

Division=Button(f2,padx=16,pady=16,bd=8,fg="black",font=('Helvetica',15,'bold'),text="/",bg="red", command=lambda: btnclick("/")).grid(row=5,column=3)
#====================================================restaurant information==============================================================================
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Dosa= StringVar()
Idli= StringVar()
Pavbhaji = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken_Burger = StringVar()

Reset()

lblReference = Label(f1,font=('Helvetica',18,'bold'),text="Reference",bd=18, anchor = 'w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('Helvetica',18,'bold'),textvariable=rand, bd=10, insertwidth = 4,
                   bg="red", justify = 'right')
txtReference.grid(row=0,column=1)


lblFries = Label(f1,font=('Helvetica',18,'bold'),text="Fries",bd=18, anchor = 'w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=('Helvetica',18,'bold'),textvariable=Fries, bd=10, insertwidth = 4,
                   bg="red", justify = 'right')
txtFries.grid(row=1,column=1)

lblBurger = Label(f1,font=('Helvetica',18,'bold'),text="Burger",bd=18, anchor = 'w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('Helvetica',18,'bold'),textvariable=Burger, bd=10, insertwidth = 4,
                   bg="red", justify = 'right')
txtBurger.grid(row=2,column=1)

lblDosa = Label(f1,font=('Helvetica',18,'bold'),text="Dosa",bd=18, anchor = 'w')
lblDosa.grid(row=3,column=0)
txtDosa=Entry(f1,font=('Helvetica',18,'bold'),textvariable=Dosa, bd=10, insertwidth = 4,
                   bg="red", justify = 'right')
txtDosa.grid(row=3,column=1)

lblIdli = Label(f1,font=('Helvetica',18,'bold'),text="Idli",bd=18, anchor = 'w')
lblIdli.grid(row=4,column=0)
txtIdli=Entry(f1,font=('Helvetica',18,'bold'),textvariable=Idli, bd=10, insertwidth = 4,
                   bg="red", justify = 'right')
txtIdli.grid(row=4,column=1)

lblPavbhaji = Label(f1,font=('Helvetica',18,'bold'),text="Pavbhaji",bd=18, anchor = 'w')
lblPavbhaji.grid(row=5,column=0)
txtPavbhaji=Entry(f1,font=('Helvetica',18,'bold'),textvariable=Pavbhaji, bd=10, insertwidth = 4,
                   bg="red", justify = 'right')
txtPavbhaji.grid(row=5,column=1)

lblChicken = Label(f1,font=('Helvetica',18,'bold'),text="Chicken Meal",bd=18, anchor = 'w')
lblChicken.grid(row=6,column=0)
txtChicken=Entry(f1,font=('Helvetica',18,'bold'),textvariable=Chicken_Burger, bd=10, insertwidth = 4,
                   bg="red", justify = 'right')
txtChicken.grid(row=6,column=1)

#==============================================resturant info 2=============================================================================
lblCost = Label(f1,font=('Helvetica',18,'bold'),text="Cost of Meal",bd=18, anchor = 'w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('Helvetica',18,'bold'),textvariable=Cost, bd=10, insertwidth = 4,
                   bg="#ffffff", justify = 'right')
txtCost.grid(row=1,column=3)

lblService = Label(f1,font=('Helvetica',18,'bold'),text="Service Charge",bd=18, anchor = 'w')
lblService.grid(row=2,column=2)
txtService=Entry(f1,font=('Helvetica',18,'bold'),textvariable=Service_Charge, bd=18, insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtService.grid(row=2,column=3)

lblStateTax = Label(f1,font=('Helvetica',18,'bold'),text="State Tax",bd=18, anchor = 'w')
lblStateTax.grid(row=3,column=2)
txtStateTax=Entry(f1,font=('Helvetica',18,'bold'),textvariable=Tax, bd=10, insertwidth = 4,
                   bg="#ffffff", justify = 'right')
txtStateTax.grid(row=3,column=3)

lblSubTotal = Label(f1,font=('Helvetica',18,'bold'),text="SubTotal",bd=18, anchor = 'w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('Helvetica',18,'bold'),textvariable=SubTotal, bd=10, insertwidth = 4,
                   bg="#ffffff", justify = 'right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost = Label(f1,font=('Helvetica',18,'bold'),text="Total Cost",bd=18, anchor = 'w')
lblTotalCost.grid(row=5,column=2)
txtTotalCost=Entry(f1,font=('Helvetica',18,'bold'),textvariable=Total, bd=10, insertwidth = 4,
                   bg="#ffffff", justify = 'right')
txtTotalCost.grid(row=5,column=3)


#====================================buttons=======================================================================================
btnTotal = Button(f1,padx = 16,pady=8,fg= "black",font=('Helvetica',18,'bold'), width =9,
                  text = "Total", bg = "red", command = Ref).grid(row=8 , column=1)

btnReset = Button(f1,padx = 16,pady=8,fg= "black",font=('Helvetica',18,'bold'), width =9,
                  text = "Reset", bg = "red", command = Reset).grid(row=8 , column=2)

btnqExit = Button(f1,padx = 16,pady=8,fg= "black",font=('Helvetica',18,'bold'), width =9,
                  text = "Exit", bg = "red", command = qExit).grid(row=8 , column=3)






root.mainloop()