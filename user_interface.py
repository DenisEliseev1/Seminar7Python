from tkinter import *
from enter_data import *

def click_menu ():
    globals()
    name_f ()
    w.geometry ('430x250')
    btn_file['state'] = 'disabled'
    win_file['state'] = 'disabled'
    txt_name = Label (w, text='Введите ФИО')
    txt_name.grid(column=0, row=4)
    win_name.grid (column=1, row=4)
    txt_number_name1 = Label (w,text='Введите номер1')
    txt_number_name1.grid(column=0, row=8)
    win_num1.grid(column=1, row=8)
    txt_number_name2 = Label (w,text='Введите номер1')
    txt_number_name2.grid(column=0, row=9)
    win_num2.grid(column=1, row=9)
    txt_number_name3 = Label (w,text='Введите номер1')
    txt_number_name3.grid(column=0, row=10)
    win_num3.grid(column=1, row=10)
    btn_number_name.grid(column=0, row=11)

def click_main ():
    globals()
    btn_create['state'] = 'disabled'
    btn_export['state'] = 'disabled'
    txt_file = Label (w, text='Введите название справочника')
    txt_file.grid(column=0, row=3)
    win_file.grid (column=1, row=3)
    btn_file.grid(column=2, row=3)

def name_f ():
    globals()
    name_file (win_file.get())

def record ():
    globals()
    record_data (str(win_file.get()), str (win_name.get()), str (win_num1.get()), str (win_num2.get()),
                 str (win_num3.get()))

w = Tk()
w.title ('Телефонный справочник')
w.geometry ('430x230')
txt_start = Label (w, text='Выберете действие')
txt_start.grid(column=0, row=0) 
btn_create = Button (w, text='Создать новый справочник', command=click_main)
btn_create.grid(column=0, row=1) 
btn_export = Button (w, text='Добавить в сущ. справочник')
btn_export.grid(column=0, row=2)
btn_file = Button (w, text='Ввод', command=click_menu)
btn_number_name = Button (w, text='Передать в справочник', command=record)
win_file = Entry (w, width=20)
win_name = Entry (w, width=20)
win_num1 = Entry (w, width=20)
win_num2 = Entry (w, width=20)
win_num3 = Entry (w, width=20)
w.mainloop()