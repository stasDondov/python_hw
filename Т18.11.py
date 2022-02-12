class CompareMixin:
    """Клас-домішок, що реалізовує стандартні методи порівнянь"""

    def __lt__(self, other):
        return (self < other)

    def __eq__(self,other):
        return not(self < other) and not(other < self)

    def __le__(self, other):
        return (self < other) and self.__eq__(other)

    def __ne__(self, other):
        return (self < other) or (other < self)

    def __ge__(self, other):
        return (other < self) and self.__eq__(other)

    def __gt__(self, other):
        return (other < self)

    
class WeightedList(list):
    """Клас для взважування списків"""

    def __init__(self, List):
        super().__init__(self)
        self.List = List # self.List - список, який слід взважити
        self.weight = sum([abs(i) for i in List]) # self.weight - вага списку

    def __lt__(self, other):
        if self.weight < other.weight:
            return (self < other)


class FullOrderWeightedList(CompareMixin, WeightedList):
    """Клас для перевірки чи є всі списки у сенсі заданого порядку"""

    def __init__(self, BigList):  # BigList - список
        super().__init__(self)
        self.BigList = BigList # BigList - список об'єктів класу WeightedList

    def isfullorder(self):
        """Перевіряє чи всі дані списки мають однакову вагу"""
        if sum([i.weight for i in self.BigList]) / len(self.BigList) == self.BigList[0].weight:
            return True
        else:
            return False


#---------------(Перевірка)-------------------------#

AA = WeightedList([1, 1, -1]) # створимо 2 взважені списки
BB = WeightedList([1, 2])

Ans = FullOrderWeightedList([AA, BB]).isfullorder()
print(Ans)

