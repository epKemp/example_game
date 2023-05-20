from tkinter import *

def add():
    c = 0
    a = int(entry1.get())
    b = int(entry2.get())
    c = a + b
    print(c)


def raz():
    c = 0
    d = 0
    a = int(entry1.get())
    b = int(entry2.get())
    # if b > a:
    #     d = a
    #     a = b
    #     b = d
    c = a -b
    print(c)


def umn():
    c = 0
    a = int(entry1.get())
    b = int(entry2.get())
    c = a * b
    print(c)


root = Tk()
root.title('виджет entry')
root.geometry('500x500')
entry1 = Entry(bg='purple', font=('CourierNew', 24))
entry1.pack()
entry2 = Entry(bg='dark green', fg='white', font=('CourierNew', 24))
entry2.pack()
btn1 = Button(text='сумма', command=add)
btn1.pack()
btn2 = Button(text='разность', command=raz)
btn2.pack()
btn3 = Button(text='произведение', command=umn)
btn3.pack()

root.mainloop()