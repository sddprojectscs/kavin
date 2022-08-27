
from tkinter import *


def submit():
    sub=Tk()
    sub.title("login.pge")
    sub.config(bg="BLACK")
    sub.geometry("600x300")
    btn4=Button(sub,text="ADD RECORD",width=20,command=submit).place(x=50,y=100)







def login():
    log=Tk()
    log.title("login.pge")
    log.config(bg="BLACK")
    log.geometry("600x300")
    lbl=Label(log,text="EMPLOYEE   MANAGEMENT",fg="WHITE",bg="BLACK",font="comic").pack()
    lbl1=Label(log,text="USERNAME",fg="WHITE",bg="BLACK",font="comic").place(x=50,y=100)
    ent1= Entry(log,width="35").place(x=150,y=100)
    lbl2=Label(log,text="PASSWORD",fg="WHITE",bg="BLACK",font="comic").place(x=50,y=150)
    ent2= Entry(log,width="35").place(x=150,y=150)

    btn1=Button(log,text="SUBMIT",width=20,command=submit).place(x=150,y=200)

def signup():
    sig=Tk()
    sig.title("signup.pge")
    sig.config(bg="BLACK")
    sig.geometry("500x300")
    lbl4=Label(sig,text="EMPLOYEE   MANAGEMENT",fg="WHITE",bg="BLACK",font="comic")
    lbl4.pack()
    lbl1=Label(sig,text="USERNAME",fg="WHITE",bg="BLACK",font="comic").place(x=50,y=100)
    ent1= Entry(sig,width="35").place(x=150,y=100)
    lbl2=Label(sig,text="PASSWORD",fg="WHITE",bg="BLACK",font="comic").place(x=50,y=150)
    ent2= Entry(sig,width="35").place(x=150,y=150)
    btn1=Button(sig,text="SUBMIT",width=20,command=submit).place(x=150,y=200)

    
#MAIN
root=Tk()
root.configure(bg="cyan")
root.geometry("500x300")

lbl=Label(text="EMPLOYEE   MANAGEMENT",fg="WHITE",bg="BLACK",font="comic")
lbl.pack()

btn1=Button(root,text="login",width=20,command=login).place(x=100,y=100)

btn2=Button(root,text="sign up",width=20,command=signup).place(x=100,y=150)



btn3=Button(root,text="QUIT",width=20,command=root.destroy).place(x=100,y=200)
    

root.mainloop()
