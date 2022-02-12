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
    font=('arial', 16)).grid(padx=5, pady=5)          # та додавання надпису до вікна

ein = Entry(finput, font=('arial', 16))
ein.grid(row=0, column=1, padx=5, pady=5)       # додавання поля введення до вікна
ein.focus()

frez = Frame(top)                           # контейнер для надпису результату
frez.pack(fill=X, expand=YES)
lrez = Label(frez,
             text='Кількість змін: ___',
             font=('arial', 16))
lrez.grid(padx=150, pady=5)                # додавання надпису до вікна


fbut = Frame(top)                           # контейнер для кнопок
fbut.pack(side=LEFT, fill=X, expand='1')
Button(fbut, text = 'Обчислити',
        command = calc,
        font=('arial', 16)).grid(row=1, column=0, padx=5, pady=5) # кнопка "Обчислити"
Button(fbut, text='Закрити',
        command=top.quit,
        font=('arial', 16)).grid(row=1, column=1, padx=250, pady=5)# кнопка "Закрити"

top.bind('<Return>', calc)                  # зв'язування з натисненням клавіш 
top.bind('<Escape>', onEscapeKey)


top.mainloop()

