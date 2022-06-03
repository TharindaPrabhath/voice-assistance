from tkinter import *
import guiAssis


reciever_email = StringVar()
subject = StringVar()
attachment = StringVar()


def interface():
    root=Tk()
    root.title("Email")

    c=Canvas(root, bg="Gray", width=700, height=520)
    c.pack()

    l1=Label(c, text="Reciever's Email", font="arial 12 bold")
    l1.place(x=20, y=30)
    e1=Entry(c, width=55, font="arial 12", textvar= reciever_email)
    e1.place(x=180, y=30)

    l2=Label(c, text="Subject", font="arial 12 bold")
    l2.place(x=20, y=70)
    e2=Entry(c, width=55, font="arial 12")
    e2.place(x=180, y=70)

    l3=Label(c, text="Attachment", font="arial 12 bold")
    l3.place(x=20, y=110)
    e3=Entry(c, width=45, font="arial 12")
    e3.place(x=180, y=110)
    btn=Button(c, text="Acces", font="arial 8 bold", width=8)
    btn.place(x=605, y=110)
    l=Label(c, text="Enter the path of the attachment")
    l.place(x=180, y=133)


    l4=Label(c, text="Message", font="arial 12 bold")
    l4.place(x=20, y=150)

    txt=Text(c, font="arial 12", width=73, height=16)
    txt.place(x=20, y=180)
        
    btn1=Button(c, text="Send", font="arial 12 bold", width=8, command=guiAssis.link_to_Assis)
    btn1.place(x=220, y=480)

    btn2=Button(c, text="Exit", font="arial 12 bold", width=8, command=root.destroy)
    btn2.place(x=380, y=480)
    
    root.mainloop()

interface()
                

