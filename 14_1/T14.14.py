'''   Умова
Описати клас для реалізації мультимножини цілих чисел на базі
словника. Мультимножина - це множина в якій для кожного елемента
запам’ятовується не лише його входження, але й кількість входжень.
Кількість входжень елемента k (1<=k<=n) у мультимножину - це
значення елемента словника з ключем k.
Реалізувати методи:
1) зробити мультимножину порожньою;
2) чи є мультимножина порожньою;
3) додати елемент до мультимножини;
4) забрати елемент з мультимножини (кількість входжень елемента
зменшується на 1, якщо елемент не входить - відмова);
5) кількість входжень елемента у мультимножину - реалізувати
особливий метод __getitem__;
6) об’єднання двох мультимножин (в результаті об’єднання кідькість
входжень елемента визначається як максимальна з двох
мультимножин) – реалізувати особливий метод для операції |
(вертикальна риска) __or__(self, other);
7) перетин двох мультимножин (в результаті кількість входжень
елемента визначається як мінімальна з двох мультимножин) –
реалізувати особливий метод для операції & __and__(self, other);
З використанням класу розв’язати задачі:
а) знайти символ, який входить у рядок S максимальну кількість разів;
б) перевірити, чи складаються рядки S1, S2 з одних і тих же символів, які
входять у ці рядки однакову кількість разів;
в) перевірити, чи вірно, що всі символи ряд
'''
from collections import defaultdict

class Multiset():
    '''Клас мультимножина'''

    def __init__(self):
        self.set = defaultdict(int)

    def clean(self):
        '''Зробити мультимножину порожньою'''
        self.set.clear()

    def isClean(self):
        '''Чи є мультимножина порожньою'''
        if self.set == defaultdict():
            return True
        else:
            return False

    def append(self, elem):
        '''Додати елемент'''
        if self.set[elem] != None:
            self.set.update({elem : self.set[elem] + 1})

    def remove(self, elem):
        '''Забрати елемент'''
        if self.set[elem] > 0:
            self.set[elem] -= 1
        else:
            print('Такого елемента немає в мультимножині')

    def __getitem__(self, item):
        '''Кількість входжень елемента у мультимножину'''
        return self.set[item]

    def __or__(self, other):
        '''Об'єднання двох мультимножин'''
        new_dict = defaultdict(int)
        for elem in self.set.keys():
            new_dict.update({elem : max(self.set[elem], other.set[elem])})
        for elem in other.set.keys():
            new_dict.update({elem : max(self.set[elem], other.set[elem])})
        return new_dict

    def __and__(self, other):
        '''Перетин двох мультимножин'''
        new_dict = defaultdict(int)
        for elem in self.set:
            if self.set[elem] > 0:
                new_dict.update({elem : min(self.set[elem], other[elem])})
        return new_dict
    
    def __str__(self):
        return str(self.set)


Vis = Multiset()
Vis.append(4)
Vis.append(1)
Vis.append(1)
Vis.append(2)

Wis = Multiset()
Wis.append(1)
Wis.append(2)
Wis.append(17)

