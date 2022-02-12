from tkinter import *

class Tex:
    def __init__(self, main):

        self.main = main
        self.text1 = Text(self.main,
                          height=10, width=30)
        self.text1.grid(row=0, column=0)

        self.lst = Listbox(self.main,
                           height=7)
        self.lst.grid(row=0, column=1)

        scrl_1 = Scrollbar(self.main,
                           command=self.lst.yview)
        scrl_1.grid(row=0, column=2)

        self.lst.config(yscrollcommand=scrl_1.set)

        Button(self.main,
               text='Прочитати',
               command=self.read).grid(row=1, column=0)

        Button(self.main,
               text='Exit',
               command=self.exit).grid(row=1, column=1)

    def read(self):
        r = self.text1.get('1.0', END)
        for word in r.split():
            self.lst.insert(END, word)

    def exit(self):
        self.main.destroy()


if __name__=='__main__':
    top = Tk()
    A = Tex(top)
    top.mainloop()

