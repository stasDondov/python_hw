from collections import defaultdict

n = int(input('Порядок матриці: '))   #задаємо матрицю
Matr = []
for i in range(n):
    S = list(map(int, input().split()))
    Matr.append(S)

d = defaultdict(list)
for i in range(len(Matr)):
    for j in range(len(Matr)):
        if Matr[i][j] != 0:
            d[(i, j)] = Matr[i][j]

Ans = max(d.values())

print(d)
print('Найбільший елемент розрідженої матриці: ', Ans)

