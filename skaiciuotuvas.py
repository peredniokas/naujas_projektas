# Patobulinti 1 užduoties programą, kad ji:
# Įvedus vardą, atspausdintų "Labas, {vardas}!" ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"


from tkinter import *

pagrindinis_langas = Tk()
pagrindinis_langas.title('Skaiciuotuvas')

def mygtuko_ivedimas():
    return
# Laukų, mygtukų formavimas
uzrasas1 = Label(pagrindinis_langas, text="")
ivedimas1 = Entry(pagrindinis_langas)
mygtukas1 = Button(pagrindinis_langas, text="1", command=mygtuko_ivedimas)
mygtukas2 = Button(pagrindinis_langas, text="2", command=mygtuko_ivedimas)
mygtukas3 = Button(pagrindinis_langas, text="3", command=mygtuko_ivedimas)
mygtukas4 = Button(pagrindinis_langas, text="4", command=mygtuko_ivedimas)
mygtukas5 = Button(pagrindinis_langas, text="5", command=mygtuko_ivedimas)
mygtukas6 = Button(pagrindinis_langas, text="6", command=mygtuko_ivedimas)
mygtukas7 = Button(pagrindinis_langas, text="7", command=mygtuko_ivedimas)
mygtukas8 = Button(pagrindinis_langas, text="8", command=mygtuko_ivedimas)
mygtukas9 = Button(pagrindinis_langas, text="9", command=mygtuko_ivedimas)
mygtukas10 = Button(pagrindinis_langas, text="0", command=mygtuko_ivedimas)
mygtukas11= Button(pagrindinis_langas, text="=", command=mygtuko_ivedimas)
mygtukas12= Button(pagrindinis_langas, text="+", command=mygtuko_ivedimas)


uzrasas2 = Label(pagrindinis_langas, text="")

# Lango piešimas
uzrasas1.grid(row=0, column=0)
ivedimas1.grid(row=0, column=1)
mygtukas1.grid(row=1, column=2)
mygtukas2.grid(row=1, column=3)
uzrasas2.grid(row=1, columnspan=3)
pagrindinis_langas.mainloop()