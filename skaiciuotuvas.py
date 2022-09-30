# Patobulinti 1 užduoties programą, kad ji:
# Įvedus vardą, atspausdintų "Labas, {vardas}!" ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter"


from tkinter import *

pagrindinis_langas = Tk()
pagrindinis_langas.title('Skaiciuotuvas')

def pasisveikinti():
    ivesta = ivedimas1.get()
    uzrasas2["text"] = (f"Labas, {ivesta}!")

# Laukų, mygtukų formavimas
uzrasas1 = Label(pagrindinis_langas, text="")
ivedimas1 = Entry(pagrindinis_langas)
mygtukas1 = Button(pagrindinis_langas, text="1", )
mygtukas2 = Button(pagrindinis_langas, text="2", )
mygtukas3 = Button(pagrindinis_langas, text="3", )
mygtukas4 = Button(pagrindinis_langas, text="4", )
mygtukas5 = Button(pagrindinis_langas, text="5", )
mygtukas6 = Button(pagrindinis_langas, text="6", )
mygtukas7 = Button(pagrindinis_langas, text="7", )
mygtukas8 = Button(pagrindinis_langas, text="8", )
mygtukas9 = Button(pagrindinis_langas, text="9", )
mygtukas10 = Button(pagrindinis_langas, text="0", )
mygtukas11= Button(pagrindinis_langas, text="=", )
mygtukas12= Button(pagrindinis_langas, text="+", )

ivedimas1.bind("<Return>", lambda event: pasisveikinti())
uzrasas2 = Label(pagrindinis_langas, text="")

# Lango piešimas
uzrasas1.grid(row=0, column=0)
ivedimas1.grid(row=0, column=1)
mygtukas1.grid(row=1, column=2)
mygtukas2.grid(row=1, column=3)
uzrasas2.grid(row=1, columnspan=3)
pagrindinis_langas.mainloop()