from tkinter import *
from collections import defaultdict
from math import sqrt, acos, sin, cos


class Tochki:

    def __init__(self, main):
        self.main = main
        self.main.geometry('+400+150')
        self.main.title('Points')
        self.dots = defaultdict(list)
        self.distances = defaultdict(list)
        self.counter = 0  # рахує к-кість точок
        self.main_init()

    def main_init(self):
        self.main.resizable(0, 0)
        Button(self.main,
               text='Нанести точки', font=15,
               command=self.points).grid(row=0, columnspan=3)

        self.btn = Button(self.main,
                          text='Exit', font=15,
                          command=self.exit)
        self.btn.grid(row=2, column=0, columnspan=3)

    def points(self):
        self.main.geometry('500x420')
        self.btn.grid(row=2, column=2)

        Button(self.main,
               text='Очистити', font=15,
               command=self.deleter).grid(row=2, column=1)

        self.canv = Canvas(self.main,
                           background='lightyellow', width=500, height=350)
        self.canv.grid(row=1, columnspan=3)

        self.canv.bind('<1>', self.click)

        Button(self.main,
               text='Намалювати коло', font=15,
               command=self.circle).grid(row=2, column=0)

    def circle(self):

        W = [i for i in self.dots.values()]
        W.append(W[0])

        self.XX0 = 0
        self.YY0 = 0

        self.Rad = 1000

        for i in W[:-1]:
            for j in W[:-1]:

                x1 = i[0]
                y1 = i[1]
                x2 = j[0]
                y2 = j[1]
                x0 = (int(x1) + int(x2)) / 2
                y0 = (int(y1) + int(y2)) / 2

                count = 0
                rad = sqrt((x1 - x0) ** 2 + (y0 - y1) ** 2)

                for d in W[:-1]:
                    x3 = d[0]
                    y3 = d[1]

                    if sqrt((x3 - x0) ** 2 + (y3 - y0) ** 2) <= rad:
                        count += 1

                if count == len(W[:-1]) and rad < self.Rad:
                    self.XX0 = x0
                    self.YY0 = y0
                    self.Rad = rad

        for i in W[:-1]:
            for j in W[:-1]:
                for t in W[:-1]:

                    x1 = int(i[0])
                    y1 = int(i[1])
                    x2 = int(j[0])
                    y2 = int(j[1])
                    x3 = int(t[0])
                    y3 = int(t[1])

                    try:
                        x0 = -(1 / 2) * ((y1 * (x2 ** 2 + y2 ** 2 - x3 ** 2 - y3 ** 2) + y2 * (
                                x3 ** 2 + y3 ** 2 - x1 ** 2 - y1 ** 2) + y3 * (x1 ** 2 + y1 ** 2 - x2 ** 2 - y2 ** 2)) /
                                         (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

                        y0 = (1 / 2) * ((x1 * (x2 ** 2 + y2 ** 2 - x3 ** 2 - y3 ** 2) + x2 * (
                                x3 ** 2 + y3 ** 2 - x1 ** 2 - y1 ** 2) + x3 * (x1 ** 2 + y1 ** 2 - x2 ** 2 - y2 ** 2)) /
                                        (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))

                        rad = sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
                        count = 0

                        for d in W[:-1]:
                            x4 = d[0]
                            y4 = d[1]

                            if sqrt((x4 - x0) ** 2 + (y4 - y0) ** 2) <= rad:
                                count += 1

                        if count == len(W[:-1]) and rad < self.Rad:
                            self.XX0 = x0
                            self.YY0 = y0
                            self.Rad = rad

                    except ZeroDivisionError:
                        pass

        self.canv.create_oval(self.XX0 - self.Rad, self.YY0 - self.Rad,
                              self.XX0 + self.Rad, self.YY0 + self.Rad, outline='blue', width=2)

    def exit(self):
        self.main.destroy()

    def click(self, event):
        xx = int(event.x)
        yy = int(event.y)
        tagg = str(self.counter)
        self.canv.create_oval(xx - 4, yy - 4, xx + 4, yy + 4, tag=tagg, fill='red')
        self.dots[tagg] = [xx, yy]
        self.counter += 1

    def deleter(self):
        for i in range(self.counter + 1):
            self.canv.delete(i)
        self.canv.delete('circle')
        self.counter = 0
        self.dots = defaultdict(list)
        self.distances = defaultdict(list)
        self.points()


if __name__ == '__main__':
    top = Tk()
    A = Tochki(top)
    top.mainloop()

