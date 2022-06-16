from tkinter import *
from tkinter import Tk, Canvas

# Window
window = Tk()

window.title("gen Calculator")
window.geometry("400x500")
window.config(background="white")

# Squares and design
sq = Canvas(window, width=400, height= 500, bg="white")
sq.create_rectangle(0, 0, 400, 500, outline = 'black', width=18)
sq.create_rectangle(30, 30, 369, 100, outline = 'black', width=8)

# Buttons
n0 = Button(window, text = "0", height= 2, width= 10)
n1 = Button(window, text = "1", height= 2, width= 10)
n2 = Button(window, text = "2", height= 2, width= 10)
n3 = Button(window, text = "3", height= 2, width= 10)
n4 = Button(window, text = "4", height= 2, width= 10)
n5 = Button(window, text = "5", height= 2, width= 10)
n6 = Button(window, text = "6", height= 2, width= 10)
n7 = Button(window, text = "7", height= 2, width= 10)
n8 = Button(window, text = "8", height= 2, width= 10)
n9 = Button(window, text = "9", height= 2, width= 10)

plus = Button(window, text = "+", height= 2, width= 10)
minus = Button(window, text = "-", height= 2, width= 10)
times = Button(window, text = "x", height= 2, width= 10)
divide = Button(window, text = ":", height= 2, width= 10)
sqrt = Button(window, text = "sqrt", height= 2, width= 10)

off = Button(window, text = "Off", height= 2, width= 10)
cc = Button(window, text = "C", height= 2, width= 10)
equal = Button(window, text = "=", height= 2, width= 10)
dot = Button(window, text = ".", height= 2, width= 10)
plus_minus = Button(window, text = "+/-", height= 2, width=10)

# Locations
plus_minus.place(x=25, y=435)
n0.place(x=115, y=435)
dot.place(x=205, y=435)
equal.place(x=295, y=435)

n1.place(x=25, y=375)
n2.place(x=115, y=375)
n3.place(x=205, y=375)
plus.place(x=295, y=375)

n4.place(x=25, y=315)
n5.place(x=115, y=315)
n6.place(x=205, y=315)
minus.place(x=295, y=315)

n7.place(x=25, y=255)
n8.place(x=115, y=255)
n9.place(x=205, y=255)
times.place(x=295, y=255)

off.place(x=25, y=195)
cc.place(x=115, y=195)
sqrt.place(x=205, y=195)
divide.place(x=295, y=195)

# Running
sq.pack()
window.mainloop()