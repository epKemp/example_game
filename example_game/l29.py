from tkinter import *
USD = 0.013
EUR = 0.012
KZT = 5.47

user_data = '200'

USD_data = int(user_data) * USD
EUR_data = int(user_data) * EUR
KZT_data = int(user_data) * KZT
"""if USD_data < 1:
    USD_data = int(USD_data * 100)
    print(f'{USD_data} ц')
if EUR_data < 1:
    EUR_data = int(EUR_data * 100)
    print(f'{EUR_data} ц')
print(print(f'{USD_data} дол., {EUR_data} евр.'))"""


def conver_to_USD():
    user = entry1.get()
    if int(user) > 0:
        USD_data = (int(user) * USD)
        if USD_data < 1:
            USD_data = str(int(USD_data * 100)) + 'cent'
        else:
            USD_data = str(USD_data) + '$'
        entry1.delete(0, END)
        entry1.insert(0, str(USD_data))
    else:
        info_label.config(fg='red')
        info_label.config(text='Проверьте введенные данные')



def conver_to_EUR():
    user = entry1.get()
    if int(user) > 0:
        EUR_data = (int(user) * EUR)
        if EUR_data < 1:
            EUR_data = str(int(EUR_data * 100)) + 'cent'
        else:
            EUR_data = str(EUR_data) + '€'
        entry1.delete(0, END)
        entry1.insert(0, str(EUR_data))
    else:
        info_label.config(fg='red')
        info_label.config(text='Проверьте введенные данные')


def conver_to_KZT():
    user = entry1.get()
    if int(user) > 0:
        KZT_data = (int(user) * KZT)
        """if KZT_data > 0:
            KZT_data = str(int(KZT_data * 100)) + 'тиын'
        else:"""
        KZT_data = str(KZT_data) + '₸'
        entry1.delete(0, END)
        entry1.insert(0, str(KZT_data))
    else:
        info_label.config(fg='red')
        info_label.config(text='Проверьте введенные данные')


root = Tk()
root.title('конвертер валют')
root.geometry('300x300')
root.resizable(False, False)
root.config(bg='black')
l1 = Label(root, text='Введите сумму в рублях',bg='black', fg='white')
l1.pack(expand=True)
entry1 = Entry(root, width=20, bg='black',fg='white')
entry1.pack()
btn1 = Button(root, text='USD',bg='black',fg='white' , command=conver_to_USD)
btn1.pack(side='left')
btn2 = Button(root, text='EUR',bg='black',fg='white' , command=conver_to_EUR)
btn2.pack(side='right')
btn3 = Button(root, text='KZT',bg='black',fg='white' , command=conver_to_KZT)
btn3.pack(side='left')
root.mainloop()