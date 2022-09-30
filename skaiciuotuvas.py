# Patobulinti 1 užduoties programą, kad ji:
# Įvedus vardą, atspausdintų "Labas, {vardas}!" ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"


from tkinter import *

pagrindinis_langas = Tk()
pagrindinis_langas.title('Skaiciuotuvas')


# Laukų, mygtukų formavimas

ivedimas1 = Entry(pagrindinis_langas, width=35, borderwidth=5)
ivedimas1.grid(row=0, column=0, columnspan=3)

def mygtuko_ivedimas():
    return

mygtukas1 = Button(pagrindinis_langas, text="1", command=mygtuko_ivedimas)
mygtukas2 = Button(pagrindinis_langas, text="2", command=mygtuko_ivedimas)
mygtukas3 = Button(pagrindinis_langas, text="3", command=mygtuko_ivedimas)
mygtukas4 = Button(pagrindinis_langas, text="4", command=mygtuko_ivedimas)
mygtukas5 = Button(pagrindinis_langas, text="5", command=mygtuko_ivedimas)
mygtukas6 = Button(pagrindinis_langas, text="6", command=mygtuko_ivedimas)
mygtukas7 = Button(pagrindinis_langas, text="7", command=mygtuko_ivedimas)
mygtukas8 = Button(pagrindinis_langas, text="8", command=mygtuko_ivedimas)
mygtukas9 = Button(pagrindinis_langas, text="9", command=mygtuko_ivedimas)
mygtukas0 = Button(pagrindinis_langas, text="0", command=mygtuko_ivedimas)
mygtukas_plius= Button(pagrindinis_langas, text="+", command=mygtuko_ivedimas)
mygtukas_lygu= Button(pagrindinis_langas, text="=", command=mygtuko_ivedimas)



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
mygtukas_plius.grid(row=1, column=2)

mygtukas_lygu.grid(row=1, column=2)

pagrindinis_langas.mainloop()