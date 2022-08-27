import tkinter as tk
import pymysql as sql
from tkinter import *
import webbrowser
from tkinter import messagebox
from PIL import ImageTk,Image

#CONNECTING TO DATABASE
db=sql.connect(host="localhost",user="root",passwd="sagar@123",database="siva")

#CREATING CURSOR
curdb=db.cursor()

def f1():
    global curdb
    ml=e2.get()
    p=e3.get()
    un=e1.get()
    q=0
    q1='select * from login'
    curdb.execute(q1)
    res1=curdb.fetchall()
          
    if un=="":
        messagebox.showinfo('','Please Enter A Valid Input!!')
    else:
        i=(un,ml,p)
        for m in res1:
            if i==m:
                q=1
            else:
                q=0
        if q==1:
            messagebox.showinfo('','The Account Already Exists , Please Enter New Values')
        else:
            q="insert into login values ('{}','{}','{}')".format(un,ml,p)
            curdb.execute(q)  
            messagebox.showinfo('','Your Mail Is Successfully Created')
            db.commit()
            sign.destroy()
        
def f2():
    global curdb,mail,pl,unl
    f=0
    mail=e2l.get()
    pl=e3l.get()
    unl=e1l.get()
    q1='select * from login'
    curdb.execute(q1)
    res1=curdb.fetchall()
    if (mail=="" or pl=='') or unl=='':
        messagebox.showinfo('','Please Enter A Valid Input!!') 

    else:
        ver=(unl,mail,pl)
        f=0
        for a in res1:
            if ver==a:
                f=1
            else:
                f=0
        if f==1:
            log.destroy
            messagebox.showinfo('','Login Successful!')
            login()
        else:
            messagebox.showinfo('','Incorrect Mail Or PassWord')
                    
def login():
    root=tk.Tk()
    root.configure(bg='dodgerblue3')
    root.geometry('500x250')
    root.minsize("500x250")
    root.resizable(False,False)
    uname,mailid,pas=unl,mail,pl
    lbl=tk.Label(root,text='WELCOME {}'.format(uname),bg='BLACK',fg='WHITE',width=100,font=('times',25))
    lbl.place(x=0,y=0)
    lbl1=tk.Label(root,text="MAILS AND SERVICES",bg='BLACK',fg='WHITE',height=1,width=100,font=('times',25))
    lbl1.pack()
    b1=tk.Button(root,text='COMPOSE A MESSAGE',bg='BLACK',width='20',height='2',fg='white',font=('comic'))
    b1.place(x=20,y=250)
def inb():
    inb=tk.Tk()
    inb.configure(bg='Black')
    inb.geometry('500x250')
    lbl1=tk.Label(inb,text="SK MAILS AND SERVICES",bg='BLACK',fg='WHITE',height=1,width=100,font=('times',25))
    lbl1.pack()
    btn1=tk.Button(inb,text="HISTORY",width='10',height='2',bg='black',fg='white')
    btn1.place(x=100,y=100)

    
def pge3():
    sub=tk.Tk()
    sub.geometry("500x250")
    sub.config(bg="#BE361A")  
    lbl1=tk.Label(sub,text="SK MAILS AND SERVICES",bg='BLACK',fg='WHITE',height=1,width=100,font=('COMIC',25))
    lbl1.pack()
    sub.mainloop()
def pge2():
    global e1,e2,e3,sign
    sign=Toplevel(window)
    sign.title('SIGN UP')
    sign.geometry("850x500")
    box=Frame(sign,width=1920 ,height=1080)
    box.place(x=0,y=0)
    img=Image.open("signupimg1.png")
    img=ImageTk.PhotoImage(img)
    lab=Label(box,image=img)
    lab.pack()
    sign.resizable(False,False)
    sign.config(bg="#BE361A")  
    lbl1=tk.Label(sign,text="SK MAILS AND SERVICES",bg='BLACK',fg='WHITE',height=1,width=100,font=('COMIC',25))
    lbl1.pack()
    lbl2=tk.Label(sign,text="MAIL ID",bg="BLACK",fg="WHITE",height='2',width='15',font=('COMIC',15))
    lbl2.place(x=100,y=200)
    lbl2=tk.Label(sign,text="PASSWORD",bg="BLACK",fg="WHITE",height='2',width='15',font=('COMIC',15))
    lbl2.place(x=100,y=250)
    lbl3=tk.Label(sign,text='USER NAME',bg="BLACK",fg="WHITE",height='2',width='15',font=('COMIC',15))
    lbl3.place(x=100,y=150)
    e1=tk.Entry(sign,width=30,font=('COMIC',16))
    e1.place(x=340,y=150)
    e2=tk.Entry(sign,width=30,font=("comic",16))
    e2.place(x=340,y=200)
    e3=tk.Entry(sign,show=u"\u25CF",width=30,font=("comic",16))
    e3.place(x=340,y=250)
    click_btn= PhotoImage(file='subimg2.png')
    img_label= Label(image=click_btn)
    btn1=tk.Button(sign,text="SUBMIT",width='105',height='40',bg='black',fg='white',command=f1,image=click_btn)
    btn1.place(x=650,y=380)
    click_btn2= PhotoImage(file='quit1.png')
    img_label2= Label(image=click_btn2)
    btn2 =tk. Button(sign,text="QUIT",width='105',height='40',bg='black',fg='white',command=sign.destroy,image=click_btn2)
    btn2.place(x=650,y=430)
    sign.mainloop()
