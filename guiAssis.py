from tkinter import *
import Assis
from PIL import ImageTk, Image 


def main_window():
    root=Tk()
    root.title("Alpha")

    c=Canvas(root, bg="Gray", width=200, height=200)
    c.pack()

    image=Image.open("D:/Python/Assistant/microphone.png")
    resized=image.resize((140,140), Image.ANTIALIAS)
    newimage=ImageTk.PhotoImage(resized)
    #Changing original image size

    button_image2=PhotoImage(file="D:/Python/Assistant/microphone.png")   
    button=Button(c, image=newimage, command=Assis.start, bg="White", bd=1)
    button.place(x=35 , y=35)
    
    
    root.mainloop()

main_window()

    