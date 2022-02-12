'''     Умова
Перевірити, чи вірно, що жоден символ рядка S1 не входить у рядок S2, та
жоден символ S2 не входить до S1
'''

from collections import Counter

S1 = Counter(input('Введіть рядок S1:\n'))
S2 = Counter(input('Введіть рядок S2:\n'))

if S1 & S2 == Counter():
    print('Вірно')
else:
    print('Невірно')

