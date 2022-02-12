from collections import defaultdict

class Multiset:
    """Клас мультимножина"""

    def __init__(self):
        self.set = defaultdict(int)  # self.set - мультимножина

    def clean(self):
        """Зробити мультимножину порожньою"""
        self.set.clear()

    def isClean(self):
        """Чи є мультимножина порожньою"""
        if self.set == defaultdict():
            return True
        else:
            return False

    def append(self, elem):  # elem - елемент, який слід додати
        """Додати елемент"""
        if self.set[elem] != None:
            self.set.update({elem: self.set[elem] + 1})

    def remove(self, elem):  # elem - елемент, який слід забрати
        """Забрати елемент"""
        if self.set[elem] > 0:
            self.set[elem] -= 1
        else:
            print('Такого елемента немає в мультимножині')

    def __getitem__(self, item):
        """Кількість входжень елемента у мультимножину"""
        return self.set[item]

    def __or__(self, other):
        """Об'єднання двох мультимножин"""
        new_dict = defaultdict(int)  # new_dict - нова мультимножина, результат об'єднання
        for elem in self.set.keys():
            new_dict.update({elem: max(self.set[elem], other.set[elem])})
        for elem in other.set.keys():
            new_dict.update({elem: max(self.set[elem], other.set[elem])})
        return new_dict

    def __and__(self, other):
        """Перетин двох мультимножин"""
        new_dict = defaultdict(int)  # new_dict - нова мультимножина, результат перетину
        for elem in self.set:
            if self.set[elem] > 0:
                new_dict.update({elem: min(self.set[elem], other[elem])})
        return new_dict

    def __str__(self):
        return str(self.set)

