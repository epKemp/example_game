from tkinter import *


def delete():
    entry1.delete(0, END)

def get_text():
    text = entry1.get()
    print(text)
    label1['text'] = text
    entry1['bg'] = text


def get_result():
    result = []
    tmp = entry2.get() #123+456
    signs = '124567890+-/* '
    s = ''
    r = 0
    for let in tmp:
        if let in signs:
            label1['text'] = ''
        else:
            label1['text'] = 'проверьте введенные данные'
            break
        if let == '+':
            s = '+'
        elif let == '-':
            s = '-'
        elif let =='/':
            s = '/'
        elif let == '*':
            s = '*'
    if s == "+":
        result = tmp.split('+')
        print(result)
    #r = int(result[0] + int(result[1]))
    for i in range(len(result)):
        r += int(result[i])
    #print(r)
    label1['text'] = r


root = Tk()
root.title('виджет entry')
root.geometry('500x500')
root.resizable(False, False)
entry1 = Entry(fg='white', bg='pink', font=('CourierNew', 24),justify='center')
entry1.pack()
entry2 = Entry( font=('CourierNew', 24))
entry2.pack(side=BOTTOM)
entry1.insert(0, 'поле для ввода')
btn_delete = Button(text='очистить', command=delete)
btn_delete.pack()
btn_get_text = Button(text='получить текст', command=get_text)
btn_get_text.pack()
btn_result = Button(text='=', command=get_result)
btn_result.pack(side=BOTTOM)
label1 = Label(text='', font=('CourierNew', 24))
label1.pack()

root.mainloop()