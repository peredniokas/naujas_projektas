from tkinter import *

pagrindinis_langas = Tk()
pagrindinis_langas.title("Skaiciuotuvas")


# Laukų, mygtukų formavimas

ivedimas1 = Entry(pagrindinis_langas, width=40, borderwidth=10)
ivedimas1.grid(row=0, column=0, columnspan=3)

def mygtuko_ivedimas(number):
    ivestas = ivedimas1.get()
    ivedimas1.delete(0, END)
    ivedimas1.insert(0, str(ivestas)+ str(number))

def mygtukas_isvalantis():
    ivedimas1.delete(0, END)

def mygtukas_plius():
    pirmas_skaicius = ivedimas1.get()
    global f_num
    global math
    math = "pridedame"
    f_num = int(pirmas_skaicius)
    ivedimas1.delete(0, END)

def mygtukas_atimti():
    pirmas_skaicius = ivedimas1.get()
    global f_num
    global match
    math = "atimame"
    f_num = int(pirmas_skaicius)
    ivedimas1.delete(0, END)

def mygtukas_dauginti():
    pirmas_skaicius = ivedimas1.get()
    global f_num
    global match
    math = "dauginame"
    f_num = int(pirmas_skaicius)
    ivedimas1.delete(0, END)

def mygtukas_dalinti():
    pirmas_skaicius = ivedimas1.get()
    global f_num
    global match
    math = "daliname"
    f_num = int(pirmas_skaicius)
    ivedimas1.delete(0, END)

def mygtukas_lygu():
    antras_skaicius = ivedimas1.get()
    ivedimas1.delete(0, END)

    if math == "pridedame":    
        ivedimas1.insert(0, f_num + int(antras_skaicius))

    elif  math == "atimame":
        ivedimas1.insert(0, f_num - int(antras_skaicius))

    elif math == "dauginame":
        ivedimas1.insert(0, f_num * int(antras_skaicius))

    elif math == "daliname":
        ivedimas1.insert(0, f_num / int(antras_skaicius))

    
   

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
mygtukas_plius = Button(pagrindinis_langas, text="+", padx=40, pady=20, command= mygtukas_plius)
mygtukas_lygu = Button(pagrindinis_langas, text="=", padx=90, pady=20, command= mygtukas_lygu)
mygtukas_isvalantis = Button(pagrindinis_langas, text="Isvalyti!", padx=70, pady=20, command= mygtukas_isvalantis)
mygtukas_atimti = Button(pagrindinis_langas, text="-", padx=40, pady=20, command= mygtukas_atimti)
mygtukas_dauginti = Button(pagrindinis_langas, text="*", padx=40, pady=20, command= mygtukas_dauginti)
mygtukas_dalinti = Button(pagrindinis_langas, text="/", padx=39, pady=20 , command= mygtukas_dalinti)



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
mygtukas0.grid(row=4, column=0)
mygtukas_plius.grid(row=5, column=0)
mygtukas_atimti.grid(row=6, column=0)
mygtukas_dauginti.grid(row=6, column=1)
mygtukas_dalinti.grid(row=6, column=2)

mygtukas_lygu.grid(row=5, column=1, columnspan=2)
mygtukas_isvalantis.grid(row=4, column=1, columnspan=2)

pagrindinis_langas.mainloop()
