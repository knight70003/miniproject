import tkinter as tk
from tkinter import *
import pyttsx3
root=Tk()

obj=LabelFrame(root,text="Text to Voice Converter",font=("Arial",15,"bold"),bd=10,relief=GROOVE,bg="lightblue",fg="black")
obj.pack(fill="both",expand="yes",padx=20,pady=20)

lbl=Label(obj,text="Enter Text",font=("Arial",12,"bold"),bg="lightblue",fg="black")
lbl.grid(row=0,column=0,padx=10,pady=10)

txt=Entry(obj,font=("Arial",12),width=40)
txt.grid(row=0,column=1,padx=10,pady=10)
def speak_text():
    text = txt.get()
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
btn=Button(obj,text="Speak",font=("Arial",12,"bold"),bg="green",fg="white",command=speak_text)
btn.grid(row=1,columnspan=2,pady=20)

root.title("Text to Voice Converter")
root.geometry("1000x300+200+200")
root.resizable(False, False)

