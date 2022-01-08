from tkinter import *
import tkinter

from tkinter.ttk import Combobox
from   tkinter import messagebox
window=Tk()
window.title("CNC")
window.geometry("600x400")
#them label
lbl=Label(window,text="Hello Linh",fg="red",font=("Arial",50))
lbl.grid(column=0,row=0)
#them textbox
txt=Entry(window,width=20)
txt.grid(column=0,row=1)
def handleButton():
    lbl.configure(text="Hi,"+txt.get())
    return
#them button
btnHello=Button(window,text="Say Hello",command=handleButton)
btnHello.grid(column=1,row=1)
#Them combobox
combo=Combobox(window)
combo['values']=("Ban1","ban2","ban3")
combo.grid(column=0,row=2)
def handleButonn1():
    #lbl.configure(text="Hello,"+combo.get())
    messagebox.showinfo("Tkinter","hi"+combo.get())
    return
btncombo=Button(window,text="combochanges",command=handleButonn1)
btncombo.grid(column=1,row=2)
window.mainloop()
