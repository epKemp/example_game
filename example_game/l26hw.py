from tkinter import *
def info_lab():
    global c
    x1 = 400
    y1 = 875
    label_1 = Label(text='Label(text, font, fg, bg)', font=('CourierNew', 24), foreground='white', bg='blue')
    c.create_window(400, 875, window=label_1, width=350, height=50)

def draw_rect():
    global c
    x1= 100
    y1 = 100
    x2 = 300
    y2 = 300
    c.create_rectangle(x1, y1, x2, y2, fill='white',tags='rect1')
    #print(c.find_all())


def draw_oval():
    global c
    x1 = 100
    y1 = 100
    x2 = 300
    y2 = 300
    c.create_oval(x1,y1,x2,y2, fill='white', tags='oval1')


# def del_info1():
#     global c
#     c.delete(info1)


def del_rect():
    global c
    c.delete('rect1',)




def del_oval():
    global c
    c.delete('oval1')



root = Tk()
root.title('l27hw')
c = Canvas(root, width=1000, height=1000, bg='blue')
c.pack(expand=True)
btn1 = Button(text='Информация о Label',command=info_lab,bg='blue')
c.create_window(100, 875, window=btn1, width=300, height=50)
btn2 = Button(text='нарисовать прямоугольник', command=draw_rect)
c.create_window(400,475,window=btn2 , width=200, height=50)
btn5 = Button(text='удалить', command=del_rect)
c.create_window(450,375,window=btn5 , width=100, height=50)
btn3 = Button(text='нарисовать овал',command=draw_oval)
c.create_window(50,475,window=btn3 , width=100, height=50)
btn4 = Button(text='удалить',command=del_oval)
c.create_window(50,375,window=btn4 , width=100, height=50)

#btn2 = Button(text='Скрыть информацию о Label', bg='blue',command=del_info1)
#c.create_window(100, 575, window=btn2, width=200, height=50)
root.mainloop()