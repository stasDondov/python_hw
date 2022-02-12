class Person:

    def __init__(self):
        self.name = None  # прізвище
        self.byear = None  # рік народження

    def input(self):  # ввести особу
        self.name = input('Прізвище: ')
        self.byear = input('Рік народження: ')

    def print(self):  # вивести особу
        print(self.name, self.byear, end=' ')


class Friend(Person):
    """Клас, що описує знайомого"""

    def __init__(self):
        Person.__init__(self)
        self.number = None  # номер телефону

    def input(self):
        """Введення інформації про знайомого"""
        Person.input(self)
        self.number = input('Номер телефону: ')

    def print(self):
        """Виведення інформації про знайомого"""
        Person.print(self)
        print(self.number)


class Dovidnik:
    """Клас для роботи з довідником"""

    def __init__(self, fname):  # fname - назва файлу, в якому зберігатиметься довідник
        self.fname = fname
        self.direct = []  # self.direct - список, що містить інформацію про знайомих

    def create(self):
        """Створення телефонного довідника"""
        File = open(self.fname, 'w')  # File - файл, у якому зберігається довідник
        File.close()

    def write(self):
        """Додавання запису про знайомого"""
        friend = Friend()
        friend.input()
        File = open(self.fname, 'a')
        self.direct.append([friend.name, friend.byear, friend.number])
        File.write(friend.name + ' ' + friend.byear + ' ' + friend.number + '\n')
        File.close()

    def search(self):
        """Пошук номера телефону"""
        name = input('Кого треба знайти? ')  # name - людина, номер якої треба повернути
        for i in self.direct:
            if i[0] == name:
                return self.direct[i][2]

    def change(self):
        """Заміна номера телефону"""
        name = input('Чий номер треба змінити? ')  # name - людина, номер якої треба змінити
        new_number = input('Новий номер: ')  # new_number - новий номер людини name
        for i in range(len(self.direct)):
            if self.direct[i][0] == name:
                self.direct[i][2] = new_number
        File = open(self.fname, 'w')
        for i in self.direct:
            File.write(i[0] + ' ' + i[1] + ' ' + i[2] + '\n')


# Перевірка
My_dovidnik = Dovidnik('myfile.txt')  # створимо об'єкт класу Dovidnik
My_dovidnik.create()  # створимо довідник
My_dovidnik.write()  # запишемо в файл трьох абонентів
My_dovidnik.write()
My_dovidnik.write()
My_dovidnik.change()  # змінимо один з номерів

