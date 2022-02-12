from tkinter import *
from random import randint
from collections import defaultdict
from math import sqrt


class Triangle:

    def __init__(self, main):

        self.main = main
        self.data = defaultdict(list)

        label_1 = Label(self.main,
                        text='Введіть N:')
        label_1.grid(row=0, column=0)

        self.entr_1 = Entry(self.main)
        self.entr_1.grid(row=0, column=1)

        Button(self.main,
               text='Згенерувати N координат',
               command=self.gener).grid(row=1, columnspan=2)

        self.lst_1 = Listbox(self.main,
                           height=4)
        self.lst_1.grid(row=2, columnspan=2)

        scrl_1 = Scrollbar(self.main,
                           command=self.lst_1.yview)
        scrl_1.grid(row=2, column=2)

        self.lst_1.config(yscrollcommand=scrl_1.set)

        Button(self.main,
               text='Exit',
               command=self.Mexit).grid(row=5, column=0)

        Button(self.main,
               text='Зобразити фігуру',
               command=self.draw).grid(row=5, column=1)

    def gener(self):
        n = int(self.entr_1.get())
        for i in range(n):
            x = randint(0, 100)
            y = randint(0, 100)
            self.data[i] = (x, y)
            self.lst_1.insert(END, 'x{}={}, y{}={}'.format(i, x, i, y))

        Max = 0
        self.koord = []
        for i1, i in self.data.items():
            for j1, j in self.data.items():
                for k1, k in self.data.items():
                    a = sqrt((i[0]-j[0])**2 + (i[1]-j[1])**2)
                    b = sqrt((j[0]-k[0])**2 + (j[1]-k[1])**2)
                    c = sqrt((k[0]-i[0])**2 + (k[1]-i[1])**2)
                    p = (a + b + c) / 2
                    S = sqrt(p*(p-a)*(p-b)*(p-c))
                    if S > Max:
                        Max = S
                        self.koord = [i1, j1, k1]
    
                        
        label_2 = Label(self.main,
                        text='Найбільша площа: {0:.2f}'.format(Max))
        label_2.grid(row=3, columnspan=2)

        lst_2 = Listbox(self.main,
                        height=3)
        lst_2.grid(row=4, columnspan=2)

        for i in self.koord:
            lst_2.insert(END,
                         'x{}={}, y{}={}'.format(i, self.data[i][0], i, self.data[i][1]))

    def Mexit(self):
        self.main.destroy()

    def draw(self):

        self.child = Toplevel(self.main)
        canv = Canvas(self.child,
                      height=200, width=200)
        canv.pack()

        A = self.data[self.koord[0]]
        B = self.data[self.koord[1]]
        C = self.data[self.koord[2]]
            
        canv.create_polygon(A[0], A[1], B[0], B[1], C[0], C[1])
        
        Button(self.child,
               text='Exit',
               command=self.exit).pack()
        
    def exit(self):
        self.child.destroy()
    
                   
if __name__ == '__main__':
    top = Tk()
    A = Triangle(top)
    top.mainloop()

