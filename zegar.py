import tkinter
import time

def wyswietlanie():
    godz1 =''
    obecna = time.strftime('%H:%M:%S')
    if obecna != godz1:
            godz1 = obecna
            l2.config(text = obecna)
    l2.after(200, wyswietlanie)

root = tkinter.Tk()
root.title("Zegar")
root.geometry('300x120')

l = tkinter.Label(root, text = 'Aktualna godzina: ', font = ('Calibri', 18), width = '20')
l.pack()
l2 = tkinter.Label(root, text = wyswietlanie, font=('Calibri', 30) ,bg = 'black', fg = 'green', height = '1', width = '10')
l2.place(x = 46, y = 40)

wyswietlanie()
root.mainloop()