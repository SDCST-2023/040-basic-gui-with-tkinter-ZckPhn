import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("example")


dogphoto = tk.PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)

label2 = tk.Label(window,text="Pochacco!", font = "Helvetica 10 bold")

label3 = tk.Label(window, text="A cuddly little puppy! This is from the same \ncreators who bought you Keropi and Kero Kero", bg="#88efff", font = "Helvetica 10 bold")

label1.place(x=87,y=0)
label2.place(x=155,y=40)
label3.place(x=3,y=100)

window.mainloop()