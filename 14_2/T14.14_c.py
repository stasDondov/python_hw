from T14_14 import Multiset

def Task_3():
    S1 = input('Введіть рядок S1:\n')
    Dict1 = Multiset()  # Dict1 - мультимножина, утворена з елементів рядка S1
    for i in S1:
        Dict1.append(i)
    S2 = input('Введіть рядок S2:\n')
    Dict2 = Multiset()  # Dict2 - мультимножина, утворена з елементів рядка S2
    for i in S2:
        Dict2.append(i)

    count = 0  # count - лічильник елементів, що входять в S2 не рідше ніж в S1
    for i in Dict1.set.keys():
        if Dict2[i] >= Dict1[i]:
            count += 1
        else:
            return 'Деякі символи входять до рядка S2 меншу клькість разів ніж до S1'
    if count == len(Dict1.set) <= len(Dict2.set):
        return 'До рядка S2 входять ті ж символи що й до S1, причому не меншу кількість разів'
    else:
        return 'До рядків входять різні символи'


# Перевірка
print(Task_3())

