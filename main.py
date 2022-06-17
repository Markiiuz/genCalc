from tkinter import *
from tkinter import Tk, Canvas
from tkinter import font as tkFont

# Window
window = Tk()

window.title("gen Calculator")
window.geometry("400x500")
window.config(background="white")

# Squares and design
sq = Canvas(window, width=400, height= 500, bg="white")
sq.create_rectangle(0, 0, 400, 500, outline = 'black', width=18) # Outer outline
sq.create_rectangle(30, 30, 369, 100, outline = 'black', width=8) # Input desplay outline
sq.create_text(43, 80, text="0", fill="black", font=('"Century Gothic" 20 bold'), anchor="w") # Answer text
sq.create_text(25, 125, text="gen Calculator", fill="black", font=('"Century Gothic" 20 bold'), anchor="w")

sq.create_rectangle(24, 434, 101, 472, outline = "black", width = 9) #plus-minus
sq.create_rectangle(114, 434, 191, 472, outline = "black", width = 9) #n0
sq.create_rectangle(204, 434, 281, 472, outline = "black", width = 9) #dot
sq.create_rectangle(294, 434, 371, 472, outline = "black", width = 9) #equal

sq.create_rectangle(24, 374, 101, 412, outline = "black", width = 9) #n1
sq.create_rectangle(114, 374, 191, 412, outline = "black", width = 9) #n2
sq.create_rectangle(204, 374, 281, 412, outline = "black", width = 9) #n3
sq.create_rectangle(294, 374, 371, 412, outline = "black", width = 9) #plus

sq.create_rectangle(24, 314, 101, 352, outline = "black", width = 9) #n4
sq.create_rectangle(114, 314, 191, 352, outline = "black", width = 9) #n5
sq.create_rectangle(204, 314, 281, 352, outline = "black", width = 9) #n6
sq.create_rectangle(294, 314, 371, 352, outline = "black", width = 9) #minus

sq.create_rectangle(24, 254, 101, 292, outline = "black", width = 9) #n7
sq.create_rectangle(114, 254, 191, 292, outline = "black", width = 9) #n8
sq.create_rectangle(204, 254, 281, 292, outline = "black", width = 9) #n9
sq.create_rectangle(294, 254, 371, 292, outline = "black", width = 9) #times

sq.create_rectangle(24, 194, 101, 232, outline = "black", width = 9) #off
sq.create_rectangle(114, 194, 191, 232, outline = "black", width = 9) #cc
sq.create_rectangle(204, 194, 281, 232, outline = "black", width = 9) #sqrt
sq.create_rectangle(294, 194, 371, 232, outline = "black", width = 9) #divide

# Buttons
n0 = Button(window, text = "0", height= 2, width= 10, border=0, background= "white")
n1 = Button(window, text = "1", height= 2, width= 10, border=0, background= "white")
n2 = Button(window, text = "2", height= 2, width= 10, border=0, background= "white")
n3 = Button(window, text = "3", height= 2, width= 10, border=0, background= "white")
n4 = Button(window, text = "4", height= 2, width= 10, border=0, background= "white")
n5 = Button(window, text = "5", height= 2, width= 10, border=0, background= "white")
n6 = Button(window, text = "6", height= 2, width= 10, border=0, background= "white")
n7 = Button(window, text = "7", height= 2, width= 10, border=0, background= "white")
n8 = Button(window, text = "8", height= 2, width= 10, border=0, background= "white")
n9 = Button(window, text = "9", height= 2, width= 10, border=0, background= "white")

plus = Button(window, text = "+", height= 2, width= 10, border=0, background= "white")
minus = Button(window, text = "-", height= 2, width= 10, border=0, background= "white")
times = Button(window, text = "x", height= 2, width= 10, border=0, background= "white")
divide = Button(window, text = ":", height= 2, width= 10, border=0, background= "white")
sqrt = Button(window, text = "sqrt", height= 2, width= 10, border=0, background= "white")

off = Button(window, text = "Off", height= 2, width= 10, border=0, background= "white")
cc = Button(window, text = "C", height= 2, width= 10, border=0, background= "white")
equal = Button(window, text = "=", height= 2, width= 10, border=0, background= "white")
dot = Button(window, text = ".", height= 2, width= 10, border=0, background= "white")
plus_minus = Button(window, text = "+/-", height= 2, width=10, border=0, background= "white")

# Button locations
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