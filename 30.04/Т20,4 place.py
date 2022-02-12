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
top.geometry('500x150')

Label(text = 'Введіть послідовність: ',
    font=('arial', 16)).place(relx=0.05, rely=0.05)
                                            # та додавання надпису до вікна
ein = Entry(font=('arial', 16))     # створення поля введення
ein.place(relx=0.5, rely=0.05)
ein.focus()

lrez = Label(text='Кількість змін: ___',
             font=('arial', 16))            # створення надпису
lrez.place(relx=0.3, rely=0.35)


Button(text = 'Обчислити',
        command = calc,
        font=('arial', 16)).place(relx=0, rely=0.7) # кнопка "Обчислити"
Button(text='Закрити',
        command=top.quit,
        font=('arial', 16)).place(relx=0.8, rely=0.7) # кнопка "Закрити"

top.bind('<Return>', calc)                  # зв'язування з натисненням клавіш 
top.bind('<Escape>', onEscapeKey)


top.mainloop()

