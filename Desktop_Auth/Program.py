import tkinter
import cProfile
from tkinter import CENTER
from tkinter import messagebox
from tkinter import Tk

window = Tk()
window.title('Авторизация')
window.geometry('450x230')
window.resizable(False, False)
font_header = ('Arial', 14)
font_entry = ('Arial', 14)
label_font = ('Arial', 14)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


def clicked(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    messagebox.showinfo(
        'Заголовок', '{username}, {password}'.format(
            username=username, password=password))

    main_label = tkinter.Label(
        window, text='Авторизация', font=font_header,
        justify=CENTER, **header_padding)
    main_label.pack()

    username_label = tkinter.Label(
        window, text='Имя пользователя', font=label_font, **base_padding)
    username_label.pack()

    username_entry = tkinter.Entry(
        window, bg='#FFFFFF', fg='#B5DEFA', font=font_entry)
    username_entry.pack()

    password_label = tkinter.Label(
        window, text='Пароль', font=label_font, **base_padding)
    password_label.pack()

    password_entry = tkinter.Entry(
        window, bg='#FFFFFF', fg='#B5DEFA', font=font_entry)
    password_entry.pack()

    send_btn = tkinter.Button(
        window, bg='#B5DEFA', text='Войти', command=clicked)
    send_btn.pack(**base_padding)


window.mainloop()
cProfile.run("window.mainloop()")
