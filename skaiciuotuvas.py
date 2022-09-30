from tkinter import *

Skaiciuotuvas = Tk()

Skaiciuotuvas.geometry("320x340")
Skaiciuotuvas.title("Pragaro Skaiciuotuvas")
input_frame = Frame(Skaiciuotuvas, width = 316, height = 50, bd = 3, highlightbackground = "Green", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = "input_text", width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

btns_frame = Frame(Skaiciuotuvas, width = 312, height = 272.5, bg = "grey")
btns_frame.pack()



Skaiciuotuvas.mainloop()