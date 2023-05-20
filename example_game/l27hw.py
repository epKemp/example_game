from tkinter import *


def get_label():
    global c
    text_lab = ("""STANDARD OPTIONS: activebackground, activeforeground, anchor,
            background, bitmap, borderwidth, cursor,
            disabledforeground, font, foreground,
            highlightbackground, highlightcolor,
            highlightthickness, image, justify,
            padx, pady, relief, takefocus, text,
            textvariable, underline, wraplength
            WIDGET-SPECIFIC OPTIONS
            height, state, width""")
    lab_1 = Label(text=text_lab)
    c.create_window(250, 250, window=lab_1, width=500, height=500, tags='l1')


def delete():
    global c
    c.delete('l1', 'l2','l3')


def get_canvas():
    global c
    text_can = ( """Canvas widget to display graphical 
                    elements like lines or text."""
                    """Valid resource
                    names: background, bd, bg, borderwidth, closeenough,
                    confine, cursor, height, highlightbackground, highlightcolor,
                    highlightthickness, insertbackground, insertborderwidth,
                    insertofftime, insertontime, insertwidth, offset, relief,
                    scrollregion, selectbackground, selectborderwidth, selectforeground,
                    state, takefocus, width, xscrollcommand, xscrollincrement,
                    yscrollcommand, yscrollincrement.""")
    lab_2 = Label(text=text_can)
    c.create_window(250, 250, window=lab_2, width=500, height=500, tags='l2')


def get_button():
    global c
    text_but = ( """STANDARD OPTIONS

            activebackground, activeforeground, anchor,
            background, bitmap, borderwidth, cursor,
            disabledforeground, font, foreground
            highlightbackground, highlightcolor,
            highlightthickness, image, justify,
            padx, pady, relief, repeatdelay,
            repeatinterval, takefocus, text,
            textvariable, underline, wraplength

        WIDGET-SPECIFIC OPTIONS

            command, compound, default, height,
            overrelief, state, width""")
    lab_3 = Label(text=text_but)
    c.create_window(250, 250, window=lab_3, width=500, height=500, tags='l3')



root = Tk()
root.title('основные виджеты')
root.geometry('1000x500')
btn1 = Button(text='Виджет Label',command=get_label)
btn2 = Button(text='Виджет Canvas', command=get_canvas)
btn3 = Button(text='Виджет  Button', command=get_button)
btn4 = Button(text='Отмена', command=delete)
btn1.pack(expand=True,side=LEFT)
btn2.pack(expand=True,side=LEFT)
btn3.pack(expand=True,side=LEFT)
btn4.pack(expand=True,side=LEFT)
c = Canvas(root, width=500, height=500, bg='white')
c.pack(side=RIGHT)




root.mainloop()