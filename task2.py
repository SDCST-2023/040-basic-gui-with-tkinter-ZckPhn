import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-town Veterinary clinic database")

button1 = tk.Label(window, text = "Search by name", font ='Helvetica 9 bold', relief=SOLID)

entry1 = tk.Entry(window, text = "")

dogphoto = tk.PhotoImage(file="dog.png")
label2 = tk.Label(window, image=dogphoto)

label3 = tk.Label(window, text = "Client database", font='Helvetica 10 bold')

cell1 = tk.Label(window, text = "Name", font = 'Helvetica 10 bold')

cell2 = tk.Label(window, text = "Type", font = 'Helvetica 10 bold')

cell3 = tk.Label(window, text = "Breed", font = 'Helvetica 10 bold')

cell4 = tk.Label(window, text = "Owner", font = 'Helvetica 10 bold')

cell5 = tk.Label(window, text = "Birthdate", font = 'Helvetica 10 bold')

bottomcell1 = tk.Entry(window, text = "")

bottomcell2 = tk.Entry(window, text = "")

bottomcell3 = tk.Entry(window, text = "")

bottomcell4 = tk.Entry(window, text = "")

bottomcell5 = tk.Entry(window, text = "")

Previousbutton = tk.Button(window, text = "< previous")

Saveentrybutton = tk.Button(window, text = "Save Entry")

Nextbutton = tk.Button(window, text = "Next >")

button1.place(x=305,y=0, width = 110)
entry1.place(x=418,y=0, width = 145, height = 25)
label2.place(x=17,y=15)
label3.place(x=202,y=45)

cell1.place(x=27.5,y=120)
bottomcell1.place(x=3,y=145, width = 97, height = 25)

cell2.place(x=133.5, y=120)
bottomcell2.place(x=104,y=145, width = 97, height = 25)

cell3.place(x=233, y=120)
bottomcell3.place(x=205, y=145, width = 97, height = 25)

cell4.place(x=338, y=120)
bottomcell4.place(x=310, y=145, width = 97, height = 25)

cell5.place(x=457, y=120)
bottomcell5.place(x=445, y=145, width = 97, height = 25)

Previousbutton.place(x=3, y=172, width = 70)

Saveentrybutton.place(x=202, y=172, width = 97, height = 25)

Nextbutton.place(x=505, y=172, width = 60)

window.mainloop()