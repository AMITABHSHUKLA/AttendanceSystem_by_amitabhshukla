from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import  PIL
from PIL import Image ,ImageTk
import cv2
import os

def upload():
    
    file_location = filedialog.askopenfilename(title = "Select image")
    name = filedialog.asksaveasfilename()
    name = name.split("/")
    n =len(name)
    naam = name[n-1]  
    img2 = Image.open(file_location,"r")
    img2.load()
    img2.save(naam+".jpg")
    
    
def showing():
    naam = person_name.get()
    filename = str(naam)+".jpg"
    print(filename)
    img = cv2.imread(filename,0)
    img = cv2.imshow("Displaying image",img)
    
def display():
    global person_name
    show = Tk()
    show.title("INPUT")
    show.config(bg="blue")
    show.geometry("400x500")
    show_lable = Label(show,text="Enter Person name",fg="black")
    show_lable.pack()
    person_name = Entry(show,width=40)
    person_name.pack(ipady=6,pady=(1,15))   
    btu = Button(show,text="Enter",padx=10,pady=10,fg="black",command = showing )
    btu.pack()

    show.mainloop()
    



root = Tk()
root.config(bg="orange")
root.geometry("500x400")
root_lable = Label(root,text="Hello",bg = "black",fg="white",padx =10,pady =10)
root_lable.pack()

b1=Button(root,text='Upload',bg ="white",fg="black",command= upload)
b1.pack(side=LEFT)

b2 = Button(root,text='Show image',bg ="white",fg="black",command= display)
b2.pack(side=RIGHT)


root.mainloop()







