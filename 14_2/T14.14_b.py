from T14_14 import Multiset

def same_syms():
    S1 = input('Введіть рядок S1:\n')
    Dict1 = Multiset()  # Dict1 - мультимножина, утворена з елеиентів рядка S1
    for i in S1:
        Dict1.append(i)
    S2 = input('Введіть рядок S2:\n')
    Dict2 = Multiset()  # Dict2 - мультимножина, утворена з елеиентів рядка S2
    for i in S2:
        Dict2.append(i)

    count = 0  # count - лічильник елементів, що входять в рядки однакову к-кість разів
    for i in Dict1.set.keys():
        if Dict2[i] == Dict1[i]:
            count += 1
        else:
            return 'Деякі символи входять до рядків різну кількість разів'
    if count == len(Dict1.set) == len(Dict2.set):
        return 'До рядків входять однакові символи однакову кількість рядків'
    else:
        return 'До рядків входять різні символи'


# Перевірка
print(same_syms())

