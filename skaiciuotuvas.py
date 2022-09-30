from tkinter import *
 
expression = ""
 
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
 
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
 
if __name__ == "__main__":
    Skaiciuotuvas = Tk()
 
    Skaiciuotuvas.configure(background="light green")
 
    Skaiciuotuvas.title("Keistas Skaiciuotuvas")
 
    Skaiciuotuvas.geometry("270x150")
 
    equation = StringVar()
 
    expression_field = Entry(Skaiciuotuvas, textvariable=equation)
 
    expression_field.grid(columnspan=4, ipadx=70)
 
    mygtukas_1 = Button(Skaiciuotuvas, text=' 1 ', fg='black', bg='red',command=lambda: press(1), height=1, width=7)
    mygtukas_2 = Button(Skaiciuotuvas, text=' 2 ', fg='black', bg='blue',command=lambda: press(2), height=1, width=7)
    mygtukas_3 = Button(Skaiciuotuvas, text=' 3 ', fg='black', bg='green',command=lambda: press(3), height=1, width=7)
    mygtukas_4 = Button(Skaiciuotuvas, text=' 4 ', fg='black', bg='yellow',command=lambda: press(4), height=1, width=7)
    mygtukas_5 = Button(Skaiciuotuvas, text=' 5 ', fg='black', bg='pink',command=lambda: press(5), height=1, width=7)
    mygtukas_6 = Button(Skaiciuotuvas, text=' 6 ', fg='black', bg='orange',command=lambda: press(6), height=1, width=7)
    mygtukas_7 = Button(Skaiciuotuvas, text=' 7 ', fg='black', bg='grey',command=lambda: press(7), height=1, width=7)
    mygtukas_8 = Button(Skaiciuotuvas, text=' 8 ', fg='black', bg='brown',command=lambda: press(8), height=1, width=7)
    mygtukas_9 = Button(Skaiciuotuvas, text=' 9 ', fg='black', bg='silver',command=lambda: press(9), height=1, width=7)
    mygtukas_0 = Button(Skaiciuotuvas, text=' 0 ', fg='black', bg='gold',command=lambda: press(0), height=1, width=7)
    
    mygtukas_sudeti = Button(Skaiciuotuvas, text=' + ', fg='black', bg='pink',command=lambda: press("+"), height=1, width=7)
    mygtukas_atimti = Button(Skaiciuotuvas, text=' - ', fg='black', bg='red',command=lambda: press("-"), height=1, width=7)
    mygtukas_dauginti = Button(Skaiciuotuvas, text=' * ', fg='black', bg='red',command=lambda: press("*"), height=1, width=7)
    mygtukas_dalinti = Button(Skaiciuotuvas, text=' / ', fg='black', bg='red',command=lambda: press("/"), height=1, width=7)
    mygtukas_lygu = Button(Skaiciuotuvas, text=' = ', fg='black', bg='red',command=equalpress, height=1, width=7)
    
    mygtukas_isvalyti = Button(Skaiciuotuvas, text='Istrinti', fg='black', bg='red',command=clear, height=1, width=7)
    mygtukas_taskas= Button(Skaiciuotuvas, text='.', fg='black', bg='red',command=lambda: press('.'), height=1, width=7)

    mygtukas_taskas.grid(row=6, column=0)
    
    mygtukas_isvalyti.grid(row=5, column='1')
    mygtukas_lygu.grid(row=5, column=2)
    mygtukas_dalinti.grid(row=5, column=3)
    mygtukas_dauginti.grid(row=4, column=3)
    mygtukas_atimti.grid(row=3, column=3)
    mygtukas_sudeti.grid(row=2, column=3)
    mygtukas_0.grid(row=5, column=0)
    mygtukas_9.grid(row=4, column=2)
    mygtukas_8.grid(row=4, column=1)
    mygtukas_7.grid(row=4, column=0)
    mygtukas_6.grid(row=3, column=2)
    mygtukas_5.grid(row=3, column=1)
    mygtukas_4.grid(row=3, column=0)
    mygtukas_3.grid(row=2, column=2)
    mygtukas_2.grid(row=2, column=1)
    mygtukas_1.grid(row=2, column=0)
    Skaiciuotuvas.mainloop()