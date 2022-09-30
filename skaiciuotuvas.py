from tkinter import *

Skaiciuotuvas = Tk()

Skaiciuotuvas.geometry("320x340")
Skaiciuotuvas.title("Pragaro Skaiciuotuvas")
input_frame = Frame(Skaiciuotuvas, width= 316, height= 50, bd= 3, highlightbackground= "Green", highlightcolor= "black")
input_frame.pack(side = TOP)

ivedimo_ekranas = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = "input_text", width = 50, bg = "Black", bd = 0, justify = RIGHT)
ivedimo_ekranas.grid(row = 0, column = 0)
ivedimo_ekranas.pack(ipady = 10)

btns_frame = Frame(Skaiciuotuvas, width= 316, height=270, bg="Pink")
btns_frame = Frame(Skaiciuotuvas, width = 312, height = 272.5, bg = "grey")
btns_frame.pack()

mygtukas1 = Button(btns_frame, text="1", command= lambda: paspaudimas(1))
mygtukas2 = Button(btns_frame, text="2", command= lambda: paspaudimas(2))
mygtukas3 = Button(btns_frame, text="3", command= lambda: paspaudimas(3))
mygtukas4 = Button(btns_frame, text="4", command= lambda: paspaudimas(4))
mygtukas5 = Button(btns_frame, text="5", command= lambda: paspaudimas(5))
mygtukas6 = Button(btns_frame, text="6", command= lambda: paspaudimas(6))
mygtukas7 = Button(btns_frame, text="7", command= lambda: paspaudimas(7))
mygtukas8 = Button(btns_frame, text="8", command= lambda: paspaudimas(8))
mygtukas9 = Button(btns_frame, text="9", command= lambda: paspaudimas(9))
mygtukas0 = Button(btns_frame, text="0", command= lambda: paspaudimas(0))

mygtukas1.grid(row=3, column=0)
mygtukas2.grid(row=3, column=1)
mygtukas3.grid(row=3, column=2)



Skaiciuotuvas.mainloop()