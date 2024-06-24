from tkinter import *

master = Tk()
master.title('Persegi Panjang')
master.geometry('300x150')
master.resizable(0,0)

Label(master, text="Panjang").grid(row=0)
Label(master, text="Lebar").grid(row=1)

Label(master, text="keliling persegi panjang").grid(row=2)
Label(master, text="luas persegi panjang").grid(row=3)

e1 = Entry(master)
e1.grid(row=0, column=1)

e2 = Entry(master)
e2.grid(row=1, column=1)

K = Entry(master, state=DISABLED)
K.grid(row=2, column=1)
L = Entry(master, state=DISABLED)
L.grid(row=3, column=1)

def calc(K, L):
		p = float(e1.get())
		l = float(e2.get())

		K.configure(state=NORMAL)
		K.delete(0, 'end')
		K.insert(0, str((2*p+l) ))
		K.configure(state=DISABLED)

		L.configure(state=NORMAL)
		L.delete(0, 'end')
		L.insert(0, str((p*l) ))
		L.configure(state=DISABLED)

Button(master, text='Quit', command=master.quit).grid(row=4, column=0, sticky=E, pady=4)
Button(master, text='Show', command=lambda: calc(K, L)).grid(row=4, column=1, sticky=W, pady=4)

master.mainloop()
