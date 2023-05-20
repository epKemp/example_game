from tkinter import *






def get_label():
    def text_copy():
        win_label.clipboard_clear()
        win_label.clipboard_append(label1['text'])

    win_label = Tk()
    win_label.title('Виджет Label')
    text_label = ( """STANDARD OPTIONS: activebackground, activeforeground, anchor,
            background, bitmap, borderwidth, cursor,
            disabledforeground, font, foreground,
            highlightbackground, highlightcolor,
            highlightthickness, image, justify,
            padx, pady, relief, takefocus, text,
            textvariable, underline, wraplength
            WIDGET-SPECIFIC OPTIONS
            height, state, width""")
    label1 = Label(win_label, text=text_label)
    label1.pack()
    btn_copy = Button(win_label,text='копировать', command='text_copy')
    btn_copy.pack()


def get_button():
    win_button = Tk()
    win_button.title('Виджет  Button')
    win_button.resizable(False, False)
    btn_info = Button(win_button, text='пример кнопки')
    text_button = ( """STANDARD OPTIONS

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
    label_info = Label(win_button, text=text_button)
    btn_info.pack(side=RIGHT)
    label_info.pack(side=LEFT)


def get_canvas():
    def draw_line():
        canv1.create_line(100,250,300,250, fill='black',tags='line1')

    def clear():
        canv1.delete('line1')
    win_canvas = Tk()
    win_canvas.title('Виджет  Canvas')
    win_canvas.resizable(False, False)
    canv1 = Canvas(win_canvas,width=500,height=500, bg='white')
    text_canvas = ( """Canvas widget to display graphical 
                    elements like lines or text."""
                    """Valid resource
                    names: background, bd, bg, borderwidth, closeenough,
                    confine, cursor, height, highlightbackground, highlightcolor,
                    highlightthickness, insertbackground, insertborderwidth,
                    insertofftime, insertontime, insertwidth, offset, relief,
                    scrollregion, selectbackground, selectborderwidth, selectforeground,
                    state, takefocus, width, xscrollcommand, xscrollincrement,
                    yscrollcommand, yscrollincrement.""")
    label1 = Label(win_canvas, text=text_canvas)
    label1.pack(side=LEFT)
    canv1.pack(side=RIGHT)
    btn_line = Button(win_canvas,text='нарисовать линию',command=draw_line)
    btn_line.pack(side=BOTTOM)
    btn_clear = Button(win_canvas,text='очистить',command=clear)
    btn_clear.pack(side=BOTTOM)




root = Tk()
root.title('основные виджеты')
root.geometry('500x500')
btn1 = Button(text='Виджет Label',command=get_label)
btn2 = Button(text='Виджет Canvas', command=get_canvas)
btn3 = Button(text='Виджет  Button', command=get_button)
btn_close = Button(text='закрыть все', command=root.quit)
btn1.pack(expand=True)
btn2.pack(expand=True)
btn3.pack(expand=True)
btn_close.pack(side=RIGHT)

root.mainloop()

