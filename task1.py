import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")

entry1 = tk.Entry(window, text = "")
entry1.pack(side = LEFT)

fLabel1 = Label(window,text="x")
fLabel1.pack(side = LEFT)

entry2 = tk.Entry(window, text = "")
entry2.pack(side = LEFT)

button1 = tk.Button(window, text = "=")
button1.pack(side = LEFT)

entry3 = tk.Entry(window, text = "")
entry3.pack(side = LEFT)



window.mainloop()