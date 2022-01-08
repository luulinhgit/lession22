from tkinter import *
import tkinter

from tkinter.ttk import Combobox
from   tkinter import messagebox
import cv2
window=Tk()
window.title("Tkinter OpenCV")
video=cv2.VideoCapture(0)
canvas_w=video.get(cv2.CAP_PROP_FRAME_WIDTH)//2
canvas_h=video.get(cv2.CAP_PROP_FRAME_HEIGHT)//2
canvas=Canvas(window,width=canvas_w,height=canvas_h,bg="red")
canvas.pack()
button=Button(window,text="black & while")
button.pack()
window.mainloop()