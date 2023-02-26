from tkinter import *
import datetime
import cv2
from PIL import Image,ImageTk
def time():
    
    with open("entry time.txt","a") as date_time:
        DT = str(datetime.datetime.now())
        date_time.write(DT +"\n")

root = Tk()
root.config(bg="orange")
root.geometry("500x600")
root_lable = Label(root,text="Hello",bg = "black",fg="white",padx =10,pady =10)
root_lable.pack()
btn = Button(root,text="LOGIN",bg="white",fg="black",padx =15,pady=15,command = time)
btn.pack(side="bottom")

#padhna hai
f1 = LabelFrame(root,bg="black")
f1.pack()
l1 = Label(f1,bg="blue")
l1.pack()
#yahan tak
cap = cv2.VideoCapture(0);
while True:
    
    ret,frame = cap.read()
    #convert frame from bgr to rgb
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #use of pillow library
    frame = ImageTk.PhotoImage(Image.fromarray(frame))
    
    l1["image"]= frame
    root.update()

root.mainloop()