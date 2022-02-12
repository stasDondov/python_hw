from math import sqrt


class Point2:
    """Клас реалізує точку площини"""

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        """Повернути координату х"""
        return self._x

    def get_y(self):
        """Повернути координату y"""
        return self._y

    def __str__(self):
        """Повернути рядок представлення точки"""
        return "({}, {})".format(self._x, self._y)


class RegularPolygone:
    """Клас для роботи з многокутниками"""

    def __init__(self, *args):                    # вершини вводяться в тій послідовності, в якій вони розміщені на
        self.Tops = []                            # поверхні многокутника
        for i in args:                            # args - кортеж з об'єктів класу Point2
            tup = (i.get_x(), i.get_y())          # self.Tops - список з кортежів, кожен кортеж - координати вершин
            self.Tops.append(tup)                 # self.side - довжина сторони многокутника

        self.side = sqrt((self.Tops[0][0] - self.Tops[1][0])**2 + (self.Tops[0][1] - self.Tops[1][1])**2)
        self.k = len(self.Tops)                   # self.k - кількість кутів многокутника

        self.X = ()                               # для знаходження площі многокутника за алгоритмом Гауса
        self.Y = ()                               # створимо кортежі з Х-ових та Y-вих координат многокутника
        for i in range(self.k):
            self.X += (self.Tops[i][0],)
            self.Y += (self.Tops[i][1],)
        self.X += (self.X[0],)
        self.Y += (self.Y[0],)

    def top(self):
        """Повернути вершини многокутника"""
        print('Координати вершин: ')
        for i in self.Tops:
            print(i)

    def perimetr(self):
        """Повернути периметр многокутника"""
        return self.k * self.side

    def plosha(self):
        """Повернути площу фігури"""
        dob1 = 0
        dob2 = 0
        for i in range(self.k):
            dob1 += self.X[i] * self.Y[i + 1]
            dob2 += self.Y[i] * self.X[i + 1]
        pl = abs(dob1 - dob2) / 2                           # площа фігури за формулою Гауса
        return pl

    def check(self, Dot):                                   # Dot - об'єкт класу Point2
        """Перевіряє, чи належить точка многокутнику"""
        count = 0                                          # з точки, яку перевіряємо випускаємо промінь,
        for i in range(self.k):                             # паралельний осі Ох в додатньому напряму
            x1 = self.X[i]                                  # count - лічильник кількості перетинів
            y1 = self.Y[i]                                  # променя зі сторонами многокутника
            x2 = self.X[i + 1]
            y2 = self.Y[i + 1]                              # якщо кількість перетинів парна - точка лежить поза
            x = Dot.get_x()                                 # многокутником
            
            if ((x - x1) * (y2 - y1)) / (x2 - x1) + y1 <= Dot.get_y():
                count += 1
         
        print(count)
        if count % 2 == 1:
            return True
        else:
            return False


# Перевірка
A = Point2(3, 3)
B = Point2(4, 5)
C = Point2(8, 4)
D = Point2(1, 5)
Fig = RegularPolygone(A, B, C, D)
T = Point2(7, 2)
print(Fig.check(T))

