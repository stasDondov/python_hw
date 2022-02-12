from tkinter import *

def calc(ev = None):
    Str = ein.get()
    C1 = Str.count('(')
    C2 = Str.count(')')
    C = min(C1, C2)
    for i in range(C):
        I1 = Str.index('(')
        I2 = Str.index(')')
        Str = Str[:I1] + Str[I2+1:]
    
    rezult = 'Результат: {}'.format(Str)      # побудова рядка для відображення
    lrez.configure(text = rezult)           # зміна надпису значенням результату


def onEscapeKey(event):
    ein.delete(0, 'end')
    top.quit()


top = Tk()

finput = Frame(top)
finput.pack(fill=X, expand=YES)
Label(finput, text = 'Введіть послідовність: ',
    font=('arial', 16)).pack(side=LEFT)     # створення надпису
                                            # та додавання надпису до вікна
ein = Entry(finput, font=('arial', 16))     # створення поля введення
ein.pack(side=LEFT, fill=X, expand=1)       # додавання поля введення до вікна

frez = Frame(top)                           # контейнер для надпису результату
frez.pack(fill=X, expand=YES)
lrez = Label(frez,
             text='Кількість змін: ___',
             font=('arial', 16))            # створення надпису
lrez.pack(side=LEFT, fill=X)                # додавання надпису до вікна


fbut = Frame(top)                           # контейнер для кнопок
fbut.pack(side=LEFT, fill=X, expand='1')
Button(fbut, text = 'Обчислити',
        command = calc,
        font=('arial', 16)).pack(side=LEFT) # кнопка "Обчислити"
Button(fbut, text='Закрити',
        command=top.quit,
        font=('arial', 16)).pack(side=RIGHT)# кнопка "Закрити"

top.bind('<Return>', calc)                  # зв'язування з натисненням клавіш 
top.bind('<Escape>', onEscapeKey)


top.mainloop()

