# Patobulinti 1 užduoties programą, kad ji:
# Įvedus vardą, atspausdintų "Labas, {vardas}!" ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"


from tkinter import *

pagrindinis_langas = Tk()
pagrindinis_langas.title("Skaiciuotuvas")


# Laukų, mygtukų formavimas

ivedimas1 = Entry(pagrindinis_langas, width=35, borderwidth=5)
ivedimas1.grid(row=0, column=0, columnspan=3)

def mygtuko_ivedimas(number):
    ivestas = ivedimas1.get()
    ivedimas1.delete(0, END)
    ivedimas1.insert(0, str(ivestas)+ str(number))

   

mygtukas1 = Button(pagrindinis_langas, text="1", padx=40, pady=20, command=lambda: mygtuko_ivedimas(1))
mygtukas2 = Button(pagrindinis_langas, text="2", padx=40, pady=20, command=lambda: mygtuko_ivedimas(2))
mygtukas3 = Button(pagrindinis_langas, text="3", padx=40, pady=20, command=lambda: mygtuko_ivedimas(3))
mygtukas4 = Button(pagrindinis_langas, text="4", padx=40, pady=20, command=lambda: mygtuko_ivedimas(4))
mygtukas5 = Button(pagrindinis_langas, text="5", padx=40, pady=20, command=lambda: mygtuko_ivedimas(5))
mygtukas6 = Button(pagrindinis_langas, text="6", padx=40, pady=20, command=lambda: mygtuko_ivedimas(6))
mygtukas7 = Button(pagrindinis_langas, text="7", padx=40, pady=20, command=lambda: mygtuko_ivedimas(7))
mygtukas8 = Button(pagrindinis_langas, text="8", padx=40, pady=20, command=lambda: mygtuko_ivedimas(8))
mygtukas9 = Button(pagrindinis_langas, text="9", padx=40, pady=20, command=lambda: mygtuko_ivedimas(9))
mygtukas0 = Button(pagrindinis_langas, text="0", padx=40, pady=20, command=lambda: mygtuko_ivedimas(0))
mygtukas_plius= Button(pagrindinis_langas, text="+", command=lambda: mygtuko_ivedimas())
mygtukas_lygu= Button(pagrindinis_langas, text="=", command=lambda: mygtuko_ivedimas())



# Lango piešimas
mygtukas1.grid(row=3, column=0)
mygtukas2.grid(row=3, column=1)
mygtukas3.grid(row=3, column=2)
mygtukas4.grid(row=2, column=0)
mygtukas5.grid(row=2, column=1)
mygtukas6.grid(row=2, column=2)
mygtukas7.grid(row=1, column=0)
mygtukas8.grid(row=1, column=1)
mygtukas9.grid(row=1, column=2)
mygtukas0.grid(row=4, column=2)
mygtukas_plius.grid(row=5, column=0)

mygtukas_lygu.grid(row=5, column=1)

pagrindinis_langas.mainloop()
