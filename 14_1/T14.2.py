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
    """Клас для роботи з правильними многокутниками"""

    def __init__(self, Tops):
        self.Tops = Tops  # self.Tops - заданий список вершин
        self.k = len(self.Tops)  # self.k - кількість вершин
        self.side = sqrt((self.Tops[0].get_x() - self.Tops[1].get_x()) ** 2 +
                         (self.Tops[0].get_y() - self.Tops[1].get_y()) ** 2)  # self.side - довжина сторони

        self.X = ()  # self.X, self.Y - кортежі необхідні для обчислення площі многокутника за алгоритмом Гауса
        self.Y = ()
        for i in range(self.k):
            self.X += (self.Tops[i].get_x(),)
            self.Y += (self.Tops[i].get_y(),)
        self.X += (self.X[0],)
        self.Y += (self.Y[0],)

    def top(self, name):  # name - назва вершини, координати якої слід повернути
        """Повернути вершини многокутника"""
        return name

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
        ans = abs(dob1 - dob2) / 2  # площа фігури за формулою Гауса
        return ans

    def __str__(self):
        """Повернути повну інформацію про многокутник"""
        tops_inf = ''
        for i in self.Tops:
            tops_inf += str(i) + '\n'
        return ('Координати вершин:\n' + tops_inf +
                'Периметр многокутника:\n {}'.format(self.perimetr()) + '\n' +
                'Площа многокутника:\n {}'.format(self.plosha()))

    def inPolygone(self, Dot):  # Dot - об'єкт класу Point2, точка, яку слід перевірити
        """Перевіряє, чи належить точка многокутнику"""
        count = 0  # з точки, яку перевіряємо "випускаємо" промінь,
        # паралельний осі Оy в додатньому напряму
        x = Dot.get_x()
        y = Dot.get_y()
        for i in range(self.k):
            x1 = self.X[i]  # count - лічильник кількості перетинів
            y1 = self.Y[i]  # променя зі сторонами многокутника
            x2 = self.X[i + 1]
            y2 = self.Y[i + 1]

            if x2 == x1:
                test = y1
            else:
                test = (x - x1) * (y2 - y1) / (x2 - x1) + y1

            if min(x1, x2) <= x <= max(x1, x2):
                if test == y:  # точка лежить на поверхні
                    count = 1
                    break
                elif test > y:
                    if x1 == x:  # промінь проходить через вершину
                        count -= 1
                    if min(x1, x2) <= x <= max(x1, x2):  # промінь проходить через сторону
                        count += 1

        if count % 2 == 1:
            return True
        else:
            return False  # якщо кількість перетинів парна - точка лежить поза многокутником


def Zadacha(*args):
    """Перевірити чи є серед многокутників такий, що охоплює всі інші"""
    areas = list(i.plosha() for i in args)  # знаходимо фігуру з найбільшою площею
    Args = list(enumerate(args))  # args - кортеж з об'єктів класу RegularPolygone
    for fig in Args:
        if fig[1].plosha() == max(areas):
            index = fig[0]  # index  -  індекс найбільшої фігури
            Big_fig = Args[index][1]  # Big_fig - найбільша фігура
            del Args[index]
            kount = 0  # kount - лічильник многокутників, які лежать всередині найбільшого
            for fig in Args:
                count = 0
                for top in fig[1].Tops:
                    if Big_fig.inPolygone(top) is True:
                        count += 1
                if count != fig[1].k:
                    return 'Серед многокутників немає такого, який охоплює всі інші многокутники'
                else:
                    kount += 1
            if kount == len(Args):
                return 'Серед многокутників є такий, який охоплює всі інші многокутники'


# Перевірка
# всі вершини многокутинка Figure1 лежать весредині Figure0, жодна з вершин Figure2 не належить іншому многокутнику
A = Point2(-4, 2)
B = Point2(1, 7)
C = Point2(6, 2)
D = Point2(1, -3)
Figure0 = RegularPolygone([A, B, C, D])

A1 = Point2(1, 1)
B1 = Point2(1, 3)
C1 = Point2(3, 3)
D1 = Point2(3, 1)
Figure1 = RegularPolygone([A1, B1, C1, D1])

A2 = Point2(4, -1)
B2 = Point2(5, -1)
C2 = Point2(5, -2)
D2 = Point2(4, -2)
Figure2 = RegularPolygone([A2, B2, C2, D2])

print(Zadacha(Figure0, Figure1, Figure2))  # перевіримо чи є серед многокутників такий, що охоплює всі інші
print(Figure0)  # виведемо інформацію про Figure0

