import tkinter
from tkinter import *
import random,string

root=tkinter.Tk()

root.title("password generator")
root.geometry("400x400")
root.resizable(False,False)

def selection():
        selection.get()

choice=IntVar()

#title
heading = Label(root,text="Password Generator",fg="black",font="areal 20")
heading.place(x=70,y=30)

#username
username=Label(root,text="Username :",font="areal").place(x=35,y=100)
e=Entry(root)
e.place(x=130,y=105)

val=IntVar()


def callback1():
    Isum.config(text=passgen1)
def callback2():
    Isum.config(text=passgen2)
def callback3():
    Isum.config(text=passgen3)




#logic
poor=string.ascii_uppercase+string.ascii_lowercase
moderate=string.ascii_uppercase+string.ascii_lowercase+string.digits
symbols="-!@#$%^&*()_-`~}{][?><,."
advance=poor+moderate+symbols



def passgen1():
            return"".join(random.sample(poor,val.get()))
def passgen2():
            return"".join(random.sample(moderate,val.get()))
def passgen3():
            return"".join(random.sample(advance,val.get()))


def spin():
    spinlab=StringVar()
    spinlab=Label(root,text="Password length",font="areal 8",padx=1,pady=1)
    spinlab.place(x=140,y=185)
    spinlen=Spinbox(root,from_=8, to_=24,textvariable=val,width=13)
    spinlen.place(x=140,y=205)

    def callback1():
        Isum.config(text=passgen1())
    def callback2():
        Isum.config(text=passgen2())
    def callback3():
        Isum.config(text=passgen3())

    def passgen1():
            return (random.sample(poor,val.get()))
    def passgen2():
            return (random.sample(moderate,val.get()))
    def passgen3():
            return (random.sample(advance,val.get()))



    def click():
            myLabel=Label(root,text="choose strength of password",font="areal 10")
            myLabel.place(x=100,y=225)
            button1=Button(root,text="poor",font="areal 8",bg="orange",fg="black",padx=15,pady=5,command=callback1)
            button1.place(x=80,y=255)
            button2=Button(root,text="moderate",font="areal 8",bg="orange",fg="black",padx=15,pady=5,command=callback2)
            button2.place(x=150,y=255)
            button3=Button(root,text="Advanced",font="areal 8",bg="orange",fg="black",padx=15,pady=5,command=callback3)
            button3.place(x=240,y=255)





    button_=Button(root,text="Next",font="areal 8",fg="black",command=click)
    button_.place(x=100,y=205)



#button
button=Button(root,text="Generate password:",font="Areal 12",bg="green",fg="white",command=spin)
button.place(x=120,y=150)

password1=str(callback1)
password2=str(callback2)
password3=str(callback3)

Isum=Label(root,text="")
Isum.pack(side=BOTTOM)


root.mainloop()