import  PIL
from PIL import Image ,ImageTk
import os 

loc = "C:\\Users\\Lenovo\\Pictures\\1664617705946.jpg"
img2 = Image.open(loc,"r")
img2.load()
img2.save("aabh.jpg")
