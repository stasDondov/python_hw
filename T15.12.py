from collections import deque
from random import randint


class DequeError(Exception):
    """Помилка взяття елемента з порожнього деку"""

    def __str__(self):
        return 'Не можна взяти елемент з порожнього деку'


class Deque:  # T15.11
    """Клас, що описує дек"""

    def __init__(self):
        self.deq = deque()  # self.deq - дек

    def isEmpty(self):
        """Чи порожній дек"""
        if self.deq == deque():
            return True
        else:
            return False

    def appendleft(self, elem):
        """Додати елемент до початку деку"""
        self.deq.appendleft(elem)

    def popleft(self):
        """Взяти елемент з початку деку"""
        if self.deq == deque():
            raise DequeError
        else:
            self.deq.popleft()

    def append(self, elem):
        """Додати елемент до кунця деку"""
        self.deq.append(elem)

    def pop(self):
        """Взяти елемент з кінця деку"""
        if self.deq == deque():
            raise DequeError
        else:
            self.deq.pop()

    def print(self):
        print(self.deq)


def Queue():
    """Моделює чергу"""
    new_queue = Deque()

    m = int(input('m = '))  # m - к-кість покупців
    T = int(input('T = '))  # T - загальний час
    t1 = int(input('t1 = '))  # t1 - обслуговування
    t2 = int(input('t2 = '))  # t2 - додавання нового покупця
    t3 = int(input('t3 = '))  # t3 - додається пільговий
    t4 = int(input('t4 = '))  # t4 - останній в черзі не витримує і йде

    for buyer in range(m):
        new_queue.append('покупець')  # створюємо задану чергу з m покупців

    time = 0  # time - лічильник хвилин
    pil_pokupez = 1
    pokupez = 1

    time1 = randint(1, t1)
    time3 = randint(1, t3)

    ch1 = time + time1  # ch1 - хвилина, від початку відрахунку, на якій закінчується обслуговування покупця
    ch2 = time + randint(1, t2)  # ch2 - хвилина, від початку відрахунку, на якій додається новий покупець
    ch3 = time + time3  # ch3 - хвилина, від початку відрахунку, на якій додається пільговий
    ch4 = time + randint(1, t4)  # ch4 - хвилина, від початку відрахунку, на якій останній йде з черги
    Real_time = 0

    while T > Real_time:
        if time == ch2:  # додавання людини
            print('До черги додано покупця')
            new_queue.append('покупець')
            ch2 = time + randint(1, t2)
            m += 1

        if time == ch3:  # пільговий
            new_queue.appendleft('пільговий покупець')
            pil_time = randint(1, t1)
            Real_time += pil_time
            print('Пільгового покупця {} обслуговано за {} хвилин'.format(pil_pokupez, pil_time))
            new_queue.popleft()
            pil_pokupez += 1
            time3 = randint(1, t3)
            ch3 = time + time3

        try:
            if time == ch4:  # покупець пішов
                print('З черги пішов покупець')
                new_queue.pop()
                ch4 = time + randint(1, t4)
                m -= 1

            if time == ch1:  # обслуговування
                Real_time += time1
                print('Покупця {} обслуговано за {} хвилин'.format(pokupez, time1))
                new_queue.popleft()
                time1 = randint(1, t1)
                ch1 = time + time1
                pokupez += 1
                m -= 1

        except DequeError:
            print('\nЗакінчились покупці, залишилось {} хвилин часу'.format(T - Real_time))
            break

        time += 1

    if m > 0:
        print('\nЧас вийшов. Залишилось {} покупців'.format(m))

    return new_queue.deq


# Перевірка
print(Queue())

