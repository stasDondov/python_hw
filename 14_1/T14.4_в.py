from collections import Counter

S1 = Counter(input('Введіть рядок S1:\n'))
S2 = Counter(input('Введіть рядок S2:\n'))

count = 0  # count - лічильник слів, що входять у S2 не рідше ніж у S1
for i in S1.keys():
    if S1[i] > S2[i]:
        print('Невірно')
        break
    else:
        count += 1

if count == len(S1):
    print('Вірно')

