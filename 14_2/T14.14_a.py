from T14_14 import Multiset


def most_com():  # a)
    S = input('Введіть рядок S:\n')
    Dict = Multiset()
    for i in S:  # робимо з рядка S мультимножину
        Dict.append(i)
    Max = max([i for i in Dict.set.values()])  # Max - максимальна кількість входжень елемента в S
    Ans = []
    for i in Dict.set.keys():
        if Dict[i] == Max:
            Ans.append(i)

    print('Символи, що входять максимальну кількість разів:')
    return Ans


# Перевірка
print(most_com())

