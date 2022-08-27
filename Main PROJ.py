from tkinter import*


from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql as sql
import tkinter as tk
#CONNECTING TO DATABASE
db=sql.connect(host="localhost",user="root",passwd="sagar@123",database="mails")
#CREATING CURSOR
curdb=db.cursor()
def checkdetails():
   uname=e1l.get()
   mail=e2l.get()
   pas=e3l.get()
   q='select * from login;'
   curdb.execute(q)
   res=curdb.fetchall()
   f=0
   if(uname=='' or mail=='') or pas=='':
      messagebox.showerror('Error','Please Fill The Required Field')
   else:
      for a in range(len(res)):
          if ((uname,mail,pas)==res[a]):
              f=1
              break
          else:
              pass
      if(f==1):
         login.destroy()
         messagebox.showinfo('','Login Successful')
      else:
         messagebox.showerror('','The Given Account Does not Exist')

def login():
    global e1l,e2l,e3l,login
    login=Tk()
    login.title('Login')
    login.config(bg='black',height=500,width=500)
    image1 = Image.open("1.jpg")
    image1= image1.resize((500,500), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test
    label1.place(x=0,y=0)
    image2 = Image.open("10.jpg")
    image2= image2.resize((80,80), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image2)
    label1 = Label(image=test)
    label1.image = test
    label1.place(x=200,y=100)
    lbl=Label(login,text='LOGIN',font=('TIMES',35),bg='black',fg='white').place(x=180,y=0)
    lbl2=Label(login,text="MAIL ID",bg="BLACK",fg="WHITE",height='2',width='14',font=('COMIC',14))
    lbl2.place(x=15,y=240)
    lbl2=Label(login,text="PASSWORD",bg="BLACK",fg="WHITE",height='2',width='14',font=('COMIC',14))
    lbl2.place(x=25,y=290)
    lbl3=Label(login,text='USER NAME',bg="BLACK",fg="WHITE",height='2',width='14',font=('COMIC',14))
    lbl3.place(x=25,y=190)
    e1l=Entry(login,width=26,font=('COMIC',13))
    e1l.place(x=200,y=200)
    e2l=Entry(login,width=26,font=("comic",13))
    e2l.place(x=200,y=250)
    e3l=Entry(login,show=u"\u25CF",width=26,font=("comic",13))
    e3l.place(x=200,y=300)
    btn1=Button(login,text="SUBMIT",font = "TIMES",activebackground='yellow',activeforeground='Black',
               bd = 2, bg = "dodgerblue3",fg='black', relief = "groove",width=10,height=1,command=checkdetails)
    btn1.place(x=280,y=350)
    login.mainloop()

def AddAccount():
   global curdb
   un=e1s.get()
   ag=e2s.get()
   gen=e3s.get()
   mob=e4s.get()
   mail=e5s.get()
   pas=e6s.get()
   q1='select * from sign'
   curdb.execute(q1)
   res1=curdb.fetchall()
   if (un=='' or ag=='') or (gen=='' or mob=='') or(mail=='' or pas==''):
      messagebox.showerror('Error','Please Fill All The Details')
   else:
      s=mail.split('@')
      if 'gmail.com' in s and len(mob)==10:
         q=(un,mail,pas)
         q3='select * from login'
         curdb.execute(q3)
         res2=curdb.fetchall()
         f2=0
         for a in range(len(res2)):
            if res2[a]==q:
               f2=1
            else:
               pass
         if f2==0:
            q2="insert into sign values('{}','{}','{}','{}','{}','{}')".format(un,ag,gen,mob,mail,pas)
            curdb.execute(q2)
            db.commit()
            messagebox.showinfo('','Your ID Is Successfully Created')
            sign.destroy()
            q4='insert into login values("{}","{}","{}")'.format(un,mail,pas)
            curdb.execute(q4)
            db.commit()
         else:
            messagebox.showerror('Error','The Given Mail Already Exist')
      else:
         messagebox.showerror('Error','Enter A Valid Mail Or Number')
      #new if condition for checking whether it is present already
      '''q2="insert into sign values('{}','{}','{}','{}','{}','{}')".format(un,ag,gen,mob,mail,pas)
      curdb.execute(q2)
      db.commit()
      messagebox.showinfo('','Your ID Is Successfully Created')'''
def CreateAccount():
   global e1s,e2s,e3s,e4s,e5s,e6s,sign
   sign=Tk()
   sign.title('Sign Up')
   sign.configure(bg='white')
   sign.geometry('450x650')
   '''image1 = Image.open("1.jpg")
   image1= image1.resize((450,650), Image.ANTIALIAS)
   test = ImageTk.PhotoImage(image1)
   label1 = Label(image=test)
   label1.image = test
   label1.place(x=0,y=0)'''
   labl=Label(text='SIGN UP',bg='white',fg='Black',font=('Times',30)).pack()
   image2 = Image.open("9.jpg")
   image2= image2.resize((80,80), Image.ANTIALIAS)
   test = ImageTk.PhotoImage(image2)
   label1 = Label(image=test)
   label1.image = test
   label1.place(x=180,y=100)
   lbl1=Label(sign,)
   #name,age,number,mail,pass
   lbl1=Label(sign,text='NAME',font=('Times',17),fg='black',bg='white').place(y=200,x=10)
   lbl2=Label(sign,text='AGE',font=('Times',17),fg='black',bg='white').place(y=250,x=10)
   lbl3=Label(sign,text='GENDER',font=('Times',17),fg='black',bg='white').place(y=300,x=10)
   lbl4=Label(sign,text='MOBILE',font=('Times',17),fg='black',bg='white').place(y=350,x=10)
   lbl5=Label(sign,text='MAIL',font=('Times',17),fg='black',bg='white').place(y=400,x=10)
   lbl6=Label(sign,text='PSWD',font=('Times',17),fg='black',bg='white').place(y=450,x=10)
   Age_Variable = tk.StringVar(sign)
   Age_Variable.set("Select")
   option='18','19','20','21','22'# given in this order
   Age_Option = tk.OptionMenu(sign, Age_Variable,*option)
   Age_Option.place(y=250,x=240)
   #We can place a cursor on entry
   e1s=Entry(sign,width=24,font=('COMIC',13),bg='white')
   e1s.place(x=180,y=205)
   e2s=Entry(sign,width=5,font=('COMIC',13),bg='white')
   e2s.place(x=180,y=255)
   e3s=Entry(sign,width=5,font=('COMIC',13),bg='white')
   e3s.place(x=180,y=305)
   e4s=Entry(sign,width=24,font=('COMIC',13),bg='white')
   e4s.place(x=180,y=355)
   e5s=Entry(sign,width=24,font=('COMIC',13),bg='white')
   e5s.place(x=180,y=405)
   e6s=Entry(sign,width=24,font=('COMIC',13),bg='white')
   e6s.place(x=180,y=455)
   Age_Variable = tk.StringVar(sign)
   Age_Variable.set("Select")
   Age_Option = tk.OptionMenu(sign, Age_Variable,
                           'Male',
                           'Female')
   Age_Option.place(y=300,x=240)
   sbtn=Button(sign,text='SUBMIT',fg = "red", font = "TIMES",activebackground='yellow',activeforeground='Black',
               bd = 2, bg = "light blue", relief = "groove",width=10,height=1,command= AddAccount)
   sbtn.place(x=160,y=500)
   sign.mainloop()
CreateAccount()
login()
'''mainwindow=Tk()
mainwindow.configure(bg='Black',height=500,width=700)
mainwindow.title('Mails And Services')
#mainwindow.resizable(False,False)
lb1=Label(mainwindow,text='MAILS AND SERVICES',height=1,width=30,font=('TIMES',30),fg='white',bg='DodgerBlue4').pack()
btn1=Button(mainwindow,text='LOGIN',height=2,width=20,bg='yellow',fg='black',command=login)
btn1.place(x=30,y=100)
btn2=Button(mainwindow,text='SIGN',height=2,width=20,bg='yellow',fg='black',command=CreateAccount)
btn2.place(x=30,y=130)'''























