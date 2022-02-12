from collections import deque
from random import randint


def Queue():
    new_queue = deque()

    m = int(input('m = '))
    T = int(input('T = '))
    t1 = int(input('t1 = '))   #  обслуговування
    t2 = int(input('t2 = '))   #  додавання

    for buyer in range(m):
        new_queue.append('покупець')

    global time, Real_time
    time = 0
    
    pokupez = 1

    time1 = randint(1, t1)

    ch1 = time + time1
    ch2 = time + randint(1, t2)
    Real_time = 0

    while T > time:

        # додавання людини
        if time == ch2:
            print('До черги додано покупця')
            new_queue.append('покупець')
            ch2 = time + randint(1, t2)
            m += 1

                # обслуговування
        if time == ch1:
            Real_time += time1
            print('Покупця {} обслуговано за {} хвилин'.format(pokupez, time1))
            new_queue.popleft()
            time1 = randint(1, t1)
            ch1 = time + time1
            pokupez += 1
            m -= 1

        if m == 0:
            print('Закінчились покупці, залишилось {} хвилин часу'.format(T - Real_time))
            break

        time += 1

    if m > 0:
        print('Час вийшов. Залишилось {} покупців'.format(m))

    return new_queue


# Перевірка
print(Queue())