def pge4():
    global e1l,e2l,e3l,log
    log=Toplevel(window)
    log.title('LOGIN')
    log.geometry("850x500")
    log.resizable(False,False)
    log.config(bg="#BE361A")
    box1=Frame(log,width=1920 ,height=1080)
    box1.place(x=0,y=0)
    img1=Image.open("logbg1.jpg")
    img1=ImageTk.PhotoImage(img1)
    lab1=Label(box1,image=img1)
    lab1.pack()
    lbl1=tk.Label(log,text="MAILS AND SERVICES",bg='BLACK',fg='WHITE',height=1,width=100,font=('COMIC',25))
    lbl1.pack()
    lbl2=tk.Label(log,text="MAIL ID",bg="BLACK",fg="WHITE",height='2',width='15',font=('COMIC',15))
    lbl2.place(x=100,y=200)
    lbl2=tk.Label(log,text="PASSWORD",bg="BLACK",fg="WHITE",height='2',width='15',font=('COMIC',15))
    lbl2.place(x=100,y=250)
    lbl3=tk.Label(log,text='USER NAME',bg="BLACK",fg="WHITE",height='2',width='15',font=('COMIC',15))
    lbl3.place(x=100,y=150)
    e1l=tk.Entry(log,width=30,font=('COMIC',13))
    e1l.place(x=340,y=155)
    e2l=tk.Entry(log,width=30,font=("comic",13))
    e2l.place(x=340,y=210)
    e3l=tk.Entry(log,show=u"\u25CF",width=30,font=("comic",13))
    e3l.place(x=340,y=260)

    click_btn= PhotoImage(file='subimg2.png')
    img_label= Label(image=click_btn)
    btn1=tk.Button(log,text="SUBMIT",width='105',height='35',bg='black',fg='white',command=f2,image=click_btn)
    btn1.place(x=450,y=300)
    
    click_btn2= PhotoImage(file='quit1.png')
    img_label2= Label(image=click_btn2)
    btn2 =tk. Button(log,text="QUIT",width='105',height='35',bg='black',fg='white',command=log.destroy,image=click_btn2)
    btn2.place(x=450,y=350)
    log.mainloop()
# MAIN
window= tk.Tk()
window.title('SK Mails And Services')
window.geometry("850x500")
window.config(bg="#BE361A")

box=Frame(window,width=1920 ,height=1080)
box.place(x=0,y=0)
img=Image.open("img1.png.jpg")
img=ImageTk.PhotoImage(img)
lab=Label(box,image=img)
lab.pack()



window.resizable(False,False)
label = tk.Label(text=" MAILS AND SERVICES",bg='BLACK',fg='WHITE',height=1,width=100,font=('COMIC',25))
label.pack()
click_btn= PhotoImage(file='log4.png')
img_label= Label(image=click_btn)
btn1=tk.Button(window,text="LOGIN",width='148',height='40',bg='black',fg='white',command=pge4,image=click_btn )
btn1.place(x=600,y=150)

click_btn1= PhotoImage(file='signup2.png')
img_label1= Label(image=click_btn1)
btn1=tk.Button(window,text="SIGN UP",width='148',height='40',fg='white',command=pge2,image=click_btn1 )
btn1.place(x=600,y=210)

click_btn2= PhotoImage(file='quit1.png')
img_label2= Label(image=click_btn2)
btn2 =tk. Button(window,text="QUIT",width='148',height='40',bg='black',fg='white',command=window.destroy,image=click_btn2)
btn2.place(x=600,y=270)
window.mainloop()
