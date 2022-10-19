from tkinter import *
import math


# 3

def calculation():
    a = ent.get()
    a = a.split()
    def addition():
        for i in a:
            if '.' in a[0] or '.' in a[-1]:
                ent.delete(0, END)
                ent.insert(0, float(a[0]) + float(a[-1]))
            else:
                ent.delete(0, END)
                ent.insert(0, int(a[0]) + int(a[-1]))

    def subtraction():
        for i in a:
            if '.' in a[0] or '.' in a[-1]:
                ent.delete(0, END)
                ent.insert(0, float(a[0]) - float(a[-1]))
            else:
                ent.delete(0, END)
                ent.insert(0, int(a[0]) - int(a[-1]))

    def multiplication():
        for i in a:
            if '.' in a[0] or '.' in a[-1]:
                ent.delete(0, END)
                ent.insert(0, float(a[0]) * float(a[-1]))
            else:
                ent.delete(0, END)
                ent.insert(0, int(a[0]) * int(a[-1]))

    def division():
        for i in a:
            if '.' in a[0] or '.' in a[-1]:
                ent.delete(0, END)
                if int(a[0]) == 0 or int(a[-1]) == 0:
                    ent.insert(0, 'None')
                else:
                    ent.insert(0, float(a[0]) / float(a[-1]))
            else:
                ent.delete(0, END)
                if int(a[0]) == 0 or int(a[-1]) == 0:
                    ent.insert(0, 'None')
                else:
                    ent.insert(0, int(a[0]) / int(a[-1]))

    def exponentiation():
        for i in a:
            if '.' in a[0] or '.' in a[-1]:
                ent.delete(0, END)
                ent.insert(0, pow(float(a[0]), float(a[-1])))
            else:
                ent.delete(0, END)
                ent.insert(0, pow(int(a[0]), int(a[-1])))

    def square_root():
        nonlocal a
        if len(a) > 1:
            for i in a:
                if '√' in i:
                    j = i.replace('√', '')
                    print(j)
                    print(a.index(i))
                    k = math.sqrt(int(j))
                    a[a.index(i)] = str(k)
                    print(a)
        else:
            for i in a:
                if '√' in i:
                    ent.delete(0, END)
                    ent.insert(0, math.sqrt(int(i[1:])))


    def сube_root():
        nonlocal a
        if len(a) > 1:
            for i in a:
                if '√' in i:
                    j = i.replace('√', '')
                    print(j)
                    print(a.index(i))
                    k = math.sqrt(int(j))
                    a[a.index(i)] = str(k)
                    print(a)
        else:
            for i in a:
                if '√' in i:
                    ent.delete(0, END)
                    ent.insert(0, math.sqrt(int(i[1:])))


    def sin():
        nonlocal a
        if len(a) > 1:
            for i in a:
                if '√' in i:
                    j = i.replace('√', '')
                    print(j)
                    print(a.index(i))
                    k = math.sqrt(int(j))
                    a[a.index(i)] = str(k)
                    print(a)
        else:
            for i in a:
                if '√' in i:
                    ent.delete(0, END)
                    ent.insert(0, math.sqrt(int(i[1:])))


    def cos():
        nonlocal a
        if len(a) > 1:
            for i in a:
                if '√' in i:
                    j = i.replace('√', '')
                    print(j)
                    print(a.index(i))
                    k = math.sqrt(int(j))
                    a[a.index(i)] = str(k)
                    print(a)
        else:
            for i in a:
                if '√' in i:
                    ent.delete(0, END)
                    ent.insert(0, math.sqrt(int(i[1:])))

    def equal():
        for i in a:
            if '√' in i:
                square_root()
        if '+' in a:
            addition()
        elif '-' in a:
            subtraction()
        elif '*' in a:
            multiplication()
        elif '/' in a:
            division()
        elif '**' in a:
            exponentiation()
    return equal()


win = Tk()
win.geometry('240x190')
win.title('Calculator')

ent = Entry(win, bd=5)
a = ent.get()
a = a.split()
btn_1 = Button(win, text='1', bd=5, command=lambda: ent.insert('insert', '1'))
btn_2 = Button(win, text='2', bd=5, command=lambda: ent.insert('insert', '2'))
btn_3 = Button(win, text='3', bd=5, command=lambda: ent.insert('insert', '3'))
btn_4 = Button(win, text='4', bd=5, command=lambda: ent.insert('insert', '4'))
btn_5 = Button(win, text='5', bd=5, command=lambda: ent.insert('insert', '5'))
btn_6 = Button(win, text='6', bd=5, command=lambda: ent.insert('insert', '6'))
btn_7 = Button(win, text='7', bd=5, command=lambda: ent.insert('insert', '7'))
btn_8 = Button(win, text='8', bd=5, command=lambda: ent.insert('insert', '8'))
btn_9 = Button(win, text='9', bd=5, command=lambda: ent.insert('insert', '9'))
btn_0 = Button(win, text='0', bd=5, command=lambda: ent.insert('insert', '0'))
btn_mult = Button(win, text='*', bd=5, command=lambda: ent.insert('insert', ' * '))
btn_div = Button(win, text='/', bd=5, command=lambda: ent.insert('insert', ' / '))
btn_sub = Button(win, text='-', bd=5, command=lambda: ent.insert('insert', ' - '))
btn_add = Button(win, text='+', bd=5, command=lambda: ent.insert('insert', ' + '))
btn_deg = Button(win, text='**', bd=5, command=lambda: ent.insert('insert', ' ** '))
btn_eq = Button(win, text='=', bd=5, command=calculation)
btn_com = Button(win, text='.', bd=5, command=lambda: ent.insert('insert', '.'))
btn_del = Button(win, text='del', bd=5, command=lambda: ent.delete(0, END))
btn_square_root = Button(win, text='√', bd=5, command=lambda: ent.insert('insert', '√'))

ent.grid(row=0, column=0, columnspan=4, stick='we')
btn_1.grid(row=3, column=0, stick='we')
btn_2.grid(row=3, column=1, stick='we')
btn_3.grid(row=3, column=2, stick='we')
btn_4.grid(row=4, column=0, stick='we')
btn_5.grid(row=4, column=1, stick='we')
btn_6.grid(row=4, column=2, stick='we')
btn_7.grid(row=5, column=0, stick='we')
btn_8.grid(row=5, column=1, stick='we')
btn_9.grid(row=5, column=2, stick='we')
btn_0.grid(row=6, column=1, stick='we')
btn_mult.grid(row=3, column=3, stick='we')
btn_div.grid(row=4, column=3, stick='we')
btn_sub.grid(row=5, column=3, stick='we')
btn_add.grid(row=6, column=3, stick='we')
btn_eq.grid(row=6, column=2, stick='we')
btn_com.grid(row=6, column=0, stick='we')
btn_deg.grid(row=2, column=0, stick='we')
btn_square_root.grid(row=2, column=1, stick='we')
btn_del.grid(row=2, column=2, columnspan=3, stick='wens')

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(0, minsize=30)

win.mainloop()

# 4

stationery = []


def data_request():
    req = tuple(input('Напишіть, який концтовар ви б хотіли додати: ').split())
    stationery.append(req)
    print(stationery)


data_request()
