from tkinter import *

def calc(ev = None):
    List = list(map(int, ein.get().split()))
    counter = 0
    for i in range(0, len(List)-1):
        if List[i] * List[i + 1] < 0:
            counter += 1
    rezult = 'Результат: {}'.format(counter)      # побудова рядка для відображення
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
ein.focus()

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

