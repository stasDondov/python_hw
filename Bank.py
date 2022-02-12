from tkinter import*


def clear():
    "Функція для очищення полів введення вікна 1"
    ein1.delete(0, 'end')
    ein2.delete(0, 'end')
    ein3.delete(0, 'end')
    Kursein1.delete(0, 'end')
    Kursein2.delete(0, 'end')
    Kursein3.delete(0, 'end')
    

def write(a = 'Bank.txt'):
    "Функція для запису даних у файл"
    with open(a, 'w') as f:
        print(ein1.get(), Kursein1.get(), file=f)
        print(ein2.get(), Kursein2.get(), file=f)
        print(ein3.get(), Kursein3.get(), file=f)


top = Tk() # вікно 1

Linput1 = Label(top,
               text = 'Введіть код валюти 1:',
               font=('arial', 16))  # надпис про код валюти 1
Linput1.pack()
ein1 = Entry(top, font=('arial', 16)) # Введення валюти 1
ein1.pack()

Kurs1 = Label(top,
              text = 'Курс валюти 1 відносно долара:',
              font=('arial', 16))  # надпис про курс валюти 1
Kurs1.pack()
Kursein1 = Entry(top, font=('arial', 16)) # введення курсу валюти 1
Kursein1.pack()


Linput2 = Label(top,
               text = 'Введіть код валюти 2:',
               font=('arial', 16))  # надпис про код валюти 2
Linput2.pack()
ein2 = Entry(top, font=('arial', 16)) # Введення коду валюти 2
ein2.pack()

Kurs2 = Label(top,
              text = 'Курс валюти 2 відносно долара:',
              font=('arial', 16)) # надпис про курс валюти 2
Kurs2.pack()
Kursein2 = Entry(top, font=('arial', 16))
Kursein2.pack() # введення курсу валюти 2


Linput3 = Label(top,
               text = 'Введіть код валюти 3:',
               font=('arial', 16))  # надпис про код валюти 2
Linput3.pack()
ein3 = Entry(top, font=('arial', 16)) # Введення коду валюти 2
ein3.pack()

Kurs3 = Label(top,
              text = 'Курс валюти 3 відносно долара: ',
              font=('arial', 16))  # надпис про курс валюти 3
Kurs3.pack()
Kursein3 = Entry(top, font=('arial', 16))
Kursein3.pack() # введення курсу валюти 3


Bwriter = Button(top, text = 'Підтвердити',
                 command = write,
                 font=('arial', 16)) # кнопка для запису даних у файл
Bwriter.pack()

Quit = Button(top, text = 'Завершити',
                 command = clear,
                 font=('arial', 16)) # кнопка для очищення полів введення
Quit.pack()

top.mainloop()
#======================================================

def clear2():
    "Функція для очищення полів введення вікна 2"
    ein11.delete(0, 'end')
    ein12.delete(0, 'end')
    moneyein.delete(0, 'end')
    

def reader(a = 'Bank.txt'):
    "Функція для зчитування даних з файлу"
    global Data
    Data = {}
    with open(a, 'r') as f:
        r = f.readlines()
        S = 'Курси валют:\n'
        for line in r:
            line = line.split()
            Data.update({line[0]:line[1]})
            S += line[0] + ' : ' + line[1] + '\n'
    return S


top2 = Tk() # вікно 2

inf = reader()
INF = Label(top2,
            text = inf,
            font=('arial', 16)) # запишемо інформацію про курси валют
INF.pack()

Linput11 = Label(top2,
                 text = 'Введіть код валюти з якої будемо переводити:',
                 font=('arial', 16))  # надпис про код валюти 1
Linput11.pack()
ein11 = Entry(top2, font=('arial', 16)) # Введення коду валюти 1
ein11.pack()

Linput12 = Label(top2,
                 text = 'Введіть код валюти в яку слід переводити:',
                 font=('arial', 16))  # надпис прокод валюти 2
Linput12.pack()
ein12 = Entry(top2, font=('arial', 16)) # Введення коду валюти 2
ein12.pack()


Money = Label(top2,
              text = 'Кількість грошей: ',
              font=('arial', 16))
Money.pack()
moneyein = Entry(top2, font=('arial', 16))
moneyein.pack()


def calc():
    "Функція для переведення грошей в іншу валюту"
    kurs = float(Data[ein12.get()]) / float(Data[ein11.get()])
    ans = (float(moneyein.get()) * kurs)
    Result.configure(text = 'Результат: {}'.format('{0:.2f}'.format(ans)))
    return ans


Result = Label(top2,
               text = 'Результат: ',
               font=('arial', 16))
Result.pack()

Bcount = Button(top2, text = 'Обчислити',
                 command = calc,
                 font=('arial', 16)) # кнопка для переведення грошей в іншу валюту
Bcount.pack()


Quit1 = Button(top2, text = 'Завершити',
                 command = clear2,
                 font=('arial', 16)) # кнопка для очищення полів введення
Quit1.pack()

top2.mainloop()

