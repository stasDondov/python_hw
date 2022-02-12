from collections import Counter

S1 = Counter(input('Введіть рядок S1:\n'))
S2 = Counter(input('Введіть рядок S2:\n'))

count = 0  # count - лічильник символів, що входять в рядки однакову к-кість разів
for i in S1.keys():
    if i not in S2.keys():
        print('\nРядки складаються з різних символів')
        break
    elif S1[i] != S2[i]:
        print('\nДеякі символи входять в рядки різну кільксть разів')
        break
    else:
        count += 1

if count == len(S1) == len(S2):
    print('\nРядки складаються з однакових символів, які входять в ці рядки однакову кількість разів')

