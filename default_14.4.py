#Task 14.4
from collections import Counter

#a)
S = input('S = ')
S = Counter(S)
Ans = S.most_common(1)[0]
print('Символ {} входить до S {} разів'.format(Ans[0], Ans[1]))

#б)
S1 = input('S1 = ')
S2 = input('S2 = ')
S1 = Counter(S1)
S2 = Counter(S2)
Ans = S1 & S2
if Ans != S1:
    print('рядки S1, S2 складаються з різних символів')
else:
    print('рядки S1, S2 складаються з однакових символів')

#в)
S1 = input('S1 = ')
S2 = input('S2 = ')
S1 = Counter(S1)
S2 = Counter(S2)
count = 0
for i in S1:
    if S1[i] > S2[i]:
        print('Невірно')
        count += 1
        break
if count == 0:
    print('Вірно')

#г)
S1 = input('S1 = ')
S2 = input('S2 = ')
S1 = Counter(S1)
S2 = Counter(S2)
if S1 & S2 == Counter():
    print('Вірно')
else:
    print('Невірно')

