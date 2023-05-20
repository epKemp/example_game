from tkinter import *
root = Tk()
root.geometry('100x200')
root.minsize(100,200)
root.maxsize(800,640)
root.attributes('-fullscreen')
root.title(' оконное приложение')
btn_1 = Button(root, text='Кнопка 1', fg='red')
btn_2 = Button(root, text='Закрыть', fg='orange', command=root.destroy)
btn_3 = Button(root, text='Кнопка 2', fg='purple')
btn_1.pack(side=BOTTOM)  # side = TOP,BOTTOM, RIGHT, LEFT
btn_2.pack(side=LEFT)
btn_3.pack(side=RIGHT)
root.mainloop()