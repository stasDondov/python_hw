from collections import Counter

S = Counter(input('Введіть рядок S:\n'))
Ans = S.most_common(1)[0]
print('Символ {} входить до S {} разів'.format(Ans[0], Ans[1]))\

