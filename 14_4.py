print('#a)')
from collections import Counter
S = input('S = ')
S = Counter(S)
Ans = S.most_common(1)[0]
print('Символ {} входить до S {} разів'.format(Ans[0], Ans[1]))


S1 = input('S1 = ')
S2 = input('S2 = ')
S1 = Counter(S1)
S2 = Counter(S2)

print('#б)')
Ans = S1 & S2
if Ans == Counter():
    print('рядки S1, S2 складаються з різних символів')
else:
    print(Ans)


print('#в)')
if len(S1 & S2) == len(S1):
    print('Вірно')
else:
    print('Невірно')


print('#г)')
if S1 & S2 == set():
    print('Вірно')
else:
    print('Невірно')

