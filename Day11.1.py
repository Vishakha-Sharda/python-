from tkinter import *
import tkinter
from tkinter import messagebox
from mysql import connector


def database():
    conn=connector.connect(
        user='root',
        password='Password',
        host='127.0.0.1',
        port='3306',
        database='college')
    mycursor=conn.cursor()
    sr_no=e_1.get()
    name=e_2.get()
    roll_no=e_3.get()
    address=e_4.get() 
    branch=l_5.get() 
    gender=var.get() 
    mycursor.execute("insert into college values(%s,%s,%s,%s,%s,%s)",(sr_no,name,roll_no,address,branch,gender))
    messagebox.showinfo("Info","Submitted")
    conn.commit()


ab=Tk()
ab.geometry("500x550")
ab.title("..Registration Form..")

l_0 = Label(ab,text="Registration form",width=20,font=("bold",22))
l_0.place(x=88,y=53)


l_1 = Label(ab,text="SR NO:",width=20,font=("bold", 10))
l_1.place(x=90,y=130)

e_1 = Entry(ab,bg='lightgrey')
e_1.place(x=210,y=130)

l_2 = Label(ab,text="NAME:",width=20,font=("bold", 10))
l_2.place(x=85,y=180)

e_2 = Entry(ab,bg='lightgrey')
e_2.place(x=210,y=180)

l_3= Label(ab,text="ROLL NO:",width=20,font=("bold",10))
l_3.place(x=82,y=230)

e_3=Entry(ab,bg='lightgrey')
e_3.place(x=210,y=230)

l_4=Label(ab,text="ADDRESS:",width=20,font=("bold", 10))
l_4.place(x=80,y=280)

e_4=Entry(ab,bg='lightgrey')
e_4.place(x=210,y=280)

l_5=Label(ab,text="BRANCH:",width=20,font=("bold", 10))
l_5.place(x=80,y=330)
l_5= StringVar(ab)
l_5.set("Select one") 

e_5= OptionMenu(ab,l_5,"CSE","IT","ECE","ME","EE")
e_5.pack()
e_5.place(x=210,y=325)

l_6 = Label(ab,text="GENDER:",font=("bold", 10))
l_6.place(x=75,y=380)
var= IntVar()
Radiobutton(ab,text="Male",padx = 5,variable=var, value=1).place(x=200,y=380)
Radiobutton(ab,text="Female",padx = 20, variable=var, value=2).place(x=270,y=380)

Button(ab,text='Submit',width=20,bg='blue',fg='white',cursor="hand2",command=database).place(x=180,y=440)
ab.mainloop()
print("registration form  seccussfully created...")