from collections import deque
from random import randint


def Queue():
    """Моделює чергу"""

    m = int(input('m = '))
    T = int(input('T = '))
    t1 = int(input('t1 = '))  # обслуговування
    t2 = int(input('t2 = '))  # додавання
    new_queue = deque()

    for buyer in range(m):
        new_queue.append('покупець')  # створюємо задану чергу з m покупців

    time = 0  # time - лічильник хвилин
    pokupez = 1

    time1 = randint(1, t1)
    ch1 = time + time1  # ch1 - хвилина, від початку відрахунку, на якій закінчується обслуговування покупця
    ch2 = time + randint(1, t2)  # ch2 - хвилина, від початку відрахунку, на якій додається
    Real_time = 0

    while T > Real_time:

        if time == ch1:  # обслуговування
            Real_time += time1
            print('Покупця {} обслуговано за {} хвилин'.format(pokupez, time1))
            new_queue.popleft()
            time1 = randint(1, t1)
            ch1 = time + time1
            pokupez += 1
            m -= 1

        if time == ch2:  # додавання людини
            print('До черги додано покупця')
            new_queue.append('покупець')
            ch2 = time + randint(1, t2)
            m += 1

        if m == 0:
            print('Закінчились покупці, залишилось {} хвилин часу'.format(T - Real_time))
            break

        time += 1

    if m > 0:
        print('Час вийшов. Залишилось {} покупців'.format(m))

    return new_queue


# Перевірка
print(Queue())

