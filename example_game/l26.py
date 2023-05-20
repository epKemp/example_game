from tkinter import *
root = Tk()
root.geometry('500x300')
root.title('справка')
#виджет лабел - текстовая метка, позволяет разместтить статический неизменяемый текст
#label_1 = Label(text='текст', foreground='grey', font=('Inoconsolata Extra Expanded', 20))
label_name = Label(root, text='Виджет Label', font=('CourierNew', 24), foreground='dark blue')
label_name.pack()
label_param =  Label(root, text='параметры:', font=('CourierNew', 20), foreground='dark blue')
label_param.pack(anchor='nw')
label_1 =  Label(root, text='text-текст метки', font=('CourierNew', 14))
label_1.pack(anchor='nw')
label_2 =  Label(root, text='foreground(fg) - цвет метки', font=('CourierNew', 14))
label_2.pack(anchor='nw')
label_3 =  Label(root, text='font - шрифт текста', font=('CourierNew', 14))
label_3.pack(anchor='nw')
btn_close  = Button(root,text='закрыть', command=root.destroy, activebackground='orange')
btn_close.place(x=0, y=0)



root.mainloop()