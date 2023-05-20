from tkinter import *
def draw_rect():
    global c
    x1= 100
    y1 = 100
    x2 = 300
    y2 = 300
    c.create_rectangle(x1, y1, x2, y2, fill='white',tags='rect1')
    #print(c.find_all())


def del_all():
    global c
    c.delete(ALL)


def del_rect():
    global c
    c.delete('rect1',)




def del_oval():
    global c
    c.delete('oval1')




root = Tk()
#root.geometry('100x200')
root.title('знакомство с canvas')
#label_1 = Label(root, text='text', background='green', fg='blue')
#label_1.place(x=50,y=100)
#Canvas - виджет для работы с графикой
c = Canvas(root, width=500, height=500, bg='purple')
c.pack(expand=True)
#c.create_line(0,0,20,0,40,50,60,0, fill='white', tags='line1')
btn1 = Button(text='нарисовать прямоугольник', command=draw_rect)
c.create_window(400,475,window=btn1 , width=200, height=50)
btn2 = Button(text='удалить', command=del_rect)
c.create_window(450,375,window=btn2 , width=100, height=50)
btn3 = Button(text='нарисовать овал',command=draw_oval)
c.create_window(50,475,window=btn3 , width=100, height=50)
btn4 = Button(text='удалить',command=del_oval)
c.create_window(50,375,window=btn4 , width=100, height=50)


c.find_all()
root.mainloop()