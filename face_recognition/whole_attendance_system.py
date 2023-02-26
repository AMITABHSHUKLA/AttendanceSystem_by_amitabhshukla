import face_recognition
import cv2
import numpy as np
from tkinter import *
from tkinter import messagebox
import datetime
from PIL import Image,ImageTk

def time():
    
    with open("entry time.txt","a") as date_time:
        if matches[best_match_index]:
            DT = str(datetime.datetime.now())
            date_time.write(name+"logged in at :" +DT +"\n")
            
        else:
            messagebox.showwarning(title="Warning",message="INVALID LOGIN")
            
            
        

root = Tk()
root.config(bg="orange")
root.geometry("500x600")
root_lable = Label(root,text="Hello",bg = "black",fg="white",padx =10,pady =10)
root_lable.pack()
btn = Button(root,text="LOGIN",bg="white",fg="black",padx =15,pady=15,command = time)
btn.pack(side="bottom")
f1 = LabelFrame(root,bg="black")
f1.pack()
l1 = Label(f1,bg="blue")
l1.pack()


video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

ami_img = face_recognition.load_image_file("amitabh.jpg")
ami_encoding = face_recognition.face_encodings(ami_img)[0]
# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding,
    ami_encoding
]
known_face_names = [
    "Barack Obama",
    "Joe Biden",
    "Amitabh "
]

while True:
   
    ret, frame = video_capture.read()

    
    rgb_frame = frame[:, :, ::-1]

    
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

       
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame = ImageTk.PhotoImage(Image.fromarray(frame))
    
    #l1["image"]= frame
    root.update()

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam

video_capture.release()
cv2.destroyAllWindows()
root.mainloop()
