#Biblioteci Utile
from tkinter import*
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb #pip install


#functionalitate

def showImage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', filetype=(("PNG file","*.png"),("JPG file","*.jpg"),("All file","*.txt")))
    img = Image.open(filename)
    width, height = img.size
    scale = min(250/width,250/height)
    img = img.resize((int(width*scale), int(height*scale)))




    img = ImageTk.PhotoImage(img)

    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

def hide():
    global secret
    message = text.get(1.0,END)
    secret = lsb.hide(str(filename),message)


def show():
    clear = lsb.reveal(filename)
    text.delete(1.0,END)
    text.insert(END,clear)


def saveImage():
    secret.save("hidden.png")


#Interfata Grafica
root = Tk()
root.title ("Proiect Criptografie")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="#80BCBD")
imageLogo = PhotoImage(file="img.png")
root.iconphoto(False,imageLogo)
Label(root,text="Crypthography",bg="#80BCBD",fg="white",font="arial 25 bold").place(x=100,y=20)

#Frame1

f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg='black')
lbl.place(x=40,y=10)

#Frame2

f2 = Frame(root,bd=3,bg="white",width=340,height=280,relief=GROOVE)
f2.place(x=350,y=80)

text = Text(f2,font="Robote 20", bg="white",fg="black", relief=GROOVE,wrap=WORD)
text.place(x=0,y=0,width=320,height=295)

scrollbar=Scrollbar(f2)
scrollbar.place(x=320,y=0,height=300)
scrollbar.configure(command=text.yview)
text.configure(yscrollcommand=scrollbar.set)

#Frame3

f3 = Frame(root,bd=3,bg="#AAD9BB",width=330,height=100,relief=GROOVE)
f3.place(x=10,y=370)

#Butoane
Button(f3,text="Open Image", width=10,height=2,font="arial 14 bold", command=showImage).place(x=20,y=30)
Button(f3,text="Save Image", width=10,height=2,font="arial 14 bold", command=saveImage).place(x=180,y=30)
Label(f3,text="Picture, Image, Photo File", bg ="#80BCBD",fg="black").place(x=20,y=5)

#Frame4

f4 = Frame(root,bd=3,bg="#AAD9BB",width=330,height=100,relief=GROOVE)
f4.place(x=360,y=370)

#Butoane
Button(f4,text="Hide Data", width=10,height=2,font="arial 14 bold", command=hide).place(x=20,y=30)
Button(f4,text="Show Data", width=10,height=2,font="arial 14 bold",command=show).place(x=180,y=30)
Label(f4,text="Picture, Image, Photo File", bg ="#80BCBD",fg="black").place(x=20,y=5)


root.mainloop()