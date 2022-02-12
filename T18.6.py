from collections import defaultdict


class Specie:
    """Клас, що описує Вид"""

    def __init__(self):
        self.name_of_S = None  # self.name_of_S - назва виду
        self.klass = None  # self.klass - назва класу

    def input(self):
        """Введення інформації про Вид"""
        self.name_of_S = input('Назва виду: ')
        self.klass = input('Клас: ')

    def print(self):
        """Виведення інформації про Вид"""
        print('Назва виду: {}\nКлас: {}'.format(self.name_of_S, self.klass))


class Flying:
    """Клас, що описує Літаюче"""

    def __init__(self):
        self.way_of_flight = None  # self.way_of_flight - спосіб польоту
        self.number_of_wings = None  # self.number_of_wings - кількість крил
        self.direction_of_flight = None  # self.direction_of_flight - напрям польоту

    def input(self):
        """Введення інформації про Літаюче"""
        self.way_of_flight = input('Спосіб польоту: ')
        self.number_of_wings = input('Кількість крил: ')
        self.direction_of_flight = input('Напрям польоту: ')

    def print(self):
        """Виведення інформації про Літаюче"""
        print('Спосіб польоту: {}\nКількість крил: {}\n'
              'Напрям польоту: {}'.format(self.way_of_flight, self.number_of_wings, self.direction_of_flight))


class FlyingCreature(Specie, Flying):
    """Клас, що описує Літаючу істоту"""

    def __init__(self):
        super().__init__()
        self.name_of_FC = None  # self.name_of_FC - назва Літаючої істоти

    def input(self):
        """Виведення інформації про Літаючу істоту"""
        Specie.input(self)
        Flying.input(self)
        self.name_of_FC = input('Назва літаючої істоти: ')
        print()

    def print(self):
        """Виведення інформації про Літаючу істоту"""
        Specie.print(self)
        Flying.print(self)
        print('Назва літаючої істоти: {}\n'.format(self.name_of_FC))


def decorator(attribute, keyword):
    """Декоратор @decorator сортує атрибути даних об'єктів
    та виводить інформацію про вид, спосіб або напрям польоту відповідно.
    1arg = attribute - атрибут, залежно від значення якого Літаючі істоти належать до відповідного
    виду/способу/напряму польоту
    2arg = keyword - слово, яке слід вставити в рядок виводу"""

    def _decorator(function):
        def __decorator(*args, **kw):
            res = function(*args, **kw)  # res - список словників з атрибутами об'єктів
            diction = defaultdict(list)  # diction - словник, значеннями якого є назви Літаючих істот
            for Dict in res:
                if Dict[attribute] in diction.keys() is False:
                    diction.update({Dict[attribute]: Dict['name_of_FC']})
                else:
                    diction[Dict[attribute]].append(Dict['name_of_FC'])
            print()
            for key in diction.keys():
                print('До {} {} належать:\n{}'.format(keyword, key, ', '.join(diction[key])))
            return res

        return __decorator

    return _decorator


class Database:
    """Клас для опрацювання списку Літаючих істот"""

    def __init__(self, List):
        self.List = List  # self.List - список об'єктів класу FlyingCreature
        self.data = []  # self.data - список, елементами якого є словники, що містять значення атрибутів кожного об'єкту списку

    @decorator('direction_of_flight', 'Напряму польоту')
    @decorator('way_of_flight', 'Способу польоту')
    @decorator('name_of_S', 'Класу')
    def create(self):
        """Метод для класифікації Літаючих істот за видом/способом/напрямом польоту"""
        for obj in self.List:
            Dict = {}  # Dict - контейнер для значень атрибутів даного об'єкта
            for key in obj.__dict__.keys():
                Dict.update({key: obj.__dict__[key]})
            self.data.append(Dict)
        return self.data


#------------------------(Перевірка)-----------------------------#

Bird1 = FlyingCreature() #створимо 3 Літаючі істоти
Bird1.input()
Bird2 = FlyingCreature()
Bird2.input()
Bird3 = FlyingCreature()
Bird3.input()

Base = Database([Bird1, Bird2, Bird3])
Base.create()

