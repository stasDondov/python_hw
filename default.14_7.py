from collections import deque
import random

d = deque()
m = int(input('m = '))

t1 = int(input('t1 = '))
t2 = int(input('t2 = '))


T = int(input('T = '))

while T > 0:
    time1 = random.randint(1, t1)
    time2 = random.randint(1, t2)
    T -= time1  #час обслуговування покупця
    d.append(time1)
    T -= time2   #час додавання нового покупця
    d.append(str(time2))
    m -= 1
    if m == 0:
        print('Черга закінчилась, ',T, 'часу залишилось.' )
        break    

print(d)
if m != 0:
    print('В черзі залишилось {} людей.'.format(m))

