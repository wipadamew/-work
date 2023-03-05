#EUR = 0.028
#JPY = 3.91
#USD = 0.030
#GBP = 0.025


from tkinter import *
from tkinter import ttk  #การwidget เข้ามาใช้ในโปรแกรม
root = Tk()
root.title("โปรแกรมแปลงสกุลเงิน")
#input
money = IntVar()
Label(text="จำนวนเงิน(THB)",padx=10,font=30).grid(row=0,sticky=W)
et1=Entry(font=30,width=30,textvariable=money)
et1.grid(row=0,column=1)

choice = StringVar(value="โปรดเลือกสกุลเงิน")
Label(text="เลือกสกลุเงิน",padx=10,font=30).grid(row=1,sticky=W)
Combo=ttk.Combobox(width=30,font=30,textvariable=choice)
Combo["values"]=("EUR","JPY","USD","GBP")
Combo.grid(row=1,column=1)

#output 
Label(text="ผลการคำนวน",padx=10,font=30).grid(row=2,sticky=W)
et2=Entry(font=30,width=30,)
et2.grid(row=2,column=1)

def calculate():
    amount=money.get()
    currency=choice.get()
    if currency == "EUR":
        et2.delete(0,END)
        result = (amount*0.026),"EUR(ยูโร)"
        et2.insert(0,result)
    elif currency == "JPY":
        et2.delete(0,END)
        result = (amount*3.91),"JPY(เยน)"
        et2.insert(0,result)
    elif currency == "USD":
        et2.delete(0,END)
        result = (amount*0.030),"USD(ดอลล่า)"
        et2.insert(0,result)
    elif currency == "GBP":
        et2.delete(0,END)
        result = (amount*0.025),"GBP(ปอนด์)"
        et2.insert(0,result)
    else :
        et2.delete(0,END)
        result = "ไม่พบข้อมูล"
        et2.insert(0,result)
    
    
Button(text="คำนวน",font=30,width=15,command=calculate).grid(row=3,column=1,sticky=W)
Button(text="ล้าง",font=30,width=15).grid(row=3,column=1,sticky=E)
root.mainloop()