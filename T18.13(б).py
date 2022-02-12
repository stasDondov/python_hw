class SeqTxt:
    """Клас-домішок для переведення числової послідовності у текст і навпаки"""

    def num_to_text(self, var):  # var - список чисел
        """Перетворює числову послідовність у текст"""
        return ', '.join([str(i) for i in var])

    def text_to_num(self, var):  # var - рядок
        """Перетворює рядок чисел у числову послідовність"""
        return [int(i) for i in var.split(', ')]


class TxtList(SeqTxt, list):
    """Клас-домішок"""
    pass


class TxtVector(TxtList):
    """Класс для обробки числового вектора"""

    def __init__(self):  # vec - заданий вектор, список            orient - орієнтація вектора (= ver \ hor)
        TxtList.__init__(self)
        self.vec = None # self.vec - заданий вектор
        self.orient = None # self.orient - орієнтація вектора (= 'вертикальна' \ 'горизонтальна')

    def save(self, filename):
        """Записує вектор у файл"""
        self.orient = input('Орієнтація вектора: ')
        print('Введіть вектор:')
        self.vec = (list(map(int, input().split())))
        self.filename = filename # self.filename - назва файлу для запису вектора
        with open(self.filename, 'w') as f:
            if self.orient == 'вертикальна':
                for i in self.vec:
                    print(i, file=f)
            elif self.orient == 'горизонтальна':
                print(self.num_to_text(self.vec), file=f)

    def read(self, filename):
        """Читає вектор з файлу"""
        self.filename = filename  # self.filename - назва файлу з вектором
        with open(self.filename, 'r') as f:
            r = f.readlines()
            if len(r) > 1:
                self.orient = 'вертикальна'
            else:
                self.orient = 'горизонтальна'
        return [self.text_to_num(j) for j in r]


class TxtMatrix(TxtList):
    """Клас для обробки матриці"""

    def __init__(self):
        TxtList.__init__(self)
        self.matr = [] # self.matr - дана матриця

    def save(self, filename):
        """Записує матрицю у файл"""
        por = int(input('Порядок матриці: '))
        print('Введіть матрицю: ')
        for line in range(por):
            line = (list(map(int, input().split())))
            self.matr.append(line)
        self.filename = filename # self.filename - назва файлу для запису матриці
        with open(self.filename, 'w') as f:
            for line in self.matr:
                print(self.num_to_text(line), file=f)

    def read(self, filename):
        """Читає матрицю з файлу"""
        self.filename = filename # self.filename - назва файлу з матрицею
        with open(self.filename, 'r') as f:
            r = f.readlines()
            return [self.text_to_num(i) for i in r]


def Multiplic(Vecfile, Matrfile):
    """Функція, що рахує добуток вектора-стовпця на "матрицю-рядок" або вектора-рядка на матрицю,
    залежно від заданої орієнтації вектора"""
    Vec = TxtVector()
    vRead = Vec.read(Vecfile) # vRead - даний вектор
    Matr = TxtMatrix()
    mRead = Matr.read(Matrfile) # mRead - дана матриця
    Ans = [] # Ans - результат множення
    
    if Vec.orient == 'вертикальна':
        assert len(mRead) == 1, 'Даний вектор не можна помножити на введену матрицю'
        # к-кість рядків матриці > 1 => множити на неї вектор-стовпчик не можна
        for i in range(len(vRead)):
            line = [] # line - рядок матриці-результату добутку
            for j in range(len(vRead)):
                line.append(int(vRead[i][0]) * mRead[0][j])
            Ans.append(line)
        with open('NewFile.txt', 'w') as f:
            for line in Ans:
                print(str(line), file=f)

    elif Vec.orient == 'горизонтальна':
        for j in range(len(mRead)):
            el = 0 # el - елемент матриці-результату
            hel = [e[j] for e in mRead] # hel - j-й стовпчик матриці mRead
            for t in range(len(hel)):
                el += vRead[0][t] * hel[t]
            Ans.append(el)
        with open('NewFile.txt', 'w') as f:
            print(str(Ans), file=f)

    return Ans


#========================(Перевірка)======================#

Q = TxtVector() # спочатку запишемо вектор і матрицю
Q.save('Vec.txt')

W = TxtMatrix()
W.save('Mat.txt')

Check = Multiplic('Vec.txt', 'Mat.txt')
print(Check)

